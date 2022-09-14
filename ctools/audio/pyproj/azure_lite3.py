import sys, os, os.path, re
import argparse

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
conn = sqlite3.connect(args.audio_db)

import dbapi_util_lite3 as dbapi_util

def make_image(name):
    filename = rf'{dbapi_dir}\lite3\{name}.py'
    print (filename)
    with open(filename, 'rb') as ifile:
        buff = ifile.read()
    size = len(buff)
    return size, dbapi_util.compress(buff)

#try:
#    from MessageDBApi import *
#    rec = MessageInsert()
#    rec.MessageLen, rec.MessageData = make_image('MessageDBApi')
#    rec.USId = 'MEME'
#    rec.execute(conn)
#    conn.commit()
#except Exception as e:
#    print('Message:', e)
#    conn.rollback()

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

#try:
#    from ResponseDBApi import *
#    rec = ResponseInsert()
#    rec.MessageLen, rec.MessageData = make_image('ResponseDBApi')
#    rec.USId = 'MEME'
#    rec.execute(conn)
#    conn.commit()
#except Exception as e:
#    print('Response:', e)
#    conn.rollback()

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

