import sys, os, os.path, re
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
cursor.execute('use mcpe')

import dbapi_util_mssql as dbapi_util

def make_image(name):
    filename = rf'{dbapi_dir}\odbc\{name}.py'
    print (filename)
    with open(filename, 'rb') as ifile:
        buff = ifile.read()
    size = len(buff)
    return size, dbapi_util.compress(buff)

try:
    from MessageDBApi import *
    rec = MessageInsert()
    rec.MessageLen, rec.MessageData = make_image('MessageDBApi')
    rec.USId = 'MEME'
    rec.execute(conn)
    conn.commit()
    getRecs = MessageSelectSome()
    records = getRecs.execute(conn)
    for got in records:
        getRec = MessageSelectOne()
        getRec.Id = got.Id
        result = getRec.readone(conn)
        result = dbapi_util.decompress(getRec.MessageLen, getRec.MessageData)
        print (len(result), result)

except Exception as e:
    print('Message:', e)
    conn.rollback()

try:
    from ReplyDBApi import *
    rec = ReplyInsert()
    rec.MessageLen, rec.MessageData = make_image('ReplyDBApi')
    rec.USId = 'MEME'
    rec.execute(conn)
    conn.commit()
except Exception as e:
    print('Reply:', e)
    conn.rollback()

try:
    from ResponseDBApi import *
    rec = ResponseInsert()
    rec.MessageLen, rec.MessageData = make_image('ResponseDBApi')
    rec.USId = 'MEME'
    rec.execute(conn)
    conn.commit()
except Exception as e:
    print('Response:', e)
    conn.rollback()

try:
    from StreamsDBApi import *
    rec = StreamsInsert(conn)
    rec.MessageLen, rec.MessageData = make_image('StreamsDBApi')
    rec.USId = 'MEME'
    rec.execute(conn)
    conn.commit()
except Exception as e:
    print('Streams:', e)
    conn.rollback()

