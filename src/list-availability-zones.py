#!/usr/bin/env python

"""
This script will query the AWS API using boto3 and provide a list (table) of all regions and availability zones.

Example Usage:

    ./list-availability-zones.py
"""

from __future__ import print_function

import boto3
import requests
import sys

from botocore.exceptions import ClientError
from prettytable import PrettyTable

unknown_string = 'unknown'
country_mapping = {
                    'af-south-1': 'Africa (Cape Town)',
                    'ap-east-1': 'Asia Pacific (Hong Kong)',
                    'ap-south-1': 'Asia Pacific (Mumbai)',
                    'ap-northeast-2': 'Asia Pacific (Seoul)',
                    'ap-southeast-1': 'Asia Pacific (Singapore)',
                    'ap-southeast-2': 'Asia Pacific (Sydney)',
                    'ap-northeast-1': 'Asia Pacific (Tokyo)',
                    'ca-central-1': 'Canada (Central)',
                    'eu-central-1': 'Europe (Frankfurt)',
                    'eu-west-1': 'Europe (Ireland)',
                    'eu-west-2': 'Europe (London)',
                    'eu-west-3': 'Europe (Paris)',
                    'eu-north-1': 'Europe (Stockholm)',
                    'eu-south-1': 'Europe (Milan)',
                    'me-south-1': 'Middle East (Bahrain)',
                    'sa-east-1': 'South America (Sao Paulo)',
                    'us-east-2': 'US East (Ohio)',
                    'us-east-1': 'US East (North Virginia)',
                    'us-west-1': 'US West (California) ',
                    'us-west-2': 'US West (Oregon)',
                  }


def main(cmdline=None):

    """
    The main function. This takes the command line arguments provided and parse them.
    """

    client = boto3.client('ec2')
    results = query_api(client)
    display_results(results)


def query_api(client):
    """
    Query the API
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
                except ClientError as e:
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

    # This runs when the application is run from the command it grabs sys.argv[1:] which is everything after
    # the program name and passes it to main the return value from main is then used as the argument to
    # sys.exit, which you can test for in the shell. program exit codes are usually 0 for ok, and non-zero
    # for something going wrong.

    sys.exit(main(sys.argv[1:]))
