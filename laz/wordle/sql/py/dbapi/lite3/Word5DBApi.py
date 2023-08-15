# This code was generated, do not modify it, modify it at source and regenerate it.
# see Word5 source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

Word5status = {}
Word5status['game'] = 0
Word5status['used'] = 1
Word5status['coll'] = 2
Word5status[0] = 'game'
Word5status[1] = 'used'
Word5status[2] = 'coll'

class DWord5():
    word: Char(6, pkey=True)
    status: Int(4)
    def _make(self): return DWord5()
    __slots__ = ['word',
        'status']
    def __init__(self):
        self.word = ''
        self.status = ''
    def _fields(self):
        return DWord5.__slots__

class Word5Insert(DWord5):
    def __init__(self):
        DWord5.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Word5 (
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

class Word5Update(DWord5):
    def __init__(self):
        DWord5.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Word5
 set
  status = @status
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status,
            self.word])

class Word5SelectOne(DWord5):
    def _get_output(self, _result):
        self.status = _result[0]
        return 1
    def execute(self, connect): # selectOne
        _command = f'''\
select
  status
 from Word5
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

class Word5SelectAll(DWord5):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, status
 from Word5
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word5SelectAll()
            record._get_output(row)
            records.append(record)
        return records

class Word5SelectAllSorted(DWord5):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAllSorted
        _command = f'''\
select
  word
, status
 from Word5
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word5SelectAllSorted()
            record._get_output(row)
            records.append(record)
        return records

class Word5ListByStatus(DWord5):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # listByStatus
        _command = f'''\
select
  word
, status
 from Word5
 where status = @status
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status])
        records = []
        for row in cursor:
            record = Word5ListByStatus()
            record._get_output(row)
            records.append(record)
        return records

