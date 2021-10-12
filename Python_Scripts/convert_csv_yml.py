#!/usr/bin/env python3
# this script will render csv output into a yaml format
# it is less efficient than working with the dictreader method but might be easier to modify in certain scenarios.

import csv
from contextlib import redirect_stdout
import os

source1 = "csv_export/device_roles.csv"
source2 = "csv_export/devices.csv"

roles = []
devices = []

def Device_Roles(file):
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            roles.append("  - role: " + row[0])
            roles.append("    type: " + row[1])
            roles.append("    vendor: " + row[2])
    print('---')
    print('device_roles:')
    for role in roles:
        print(role)

def Devices(file):
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            devices.append("  - hostname: " + row[0])
            devices.append("    mgmt_ip: " + row[1])
            devices.append("    model: " + row[2])
            devices.append("    vendor: " + row[3])
            devices.append("    role: " + row[4])
            devices.append("    location: " + row[5])
    print('devices:')
    for device in devices:
        print(device)

if __name__ == '__main__':

    os.chdir('..') # change to parent dir so we can use relative paths
    with open('roles/build_netbox_db/vars/main.yml', 'w') as file1:
        with redirect_stdout(file1):
            Device_Roles(source1)

    with open('roles/build_netbox_db/vars/main.yml', 'a') as file1:
        with redirect_stdout(file1):
            Devices(source2)
