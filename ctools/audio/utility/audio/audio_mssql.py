import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',  type=str, default=r'C:\vlab\python\ctools\audio\utility\audio')
arg_parser.add_argument('-s', '--server',     type=str)
arg_parser.add_argument('-u', '--user',       type=str)
arg_parser.add_argument('-p', '--password',   type=str)
args = arg_parser.parse_args()

audio_dir = args.audio_dir
pyasdata_dir = rf'{audio_dir}\pyasdata'
support_dir = rf'{audio_dir}\support'
dbapi_dir =  rf'{audio_dir}\dbapi'
mssql_dir =  rf'{dbapi_dir}\mssql'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(mssql_dir)
import pymssql
from audio import *
conn = pymssql.connect(host=args.server, user=args.user, password=args.password)
set_connect(conn)

main(pyasdata_dir)