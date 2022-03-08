#!/usr/bin/python3

import os, os.path, glob
split = os.path.split
splitext = os.path.splitext

inner_dirs = ['0123456789', 'ABC', 'DEFG', 'HIJKL', 'MNO', 'PQR', 'STUV', 'WXYZ']
outer_dirs =['/elements/Series', '/firstfour/Series', '/new3/Series', '/third3']

list = []
for outer in outer_dirs:
    for inner in inner_dirs:
        files = glob.glob('%s/%s/*' % (outer, inner))
        for file in files:
            dir, name = split(file)
            list.append('%s %s|%s' % (name, dir, file))
for name in sorted(list):
    print (name)
            