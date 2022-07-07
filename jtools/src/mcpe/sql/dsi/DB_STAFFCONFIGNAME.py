from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffConfigName(object):
  __slots__ = ['_connect', '_query', 'Config_Name', 'StaffId', 'Default1', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Config_Name = ''
    self.StaffId = ''
    self.Default1 = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Config_Name = result[0]
    self.StaffId = result[1]
    self.Default1 = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
  def _data(self):
    return [self.Config_Name, self.StaffId, self.Default1, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Config_Name|StaffId|Default1|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffConfigNameInsert', self._data())
    self._store(result)
  def runInsert(self, Config_Name, StaffId, Default1, USId, Tmstamp):
    self.Config_Name = Config_Name
    self.StaffId = StaffId
    self.Default1 = Default1
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StaffConfigNameUpdate', self._data())
    self._store(result)
  def runUpdate(self, Config_Name, StaffId, Default1, USId, Tmstamp):
    self.Config_Name = Config_Name
    self.StaffId = StaffId
    self.Default1 = Default1
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StaffConfigNameSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Config_Name, StaffId):
    self.Config_Name = Config_Name
    self.StaffId = StaffId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def runDeleteAll(self):
    self._connect.action('StaffConfigNameDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('StaffConfigNameSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffConfigName(self._connect)
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

class DBStaffConfigNameDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Config_Name', 'StaffId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Config_Name = ''
    self.StaffId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Config_Name = result[0]
    self.StaffId = result[1]
  def _data(self):
    return [self.Config_Name, self.StaffId]
  def _fields(self):
    return 'Config_Name|StaffId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffConfigNameDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Config_Name, StaffId):
    self.Config_Name = Config_Name
    self.StaffId = StaffId
    self.execDeleteOne()

class DBStaffConfigNameExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Config_Name', 'StaffId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Config_Name = ''
    self.StaffId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Config_Name = result[1]
    self.StaffId = result[2]
  def _data(self):
    return [self.Count, self.Config_Name, self.StaffId]
  def _fields(self):
    return 'Count|Config_Name|StaffId'.split('|')
  def execExists(self):
    result = self._connect.action('StaffConfigNameExists', self._data())
    self._store(result)
  def readExists(self, Config_Name, StaffId):
    self.Config_Name = Config_Name
    self.StaffId = StaffId
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStaffConfigNameCount(object):
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
    result = self._connect.action('StaffConfigNameCount', self._data())
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

