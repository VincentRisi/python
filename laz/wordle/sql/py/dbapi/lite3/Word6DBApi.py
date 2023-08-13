# This code was generated, do not modify it, modify it at source and regenerate it.
# see Word6 source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

Word6status = {}
Word6status['game'] = 0
Word6status['used'] = 1
Word6status['coll'] = 2
Word6status[0] = 'game'
Word6status[1] = 'used'
Word6status[2] = 'coll'

class DWord6():
    word: Char(7, pkey=True)
    status: Int(4)
    def _make(self): return DWord6()
    __slots__ = ['word',
        'status']
    def __init__(self):
        self.word = ''
        self.status = ''
    def _fields(self):
        return DWord6.__slots__

class Word6Insert(DWord6):
    def __init__(self):
        DWord6.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Word6 (
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

class Word6Update(DWord6):
    def __init__(self):
        DWord6.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Word6
 set
  status = @status
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status,
            self.word])

class Word6SelectOne(DWord6):
    def _get_output(self, _result):
        self.status = _result[0]
        return 1
    def execute(self, connect): # selectOne
        _command = f'''\
select
  status
 from Word6
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.word])
        result = cursor.fetchone()
        if result == None:
            return False
        self._get_output(result)
        return True

class Word6SelectAll(DWord6):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, status
 from Word6
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word6SelectAll()
            record._get_output(row)
            records.append(record)
        return records

class Word6SelectAllSorted(DWord6):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAllSorted
        _command = f'''\
select
  word
, status
 from Word6
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word6SelectAllSorted()
            record._get_output(row)
            records.append(record)
        return records

class Word6ByStatus(DWord6):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # byStatus
        _command = f'''\
select
  word
, status
 from Word6
 where status = @status
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status])
        records = []
        for row in cursor:
            record = Word6ByStatus()
            record._get_output(row)
            records.append(record)
        return records

