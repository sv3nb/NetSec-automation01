#!/usr/bin/env python3
# this script will render csv output into a yaml format

import csv
import yaml
from contextlib import redirect_stdout
import os
from shutil import copyfile
from create_device_types import Create_Device_Types

roles = "csv_export/device_roles_02.csv"
devices = "csv_export/devices_02.csv"
main_yml = "roles/build_netbox_db/vars/main.yml"

def CSV_Yaml_Converter(file):
    '''Converts a CSV to a yaml file. It counts the number of columns using the fieldnames property
       Then uses a while loop to print the header + row value.
       Make sure to remove spaces between the columns in the CSV file.

       Example CSV format:
            Role,Type,Vendor
            Firewall,Fortigate_81E,Fortinet
            Edge,C7200,Cisco
            Switch,224E,Fortinet

       Example Yaml output:
            - Role: Firewall
              Type: Fortigate_81E
              Vendor: Fortinet
            ...
    '''
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        headers = reader.fieldnames # these are the column headers in a list ['role', 'model', 'type']

        for row in reader:
            i = 0 # start at first list index
            print("  - " + headers[i] + ": " + row[headers[i]]) # the first device role needs to be printer as "- role: Edge"
            while i < (len(headers)-1): # the list index starts at 0 we this is to avoid the "list index out of range" error
                i += 1
                print("    " + headers[i] + ": " + row[headers[i]])


if __name__ == '__main__':

    os.chdir('..') # change to parent directory "netbox" so we can use relative paths
    # open a new yml file to write output to
    with open('roles/build_netbox_db/vars/main.yml', 'w') as output_file:
        output_file.write("---\n") # start of yaml file
        output_file.write("device_roles:\n")
        with redirect_stdout(output_file):
            CSV_Yaml_Converter(roles)

    # append second output to yml file
    with open('roles/build_netbox_db/vars/main.yml', 'a') as output_file:
        output_file.write("devices:\n")
        with redirect_stdout(output_file):
            CSV_Yaml_Converter(devices)

    # call function from create_device_types.py
    with open('roles/build_netbox_db/vars/main.yml', 'a') as output_file:
        with redirect_stdout(output_file):
            Create_Device_Types(main_yml)

    # Here you copy this file to other roles that need it
    copyfile('roles/build_netbox_db/vars/main.yml', 'roles/ipam_netbox_db/vars/main.yml')
