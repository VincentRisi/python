from INTRINSICS import *
### generated code from DBPortal ###

class DBFieldSearchDef(object):
  __slots__ = ['_connect', '_query', 'Id', 'Tag', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Tag = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Tag = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.Id, self.Tag, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Tag|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FieldSearchDefInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Tag, USId, TmStamp):
    self.Id = Id
    self.Tag = Tag
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('FieldSearchDefUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Tag, USId, TmStamp):
    self.Id = Id
    self.Tag = Tag
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('FieldSearchDefSelectOne', self._data())
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
    self._query = self._connect.query('FieldSearchDefSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFieldSearchDef(self._connect)
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

class DBFieldSearchDefDeleteOne(object):
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
    result = self._connect.action('FieldSearchDefDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBFieldSearchDefCount(object):
  __slots__ = ['_connect', '_query', 'NoOf']
  def __init__(self, connect=None):
    self._connect = connect
    self.NoOf = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.NoOf = result[0]
  def _data(self):
    return [self.NoOf]
  def _fields(self):
    return 'NoOf'.split('|')
  def execCount(self):
    result = self._connect.action('FieldSearchDefCount', self._data())
    self._store(result)
  def readCount(self):
    try:
      self.execCount()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

