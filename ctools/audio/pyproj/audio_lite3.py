import argparse
x = '''
-a C:\vlab\python\ctools\audio\pyproj 
-d C:\vlab\python\ctools\audio\pyproj\books.db 
-g C:\vlab\python\jtools\out\audio\sql\py 
-p C:\vlab\python\pytools 
-t c:\vlab\python\jtools\out\audio\sql\ddl\lite3\audio.sql
'''
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',   type=str, default=r'C:\vlab\python\ctools\audio\pyproj')
arg_parser.add_argument('-d', '--audio_db',    type=str, default=r'C:\vlab\python\ctools\audio\pyproj\books.db')
arg_parser.add_argument('-g', '--genned_dir',  type=str, default=r'C:\vlab\python\jtools\out\audio\sql\py')
arg_parser.add_argument('-p', '--pytools_dir', type=str, default=r'C:\vlab\python\pytools')
arg_parser.add_argument('-t', '--table_sqldb', type=str, default=r'C:\vlab\python\jtools\out\audio\sql\ddl\lite3\audio.sql')
args = arg_parser.parse_args()

audio_dir = args.audio_dir
genned_dir = args.genned_dir
pytools_dir = args.pytools_dir
pyasdata_dir = rf'{audio_dir}\pyasdata'
support_dir = rf'{pytools_dir}'
dbapi_dir =  rf'{genned_dir}\dbapi'
lite3_dir =  rf'{dbapi_dir}\lite3'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(lite3_dir)
for path in sys.path: print (path)
import sqlite3
from audio import *
conn = sqlite3.connect(args.audio_db)
set_connect(conn)

def run(conn, command, remove=''):
  cursor = conn.cursor()
  if len(remove) > 0: command = command.replace(remove,'')
  cursor.execute(command)

def make_tables():
  table_sql = args.table_sqldb
  conn = sqlite3.connect(args.audio_db)
  with open(table_sql, 'rt') as ifile: lines = ifile.readlines()
  NONE, START, NEXT = range(3) 
  state = START
  command = ''
  for line in lines:
    line = line.rstrip()
    if len(line) == 0:
      state = START
      command = ''
      continue
    if state == START:
      command += f'{line}\n'
      if line[-1] == ';':
        run (conn, command)
        state = NONE
      else:
        state = NEXT
      continue
    if state == NEXT:
      command += f'{line}\n'
      if line[-1] == ';':
        run (conn, command)
        state = NONE

#make_tables()
main(pyasdata_dir)
#seconds:102.00064086914062