#!/usr/bin/python3

import os, os.path, datetime, argparse
date = datetime.date
today = date.today
year = today().year
dd = today().day
mm = today().month
access = os.access
system = os.system
exists = os.path.exists
split = os.path.split
splitext = os.path.splitext

parser = argparse.ArgumentParser()
parser.add_argument("usedir")
args = parser.parse_args()
usedir = args.usedir

def lnsub(name):
    name = name.upper()
    if name[:4] == 'THE ' or name[:4].lower() == 'the.':
        name = name[4:]
    if name[:1] in '0123456789':
        name = '0123456789'
    elif name[:1] in 'ABC':
        name = 'ABC'
    elif name[:1] in 'DEFG':
        name = 'DEFG'    
    elif name[:1] in 'HIJKL':
        name = 'HIJKL'  
    elif name[:1] in 'MNO':
        name = 'MNO'  
    elif name[:1] in 'PQR':
        name = 'PQR'  
    elif name[:1] in 'STUV':
        name = 'STUV'  
    elif name[:1] in 'WXYZ':
        name = 'WXYZ'  
    else:
        name = name[:1]
    return name

root = '/wdblue4a/garethset'    
def fixname(name):
    return f"{root}/{lnsub(name)}/{name.replace(' ','')}"

if exists(usedir):
    _, name = split(usedir)
    command = f'ln -sf "{usedir}" "{fixname(name)}"'
    print (command)
'''
xx = ln -sf "/third3/STUV/Upstart  Crow"/ UpstartCrow
'''

