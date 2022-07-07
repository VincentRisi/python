from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffQueueConfigAllOf(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'Name', 'QueueId']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.Name = ''
    self.QueueId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.Name = result[1]
    self.QueueId = result[2]
  def _data(self):
    return [self.InStaffId, self.Name, self.QueueId]
  def _fields(self):
    return 'InStaffId|Name|QueueId'.split('|')
  def queryAllOf(self):
    self._query = self._connect.query('StaffQueueConfigAllOf', self._data())
  def fetchAllOf(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffQueueConfigAllOf(self._connect)
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

class DBStaffQueueConfigAllPerName(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'InName', 'QueueId', 'Name', 'QueueType']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.InName = ''
    self.QueueId = ''
    self.Name = ''
    self.QueueType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.InName = result[1]
    self.QueueId = result[2]
    self.Name = result[3]
    self.QueueType = result[4]
  def _data(self):
    return [self.InStaffId, self.InName, self.QueueId, self.Name, self.QueueType]
  def _fields(self):
    return 'InStaffId|InName|QueueId|Name|QueueType'.split('|')
  def queryAllPerName(self):
    self._query = self._connect.query('StaffQueueConfigAllPerName', self._data())
  def fetchAllPerName(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffQueueConfigAllPerName(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAllPerName(self):
    self._connect.cancel(self._query)
  def loadAllPerName(self):
    self.queryAllPerName()
    result = []
    while 1:
      rc, rec = self.fetchAllPerName()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStaffQueueConfigDelAllPerName(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'InName']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.InName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.InName = result[1]
  def _data(self):
    return [self.InStaffId, self.InName]
  def _fields(self):
    return 'InStaffId|InName'.split('|')
  def execDelAllPerName(self):
    result = self._connect.action('StaffQueueConfigDelAllPerName', self._data())
    self._store(result)
  def runDelAllPerName(self, InStaffId, InName):
    self.InStaffId = InStaffId
    self.InName = InName
    self.execDelAllPerName()

