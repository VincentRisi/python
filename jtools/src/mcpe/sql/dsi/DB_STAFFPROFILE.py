from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffProfile(object):
  __slots__ = ['_connect', '_query', 'Staffid', 'Function', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Staffid = ''
    self.Function = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Staffid = result[0]
    self.Function = result[1]
    self.USId = result[2]
    self.Tmstamp = result[3]
  def _data(self):
    return [self.Staffid, self.Function, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Staffid|Function|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffProfileInsert', self._data())
    self._store(result)
  def runInsert(self, Staffid, Function, USId, Tmstamp):
    self.Staffid = Staffid
    self.Function = Function
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StaffProfileUpdate', self._data())
    self._store(result)
  def runUpdate(self, Staffid, Function, USId, Tmstamp):
    self.Staffid = Staffid
    self.Function = Function
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StaffProfileSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Staffid, Function):
    self.Staffid = Staffid
    self.Function = Function
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
    self._connect.action('StaffProfileDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('StaffProfileSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffProfile(self._connect)
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

class DBStaffProfileDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Staffid', 'Function']
  def __init__(self, connect=None):
    self._connect = connect
    self.Staffid = ''
    self.Function = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Staffid = result[0]
    self.Function = result[1]
  def _data(self):
    return [self.Staffid, self.Function]
  def _fields(self):
    return 'Staffid|Function'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffProfileDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Staffid, Function):
    self.Staffid = Staffid
    self.Function = Function
    self.execDeleteOne()

class DBStaffProfileExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Staffid', 'Function']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Staffid = ''
    self.Function = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Staffid = result[1]
    self.Function = result[2]
  def _data(self):
    return [self.Count, self.Staffid, self.Function]
  def _fields(self):
    return 'Count|Staffid|Function'.split('|')
  def execExists(self):
    result = self._connect.action('StaffProfileExists', self._data())
    self._store(result)
  def readExists(self, Staffid, Function):
    self.Staffid = Staffid
    self.Function = Function
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStaffProfileCount(object):
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
    result = self._connect.action('StaffProfileCount', self._data())
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

