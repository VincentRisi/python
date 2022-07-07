from INTRINSICS import *
### generated code from DBPortal ###

class DBScriptsList(object):
  __slots__ = ['_connect', '_query', 'VersionType', 'Name', 'Version']
  def __init__(self, connect=None):
    self._connect = connect
    self.VersionType = 0
    self.Name = ''
    self.Version = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.VersionType = result[0]
    self.Name = result[1]
    self.Version = result[2]
  def _data(self):
    return [self.VersionType, self.Name, self.Version]
  def _fields(self):
    return 'VersionType|Name|Version'.split('|')
  def queryList(self):
    self._query = self._connect.query('ScriptsList', self._data())
  def fetchList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelList(self):
    self._connect.cancel(self._query)
  def loadList(self):
    self.queryList()
    result = []
    while 1:
      rc, rec = self.fetchList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBScriptsStaffList(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'VersionType', 'Name', 'Version', 'AccessType']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.VersionType = 0
    self.Name = ''
    self.Version = 0
    self.AccessType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.VersionType = result[1]
    self.Name = result[2]
    self.Version = result[3]
    self.AccessType = result[4]
  def _data(self):
    return [self.StaffId, self.VersionType, self.Name, self.Version, self.AccessType]
  def _fields(self):
    return 'StaffId|VersionType|Name|Version|AccessType'.split('|')
  def queryStaffList(self):
    self._query = self._connect.query('ScriptsStaffList', self._data())
  def fetchStaffList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsStaffList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStaffList(self):
    self._connect.cancel(self._query)
  def loadStaffList(self):
    self.queryStaffList()
    result = []
    while 1:
      rc, rec = self.fetchStaffList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBScriptsStaffGroupList(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId', 'VersionType', 'Name', 'Version', 'AccessType']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
    self.VersionType = 0
    self.Name = ''
    self.Version = 0
    self.AccessType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
    self.VersionType = result[2]
    self.Name = result[3]
    self.Version = result[4]
    self.AccessType = result[5]
  def _data(self):
    return [self.StaffId, self.GroupId, self.VersionType, self.Name, self.Version, self.AccessType]
  def _fields(self):
    return 'StaffId|GroupId|VersionType|Name|Version|AccessType'.split('|')
  def queryStaffGroupList(self):
    self._query = self._connect.query('ScriptsStaffGroupList', self._data())
  def fetchStaffGroupList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsStaffGroupList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStaffGroupList(self):
    self._connect.cancel(self._query)
  def loadStaffGroupList(self):
    self.queryStaffGroupList()
    result = []
    while 1:
      rc, rec = self.fetchStaffGroupList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBScriptsCheck(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'NoOf']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.NoOf = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.NoOf = result[2]
  def _data(self):
    return [self.Name, self.VersionType, self.NoOf]
  def _fields(self):
    return 'Name|VersionType|NoOf'.split('|')
  def execCheck(self):
    result = self._connect.action('ScriptsCheck', self._data())
    self._store(result)
  def readCheck(self, Name, VersionType):
    self.Name = Name
    self.VersionType = VersionType
    try:
      self.execCheck()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBScriptsAdd(object):
  __slots__ = ['_connect', '_query', 'InName', 'InVersionType', 'InUSId', 'OutVersion', 'OutTmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InName = ''
    self.InVersionType = 0
    self.InUSId = ''
    self.OutVersion = 0
    self.OutTmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InName = result[0]
    self.InVersionType = result[1]
    self.InUSId = result[2]
    self.OutVersion = result[3]
    self.OutTmstamp = result[4]
  def _data(self):
    return [self.InName, self.InVersionType, self.InUSId, self.OutVersion, self.OutTmstamp]
  def _fields(self):
    return 'InName|InVersionType|InUSId|OutVersion|OutTmstamp'.split('|')
  def execAdd(self):
    result = self._connect.action('ScriptsAdd', self._data())
    self._store(result)
  def runAdd(self, InName, InVersionType, InUSId, OutVersion, OutTmstamp):
    self.InName = InName
    self.InVersionType = InVersionType
    self.InUSId = InUSId
    self.OutVersion = OutVersion
    self.OutTmstamp = OutTmstamp
    self.execAdd()

class DBScriptsRemove(object):
  __slots__ = ['_connect', '_query', 'InName', 'InVersionType', 'IOVersion', 'InUSId', 'OutTmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InName = ''
    self.InVersionType = 0
    self.IOVersion = 0
    self.InUSId = ''
    self.OutTmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InName = result[0]
    self.InVersionType = result[1]
    self.IOVersion = result[2]
    self.InUSId = result[3]
    self.OutTmstamp = result[4]
  def _data(self):
    return [self.InName, self.InVersionType, self.IOVersion, self.InUSId, self.OutTmstamp]
  def _fields(self):
    return 'InName|InVersionType|IOVersion|InUSId|OutTmstamp'.split('|')
  def execRemove(self):
    result = self._connect.action('ScriptsRemove', self._data())
    self._store(result)
  def runRemove(self, InName, InVersionType, IOVersion, InUSId, OutTmstamp):
    self.InName = InName
    self.InVersionType = InVersionType
    self.IOVersion = IOVersion
    self.InUSId = InUSId
    self.OutTmstamp = OutTmstamp
    self.execRemove()

class DBScriptsPromote(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'Version', 'USId', 'Tmstamp', 'NewVersion']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.Version = 0
    self.USId = ''
    self.Tmstamp = ''
    self.NewVersion = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.Version = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
    self.NewVersion = result[5]
  def _data(self):
    return [self.Name, self.VersionType, self.Version, self.USId, self.Tmstamp, self.NewVersion]
  def _fields(self):
    return 'Name|VersionType|Version|USId|Tmstamp|NewVersion'.split('|')
  def execPromote(self):
    result = self._connect.action('ScriptsPromote', self._data())
    self._store(result)
  def runPromote(self, Name, VersionType, Version, USId, Tmstamp, NewVersion):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.NewVersion = NewVersion
    self.execPromote()

class DBScriptsSaveAs(object):
  __slots__ = ['_connect', '_query', 'Name', 'NewName', 'VersionType', 'Version', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.NewName = ''
    self.VersionType = 0
    self.Version = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.NewName = result[1]
    self.VersionType = result[2]
    self.Version = result[3]
    self.USId = result[4]
    self.Tmstamp = result[5]
  def _data(self):
    return [self.Name, self.NewName, self.VersionType, self.Version, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Name|NewName|VersionType|Version|USId|Tmstamp'.split('|')
  def execSaveAs(self):
    result = self._connect.action('ScriptsSaveAs', self._data())
    self._store(result)
  def runSaveAs(self, Name, NewName, VersionType, Version, USId, Tmstamp):
    self.Name = Name
    self.NewName = NewName
    self.VersionType = VersionType
    self.Version = Version
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execSaveAs()

class DBScriptsRead(object):
  __slots__ = ['_connect', '_query', 'Name', 'StoreType', 'VersionType', 'Version', 'Part', 'OfParts', 'Content']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.StoreType = 0
    self.VersionType = 0
    self.Version = 0
    self.Part = 0
    self.OfParts = 0
    self.Content = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.StoreType = result[1]
    self.VersionType = result[2]
    self.Version = result[3]
    self.Part = result[4]
    self.OfParts = result[5]
    self.Content = result[6]
  def _data(self):
    return [self.Name, self.StoreType, self.VersionType, self.Version, self.Part, self.OfParts, self.Content]
  def _fields(self):
    return 'Name|StoreType|VersionType|Version|Part|OfParts|Content'.split('|')
  def queryRead(self):
    self._query = self._connect.query('ScriptsRead', self._data())
  def fetchRead(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsRead(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelRead(self):
    self._connect.cancel(self._query)
  def loadRead(self):
    self.queryRead()
    result = []
    while 1:
      rc, rec = self.fetchRead()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBScriptsWrite(object):
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
  def execWrite(self):
    result = self._connect.action('ScriptsWrite', self._data())
    self._store(result)
  def runWrite(self, Name, VersionType, Version, StoreType, Part, OfParts, Content, USId, Tmstamp):
    self.Name = Name
    self.VersionType = VersionType
    self.Version = Version
    self.StoreType = StoreType
    self.Part = Part
    self.OfParts = OfParts
    self.Content = Content
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execWrite()

class DBScriptsLoad(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'StoreType', 'Version', 'Part', 'OfParts', 'Content']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.StoreType = 0
    self.Version = 0
    self.Part = 0
    self.OfParts = 0
    self.Content = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.StoreType = result[2]
    self.Version = result[3]
    self.Part = result[4]
    self.OfParts = result[5]
    self.Content = result[6]
  def _data(self):
    return [self.Name, self.VersionType, self.StoreType, self.Version, self.Part, self.OfParts, self.Content]
  def _fields(self):
    return 'Name|VersionType|StoreType|Version|Part|OfParts|Content'.split('|')
  def queryLoad(self):
    self._query = self._connect.query('ScriptsLoad', self._data())
  def fetchLoad(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsLoad(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelLoad(self):
    self._connect.cancel(self._query)
  def loadLoad(self):
    self.queryLoad()
    result = []
    while 1:
      rc, rec = self.fetchLoad()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBScriptsSetLockStatus(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'IDELock']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.IDELock = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.IDELock = result[2]
  def _data(self):
    return [self.Name, self.VersionType, self.IDELock]
  def _fields(self):
    return 'Name|VersionType|IDELock'.split('|')
  def execSetLockStatus(self):
    result = self._connect.action('ScriptsSetLockStatus', self._data())
    self._store(result)
  def runSetLockStatus(self, Name, VersionType, IDELock):
    self.Name = Name
    self.VersionType = VersionType
    self.IDELock = IDELock
    self.execSetLockStatus()

class DBScriptsGetLockStatusForUpdt(object):
  __slots__ = ['_connect', '_query', 'Name', 'VersionType', 'IDELock']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.VersionType = 0
    self.IDELock = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.VersionType = result[1]
    self.IDELock = result[2]
  def _data(self):
    return [self.Name, self.VersionType, self.IDELock]
  def _fields(self):
    return 'Name|VersionType|IDELock'.split('|')
  def execGetLockStatusForUpdt(self):
    result = self._connect.action('ScriptsGetLockStatusForUpdt', self._data())
    self._store(result)
  def readGetLockStatusForUpdt(self, Name, VersionType):
    self.Name = Name
    self.VersionType = VersionType
    try:
      self.execGetLockStatusForUpdt()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBScriptsGrabTmStamps(object):
  __slots__ = ['_connect', '_query', 'VersionType', 'Name', 'Stamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.VersionType = 0
    self.Name = ''
    self.Stamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.VersionType = result[0]
    self.Name = result[1]
    self.Stamp = result[2]
  def _data(self):
    return [self.VersionType, self.Name, self.Stamp]
  def _fields(self):
    return 'VersionType|Name|Stamp'.split('|')
  def queryGrabTmStamps(self):
    self._query = self._connect.query('ScriptsGrabTmStamps', self._data())
  def fetchGrabTmStamps(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptsGrabTmStamps(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGrabTmStamps(self):
    self._connect.cancel(self._query)
  def loadGrabTmStamps(self):
    self.queryGrabTmStamps()
    result = []
    while 1:
      rc, rec = self.fetchGrabTmStamps()
      if rc == 0:
        break
      result.append(rec)
    return result

