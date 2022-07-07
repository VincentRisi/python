from INTRINSICS import *
### generated code from DBPortal ###

TestMessageMessageTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  }
TestMessageStatusConst = {
  'None' : 0, 0 : 'None',
  'Pending' : 1, 1 : 'Pending',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
class DBTestMessage(object):
  __slots__ = ['_connect', '_query', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.SourceSysid = result[1]
    self.Reference = result[2]
    self.SourceQueue = result[3]
    self.QueueID = result[4]
    self.ResponseQueue = result[5]
    self.EventQueueID = result[6]
    self.StreamCount = result[7]
    self.MessageLen = result[8]
    self.MessageData = result[9]
    self.MessageType = result[10]
    self.Priority = result[11]
    self.Status = result[12]
    self.DateCreated = result[13]
    self.USId = result[14]
    self.TMStamp = result[15]
  def _data(self):
    return [self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageData|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def execSelectOne(self):
    result = self._connect.action('TestMessageSelectOne', self._data())
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

