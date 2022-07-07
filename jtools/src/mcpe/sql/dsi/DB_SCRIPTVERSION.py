from INTRINSICS import *
### generated code from DBPortal ###

ScriptVersionVersionTypeConst = {
  'Test' : 0, 0 : 'Test',
  'QA' : 1, 1 : 'QA',
  'Live' : 2, 2 : 'Live',
  'Expired' : 3, 3 : 'Expired',
  }
class DBScriptVersion(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'Version', 'IDELock', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.Version = 0
    self.IDELock = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.Version = result[2]
    self.IDELock = result[3]
    self.USId = result[4]
    self.Tmstamp = result[5]
  def _data(self):
    return [self.Name, self.VersionType, self.Version, self.IDELock, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Name|VersionType|Version|IDELock|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('ScriptVersionInsert', self._data())
    self._store(result)
  def runInsert(self, Name, VersionType, Version, IDELock, USId, Tmstamp):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.IDELock = IDELock
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execSelectOne(self):
    result = self._connect.action('ScriptVersionSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name, VersionType):
    self.Name = Name
    self.VersionType = VersionType
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
    self._query = self._connect.query('ScriptVersionSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptVersion(self._connect)
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
  def execUpdate(self):
    result = self._connect.action('ScriptVersionUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, VersionType, Version, IDELock, USId, Tmstamp):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.IDELock = IDELock
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()

class DBScriptVersionDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
  def _data(self):
    return [self.Name, self.VersionType]
  def _fields(self):
    return 'Name|VersionType'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('ScriptVersionDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name, VersionType):
    self.Name = Name
    self.VersionType = VersionType
    self.execDeleteOne()

