# This code was generated, do not modify it, modify it at source and regenerate it.
# see Word8 source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

Word8status = {}
Word8status['game'] = 0
Word8status['used'] = 1
Word8status['coll'] = 2
Word8status[0] = 'game'
Word8status[1] = 'used'
Word8status[2] = 'coll'

class DWord8():
    word: Char(9, pkey=True)
    status: Int(4)
    def _make(self): return DWord8()
    __slots__ = ['word',
        'status']
    def __init__(self):
        self.word = ''
        self.status = ''
    def _fields(self):
        return DWord8.__slots__

class Word8Insert(DWord8):
    def __init__(self):
        DWord8.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Word8 (
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

class Word8Update(DWord8):
    def __init__(self):
        DWord8.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Word8
 set
  status = @status
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status,
            self.word])

class Word8SelectOne(DWord8):
    def _get_output(self, _result):
        self.status = _result[0]
        return 1
    def execute(self, connect): # selectOne
        _command = f'''\
select
  status
 from Word8
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

class Word8SelectAll(DWord8):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, status
 from Word8
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word8SelectAll()
            record._get_output(row)
            records.append(record)
        return records

class Word8SelectAllSorted(DWord8):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # selectAllSorted
        _command = f'''\
select
  word
, status
 from Word8
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = Word8SelectAllSorted()
            record._get_output(row)
            records.append(record)
        return records

class Word8ByStatus(DWord8):
    def _get_output(self, _result):
        self.word = _result[0]
        self.status = _result[1]
        return 2
    def execute(self, connect): # byStatus
        _command = f'''\
select
  word
, status
 from Word8
 where status = @status
 order by word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.status])
        records = []
        for row in cursor:
            record = Word8ByStatus()
            record._get_output(row)
            records.append(record)
        return records

