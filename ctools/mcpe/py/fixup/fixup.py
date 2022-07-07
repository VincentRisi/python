import sys, glob, os, os.path

src_dir = r'C:\vlab\python\jtools\src\mcpe\sql\si'

top = '''\
DATABASE VLAB 
PACKAGE  vlab.mcpe
OUTPUT   %s
SERVER   LV01
SCHEMA   DBUD00
USERID   dbu
PASSWORD dbudev
'''

def cleanup(line):
    if 'tinyint' in line:
        line = line.replace('tinyint','byte   ')
    if '$PYTHON' in line:
        line = line.replace('$PYTHON','')
    if '(NOIDL)' in line:
        line = line.replace('(NOIDL)','')
    if '(Multiple)' in line:
        line = line.replace('(Multiple)','(1000)')
    if '(SQL CODE)' in line:
        line = line.replace('(SQL CODE)','(SQLCODE)')
    if '$' in line:
        line = line.replace('$','&')
    if '#' in line:
        line = line.replace('#','//')
    return line
        
files = glob.glob(f'{src_dir}\\*.si')
for file in files:
    with open(file, 'rt') as ifile:
        lines = ifile.readlines()
    if lines[0].startswith('DATABASE'):
        continue
    outlist = list()
    _,name = os.path.split(file)
    base,_ = os.path.splitext(name)
    for line in lines:
        if line.startswith('CONNECT'): continue
        if line.startswith('$LOOKUP'): continue
        if line.startswith('$NODOMAIN'): continue
        if line.startswith('$DESCR'): continue
        if line.startswith('$SHOW'): continue
        if line.startswith('$PARM'): continue
        if line.startswith('SERVER'):
            toplines = (top % (base)).splitlines()
            for l in toplines:
                outlist.append(f'{l}\n')
            continue
        for skip in ['CONNECT','$LOOKUP','$NODOMAIN','$DESCR','$SHOW']:
            if skip in line:
                continue
        outlist.append(cleanup(line))
    os.rename(file, file.replace('.si','.bak'))
    with open(file, 'wt') as ofile:
        ofile.writelines(outlist)

