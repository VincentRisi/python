from sqlite3 import DatabaseError
import sys, os, os.path, re
from aaxlist import books
from math import ceil
class _obj: pass
import dbapi_util as util

from DB_BOOK import DBBook
from DB_COVER import DBCover
from DB_AUTHOR import DBAuthor
from DB_COAUTHORS import DBCoAuthors
from DB_NARRATOR import DBNarrator
from DB_CONARRATORS import DBCoNarrators
from DB_SERIES import DBSeries

authors = dict()
narrators = dict()
series = dict()
coauthors = list()
conarrators = list()
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

def add_narrators():
  global conn
  conn.rollback()
  count = 0
  for narratorId in narrators:
    narratorName = narrators[narratorId]
    rec = DBNarrator(conn)
    print (narratorId, narratorName)
    rec.runInsert(narratorId, narratorName)
    count += 1
    if count > 100:
      count = 0
      conn.commit()
  if count > 0:
    conn.commit()

def add_series():
  global conn
  conn.rollback()
  count = 0
  for seriesId in series:
    entry = series[seriesId]
    seriesName = entry.series
    rec = DBSeries(conn)
    print (seriesId, seriesName)
    rec.runInsert(seriesId, seriesName)
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
    if hasattr(book, 'series'):
      rec.seriesId = book.series_id
      rec.bookSeq = book.book[0:16]
    else:
      rec.seriesId = None
      rec.bookSeq = None
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

def add_coauthors():
  global conn
  conn.rollback()
  count = 0
  for entry in coauthors:
    bookId, authorId, no = entry
    if no == 0: continue
    rec = DBCoAuthors(conn)
    print (bookId, authorId, no)
    try:
      rec.runInsert(bookId, authorId, no)
      count += 1
      if count > 100:
        count = 0
        conn.commit()
    except:
      print ('ouch', bookId, authorId, no)
  if count > 0:
    conn.commit()

def add_conarrators():
  global conn
  conn.rollback()
  count = 0
  for entry in conarrators:
    bookId, narratorId, no = entry
    if no == 0: continue
    rec = DBCoNarrators(conn)
    print (bookId, narratorId, no)
    try:
      rec.runInsert(bookId, narratorId, no)
      count += 1
      if count > 100:
        count = 0
        conn.commit()
    except:
      print ('ouch', bookId, narratorId, no)
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

def do_narrator(data):
  data = data.replace(', and more','')
  data = data.replace(' and ',',').replace(' ','').replace('.','')
  arr = data.split(',')
  return_id = list()
  for narrator in arr:
    id = make_id(narrator)
    return_id.append(id)
    if  not id in narrators:
      narrators[id] = narrator
    return return_id

def do_author(data):
  data = data.replace(', and more','')
  n = data.find(' and ')
  if n > 0:
    b = data.find('(')
    e = data.find(')')
    if b > 0 and e > 0 and n > b and n < e:
      data = data.replace(' and ', ':')
  data = data.replace(' and ',',').replace(' ','').replace('.','')
  arr = data.split(',')
  return_id = list()
  extras = list()
  for author in arr:
    author, extra = get_extra(author)
    id = make_id(author)
    return_id.append(id)
    if not id in authors:
      a = _obj() 
      authors[id] = a
      a.author = author
      a.extra = list()
    else:
      a = authors[id]
    if len(extra) > 0:
      a.extra.append(extra)
  return return_id

def do_book(book):
  data = book.album.replace(' and ',',').replace(' ','').replace('.','').replace(':','')
  book.id = make_id(data)
  if hasattr(book, 'series') == False:
    book.series = data
    book.book = 'Single'
  book.series_id = make_id(book.series)
  if not book.series_id in series:
    s = _obj()
    series[book.series_id] = s
    s.series = book.series
  
def process(book):
  ids = do_author(book.author)
  book.authors = ids
  if hasattr(book, 'narrator'):
    ids = do_narrator(book.narrator)
  else:
    ids = do_narrator('Audible')
  book.narrators = ids
  do_book(book)

def set_connect(_conn):
  global conn
  conn = _conn

import time
def main(pyasdata_dir):
  start_time = time.time()
  global conn
  #print (dir(conn))
  if os.path.exists(rf'{pyasdata_dir}\ids_list.txt'):
    with open(rf'{pyasdata_dir}\ids_list.txt', 'rt') as ifile:
      lines=ifile.readlines()
    for line in lines:
      key, data = line[:-1].split('=')
      ids[key] = data.split('|')
  for bk in books:
    book = books[bk]
    process(book)
    if len(book.authors) > 1:
      for i, a in enumerate(book.authors):
        coauthors.append([book.id,a,i])
    if len(book.narrators) > 1:
      for i, n in enumerate(book.narrators):
        conarrators.append([book.id,n,i])
  for au in sorted(authors):
    author = authors[au]
    print (au, author.author, author.extra)
  for nr in sorted(narrators):
    narrator = narrators[nr]
    print (nr, narrator)
  for ss in sorted(series):
    obj = series[ss]
    print (ss, obj.series)
  add_authors()
  add_narrators()
  add_series()
  add_books()
  add_coauthors()
  add_conarrators()
  end_time = time.time()
  print (f'seconds:{end_time - start_time}')
  with open(rf'{pyasdata_dir}\ids_list.txt', 'wt') as ofile:
    for key in sorted(ids):
      data = repr(ids[key]).replace("['",'').replace("']",'').replace("', '",'|')
      ofile.write(f'{key}={data}\n')
