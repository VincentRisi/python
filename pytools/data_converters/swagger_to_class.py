from tkinter import Y
import yaml
import json
import os

import argparse
arg_parser = argparse.ArgumentParser(
    prog='swagger_to_class', 
    description='Swagger or Openapi used to generate Python classes',
    epilog='Bottom of help')
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
arg_parser.add_argument('-p', '--path', type=str)
args = arg_parser.parse_args()
print (args.path)

class Field:
    def __init__(self):
        self.name = ''
        self.type = None
        self.format = None
        self.minLength = None
        self.maxLength = None
        self.ref = None

class Struct: #in openapi components.schemas
    def __init__(self):
        self.name = ''
        self.required = []
        self.type = None
        self.ref = None
        self.fields = []

def clear_ref(value):
    value = value.replace('#/definitions/','').replace('#/components/schemas/','')
    return value

def process_parameters(structures, parameters):
    for field in parameters:
        struct = Struct()
        struct.name = field['name'] if 'name' in field else field

def process_paths(structures, paths):
    for command in paths:
        activity = paths[command]
        if not 'post' in activity:
            continue
        post = activity['post']
        operationId = post['operationId']
        if operationId != args.path:
            continue
        
def process_definitions(structures, definitions):
    for def_name in definitions:
        struct = Struct()
        structures[def_name] = struct
        struct.name = def_name
        if 'required' in definitions[def_name]:
            for required in definitions[def_name]['required']:
                struct.required.append(required)
        if 'type' in definitions[def_name]:
            struct.type = definitions[def_name]['type']
        if '$ref' in definitions[def_name]:
            struct.ref = clear_ref(definitions[def_name]['$ref'])
        if not 'properties' in definitions[def_name]:
            continue
        properties = definitions[def_name]['properties']
        for prop_name in properties:
            field = Field()
            field.name = prop_name
            struct.fields.append(field)
            for key in properties[prop_name]:
                value = properties[prop_name][key]
                if key == 'type': field.type = value
                elif key == 'format': field.format = value
                elif key == 'minLength': field.minLength = value
                elif key == 'maxLength': field.maxLength = value
                elif key == '$ref': field.ref = clear_ref(value)

def main():
    if not os.path.exists(args.infile):
        print (f'ERROR: {args.infile} does not exist.')
        return False
    path, extension = os.path.splitext(args.infile)
    if not extension in ['.json', '.yaml']:
        print (f'ERROR: {args.infile} is not JSON or YAML.')
        return False
    head, base = os.path.split(path)
    with open(args.infile, 'r') as ifile:
        data_string = ifile.read()
    if extension in ['.json']:
        data_dict = json.loads(data_string)
    elif extension in ['.yaml']:
        data_dict = yaml.safe_load(data_string)
    structures = {}
    if 'parameters' in data_dict:
        parameters = data_dict['parameters']
        process_parameters(structures, parameters)
    if 'paths' in data_dict:
        paths = data_dict['paths']
        process_paths(structures, paths)
    if 'definitions' in data_dict:
        definitions = data_dict['definitions']
        process_definitions(structures, definitions)    
    return True

if __name__ == '__main__':
    main()
