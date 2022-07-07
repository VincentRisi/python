from INTRINSICS import *
### generated code from DBPortal ###

class DBBankCorrespondents(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'Correspondent', 'CreateDate', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.Correspondent = ''
    self.CreateDate = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.Correspondent = result[2]
    self.CreateDate = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.Correspondent, self.CreateDate, self.USId, self.TmStamp]
  def _fields(self):
    return 'SwiftAddress|CurrId|Correspondent|CreateDate|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('BankCorrespondentsInsert', self._data())
    self._store(result)
  def runInsert(self, SwiftAddress, CurrId, Correspondent, CreateDate, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.Correspondent = Correspondent
    self.CreateDate = CreateDate
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('BankCorrespondentsUpdate', self._data())
    self._store(result)
  def runUpdate(self, SwiftAddress, CurrId, Correspondent, CreateDate, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.Correspondent = Correspondent
    self.CreateDate = CreateDate
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('BankCorrespondentsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, SwiftAddress, CurrId, Correspondent):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.Correspondent = Correspondent
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBBankCorrespondentsDeleteOne(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'Correspondent']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.Correspondent = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.Correspondent = result[2]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.Correspondent]
  def _fields(self):
    return 'SwiftAddress|CurrId|Correspondent'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('BankCorrespondentsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, SwiftAddress, CurrId, Correspondent):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.Correspondent = Correspondent
    self.execDeleteOne()

class DBBankCorrespondentsGet(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'Correspondent']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.Correspondent = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.Correspondent = result[2]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.Correspondent]
  def _fields(self):
    return 'SwiftAddress|CurrId|Correspondent'.split('|')
  def queryGet(self):
    self._query = self._connect.query('BankCorrespondentsGet', self._data())
  def fetchGet(self):
    rc, result = self._connect.fetch(self._query)
    record = DBBankCorrespondentsGet(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGet(self):
    self._connect.cancel(self._query)
  def loadGet(self):
    self.queryGet()
    result = []
    while 1:
      rc, rec = self.fetchGet()
      if rc == 0:
        break
      result.append(rec)
    return result

