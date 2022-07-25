import sys, os, os.path, re
from aaxlist import books
class _obj: pass

authors = dict()
narrators = dict()
series = dict()
coauthors = list()
conarrators = list()
ids = dict()

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

def run(con, command):
  cursor = con.cursor()
  cursor.execute(command.replace('main.',''))

def make_tables():
  table_sql = (r'C:\vlab\python\jtools\out\audio\sql\ddl\mssql\audio.sql')
  con = sqmssql.connect(r'C:\vlab\python\ctools\audio\utility\audio\books.db')
  with open(table_sql, 'rt') as ifile: lines = ifile.readlines()
  NONE, START, NEXT = range(3) 
  state = START
  command = ''
  for line in lines:
    line = line.rstrip()
    if len(line) == 0:
      state = START
      command = ''
      continue
    if state == START:
      command += f'{line}\n'
      if line[-1] == ';':
        run (con, command)
        state = NONE
      else:
        state = NEXT
      continue
    if state == NEXT:
      command += f'{line}\n'
      if line[-1] == ';':
        run (con, command)
        state = NONE

def main(pyasdata_dir):
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
  with open(rf'{pyasdata_dir}\ids_list.py', 'wt') as ofile:
    ofile.write('ids = dict()\n')
    for key in sorted(ids):
      x = repr(ids[key])
      ofile.write(f'ids[{repr(key)}]={x}\n')
