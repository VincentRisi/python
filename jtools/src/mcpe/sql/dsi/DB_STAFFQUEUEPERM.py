from INTRINSICS import *
### generated code from DBPortal ###

StaffQueuePermStatusConst = {
  'ViewOnly' : 0, 0 : 'ViewOnly',
  'ViewRoute' : 1, 1 : 'ViewRoute',
  }
class DBStaffQueuePerm(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'QueueId', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.QueueId = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.StaffId, self.QueueId, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'StaffId|QueueId|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffQueuePermInsert', self._data())
    self._store(result)
  def runInsert(self, StaffId, QueueId, Status, USId, TmStamp):
    self.StaffId = StaffId
    self.QueueId = QueueId
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()

class DBStaffQueuePermDeleteOne(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'QueueId']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.QueueId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.QueueId = result[1]
  def _data(self):
    return [self.StaffId, self.QueueId]
  def _fields(self):
    return 'StaffId|QueueId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffQueuePermDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, StaffId, QueueId):
    self.StaffId = StaffId
    self.QueueId = QueueId
    self.execDeleteOne()

