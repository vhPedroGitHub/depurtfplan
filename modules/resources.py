import json
import os

from modules.get_info import *

class Resource:
    def __init__(self, address, type, mode, action, all_config):
        self.address = address
        self.type = type
        self.action = action
        self.mode = mode
        self.all_config = all_config

class OP_Plan:
    def __init__(self, resources_changes):
        self.resources_changes = resources_changes
    
    def get_all_resources(self):
        lista_recursos = []
        for resource in self.resources_changes:
            change = resource['change']['actions']
            if 'delete' in change and 'create' in change:
                resource['change'] = 'delete_create'
            elif 'delete' in change:
                resource['change'] = 'delete'
            elif 'create' in change:
                resource['change'] = 'create'
            elif 'update' in change:
                resource['change'] = 'update'
            else:
                resource['change'] = 'no_changes'
            lista_recursos.append(Resource(resource['address'], resource['type'], resource['mode'], resource['change'], resource))
        return lista_recursos