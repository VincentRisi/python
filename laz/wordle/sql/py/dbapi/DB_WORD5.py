# This code was generated, do not modify it, modify it at source and regenerate it.
# see Word5 source file

from Word5DBApi import *

Word5statusConst = Word5status

class DBWord5(DWord5):
    def __init__(self, connect):
        DWord5.__init__(self)
        self.connect = connect
    def set_connect(self, connect):
        self.connect = connect
    def execInsert(self):
        dbapi = Word5Insert()
        dbapi.word = self.word
        dbapi.status = self.status
        dbapi.execute(self.connect)
    def runInsert(self, word, status):
        self.word = word
        self.status = status
        self.execInsert()
    def execUpdate(self):
        dbapi = Word5Update()
        dbapi.status = self.status
        dbapi.word = self.word
        dbapi.execute(self.connect)
    def runUpdate(self, status, word):
        self.status = status
        self.word = word
        self.execUpdate()
    def execSelectOne(self):
        dbapi = Word5SelectOne()
        dbapi.word = self.word
        rc, record = dbapi.readone(self.connect)
        if rc == False: return 0
        self.status = record.status
        return 1
    def readSelectOne(self, word):
        self.word = word
        return self.execSelectOne()
    def loadSelectAll(self):
        dbapi = Word5SelectAll()
        records = dbapi.execute(self.connect)
        others = list()
        for rec in records:
            other = DWord5()
            other.word = rec.word
            other.status = rec.status
            others.append(other)
        return others
    def execSelectAll(self):
        return self.loadSelectAll()
    def loadSelectAllSorted(self):
        dbapi = Word5SelectAllSorted()
        records = dbapi.execute(self.connect)
        others = list()
        for rec in records:
            other = DWord5()
            other.word = rec.word
            other.status = rec.status
            others.append(other)
        return others
    def execSelectAllSorted(self):
        return self.loadSelectAllSorted()
    def loadListByStatus(self):
        dbapi = Word5ListByStatus()
        dbapi.status = self.status
        records = dbapi.execute(self.connect)
        others = list()
        for rec in records:
            other = DWord5()
            other.word = rec.word
            other.status = rec.status
            others.append(other)
        return others
    def execListByStatus(self, status):
        self.status = status
        return self.loadListByStatus()

class DBWord5DictList(DWord5DictList):
    def __init__(self, connect):
        DWord5DictList.__init__(self)
        self.connect = connect
    def set_connect(self, connect):
        self.connect = connect
    def loadDictList(self):
        dbapi = Word5DictList()
        records = dbapi.execute(self.connect)
        others = list()
        for rec in records:
            other = DWord5DictList()
            other.word = rec.word
            others.append(other)
        return others
    def execDictList(self):
        return self.loadDictList()
