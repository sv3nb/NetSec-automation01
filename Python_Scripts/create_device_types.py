#!/usr/bin/env python3
# this script can be used to extract a unique list of dictionaries (device types)
# from the device roles dictionary

import yaml
import os

def Create_Device_Types(main_yml):
    '''
    The following script can be used if we dont have a separate file containing
    a unique list of dictionaries for the device types or models
    This was difficult to solve in Ansible so this function was made to solve this.
    '''
    device_types = []
    try:
        with open(main_yml) as f:
            device_roles = yaml.safe_load(f)
            L = device_roles['device_roles'] # we only need this dictionary
            unique_list = list({v['type']:v for v in L}.values()) # this ensures the type key is unique for each nested dictionary
            for type in unique_list:
                device_types.append("  - type: " + type['type'])
                device_types.append("    vendor: " + type['vendor'])
                device_types.append("    u_height: 1")
                # omit the role key since we do not need it
            print("device_types:")
            for type in device_types:
                print(type)
    except KeyError:
        print("check if you reference the correct key names from the vars/main.yml file")

'''
if __name__ == '__main__':
    os.chdir('..')
    # open a new yml file to append output to
    with open('roles/build_netbox_db/vars/main.yml', 'a') as file1:
        file1.write("device_types:\n")
        with redirect_stdout(file1):
            Create_Device_Types(source1)
'''
