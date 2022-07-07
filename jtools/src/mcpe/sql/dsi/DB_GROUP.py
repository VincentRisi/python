from INTRINSICS import *
### generated code from DBPortal ###

class DBGrps(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'Name', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.Name = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.Name = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.GroupId, self.Name, self.USId, self.TmStamp]
  def _fields(self):
    return 'GroupId|Name|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('GrpsInsert', self._data())
    self._store(result)
  def runInsert(self, GroupId, Name, USId, TmStamp):
    self.GroupId = GroupId
    self.Name = Name
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('GrpsUpdate', self._data())
    self._store(result)
  def runUpdate(self, GroupId, Name, USId, TmStamp):
    self.GroupId = GroupId
    self.Name = Name
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def querySelectAll(self):
    self._query = self._connect.query('GrpsSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBGrps(self._connect)
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
  def execSelectOne(self):
    result = self._connect.action('GrpsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, GroupId):
    self.GroupId = GroupId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBGrpsDeleteOne(object):
  __slots__ = ['_connect', '_query', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
  def _data(self):
    return [self.GroupId]
  def _fields(self):
    return 'GroupId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('GrpsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, GroupId):
    self.GroupId = GroupId
    self.execDeleteOne()

class DBGrpsListAll(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.Name = result[1]
  def _data(self):
    return [self.GroupId, self.Name]
  def _fields(self):
    return 'GroupId|Name'.split('|')
  def queryListAll(self):
    self._query = self._connect.query('GrpsListAll', self._data())
  def fetchListAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBGrpsListAll(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelListAll(self):
    self._connect.cancel(self._query)
  def loadListAll(self):
    self.queryListAll()
    result = []
    while 1:
      rc, rec = self.fetchListAll()
      if rc == 0:
        break
      result.append(rec)
    return result

