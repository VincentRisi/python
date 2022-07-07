from INTRINSICS import *
### generated code from DBPortal ###

class DBStreamType(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.Id, self.Descr, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Descr|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StreamTypeInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Descr, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StreamTypeUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Descr, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StreamTypeSelectOne', self._data())
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
    self._query = self._connect.query('StreamTypeSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamType(self._connect)
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

class DBStreamTypeDeleteOne(object):
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
    result = self._connect.action('StreamTypeDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

