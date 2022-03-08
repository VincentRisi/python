import sys
sys.path.append(r'C:\vlab\python\ctools\audio\utility\audio\pyasdata')
sys.path.append(r'C:\vlab\python\ctools\audio\utility\audio\generated')
import re
from aaxlist import books
class _obj: pass

authors = dict()
ids = dict()

def make_id(data):
  r = re.findall('([A-Z])', data)
  if len(r) > 0:
    x = ''.join(r)
  elif len(data) > 0:
    x = data.replace(')','')
  else:
    x = 'ANON'
  key = x[:8]
  if not key in ids:
    ids[key] = list()
  if not data in ids[key]:
    ids[key].append(data)
  n = ids[key].index(data)
  return '%s%02d' % (key, n+1)

def get_extras(a, author):
  n = author.find('(')
  if n > 0:
    a.extra += author[n+1:-1]
    author = author[:n]
  n = author.find('-')
  if n > 0:
    a.extra += author[n+1:]
    author = author[:n]
  return author

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
  for i, author in enumerate(arr):
    _a = _obj()
    _a.extra = ''
    author = get_extras(_a, author)
    _a.id = make_id(author)
    if i == 0:
      return_id = _a.id
    if not author in authors: 
      authors[author]=_a
    elif len(_a.extra) > 0 and not _a.extra in authors[author].extra:
      authors[author].extra += ' %s' % _a.extra
  return return_id

def do_book(book):
  data = book.album.replace(' and ',',').replace(' ','').replace('.','')
  book.id = make_id(data)
  print (book.id, book.album, book.filename, book.authorId)

def process(book):
  id = do_author(book.author)
  book.authorId = id
  do_book(book)

def main():
  for k in books:
    book = books[k]
    process(book)
  for author in authors:
    print (author, authors[author].id, authors[author].extra)
main()
