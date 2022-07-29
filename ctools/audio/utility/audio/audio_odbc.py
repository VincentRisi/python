import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',  type=str, default=r'C:\vlab\python\ctools\audio\utility\audio')
arg_parser.add_argument('-g', '--genned_dir',  type=str, default=r'C:\vlab\python\jtools\out\audio\sql\py')
arg_parser.add_argument('-p', '--pytools_dir', type=str, default=r'C:\vlab\python\pytools')
arg_parser.add_argument('-s', '--server',     type=str)
arg_parser.add_argument('-u', '--user',       type=str)
arg_parser.add_argument('-P', '--password',   type=str)
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
conn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=%s\instance1;DATABASE=master;UID=%s;PWD=%s' % (args.server,args.user,args.password))
#set_connect(conn)
#from audio import *

#main(pyasdata_dir)
#connSqlServer = pyodbc.connect(f'DRIVER={SQL Server Native Client 10.0};SERVER=192.106.0.102\instance1;DATABASE=master;UID=sql2008;PWD=password123')