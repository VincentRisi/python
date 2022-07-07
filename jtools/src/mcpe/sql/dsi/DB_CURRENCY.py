from INTRINSICS import *
### generated code from DBPortal ###

CurrencyStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  }
class DBCurrency(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Comments', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Comments = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Comments = result[2]
    self.Status = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.Id, self.Descr, self.Comments, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Descr|Comments|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('CurrencyInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Descr, Comments, Status, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.Comments = Comments
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('CurrencyUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Descr, Comments, Status, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.Comments = Comments
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('CurrencySelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id):
    self.Id = Id
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
    self._query = self._connect.query('CurrencySelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBCurrency(self._connect)
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

class DBCurrencyDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
  def _data(self):
    return [self.Id]
  def _fields(self):
    return 'Id'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('CurrencyDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBCurrencyUpdAllStatus(object):
  __slots__ = ['_connect', '_query', 'inStatus']
  def __init__(self, connect=None):
    self._connect = connect
    self.inStatus = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inStatus = result[0]
  def _data(self):
    return [self.inStatus]
  def _fields(self):
    return 'inStatus'.split('|')
  def execUpdAllStatus(self):
    result = self._connect.action('CurrencyUpdAllStatus', self._data())
    self._store(result)
  def runUpdAllStatus(self, inStatus):
    self.inStatus = inStatus
    self.execUpdAllStatus()

