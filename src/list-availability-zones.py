#!/usr/bin/env python
# pylint: disable=C0103


"""
This script will query the AWS API using boto3 and provide a list (table) of all regions and availability zones.

Example Usage:

    ./list-availability-zones.py
"""

from __future__ import print_function

import sys
import boto3

from botocore.exceptions import ClientError
from prettytable import PrettyTable

# pylint: disable=C0103
unknown_string = 'unknown'


def main(_cmdline=None) -> None:
    """
    Something to go here
    """

    country_mapping = get_country_mapping()

    client = boto3.client('ec2')
    results = query_api(client, country_mapping)
    display_results(results)


def get_country_mapping():
    """
    something here
    """

    ssm = boto3.client('ssm')

    regions = {}
    for nsc in get_region_short_codes(ssm):
        regions[nsc] = get_region_long_name(ssm, nsc)

    sorted_regions = dict(sorted(regions.items()))

    return sorted_regions


def get_region_long_name(ssm, short_code):
    """
    something here
    """

    param_name = (
        '/aws/service/global-infrastructure/regions/'
        f'{short_code}/longName'
    )
    response = ssm.get_parameters(
        Names=[param_name]
    )
    return response['Parameters'][0]['Value']


def get_region_short_codes(ssm):
    """
    something here
    """

    output = set()
    for page in ssm.get_paginator('get_parameters_by_path').paginate(
        Path='/aws/service/global-infrastructure/regions'
    ):
        output.update(p['Value'] for p in page['Parameters'])

    return output


def query_api(client, country_mapping):
    """
    Something to go here
    """

    results = []

    try:
        response = client.describe_regions(AllRegions=True)
    except ClientError as e:
        print("Error: " + str(e))
    else:
        if 'Regions' in response:
            for region in response['Regions']:
                azs = []

                my_region_name = region['RegionName']
                ec2_region = boto3.client('ec2', region_name=my_region_name)
                my_region = [{'Name': 'region-name', 'Values': [my_region_name]}]

                try:
                    aws_azs = ec2_region.describe_availability_zones(Filters=my_region)
                except ClientError as _e:
                    az_list = ''
                    az_count = ''
                else:
                    for az in aws_azs['AvailabilityZones']:
                        zone = az['ZoneName'].replace(my_region_name, '')
                        azs.append(zone)
                        az_list = ', '.join(azs)
                        az_count = len(azs)

                results.append({
                                'RegionName': my_region_name,
                                'Location': country_mapping[my_region_name] if my_region_name in country_mapping else unknown_string,
                                'AZS': az_list,
                                'AZ_COUNT': az_count,
                               })
    return results


def display_results(results):
    """
    Display the results
    """

    table = PrettyTable()

    table.field_names = [
                         'Region Name',
                         'Location',
                         'Availability Zones',
                         'Count',
                        ]

    for parts in results:
        table.add_row([
                       parts['RegionName'],
                       parts['Location'],
                       parts['AZS'],
                       parts['AZ_COUNT'],
                      ])

    table.sortby = 'Region Name'
    print(table)


if __name__ == "__main__":
    main(sys.argv[1:])
