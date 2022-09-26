import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',   type=str, default=r'C:\vlab\python\ctools\audio\pyproj')
arg_parser.add_argument('-g', '--genned_dir',  type=str, default=r'C:\vlab\python\jtools\out\audio\sql\py')
arg_parser.add_argument('-p', '--pytools_dir', type=str, default=r'C:\vlab\python\pytools')
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
mssql_dir =  rf'{dbapi_dir}\mssql'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(mssql_dir)
import pymssql
conn = pymssql.connect(host=args.server, user=args.user, password=args.password)
cursor = conn.cursor()
cursor.execute('use audio')
import dbapi_util_mssql as util
from audio import *
set_connect(conn)
main(pyasdata_dir)
#seconds:188.450932264328