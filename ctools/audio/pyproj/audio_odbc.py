import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',   type=str, default=r'C:\vlab\python\ctools\audio\pyproj')
arg_parser.add_argument('-g', '--genned_dir',  type=str, default=r'C:\vlab\python\jtools\out\audio\sql\py')
arg_parser.add_argument('-p', '--pytools_dir', type=str, default=r'C:\vlab\python\pytools')
arg_parser.add_argument('-d', '--driver',      type=str)
arg_parser.add_argument('-D', '--database',    type=str)
arg_parser.add_argument('-s', '--server',      type=str)
arg_parser.add_argument('-u', '--user',        type=str)
arg_parser.add_argument('-P', '--password',    type=str)
args = arg_parser.parse_args()
audio_dir = args.audio_dir
genned_dir = args.genned_dir
pytools_dir = args.pytools_dir
pyasdata_dir = rf'{audio_dir}\pyasdata'
support_dir = rf'{pytools_dir}'
dbapi_dir =  rf'{genned_dir}\dbapi'
odbc_dir =  rf'{dbapi_dir}\odbc'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(odbc_dir)
import pyodbc
connstr = f'''\
Driver={args.driver};\
Server={args.server};\
Database={args.database};\
UID={args.user};\
PWD={args.password};\
'''
print (connstr)
conn = pyodbc.connect(connstr)
cursor = conn.cursor()
cursor.execute('use audio')
from audio import *
set_connect(conn)
main(pyasdata_dir)
#seconds:190.55233788490295