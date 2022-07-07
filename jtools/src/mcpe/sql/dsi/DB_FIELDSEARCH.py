from INTRINSICS import *
### generated code from DBPortal ###

class DBFieldSearch(object):
  __slots__ = ['_connect', '_query', 'id', 'Tag', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.id = 0
    self.Tag = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.id = result[0]
    self.Tag = result[1]
    self.USId = result[2]
    self.Tmstamp = result[3]
  def _data(self):
    return [self.id, self.Tag, self.USId, self.Tmstamp]
  def _fields(self):
    return 'id|Tag|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FieldSearchInsert', self._data())
    self._store(result)
  def runInsert(self, id, Tag, USId, Tmstamp):
    self.id = id
    self.Tag = Tag
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execSelectOne(self):
    result = self._connect.action('FieldSearchSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, id):
    self.id = id
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
    self._query = self._connect.query('FieldSearchSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFieldSearch(self._connect)
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

class DBFieldSearchExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.id = result[1]
  def _data(self):
    return [self.Count, self.id]
  def _fields(self):
    return 'Count|id'.split('|')
  def execExists(self):
    result = self._connect.action('FieldSearchExists', self._data())
    self._store(result)
  def readExists(self, id):
    self.id = id
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBFieldSearchCount(object):
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
    result = self._connect.action('FieldSearchCount', self._data())
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

