from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffQueuePermGetAll(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'QueueId', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.QueueId = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.InStaffId, self.QueueId, self.Status]
  def _fields(self):
    return 'InStaffId|QueueId|Status'.split('|')
  def queryGetAll(self):
    self._query = self._connect.query('StaffQueuePermGetAll', self._data())
  def fetchGetAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffQueuePermGetAll(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetAll(self):
    self._connect.cancel(self._query)
  def loadGetAll(self):
    self.queryGetAll()
    result = []
    while 1:
      rc, rec = self.fetchGetAll()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStaffQueuePermUpdStatus(object):
  __slots__ = ['_connect', '_query', 'InStaffId', 'InQueueId', 'InStatus']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStaffId = ''
    self.InQueueId = ''
    self.InStatus = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStaffId = result[0]
    self.InQueueId = result[1]
    self.InStatus = result[2]
  def _data(self):
    return [self.InStaffId, self.InQueueId, self.InStatus]
  def _fields(self):
    return 'InStaffId|InQueueId|InStatus'.split('|')
  def execUpdStatus(self):
    result = self._connect.action('StaffQueuePermUpdStatus', self._data())
    self._store(result)
  def runUpdStatus(self, InStaffId, InQueueId, InStatus):
    self.InStaffId = InStaffId
    self.InQueueId = InQueueId
    self.InStatus = InStatus
    self.execUpdStatus()

