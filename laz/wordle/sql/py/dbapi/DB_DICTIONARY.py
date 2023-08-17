# This code was generated, do not modify it, modify it at source and regenerate it.
# see Dictionary source file

from DictionaryDBApi import *

class DBDictionary(DDictionary):
    def __init__(self, connect):
        DDictionary.__init__(self)
        self.connect = connect
    def set_connect(self, connect):
        self.connect = connect
    def execInsert(self):
        dbapi = DictionaryInsert()
        dbapi.word = self.word
        dbapi.meaning = self.meaning
        dbapi.execute(self.connect)
    def runInsert(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.execInsert()
    def execUpdate(self):
        dbapi = DictionaryUpdate()
        dbapi.meaning = self.meaning
        dbapi.word = self.word
        dbapi.execute(self.connect)
    def runUpdate(self, meaning, word):
        self.meaning = meaning
        self.word = word
        self.execUpdate()
    def execSelectOne(self):
        dbapi = DictionarySelectOne()
        dbapi.word = self.word
        rc, record = dbapi.readone(self.connect)
        if rc == False: return 0
        self.meaning = record.meaning
        return 1
    def readSelectOne(self, word):
        self.word = word
        return self.execSelectOne()
    def loadSelectAll(self):
        dbapi = DictionarySelectAll()
        records = dbapi.execute(self.connect)
        others = list()
        for rec in records:
            other = DDictionary()
            other.word = rec.word
            other.meaning = rec.meaning
            others.append(other)
        return others
    def execSelectAll(self):
        return self.loadSelectAll()

class DBDictionaryExists(DDictionaryExists):
    def __init__(self, connect):
        DDictionaryExists.__init__(self)
        self.connect = connect
    def set_connect(self, connect):
        self.connect = connect
    def execExists(self):
        dbapi = DictionaryExists()
        dbapi.word = self.word
        rc, record = dbapi.readone(self.connect)
        if rc == False: return 0
        self.noOf = record.noOf
        return 1
    def readExists(self, word):
        self.word = word
        return self.execExists()
