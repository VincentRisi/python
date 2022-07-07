from INTRINSICS import *
### generated code from DBPortal ###

ScriptsVersionTypeConst = {
  'Test' : 0, 0 : 'Test',
  'QA' : 1, 1 : 'QA',
  'Live' : 2, 2 : 'Live',
  'Expired' : 3, 3 : 'Expired',
  }
ScriptsStoreTypeConst = {
  'Source' : 0, 0 : 'Source',
  'Description' : 1, 1 : 'Description',
  'Compiled' : 2, 2 : 'Compiled',
  'Compressed' : 3, 3 : 'Compressed',
  }
class DBScripts(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'Version', 'StoreType', 'Part', 'OfParts', 'Content', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.Version = 0
    self.StoreType = 0
    self.Part = 0
    self.OfParts = 0
    self.Content = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.Version = result[2]
    self.StoreType = result[3]
    self.Part = result[4]
    self.OfParts = result[5]
    self.Content = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.Name, self.VersionType, self.Version, self.StoreType, self.Part, self.OfParts, self.Content, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Name|VersionType|Version|StoreType|Part|OfParts|Content|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('ScriptsInsert', self._data())
    self._store(result)
  def runInsert(self, Name, VersionType, Version, StoreType, Part, OfParts, Content, USId, Tmstamp):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.StoreType = StoreType
    self.Part = Part
    self.OfParts = OfParts
    self.Content = Content
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execSelectOne(self):
    result = self._connect.action('ScriptsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name, Version, StoreType, Part):
    self.Name = Name
    self.Version = Version
    self.StoreType = StoreType
    self.Part = Part
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
    self._query = self._connect.query('ScriptsSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScripts(self._connect)
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
    result = self._connect.action('ScriptsUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, VersionType, Version, StoreType, Part, OfParts, Content, USId, Tmstamp):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.StoreType = StoreType
    self.Part = Part
    self.OfParts = OfParts
    self.Content = Content
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()

class DBScriptsDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Name', 'Version', 'StoreType', 'Part']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Version = 0
    self.StoreType = 0
    self.Part = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Version = result[1]
    self.StoreType = result[2]
    self.Part = result[3]
  def _data(self):
    return [self.Name, self.Version, self.StoreType, self.Part]
  def _fields(self):
    return 'Name|Version|StoreType|Part'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('ScriptsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name, Version, StoreType, Part):
    self.Name = Name
    self.Version = Version
    self.StoreType = StoreType
    self.Part = Part
    self.execDeleteOne()

class DBScriptsVersions(object):
  __slots__ = ['_connect', '_query', 'Name', 'Version', 'Removed', 'Active', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Version = 0
    self.Removed = 0
    self.Active = 0
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Version = result[1]
    self.Removed = result[2]
    self.Active = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Name, self.Version, self.Removed, self.Active, self.TmStamp]
  def _fields(self):
    return 'Name|Version|Removed|Active|TmStamp'.split('|')
  def queryVersions(self):
    self._query = self._connect.query('ScriptsVersions', self._data())
  def fetchVersions(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsVersions(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelVersions(self):
    self._connect.cancel(self._query)
  def loadVersions(self):
    self.queryVersions()
    result = []
    while 1:
      rc, rec = self.fetchVersions()
      if rc == 0:
        break
      result.append(rec)
    return result

