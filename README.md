<h1 align="center">
	<a href="https://github.com/WolfSoftware">
		<img src="https://raw.githubusercontent.com/WolfSoftware/branding/master/images/general/banners/64/black-and-white.png" alt="Wolf Software Logo" />
	</a>
	<br>
	List all AWS regions and availability zones
</h1>


<p align="center">
	<a href="https://travis-ci.com/AWSToolbox/list-availability-zones">
		<img src="https://img.shields.io/travis/com/AWSToolbox/list-availability-zones/master?style=for-the-badge&logo=travis" alt="Build Status">
	</a>
	<a href="https://github.com/AWSToolbox/list-availability-zones/releases/latest">
		<img src="https://img.shields.io/github/v/release/AWSToolbox/list-availability-zones?color=blue&style=for-the-badge&logo=github&logoColor=white&label=Latest%20Release" alt="Release">
	</a>
	<a href="https://github.com/AWSToolbox/list-availability-zones/releases/latest">
		<img src="https://img.shields.io/github/commits-since/AWSToolbox/list-availability-zones/latest.svg?color=blue&style=for-the-badge&logo=github&logoColor=white" alt="Commits since release">
	</a>
	<a href="LICENSE.md">
		<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" alt="Software License">
	</a>
	<br>
	<a href=".github/CODE_OF_CONDUCT.md">
		<img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/CONTRIBUTING.md">
		<img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/SECURITY.md">
		<img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/SUPPORT.md">
		<img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
</p>

## Overview

This script will display a list of all available regions and their availability zones.

### Installation

Once you have cloned the code you will need to install the required python packages.

```
pip install -r requirements.txt 
```
> The requirements file is in the src directory

### Usage

```shell
./list-availability-zones.py
```

### Requirements

You will need a valid set of AWS credentials in order to run this command.

### Example output

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

> If a cell is empty it is because you are not opt'd into that region and therefore we cannot query that information.

## Regions

If you want information relating to regions only then please have a look at out [List Regions](https://github.com/AWSToolbox/list-regions) script.

> Listing regions only runs a **LOT** faster, so please make sure you select the correct script.

## Contributors

<p>
	<a href="https://github.com/TGWolf">
		<img src="https://img.shields.io/badge/Wolf-black?style=for-the-badge" />
	</a>
</p>

## Show Support

<p>
	<a href="https://ko-fi.com/wolfsoftware">
		<img src="https://img.shields.io/badge/Ko%20Fi-blue?style=for-the-badge&logo=ko-fi&logoColor=white" />
	</a>
</p>
