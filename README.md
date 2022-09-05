# EC2 Inventory

## Introduction

This tool gets EC2 instance inventory, total storage size attached to the instance and shows details of the instance type (for instance, for t2.micro shows 1024MiB RAM, 1 vCPU)

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