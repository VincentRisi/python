import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-a', '--audio_dir',  type=str, default=r'C:\vlab\python\ctools\audio\pyproj')
args = arg_parser.parse_args()

audio_dir = args.audio_dir
pyasdata_dir = rf'{audio_dir}\pyasdata'
support_dir = rf'{audio_dir}\support'
dbapi_dir =  rf'{audio_dir}\dbapi'
oracle_dir =  rf'{dbapi_dir}\oracle'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(oracle_dir)
import cx_Oracle
from audio import *

main(pyasdata_dir)