from INTRINSICS import *
### generated code from DBPortal ###

DatesDateTypeConst = {
  'RunDate' : 0, 0 : 'RunDate',
  'ReleaseDate' : 1, 1 : 'ReleaseDate',
  }
class DBDates(object):
  __slots__ = ['_connect', '_query', 'DateType', 'Description', 'Value', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateType = 0
    self.Description = ''
    self.Value = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateType = result[0]
    self.Description = result[1]
    self.Value = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.DateType, self.Description, self.Value, self.USId, self.TmStamp]
  def _fields(self):
    return 'DateType|Description|Value|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('DatesInsert', self._data())
    self._store(result)
  def runInsert(self, DateType, Description, Value, USId, TmStamp):
    self.DateType = DateType
    self.Description = Description
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('DatesUpdate', self._data())
    self._store(result)
  def runUpdate(self, DateType, Description, Value, USId, TmStamp):
    self.DateType = DateType
    self.Description = Description
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('DatesSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, DateType):
    self.DateType = DateType
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
    self._query = self._connect.query('DatesSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDates(self._connect)
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

class DBDatesExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'DateType']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.DateType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.DateType = result[1]
  def _data(self):
    return [self.Count, self.DateType]
  def _fields(self):
    return 'Count|DateType'.split('|')
  def execExists(self):
    result = self._connect.action('DatesExists', self._data())
    self._store(result)
  def readExists(self, DateType):
    self.DateType = DateType
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBDatesGet(object):
  __slots__ = ['_connect', '_query', 'DateType', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateType = 0
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateType = result[0]
    self.Value = result[1]
  def _data(self):
    return [self.DateType, self.Value]
  def _fields(self):
    return 'DateType|Value'.split('|')
  def execGet(self):
    result = self._connect.action('DatesGet', self._data())
    self._store(result)
  def readGet(self, DateType):
    self.DateType = DateType
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBDatesSetOracleDate(object):
  __slots__ = ['_connect', '_query', 'DateType', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateType = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateType = result[0]
    self.USId = result[1]
  def _data(self):
    return [self.DateType, self.USId]
  def _fields(self):
    return 'DateType|USId'.split('|')
  def execSetOracleDate(self):
    result = self._connect.action('DatesSetOracleDate', self._data())
    self._store(result)
  def runSetOracleDate(self, DateType, USId):
    self.DateType = DateType
    self.USId = USId
    self.execSetOracleDate()

class DBDatesInc(object):
  __slots__ = ['_connect', '_query', 'DateType', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateType = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateType = result[0]
    self.USId = result[1]
  def _data(self):
    return [self.DateType, self.USId]
  def _fields(self):
    return 'DateType|USId'.split('|')
  def execInc(self):
    result = self._connect.action('DatesInc', self._data())
    self._store(result)
  def runInc(self, DateType, USId):
    self.DateType = DateType
    self.USId = USId
    self.execInc()

