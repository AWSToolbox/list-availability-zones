"""
This module provides functions to generate and display a list of AWS regions and their corresponding availability zones.

It retrieves region information from AWS SSM and EC2 services. Threading is used to parallelize API calls for improved performance.

Functions:
    get_availability_zones: Generates and returns the availability zone list.
    create_boto3_session: Creates a boto3 session using the specified authentication method.
    get_country_mapping: Retrieves a mapping of AWS region short codes to their long names.
    get_region_long_name: Retrieves the long name of a region given its short code.
    get_region_short_codes: Retrieves a set of region short codes.
    query_api: Queries the AWS API to get a list of regions and their availability zones.

Dependencies:
    - boto3: AWS SDK for Python
    - botocore: Low-level, data-driven core of boto3
    - yaspin: A lightweight terminal spinner
"""

from typing import Any, Dict, List, Set
import concurrent.futures
import threading
from types import SimpleNamespace

import boto3  # type: ignore pylint: disable=import-error
from botocore.exceptions import ClientError, BotoCoreError  # type: ignore pylint: disable=import-error

from yaspin import yaspin

from .exceptions import AWSAvailabilityZonesError


def get_availability_zones(config: SimpleNamespace) -> List[Dict[str, Any]]:
    """
    Generate and return the availability zone list for the specified AWS account.

    Arguments:
        config (SimpleNamespace): Configuration object containing parsed command line arguments,
                                  including the AWS profile name and number of worker threads.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing region and availability zone information.
    """
    try:
        session: Any = create_boto3_session(config)
        client: Any = session.client('ec2')
        with yaspin(text="Generating Availability Zone List", color="cyan") as spinner:
            country_mapping: Dict[str, str] = get_country_mapping(session)
            results: List[Dict[str, Any]] = query_api(client, country_mapping, config)
            spinner.ok("Complete")
        return results
    except AWSAvailabilityZonesError as e:
        raise AWSAvailabilityZonesError(f"Failed to get availability zones: {e}") from e


def create_boto3_session(config: SimpleNamespace) -> boto3.Session:
    """
    Create a boto3 session using the specified authentication method.

    Arguments:
        config (SimpleNamespace): Configuration object containing parsed command line arguments.

    Returns:
        boto3.Session: A boto3 session object
    """
    try:
        if config.profile:
            return boto3.Session(profile_name=config.profile)
        return boto3.Session()
    except (BotoCoreError, ClientError) as e:
        raise AWSAvailabilityZonesError(f"Failed to create boto3 session: {e}") from e


def get_country_mapping(session: boto3.Session) -> Dict[str, str]:
    """
    Retrieve a mapping of AWS region short codes to their long names.

    Arguments:
        session (boto3.Session): The boto3 session.

    Returns:
        Dict[str, str]: A dictionary mapping region short codes to long names.
    """
    try:
        ssm_client: Any = session.client('ssm')
        regions: Dict[str, str] = {}
        for nsc in get_region_short_codes(ssm_client):
            regions[nsc] = get_region_long_name(ssm_client, nsc)
        return dict(sorted(regions.items()))
    except (BotoCoreError, ClientError) as e:
        raise AWSAvailabilityZonesError(f"Failed to get country mapping: {e}") from e


def get_region_long_name(ssm: Any, short_code: str) -> str:
    """
    Retrieve the long name of a region given its short code.

    Arguments:
        ssm (Any): The SSM client.
        short_code (str): The short code of the region.

    Returns:
        str: The long name of the region.
    """
    try:
        param_name: str = f'/aws/service/global-infrastructure/regions/{short_code}/longName'
        response: Any = ssm.get_parameters(Names=[param_name])
        return response['Parameters'][0]['Value']
    except (BotoCoreError, ClientError) as e:
        raise AWSAvailabilityZonesError(f"Failed to get region long name for {short_code}: {e}") from e


def get_region_short_codes(ssm: Any) -> Set[str]:
    """
    Retrieve a set of region short codes.

    Arguments:
        ssm (Any): The SSM client.

    Returns:
        Set[str]: A set of region short codes.
    """
    try:
        output: Set[str] = set()
        paginator: Any = ssm.get_paginator('get_parameters_by_path')
        for page in paginator.paginate(Path='/aws/service/global-infrastructure/regions'):
            output.update(p['Value'] for p in page['Parameters'])
        return output
    except (BotoCoreError, ClientError) as e:
        raise AWSAvailabilityZonesError(f"Failed to get region short codes: {e}") from e


def query_api(client: Any, country_mapping: Dict[str, str], config: SimpleNamespace) -> List[Dict[str, Any]]:
    """
    Query the AWS API to get a list of regions and their availability zones.

    Arguments:
        client (Any): The EC2 client.
        country_mapping (Dict[str, str]): The country mapping dictionary.
        workers (int): Number of worker threads to use.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing region and availability zone information.
    """
    try:
        response: Any = client.describe_regions(AllRegions=True)
    except ClientError as e:
        raise AWSAvailabilityZonesError(f"Failed to describe regions: {e}") from e

    if 'Regions' not in response:
        return []

    regions: Any = response['Regions']
    return process_regions(regions, country_mapping, config.threads)


def process_regions(regions: List[Dict[str, Any]], country_mapping: Dict[str, str], threads: int) -> List[Dict[str, Any]]:
    """
    Process each region to retrieve its availability zones concurrently.

    Arguments:
        regions (List[Dict[str, Any]]): List of region dictionaries.
        country_mapping (Dict[str, str]): The country mapping dictionary.
        workers (int): Number of worker threads to use.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing processed region and availability zone information.
    """
    results: List[Dict[str, Any]] = []
    lock = threading.Lock()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures: List[concurrent.futures.Future[Dict[str, Any]]] = [
            executor.submit(process_region, region, country_mapping) for region in regions
        ]
        for future in concurrent.futures.as_completed(futures):
            try:
                result: Dict[str, Any] = future.result()
                with lock:
                    results.append(result)
            except Exception as e:
                print(f"Error processing future result: {e}")

    return results


def process_region(region: Dict[str, Any], country_mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Process a single region to retrieve its availability zones.

    Arguments:
        region (Dict[str, Any]): A dictionary containing region information.
        country_mapping (Dict[str, str]): The country mapping dictionary.

    Returns:
        Dict[str, Any]: A dictionary containing processed region and availability zone information.
    """
    my_region_name: str = region['RegionName']
    try:
        ec2_region: Any = boto3.client('ec2', region_name=my_region_name)
        azs: List[str] = []
        my_region: List[Dict[str, Any]] = [{'Name': 'region-name', 'Values': [my_region_name]}]

        try:
            aws_azs: Any = ec2_region.describe_availability_zones(Filters=my_region)
            for az in aws_azs['AvailabilityZones']:
                zone: str = az['ZoneName'].replace(my_region_name, '')
                azs.append(zone)
            az_list: str = ', '.join(azs)
            az_count: int = len(azs)
        except ClientError:
            az_list = ''
            az_count = 0

        return {
            'RegionName': my_region_name,
            'Location': country_mapping.get(my_region_name, "unknown"),
            'AZS': az_list,
            'AZ_COUNT': az_count,
        }
    except (BotoCoreError, ClientError) as e:
        print(f"Failed to process region {my_region_name}: {e}")
        return {
            'RegionName': my_region_name,
            'Location': country_mapping.get(my_region_name, "unknown"),
            'AZS': '',
            'AZ_COUNT': 0,
        }
