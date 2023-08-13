# This code was generated, do not modify it, modify it at source and regenerate it.
# see Word7 source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

Word7status = {}
Word7status['game'] = 0
Word7status['used'] = 1
Word7status['coll'] = 2
Word7status[0] = 'game'
Word7status[1] = 'used'
Word7status[2] = 'coll'

class DWord7():
    word: Char(8, pkey=True)
    status: Int(4)
    def _make(self): return DWord7()
    __slots__ = ['word',
        'status']
    def __init__(self):
        self.word = ''
        self.status = ''
    def _fields(self):
        return DWord7.__slots__

class Word7Insert(DWord7):
    def __init__(self):
        DWord7.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Word7 (
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

class Word7Update(DWord7):
    def __init__(self):
        DWord7.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Word7
 set
  status = @status
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status,
            self.word])

class Word7SelectOne(DWord7):
    def _get_output(self, _result):
        self.status = _result[0]
        return 1
    def execute(self, connect): # selectOne
        _command = f'''\
select
  status
 from Word7
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

class Word7SelectAll(DWord7):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, status
 from Word7
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word7SelectAll()
            record._get_output(row)
            records.append(record)
        return records

class Word7SelectAllSorted(DWord7):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAllSorted
        _command = f'''\
select
  word
, status
 from Word7
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word7SelectAllSorted()
            record._get_output(row)
            records.append(record)
        return records

class Word7ByStatus(DWord7):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # byStatus
        _command = f'''\
select
  word
, status
 from Word7
 where status = @status
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status])
        records = []
        for row in cursor:
            record = Word7ByStatus()
            record._get_output(row)
            records.append(record)
        return records

