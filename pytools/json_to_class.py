from io import StringIO
import os
import yaml
import json
from datetime import datetime
import uuid
import re
import yaml.loader

import argparse
arg_parser = argparse.ArgumentParser(
    prog='json_to_class', 
    description='JSON or YAML used to generate Python classes',
    epilog='Bottom of help')
arg_parser.add_argument('infile')
arg_parser.add_argument('outfile')
arg_parser.add_argument('-u', '--usefile', type=str)
arg_parser.add_argument('-v', '--verbose', action='store_true')
arg_parser.add_argument('-x', '--expand', action='store_true')
args = arg_parser.parse_args()

def make_class_name(name):
    if name[0] in 'abcdefghijklmnopqrstuvwxyz':
        return name[0].upper()+name[1:]
    return f'{name}Class'

def get_annotation(annotations, field):
    if field in annotations:
        return annotations[field]
    return make_class_name(field)

def get_type(input_field, input_entry):
    input_type = type(input_field).__name__
    if input_type == 'dict':
        return make_class_name(input_entry)
    elif input_type == 'list':
        return f'[ {make_class_name(input_entry)} ] # type: ignore'
    elif re.match('^-?[0-9]+$', input_field) != None:
        return 'int'
    elif re.match('^-?[0-9]*.[0-9]+$', input_field) != None:
        return 'float'
    elif input_field in ['true','false']:
        return 'bool'
    elif len(input_field) == 36:
        if re.match('[0-9A-Fa-f-]+', input_field) != None:
           l = input_field.split('-')
           if len(l) == 5 and len(l[0]) == 8 and len(l[1]) == 4 and len(l[2]) == 4 and len(l[3]) == 4:
               return 'uuid'
    elif len(input_field) == 10:
        if input_field[4] == '-' and input_field[7] == '-' and re.match('^[0-2]', input_field) != None:
            return 'date'
    elif len(input_field) > 18:
        if input_field[4] == '-' and input_field[7] == '-' and input_field[10] == 'T' and input_field[13] ==':':
            return 'datetime'
        else:
            return 'str'
    else:
        return 'str'

def check_type(annotations, input_field, input_entry):
    t = get_type(input_field, input_entry)
    if t != annotations[input_entry]:
        annotations[input_entry] = 'str'

class Builder:
    classes: dict
    annotations: dict
    depths: dict
    max_depth: int
    usage: list
    usefile: str
    def __init__(self):
       self.classes = dict()
       self.annotations = dict()
       self.depths = dict()
       self.max_depth = 0
       self.usage = list()
       self.usefile = str
       self.uses_io = None

def quoted(input_field):
    if re.match('^-?[0-9]+$', input_field) != None:
        return input_field
    elif re.match('^-?[0-9]*.[0-9]+$', input_field) != None:
        return input_field
    elif input_field == 'true':
        return 'True'
    elif input_field == 'false':
        return 'False'
    return f"'{input_field}'"

def do_expand(uses_io, dotted, fixed_name, input_field):
    for i, entry_dict in enumerate(input_field):
        uses_io.write(f'{dotted}.{fixed_name}.append({make_class_name(fixed_name)}())\n')
        for key in entry_dict:
            uses_io.write(f'{dotted}.{fixed_name}[{i}].{key} = {quoted(entry_dict[key])}\n')


def recurse(builder, class_name, input_dict, depth, doset=True):
    verbose = args.verbose
    if verbose:
        def indent(depth):
            return ' '*(depth*4)
    def dotted(listof):
        dot = ''
        value = ''
        for field in listof:
            value = f'{value}{dot}{field}'
            dot = '.'
        return value
    classes = builder.classes
    annotations = builder.annotations
    depths = builder.depths
    usage = builder.usage
    uses_io = builder.uses_io
    if len(usage) <= depth:
        usage.append(class_name)
    else:
        usage[depth] = class_name
    if depth > builder.max_depth:
        builder.max_depth = depth
    if class_name not in classes:
       classes[class_name] = []
       depths[class_name] = depth
    for input_entry in input_dict:
        fixed_name = input_entry.replace('-','_')
        input_field = input_dict[input_entry]
        if fixed_name not in classes[class_name]: 
            classes[class_name].append(fixed_name)
        if input_entry not in annotations:
            annotations[fixed_name] = get_type(input_field, input_entry)
        else:
            check_type(annotations, input_field, input_entry)
        if type(input_field) is dict:
            recurse(builder, input_entry, input_field, depth+1)
            del usage[depth+1]
        elif type(input_field) is list:
            for i, list_entry in enumerate(input_field):
                if i == 0:
                    if type(list_entry) is dict:
                       recurse(builder, input_entry, list_entry, depth+1, False)
                       del usage[depth+1]
                       if uses_io != None:
                           if args.expand == False:
                               uses_io.write(f'{dotted(usage)}.{fixed_name} = {input_field}\n')
                           else:
                               do_expand(uses_io, dotted(usage), fixed_name, input_field)
                    else:
                        pass
                #break
        elif doset:
            if uses_io != None: uses_io.write(f'{dotted(usage)}.{fixed_name} = {quoted(input_field)}\n')

inits = {}
inits['str'] = "''"
inits['int'] = 0
inits['uuid'] = "''"
inits['bool'] = 'False'
inits['float'] = 0.0
inits['date'] = 'datetime.date()'
inits['datetime'] = 'datetime.now()'

def build_classes(code, builder):
    classes = builder.classes
    annotations = builder.annotations
    depths = builder.depths
    depth = builder.max_depth
    code.write('from datetime import datetime\n')
    code.write('import uuid\n\n')
    while depth >= 0:
        for class_entry in classes:
            if depths[class_entry] == depth:
                code.write(f'class {make_class_name(class_entry)}:\n')
                for field_name in classes[class_entry]:
                    code.write(f'    {field_name}: {annotations[field_name]}\n')
                code.write('    def __init__(self):\n')
                for field_name in classes[class_entry]:
                    annot = annotations[field_name] 
                    if annot not in inits:
                        if annot[0] == '[':
                            code.write(f'        self.{field_name} = list()\n')
                        else:
                            code.write(f'        self.{field_name} = {annot}()\n')
                    else:
                        code.write(f'        self.{field_name} = {inits[annot]}\n')
                code.write('\n')
        depth = depth - 1

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
    code_builder = Builder()
    if args.usefile != None:
        uses = code_builder.uses_io = StringIO()
        main_class = make_class_name(base)
        uses.write(f'from {base} import *\n\n')
        uses.write(f'{base} = {main_class}()\n')
    if extension in ['.json']:
        data_dict = json.loads(data_string)
    elif extension in ['.yaml']:
        data_dict = yaml.safe_load(data_string)
    recurse(code_builder, base, data_dict, 0)
    if code_builder.uses_io != None:
        code_builder.uses_io.seek(0)
        block = code_builder.uses_io.read()
        if args.verbose: print(block)
        with open(args.usefile, 'w') as f:
            f.write(block)
    code = StringIO()
    build_classes(code, code_builder)
    code.seek(0)
    block = code.read()
    if args.verbose: print(block)
    with open(args.outfile, "w") as f:
        f.write(block)
    return 0

if __name__ == '__main__':
    main()
