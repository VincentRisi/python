from sqlite3 import DatabaseError
import sys, os, os.path, re
from aaxlist import books
from math import ceil
class _obj: pass
import dbapi_util as util

from DB_BOOK import DBBook
from DB_AUTHOR import DBAuthor

authors = dict()
ids = dict()

def make_list(data):
    result = ''
    for i, entry in enumerate(data):
        if i > 0:
            result += ', '
        result += entry
    return result

def add_authors():
  global conn
  conn.rollback()
  count = 0
  for authorId in authors:
    entry = authors[authorId]
    rec = DBAuthor(conn)
    extra = make_list(entry.extra)
    authorName = entry.author
    print (authorId, authorName, extra)
    rec.runInsert(authorId, authorName, extra)
    count += 1
    if count > 100:
      count = 0
      conn.commit()
  if count > 0:
    conn.commit()

def add_books():
  global conn
  conn.rollback()
  count = 0
  for key in books:
    book = books[key]
    rec = DBBook(conn)
    rec.bookId = book.id
    rec.bookName = book.name
    rec.authorId = book.authors[0]
    rec.narratorId = book.narrators[0]
    if hasattr(book, 'comment'):
      rec.comment = book.comment[0:500]
    else:
      rec.comment = None
    rec.description = book.description[0:4000]
    if hasattr(book, 'genre'):
      rec.genre = book.genre
    else:
      rec.genre = None
    if hasattr(book, 'released'):
      rec.released = book.released
    else:
      rec.released = None
    try:
      print (rec.bookId, rec.bookName, rec.authorId)
      rec.execInsert()
      ucover = util.a85decode(book.cover)
      coverLen = len(ucover)
      noParts = ceil(coverLen / 64000)
      partNo = 0
      while noParts > 0:
        partNo += 1
        noParts -= 1
        part = ucover[:64000]
        ucover = ucover[64000:]
        zcover = util.compress(part)
        crec = DBCover(conn)
        crec.bookId = rec.bookId
        crec.partNo = partNo
        crec.coverLen = coverLen
        crec.cover = zcover
        crec.status = 0
        crec.execInsert()
        count += 1
        if count > 100:
          count = 0
          conn.commit()
    except Exception as error:
      print (error)
      print ('ouch', rec.bookId, repr(rec.bookName), rec.authorId)
      
  if count > 0:
    conn.commit()

def make_id(data):
  r = re.findall('([A-Z])', data)
  if len(r) > 0:
    keyAZ = ''.join(r)
  elif len(data) > 0:
    keyAZ = data.replace(')','')
  else:
    keyAZ = 'ANON'
  key = keyAZ[:7]
  r = re.findall('([A-Za-z0-9])', data)
  if len(r) > 0:
    dataAnum = ''.join(r)
  elif len(data) > 0:
    dataAnum = data.replace(')','')
  else:
    dataAnum = 'ANON'
  data = dataAnum
  if not key in ids:
    ids[key] = list()
  if not data in ids[key]:
    ids[key].append(data)
  n = ids[key].index(data)
  return '%s%03d' % (key, n+1)

def get_extra(author):
  extra = ''
  n = author.find('(')
  if n > 0:
    extra = author[n+1:-1]
    author = author[:n]
  n = author.find('-')
  if n > 0:
    extra = author[n+1:]
    author = author[:n]
  return author, extra

def do_author(data):
  arr = data.split(',')
  return_id = list()
  for author in arr:
    id = make_id(author)
    return id

def do_book(book):
  book.id = make_id(book.filename)
  
def process(book):
  authorId = do_author(book.author)
  do_book(book)

def set_connect(_conn):
  global conn
  conn = _conn

import time
def main(pyasdata_dir):
  start_time = time.time()
  global conn
  if os.path.exists(rf'{pyasdata_dir}\ids_list.txt'):
    with open(rf'{pyasdata_dir}\ids_list.txt', 'rt') as ifile:
      lines=ifile.readlines()
    for line in lines:
      key, data = line[:-1].split('=')
      ids[key] = data.split('|')
  for bk in books:
    book = books[bk]
    process(book)
  end_time = time.time()
  print (f'seconds:{end_time - start_time}')
  with open(rf'{pyasdata_dir}\ids_list.txt', 'wt') as ofile:
    for key in sorted(ids):
      data = repr(ids[key]).replace("['",'').replace("']",'').replace("', '",'|')
      ofile.write(f'{key}={data}\n')
