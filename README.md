<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/AWSToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/awstoolbox/black-and-white-circle-256.png" alt="AWSToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-availability-zones/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/AWSToolbox/list-availability-zones/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/AWSToolbox/list-availability-zones?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones">
        <img src="https://img.shields.io/github/created-at/AWSToolbox/list-availability-zones?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-availability-zones/releases/latest">
        <img src="https://img.shields.io/github/v/release/AWSToolbox/list-availability-zones?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/releases/latest">
        <img src="https://img.shields.io/github/release-date/AWSToolbox/list-availability-zones?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/releases/latest">
        <img src="https://img.shields.io/github/commits-since/AWSToolbox/list-availability-zones/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-availability-zones/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-availability-zones/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This Python package allows you to list all availability zones configured for a given AWS account. It is part of our larger
[AWS Toolkit](https://github.com/AWSToolbox).

### Installation

To install the package, use:

```sh
pip install wolfsoftware.list-availability-zones
```

### Usage

To list all availability zones for your AWS account, use the following command:

```sh
usage: list-availability-zones [-h] [-V] [-p PROFILE] [-t THREADS]

List all availability zones configured for an account.

Flags:
  -h, --help            Show this help message and exit
  -V, --version         Show program's version number and exit.

Optional arguments:
  -p PROFILE, --profile PROFILE
                        AWS profile name from ~/.aws/credentials (default: None)
  -t THREADS, --threads THREADS
                        The number of threads to use (default: 8)
```

### Requirements

You will need a valid set of AWS credentials to run this command. These credentials should be configured in your `~/.aws/credentials` file.

### Example Output

Below is an example of the output you can expect from running this command:

```
+----------------+---------------------------+--------------------+-------+
|  Region Name   |          Location         | Availability Zones | Count |
+----------------+---------------------------+--------------------+-------+
|   af-south-1   |     Africa (Cape Town)    |                    |       |
|   ap-east-1    |  Asia Pacific (Hong Kong) |                    |       |
| ap-northeast-1 |    Asia Pacific (Tokyo)   |      a, c, d       |   3   |
| ap-northeast-2 |    Asia Pacific (Seoul)   |     a, b, c, d     |   4   |
|   ap-south-1   |   Asia Pacific (Mumbai)   |      a, b, c       |   3   |
| ap-southeast-1 |  Asia Pacific (Singapore) |      a, b, c       |   3   |
| ap-southeast-2 |   Asia Pacific (Sydney)   |      a, b, c       |   3   |
|  ca-central-1  |      Canada (Central)     |      a, b, d       |   3   |
|  eu-central-1  |     Europe (Frankfurt)    |      a, b, c       |   3   |
|   eu-north-1   |     Europe (Stockholm)    |      a, b, c       |   3   |
|   eu-south-1   |       Europe (Milan)      |                    |       |
|   eu-west-1    |      Europe (Ireland)     |      a, b, c       |   3   |
|   eu-west-2    |      Europe (London)      |      a, b, c       |   3   |
|   eu-west-3    |       Europe (Paris)      |      a, b, c       |   3   |
|   me-south-1   |   Middle East (Bahrain)   |                    |       |
|   sa-east-1    | South America (Sao Paulo) |      a, b, c       |   3   |
|   us-east-1    |  US East (North Virginia) |  a, b, c, d, e, f  |   6   |
|   us-east-2    |       US East (Ohio)      |      a, b, c       |   3   |
|   us-west-1    |   US West (California)    |        a, c        |   2   |
|   us-west-2    |      US West (Oregon)     |     a, b, c, d     |   4   |
+----------------+---------------------------+--------------------+-------+
```

> Note: If a cell is empty, it means you are not opted into that region and therefore the information cannot be queried.

### Additional Information

For more tools and utilities, check out our [AWS Toolkit](https://github.com/AWSToolbox).

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
