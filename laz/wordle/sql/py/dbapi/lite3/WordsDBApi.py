# This code was generated, do not modify it, modify it at source and regenerate it.
# see Words source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

Wordsstatus = {}
Wordsstatus['game'] = 0
Wordsstatus['used'] = 1
Wordsstatus['coll'] = 2
Wordsstatus[0] = 'game'
Wordsstatus[1] = 'used'
Wordsstatus[2] = 'coll'

class DWords():
    word: Char(6, pkey=True)
    status: Int(4)
    def _make(self): return DWords()
    __slots__ = ['word',
        'status']
    def __init__(self):
        self.word = ''
        self.status = ''
    def _fields(self):
        return DWords.__slots__

class WordsInsert(DWords):
    def __init__(self):
        DWords.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Words (
  word,
  status
 ) 
 values (
   @word,
   @status
 )
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.word,
            self.status])

class WordsUpdate(DWords):
    def __init__(self):
        DWords.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Words
 set
  status = @status
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status,
            self.word])

class WordsSelectAll(DWords):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, status
 from Words
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = WordsSelectAll()
            record._get_output(row)
            records.append(record)
        return records

