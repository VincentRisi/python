# This code was generated, do not modify it, modify it at source and regenerate it.
# see Dictionary source file

import dbapi_util_lite3 as dbapi_util
from dbapi_annotate import *

class DDictionary():
    word: Char(9, pkey=True)
    meaning: Char(4097)
    def _make(self): return DDictionary()
    __slots__ = ['word',
        'meaning']
    def __init__(self):
        self.word = ''
        self.meaning = ''
    def _fields(self):
        return DDictionary.__slots__

class DDictionaryExists():
    word: Char(9, pkey=True)
    noOf: Int(4)
    def _make(self): return DDictionaryExists()
    __slots__ = ['word',
        'noOf']
    def __init__(self):
        self.word = ''
        self.noOf = ''
    def _fields(self):
        return DDictionaryExists.__slots__

class DictionaryInsert(DDictionary):
    def __init__(self):
        DDictionary.__init__(self)
    def execute(self, connect): # insert
        _command = f'''\
insert into Dictionary (
  word,
  meaning
 ) 
 values (
   @word,
   @meaning
 )
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.word,
            self.meaning])

class DictionaryUpdate(DDictionary):
    def __init__(self):
        DDictionary.__init__(self)
    def execute(self, connect): # update
        _command = f'''\
update Dictionary
 set
  meaning = @meaning
 where word = @word
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.meaning,
            self.word])

class DictionarySelectOne(DDictionary):
    def _get_output(self, _result):
        self.meaning = _result[0]
        return 1
    def execute(self, connect): # selectOne
        _command = f'''\
select
  meaning
 from Dictionary
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

class DictionaryExists(DDictionaryExists):
    def _get_output(self, _result):
        self.noOf = _result[0]
        return 1
    def execute(self, connect): # exists
        _command = f'''\
select count(*) noOf from Dictionary
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

class DictionarySelectAll(DDictionary):
    def _get_output(self, _result):
        self.word = _result[0]
        self.meaning = _result[1]
        return 2
    def execute(self, connect): # selectAll
        _command = f'''\
select
  word
, meaning
 from Dictionary
'''
        cursor = connect.cursor()
        cursor.execute(_command)
        records = []
        for row in cursor:
            record = DictionarySelectAll()
            record._get_output(row)
            records.append(record)
        return records

