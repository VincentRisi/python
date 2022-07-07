from INTRINSICS import *
### generated code from DBPortal ###

class DBStaff(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Description', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Description = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Description = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Id, self.Name, self.Description, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Name|Description|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Name, Description, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Description = Description
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StaffUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Name, Description, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Description = Description
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def querySelectAll(self):
    self._query = self._connect.query('StaffSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaff(self._connect)
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
    result = self._connect.action('StaffSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id):
    self.Id = Id
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStaffDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
  def _data(self):
    return [self.Id]
  def _fields(self):
    return 'Id'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBStaffListAll(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Description']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Description = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Description = result[2]
  def _data(self):
    return [self.Id, self.Name, self.Description]
  def _fields(self):
    return 'Id|Name|Description'.split('|')
  def queryListAll(self):
    self._query = self._connect.query('StaffListAll', self._data())
  def fetchListAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffListAll(self._connect)
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

