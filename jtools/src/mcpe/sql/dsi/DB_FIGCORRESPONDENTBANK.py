from INTRINSICS import *
### generated code from DBPortal ###

class DBFigCorrespondentBank(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrId', 'RankType', 'Rank', 'SwiftAddress', 'Frequency', 'Counter', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrId = ''
    self.RankType = ''
    self.Rank = 0
    self.SwiftAddress = ''
    self.Frequency = 0
    self.Counter = 0
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
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
    self.Status = result[7]
    self.USId = result[8]
    self.TmStamp = result[9]
  def _data(self):
    return [self.Country, self.CurrId, self.RankType, self.Rank, self.SwiftAddress, self.Frequency, self.Counter, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Country|CurrId|RankType|Rank|SwiftAddress|Frequency|Counter|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FigCorrespondentBankInsert', self._data())
    self._store(result)
  def runInsert(self, Country, CurrId, RankType, Rank, SwiftAddress, Frequency, Counter, Status, USId, TmStamp):
    self.Country = Country
    self.CurrId = CurrId
    self.RankType = RankType
    self.Rank = Rank
    self.SwiftAddress = SwiftAddress
    self.Frequency = Frequency
    self.Counter = Counter
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('FigCorrespondentBankUpdate', self._data())
    self._store(result)
  def runUpdate(self, Country, CurrId, RankType, Rank, SwiftAddress, Frequency, Counter, Status, USId, TmStamp):
    self.Country = Country
    self.CurrId = CurrId
    self.RankType = RankType
    self.Rank = Rank
    self.SwiftAddress = SwiftAddress
    self.Frequency = Frequency
    self.Counter = Counter
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('FigCorrespondentBankSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Country, CurrId, RankType, SwiftAddress):
    self.Country = Country
    self.CurrId = CurrId
    self.RankType = RankType
    self.SwiftAddress = SwiftAddress
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('FigCorrespondentBankSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFigCorrespondentBank(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectAll(self):
    self._connect.cancel(self._query)
  def loadSelectAll(self):
    self.querySelectAll()
    result = []
    while 1:
      rc, rec = self.fetchSelectAll()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBFigCorrespondentBankDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrId', 'RankType', 'SwiftAddress']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrId = ''
    self.RankType = ''
    self.SwiftAddress = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrId = result[1]
    self.RankType = result[2]
    self.SwiftAddress = result[3]
  def _data(self):
    return [self.Country, self.CurrId, self.RankType, self.SwiftAddress]
  def _fields(self):
    return 'Country|CurrId|RankType|SwiftAddress'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('FigCorrespondentBankDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Country, CurrId, RankType, SwiftAddress):
    self.Country = Country
    self.CurrId = CurrId
    self.RankType = RankType
    self.SwiftAddress = SwiftAddress
    self.execDeleteOne()

