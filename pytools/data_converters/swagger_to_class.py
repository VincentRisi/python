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

class Struct:
    def __init__(self):
        pass

class Builder:
    data_dict: dict
    fields: dict
    operationId: str
    tags: list[str]
    
    def __init__(self):
        self.fields = dict()
        self.operationId = ''
        self.structs = dict()

    def get_field(self, ref):
        array = ref.split('/')
        if len(array) == 3:
            field = self.data_dict[array[1]][array[2]]
        elif len(array) == 4:
            field = self.data_dict[array[1]][array[2]][array[3]]
        return field

    def recurse_field(self, field, depth=0):
        struct = Struct()
        for key in field:
            setattr(struct, key, field[key])
        self.structs[struct.name] = struct
        if 'schema' in field:
            ref = struct.schema['$ref']
            inner_field = self.get_field(ref)
            if 'type' in inner_field and inner_field['type'] == 'object':
                properties = inner_field['properties']
        #recurse_field(builder, data_dict, inner_field, depth+1)

    def load_data(self):
        paths = self.data_dict['paths']
        for key in paths:
            self.command_line = key
            ndict = paths[key]
            if not 'post' in ndict: continue
            ndict = ndict['post']
            if not 'operationId' in ndict: continue
            self.operationId = ndict['operationId']
            if self.operationId != args.path: continue
            self.tags = ndict['tags'] if 'tags' in ndict else [] 
            parameters = ndict['parameters'] if 'parameters' in ndict else None
            for pdict in parameters:
                if '$ref' in pdict:
                    ref = pdict['$ref']
                    field = self.get_field(ref)
                    self.recurse_field(field)
                else:
                    self.recurse_field(pdict)
            break

def main():
    if not os.path.exists(args.infile):
        print (f'ERROR: {args.infile} does not exist.')
        return False
    path, extension = os.path.splitext(args.infile)
    if not extension in ['.json', '.yaml']:
        print (f'ERROR: {args.infile} is not JSON or YAML.')
        return False
    head, base = os.path.split(path)
    builder = Builder()
    with open(args.infile, 'r') as ifile:
        data_string = ifile.read()
    if extension in ['.json']:
        builder.data_dict = json.loads(data_string)
    elif extension in ['.yaml']:
        builder.data_dict = yaml.safe_load(data_string)
    builder.load_data()
    return True

if __name__ == '__main__':
    main()
