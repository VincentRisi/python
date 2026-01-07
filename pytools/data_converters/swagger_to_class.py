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

def clear_ref(value):
    value = value.replace('#/definitions/','').replace('#/components/schemas/','')
    return value

class Builder:
    fields: dict
    operationId: str
    tags: list[str]
    def __init__(self):
        self.fields = dict()
        self.operationId = ''

def get_field(data_dict, ref):
    array = ref.split('/')
    if len(array) == 3:
        field = data_dict[array[1]][array[2]]
    elif len(array) == 4:
        field = data_dict[array[1]][array[2]][array[3]]
    return field

class Struct():
    pass
def recurse_field(builder, data_dict, field):
    struct = Struct()
    for key in field:
        setattr(struct, key, field[key])
    pass

def load_data(builder, data_dict):
    paths = data_dict['paths']
    for key in paths:
        command_line = key
        ndict = paths[key]
        if not 'post' in ndict: continue
        ndict = ndict['post']
        if not 'operationId' in ndict: continue
        operationId = ndict['operationId']
        if operationId != args.path: continue
        tags = ndict['tags'] if 'tags' in ndict else [] 
        builder.operationId = operationId
        builder.tags = tags
        parameters = ndict['parameters'] if 'parameters' in ndict else None
        for pdict in parameters:
            if '$ref' in pdict:
                ref = pdict['$ref']
                field = get_field(data_dict, ref)
                recurse_field(builder, data_dict, field)
            else:
                recurse_field(builder, data_dict, pdict)
        break
    pass    

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
    builder = Builder()
    load_data(builder, data_dict)
##    structures = {}
##    if 'parameters' in data_dict:
##        parameters = data_dict['parameters']
##        process_parameters(structures, parameters)
##    if 'paths' in data_dict:
##        paths = data_dict['paths']
##        process_paths(structures, paths)
##    if 'definitions' in data_dict:
##        definitions = data_dict['definitions']
##        process_definitions(structures, definitions)    
    return True

if __name__ == '__main__':
    main()
