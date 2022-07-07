from INTRINSICS import *
### generated code from DBPortal ###

class DBFigCorrespondentBankGetBySwiftList(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrId', 'RankType', 'Rank', 'SwiftAddress', 'Frequency', 'Counter', 'SwiftList']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrId = ''
    self.RankType = ''
    self.Rank = 0
    self.SwiftAddress = ''
    self.Frequency = 0
    self.Counter = 0
    self.SwiftList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrId = result[1]
    self.RankType = result[2]
    self.Rank = result[3]
    self.SwiftAddress = result[4]
    self.Frequency = result[5]
    self.Counter = result[6]
    self.SwiftList = result[7]
  def _data(self):
    return [self.Country, self.CurrId, self.RankType, self.Rank, self.SwiftAddress, self.Frequency, self.Counter, self.SwiftList]
  def _fields(self):
    return 'Country|CurrId|RankType|Rank|SwiftAddress|Frequency|Counter|SwiftList'.split('|')
  def queryGetBySwiftList(self):
    self._query = self._connect.query('FigCorrespondentBankGetBySwiftList', self._data())
  def fetchGetBySwiftList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFigCorrespondentBankGetBySwiftList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetBySwiftList(self):
    self._connect.cancel(self._query)
  def loadGetBySwiftList(self):
    self.queryGetBySwiftList()
    result = []
    while 1:
      rc, rec = self.fetchGetBySwiftList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBFigCorrespondentBankGetByCountry(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrId', 'RankType', 'Rank', 'SwiftAddress', 'Frequency', 'Counter']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrId = ''
    self.RankType = ''
    self.Rank = 0
    self.SwiftAddress = ''
    self.Frequency = 0
    self.Counter = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrId = result[1]
    self.RankType = result[2]
    self.Rank = result[3]
    self.SwiftAddress = result[4]
    self.Frequency = result[5]
    self.Counter = result[6]
  def _data(self):
    return [self.Country, self.CurrId, self.RankType, self.Rank, self.SwiftAddress, self.Frequency, self.Counter]
  def _fields(self):
    return 'Country|CurrId|RankType|Rank|SwiftAddress|Frequency|Counter'.split('|')
  def queryGetByCountry(self):
    self._query = self._connect.query('FigCorrespondentBankGetByCountry', self._data())
  def fetchGetByCountry(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFigCorrespondentBankGetByCountry(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetByCountry(self):
    self._connect.cancel(self._query)
  def loadGetByCountry(self):
    self.queryGetByCountry()
    result = []
    while 1:
      rc, rec = self.fetchGetByCountry()
      if rc == 0:
        break
      result.append(rec)
    return result

