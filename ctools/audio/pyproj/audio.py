import sys, os, os.path, re
from aaxlist import books
from math import ceil
class _obj: pass

from DB_BOOK import DBBook
from DB_AUTHOR import DBAuthor
from DB_NARRATOR import DBNarrator

authors = dict()
narrators = dict()
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
    name = authors[authorId]
    rec = DBAuthor(conn)
    #extra = make_list(entry.extra)
    authorName = name
    print (authorId, authorName)
    rec.runInsert(authorId, authorName)
    count += 1
    if count > 100:
      count = 0
      conn.commit()
  if count > 0:
    conn.commit()

def add_narrators():
  global conn
  conn.rollback()
  count = 0
  for narratorId in narrators:
    name = narrators[narratorId]
    rec = DBNarrator(conn)
    #extra = make_list(entry.extra)
    narratorName = name
    print (narratorId, narratorName)
    rec.runInsert(narratorId, narratorName)
    count += 1
    if count > 100:
      count = 0
      conn.commit()
  if count > 0:
    conn.commit()

def derive_comment(book):
   n = book.description.rfind('. ', 0, 256)
   if n > 0:
     return book.description[:n]
   return book.description[:80]

'''
authorId 
bookId 
partNo 
bookName 
fileName 
album 
authors 
narrators 
comment 
description 

filename 
sti 
aacr 
aart 
atnu 
cdek 
cdet 
cprt 
guid 
prid 
released 
vers 
album 
author 
comment 
atday 
description 
genre 
name 
narrator 
publisher 
'''
def get_partno(book):
  for field in (book.name, book.filename):
    result = re.search(r'.*(part).?([0-9]+)',field.lower())
    if result == None: continue
    print (result.group(2))
    return result.group(2)
  return '0'

def add_books():
  global conn
  conn.rollback()
  count = 0
  for book in books:
    rec = DBBook(conn)
    rec.authorId = book.authorId
    rec.bookId = book.bookId
    rec.partNo = get_partno(book)
    rec.bookName = book.name
    rec.fileName = book.filename
    rec.album = book.album
    rec.authors = book.author 
    rec.narrators = book.narrator
    rec.comment = derive_comment(book)
    rec.description = book.description
    try:
      print (rec.authorId, rec.bookId, rec.bookName)
      rec.execInsert()
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
  for i, author in enumerate(arr):
    id = make_id(author)
    if i == 0:
      result = id
    if not id in authors:
      authors[id] = author.strip()
  return result

def do_narrator(data):
  arr = data.split(',')
  for i, narrator in enumerate(arr):
    id = make_id(narrator)
    if i == 0:
      result = id
    if not id in narrators:
      narrators[id] = narrator.strip()
  return result

def do_book(book):
  book.bookId = make_id(book.filename)
  
def process(book):
  book.authorId = do_author(book.author)
  if hasattr(book, 'narrator') == False:
      book.narrator = book.author
  book.narratorId = do_narrator(book.narrator)
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
  for book in books:
    process(book)
  #add_authors()
  #add_narrators()
  add_books()
  end_time = time.time()
  print (f'seconds:{end_time - start_time}')
  with open(rf'{pyasdata_dir}\ids_list.txt', 'wt') as ofile:
    for key in sorted(ids):
      data = repr(ids[key]).replace("['",'').replace("']",'').replace("', '",'|')
      ofile.write(f'{key}={data}\n')
