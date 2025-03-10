# Los archivos json deben de estar en el directorio books
import json
import os
def len_root_module_resources():    
    return len(root_module_resources)

def len_root_child_modules():    
    return len(child_modules)

def len_resources_drift():    
    return len(resources_drift)

def len_resources_changed():    
    return len(resources_changes)

def len_outputs_changed():    
    return len(outputs_changed)

def len_all_child_resources():
    all_child_resources = 0
    for child_module in child_modules:
        all_child_resources += len(child_module['resources'])
    return all_child_resources

def len_total_resources():
    return len_root_module_resources() + len_all_child_resources()

def get_json_data():
    FILE_DIR = input("Put the file path should be a json archive -> ")

    if not os.path.isfile(FILE_DIR):
        raise FileNotFoundError(f"The file {FILE_DIR} does not exist.")

    with open(FILE_DIR, 'r') as file:
        json_data = json.load(file)
    return json_data

def get_changed_resources():
    delete_to_create = 0
    only_delete = 0
    only_create = 0
    only_update = 0
    no_changes = 0

    for resource in resources_changes:
        change = resource['change']['actions']
        if 'delete' in change and 'create' in change:
            delete_to_create += 1
        elif 'delete' in change:
            only_delete += 1
        elif 'create' in change:
            only_create += 1
        elif 'update' in change:
            only_update += 1
        else:
            no_changes += 1
    return delete_to_create, only_delete, only_create, only_update, no_changes


# Ahora separaremos el json en varias variables que contendran datos de interes
json_data = get_json_data()

root_module = json_data['planned_values']['root_module']
root_module_resources = root_module['resources']

child_modules = root_module['child_modules']

resources_drift = json_data.get('resource_drift', [])
resources_changes = json_data['resource_changes']
outputs_changed = json_data['output_changes']

