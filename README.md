# EC2 Inventory

## Introduction

This tool gets EC2 instance inventory, total storage size attached to the instance and shows details of the instance type (for instance, for t2.micro shows 1024MiB RAM, 1 vCPU)

## Installation

Clone this repo using git clone ("main" is the default branch)

If you prefer to use virtualenv:

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -U -r requirements.txt
```

If NOT using virtualenv:

```
$ sudo pip install -U -r requirements.txt
```
This option may change your system-wide Python installation.

## Usage

```
usage: main.py [-h] [-F FILE]

Get EC2 inventory report in current region, outputs to CSV file (need to provide -F argument)

options:
  -h, --help            show this help message and exit
  -F FILE, --file FILE  Provide CSV file name
``` 

## Author
(C) 2022, Google: fsalaman@google.com