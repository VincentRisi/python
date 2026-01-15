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
arg_parser.add_argument('-m', '--method', type=str, default='post')
args = arg_parser.parse_args()

APIKEY = 'apiKey'
ARRAY = 'array'
BASEPATH = 'basePath'
CODE = 'code'
CONSUMES = 'consumes'
CONTACT = 'contact'
DATE_TIME = 'date-time'
DECIMAL = 'decimal'
DELETE = 'delete'
DESCRIPTION = 'description'
EMAIL = 'email'
GET = 'get'
HEAD = 'HEAD'
IN = 'in'
INFO = 'info'
INT32 = 'int32'
INTEGER = 'integer'
ITEMS = 'items'
FALSE = 'false'
FORMAT = 'format'
MAXITEMS = 'maxItems'
MAXLENGTH = 'minLength'
MINITEMS = 'minItems'
MINLENGTH = 'minLength'
NAME = 'name'
NUMBER = 'number'
OBJECT = 'object'
OPERATIONID = 'operationId'
OPTIONS = 'options'
PARAMETERS = 'parameters'
PATCH = 'patch'
PATHS = 'paths'
POST = 'post'
PRODUCES = 'produces'
PROPERTIES = 'properties' 
PUT = 'put'
REF = '$ref'
REQUIRED = 'required'
RESPONSES = 'responses'
SCHEMA = 'schema'
SCHEMES = 'schemes'
STRING = 'string'
SUMMARY = 'summary'
TAGS = 'tags'
TITLE = 'title'
TRUE = 'true'
TYPE = 'type'
VERSION = 'version'
HTTP_METHODS = [GET,POST,PUT,PATCH,DELETE,HEAD,OPTIONS]

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
            if key == NAME:
               self.structs[struct.name] = struct
        if SCHEMA in field:
            ref = struct.schema[REF]
            inner_field = self.get_field(ref)
            if TYPE in inner_field: 
                if inner_field[TYPE] == OBJECT:
                    properties = inner_field[PROPERTIES]
                    for prop_field in properties:
                        if REF in properties[prop_field]:
                            obj_ref = properties[prop_field][REF]
                            object_field = self.get_field(obj_ref)
                pass
        #recurse_field(builder, data_dict, inner_field, depth+1)

    def load_data(self):
        paths = self.data_dict[PATHS]
        for key in paths:
            self.command_line = key
            ndict = paths[key]
            if not args.method in ndict: continue
            ndict = ndict[args.method]
            if not OPERATIONID in ndict: continue
            self.operationId = ndict[OPERATIONID]
            if self.operationId != args.path: continue
            self.tags = ndict[TAGS] if TAGS in ndict else [] 
            parameters = ndict[PARAMETERS] if PARAMETERS in ndict else None
            for pdict in parameters:
                if REF in pdict:
                    ref = pdict[REF]
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
    if args.method not in HTTP_METHODS:
        print (f'ERROR: {args.method} not a valid HTTP Method')
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
