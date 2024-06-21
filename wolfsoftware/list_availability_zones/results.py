"""
This module provides a function to display AWS region and availability zone information in a table format.

The `display_results` function takes a list of dictionaries containing AWS region information and
displays it using the PrettyTable library. Each dictionary in the list should contain the keys
'RegionName', 'Location', 'AZS', and 'AZ_COUNT'. The table is sorted by the 'Region Name' field
before being printed.

Dependencies:
    - prettytable: A library for creating simple ASCII tables

Usage Example:
    results = [
        {
            'RegionName': 'us-east-1',
            'Location': 'North Virginia',
            'AZS': 'a, b, c',
            'AZ_COUNT': 3
        },
        {
            'RegionName': 'us-west-1',
            'Location': 'California',
            'AZS': 'a, b',
            'AZ_COUNT': 2
        }
    ]
    display_results(results)
"""

from typing import Any, Dict, List
from prettytable import PrettyTable


def display_results(results: List[Dict[str, Any]]) -> None:
    """
    Display the results in a table format.

    Arguments:
        results (List[Dict[str, Any]]): The list of results to display.
    """
    table = PrettyTable()
    table.field_names = ['Region Name', 'Location', 'Availability Zones', 'Count']

    for parts in results:
        table.add_row([
            parts['RegionName'],
            parts['Location'],
            parts['AZS'],
            parts['AZ_COUNT'] if parts['AZ_COUNT'] != 0 else ''
        ])

    table.sortby = 'Region Name'
    print(table)
