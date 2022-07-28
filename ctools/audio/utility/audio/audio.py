import sys, os, os.path, re
from aaxlist import books
class _obj: pass

from DB_BOOK import DBBook
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
      rec.seriesId = book.series
      rec.bookSeq = book.book
    else:
      rec.seriesId = ''
      rec.bookSeq = ''
    if hasattr(book, 'comment'):
      rec.comment = book.comment
    else:
      rec.comment = ''
    rec.description = book.description
    if hasattr(book, 'genre'):
      rec.genre = book.genre
    else:
      rec.genre = ''
    if hasattr(book, 'released'):
      rec.released = book.released
    else:
      rec.released = ''
    rec.execInsert()
    count += 1
    if count > 100:
      count = 0
      conn.commit()
  if count > 0:
    conn.commit()
 

def make_id(data):
  r = re.findall('([A-Z])', data)
  if len(r) > 0:
    x = ''.join(r)
  elif len(data) > 0:
    x = data.replace(')','')
  else:
    x = 'ANON'
  key = x[:7]
  r = re.findall('([A-Za-z0-9])', data)
  if len(r) > 0:
    x = ''.join(r)
  elif len(data) > 0:
    x = data.replace(')','')
  else:
    x = 'ANON'
  data = x
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
  data = book.album.replace(' and ',',').replace(' ','').replace('.','')
  book.id = make_id(data)
  if hasattr(book, 'series'):
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
  book.narrators = ids
  do_book(book)

def set_connect(_conn):
  global conn
  conn = _conn

def main(pyasdata_dir):
  global conn
  print (dir(conn))
  if os.path.exists(rf'{pyasdata_dir}\ids_list.py'):
    from ids_list import ids
  for bk in books:
    book = books[bk]
    process(book)
    for a in book.authors:
      coauthors.append([book.id,a])
    for n in book.narrators:
      conarrators.append([book.id,n])
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
  with open(rf'{pyasdata_dir}\ids_list.py', 'wt') as ofile:
    ofile.write('ids = dict()\n')
    for key in sorted(ids):
      x = repr(ids[key])
      ofile.write(f'ids[{repr(key)}]={x}\n')
