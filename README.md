# NetSec-automation01
 IAAC conversion
 
 This repository is to demonstrate Network As Code or IAAC principles.
 By using a combination of Python, Ansible and Netbox i wanted to create
 a dynamic network inventory and IPAM solution for customers who dont have a proper solution in place.
 
 The python scripts are used to convert data provided in CSV format into proper YAML.
 These YAML files are then used by Ansible to initally build the Netbox Database.
 
 Subsequent additions of sites, devices, vlans, etc in Netbox can be synced with  Ansible for automatic deployment of network services
 
