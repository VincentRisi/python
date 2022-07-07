from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffQueueConfig(object):
  __slots__ = ['_connect', '_query', 'Staffid', 'Name', 'Queueid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Staffid = ''
    self.Name = ''
    self.Queueid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Staffid = result[0]
    self.Name = result[1]
    self.Queueid = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
  def _data(self):
    return [self.Staffid, self.Name, self.Queueid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Staffid|Name|Queueid|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffQueueConfigInsert', self._data())
    self._store(result)
  def runInsert(self, Staffid, Name, Queueid, USId, Tmstamp):
    self.Staffid = Staffid
    self.Name = Name
    self.Queueid = Queueid
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StaffQueueConfigUpdate', self._data())
    self._store(result)
  def runUpdate(self, Staffid, Name, Queueid, USId, Tmstamp):
    self.Staffid = Staffid
    self.Name = Name
    self.Queueid = Queueid
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StaffQueueConfigSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Staffid, Name, Queueid):
    self.Staffid = Staffid
    self.Name = Name
    self.Queueid = Queueid
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
    self._connect.action('StaffQueueConfigDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('StaffQueueConfigSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffQueueConfig(self._connect)
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

class DBStaffQueueConfigDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Staffid', 'Name', 'Queueid']
  def __init__(self, connect=None):
    self._connect = connect
    self.Staffid = ''
    self.Name = ''
    self.Queueid = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Staffid = result[0]
    self.Name = result[1]
    self.Queueid = result[2]
  def _data(self):
    return [self.Staffid, self.Name, self.Queueid]
  def _fields(self):
    return 'Staffid|Name|Queueid'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffQueueConfigDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Staffid, Name, Queueid):
    self.Staffid = Staffid
    self.Name = Name
    self.Queueid = Queueid
    self.execDeleteOne()

class DBStaffQueueConfigExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Staffid', 'Name', 'Queueid']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Staffid = ''
    self.Name = ''
    self.Queueid = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Staffid = result[1]
    self.Name = result[2]
    self.Queueid = result[3]
  def _data(self):
    return [self.Count, self.Staffid, self.Name, self.Queueid]
  def _fields(self):
    return 'Count|Staffid|Name|Queueid'.split('|')
  def execExists(self):
    result = self._connect.action('StaffQueueConfigExists', self._data())
    self._store(result)
  def readExists(self, Staffid, Name, Queueid):
    self.Staffid = Staffid
    self.Name = Name
    self.Queueid = Queueid
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStaffQueueConfigCount(object):
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
    result = self._connect.action('StaffQueueConfigCount', self._data())
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

