from modules.get_info_data_variables import (
    len_all_child_resources, 
    len_root_module_resources, 
    len_resources_drift, 
    len_outputs_changed, 
    len_total_resources 
)
from modules.get_info_data_variables import ( 
    delete_to_create, 
    only_delete, 
    only_create, 
    only_update, 
    no_changes,
    list_resources_create,
    list_resources_delete,
    list_resources_update,
    list_resources_delete_create,
    list_resources_no_changes, 
    all_resources, 
    dict_types
)

def print_welcome():
    # Imprimimos mensajes de bienvenida
    print("Welcome to the Terraform Plan Analyzer")
    print("This script will analyze the output of a terraform plan command and show you the resources that will be created, updated or destroyed")

def print_summary1():
    print(f'There are {len_root_module_resources()} resources in the root module')
    print(f'There are {len_all_child_resources()} resources in the child modules')
    print(f'Total resources: {len_total_resources()}')
    print(f'There are {len_resources_drift()} resources with drift')
    print(f'You can see {len_outputs_changed()} outputs that will change its config')

def print_summary2():
    print('\n\n\n\n\n\n')
    print(f'There are {delete_to_create} resources that will be deleted and created again')
    print(f'There are {only_delete} resources that will be deleted')
    print(f'There are {only_create} resources that will be created')
    print(f'There are {only_update} resources that will be updated')
    print(f'There are {no_changes} resources that will not change')

def print_mens1():
    print('\n\n\n\n\n\n')
    print(f'Now we will show you the resources that will be created, updated or destroyed, etc...')

def print_general_mens1():
    print_welcome()

    input("Press Enter to continue...")

    print_summary1()

    input("Press Enter to continue...")

    print_summary2()

def print_general_mens2():
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

    for resource_type, resources in dict_types.items():
        print(f'\nResources of type {resource_type}:')
        for resource in resources:
            print(f'Address: {resource.address}, action: {resource.action}')

        input("Press Enter to continue...")

def print_resources(resources, title):
    print(f'\n{title}:')
    i = 1
    j = 0
    for resource in resources:
        print(f'{i}. Address: {resource.address}, mode: {resource.mode}')
        i += 1
        j += 1
        if j == 10:
            input("Press Enter to continue...")
            j = 0
    input("Press Enter to continue...")