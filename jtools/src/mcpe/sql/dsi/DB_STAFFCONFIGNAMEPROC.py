from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffConfigNameDefault(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'InDefault1', 'Config_Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.InDefault1 = 0
    self.Config_Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.InDefault1 = result[1]
    self.Config_Name = result[2]
  def _data(self):
    return [self.InStaffId, self.InDefault1, self.Config_Name]
  def _fields(self):
    return 'InStaffId|InDefault1|Config_Name'.split('|')
  def execDefault(self):
    result = self._connect.action('StaffConfigNameDefault', self._data())
    self._store(result)
  def readDefault(self, InStaffId, InDefault1):
    self.InStaffId = InStaffId
    self.InDefault1 = InDefault1
    try:
      self.execDefault()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStaffConfigNameAllOf(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'Config_Name', 'Default1']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.Config_Name = ''
    self.Default1 = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.Config_Name = result[1]
    self.Default1 = result[2]
  def _data(self):
    return [self.InStaffId, self.Config_Name, self.Default1]
  def _fields(self):
    return 'InStaffId|Config_Name|Default1'.split('|')
  def queryAllOf(self):
    self._query = self._connect.query('StaffConfigNameAllOf', self._data())
  def fetchAllOf(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffConfigNameAllOf(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAllOf(self):
    self._connect.cancel(self._query)
  def loadAllOf(self):
    self.queryAllOf()
    result = []
    while 1:
      rc, rec = self.fetchAllOf()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStaffConfigNameUpdateDefault(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'InConfig_Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.InConfig_Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.InConfig_Name = result[1]
  def _data(self):
    return [self.InStaffId, self.InConfig_Name]
  def _fields(self):
    return 'InStaffId|InConfig_Name'.split('|')
  def execUpdateDefault(self):
    result = self._connect.action('StaffConfigNameUpdateDefault', self._data())
    self._store(result)
  def runUpdateDefault(self, InStaffId, InConfig_Name):
    self.InStaffId = InStaffId
    self.InConfig_Name = InConfig_Name
    self.execUpdateDefault()

class DBStaffConfigNameAllToNonDefault(object):
  __slots__ = ['_connect', '_query', 'InStaffId']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
  def _data(self):
    return [self.InStaffId]
  def _fields(self):
    return 'InStaffId'.split('|')
  def execAllToNonDefault(self):
    result = self._connect.action('StaffConfigNameAllToNonDefault', self._data())
    self._store(result)
  def runAllToNonDefault(self, InStaffId):
    self.InStaffId = InStaffId
    self.execAllToNonDefault()

