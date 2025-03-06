import json
import os

# Pedir el directorio del archivo

# Imprimimos mensajes de bienvenida
print("Welcome to the Terraform Plan Analyzer")
print("This script will analyze the output of a terraform plan command and show you the resources that will be created, updated or destroyed")

from modules.get_info import * 
from modules.resources import *

print(f'There are {len_root_module_resources()} resources in the root module')
print(f'There are {len_all_child_resources()} resources in the child modules')
print(f'Total resources: {len_total_resources()}')
print(f'There are {len_resources_drift()} resources with drift')
print(f'You can see {len_outputs_changed()} outputs that will change its config')

input("Press Enter to continue...")
# variables para saber el proceso de cambio de mis recursos
delete_to_create, only_delete, only_create, only_update, no_changes = get_changed_resources()

print('\n\n\n\n\n\n')
print(f'There are {delete_to_create} resources that will be deleted and created again')
print(f'There are {only_delete} resources that will be deleted')
print(f'There are {only_create} resources that will be created')
print(f'There are {only_update} resources that will be updated')
print(f'There are {no_changes} resources that will not change')

input("Press Enter to continue...")
print('\n\n\n\n\n\n')

print('Now we will show you the resources that will be created, updated or destroyed, etc...')

OP_Plan = OP_Plan(resources_changes)

all_resources = OP_Plan.get_all_resources()

list_resources_create = []
list_resources_update = []
list_resources_delete = []
list_resources_delete_create = []
list_resources_no_changes = []
dict_types = {}

for resource in all_resources:
    if resource.action == 'create':
        list_resources_create.append(resource)
    elif resource.action == 'update':
        list_resources_update.append(resource)
    elif resource.action == 'delete':
        list_resources_delete.append(resource)
    elif resource.action == 'delete_create':
        list_resources_delete_create.append(resource)
    else:
        list_resources_no_changes.append(resource)

i = 1
j = 0
def print_resources(resources, title):
    print(f'\n{title}:')
    i = 1
    j = 0
    for resource in resources:
        i += 1
        j += 1
        print(f'{i}. Address: {resource.address}, mode: {resource.mode}')
        if j == 10:
            input("Press Enter to continue...")
            j = 0

print_resources(list_resources_create, 'Resources to be created')
print_resources(list_resources_update, 'Resources to be updated')
print_resources(list_resources_delete, 'Resources to be deleted')
print_resources(list_resources_delete_create, 'Resources to be deleted and created again')
print_resources(list_resources_no_changes, 'Resources with no changes')

print('\n\n\n\n\n\n')
print('Now we will show you the resources by type')
for resource in all_resources:
    if resource.type not in dict_types:
        dict_types[resource.type] = []
    dict_types[resource.type].append(resource)

j = 0
for resource_type, resources in dict_types.items():
    print(f'\nResources of type {resource_type}:')
    for resource in resources:
        print(f'Address: {resource.address}, mode: {resource.mode}')
        j += 1
        if j == 10:
            input("Press Enter to continue...")
            j = 0

