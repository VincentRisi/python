from INTRINSICS import *
### generated code from DBPortal ###

QueueRecoveryQueueTypeConst = {
  'Message' : 0, 0 : 'Message',
  'Stream' : 1, 1 : 'Stream',
  'Response' : 2, 2 : 'Response',
  'Reply' : 3, 3 : 'Reply',
  }
QueueRecoveryStatusConst = {
  'OK' : 0, 0 : 'OK',
  'Error' : 1, 1 : 'Error',
  }
class DBQueueRecovery(object):
  __slots__ = ['_connect', '_query', 'QueueId', 'QueueType', 'MessageID', 'Ses', 'Seq', 'Reference', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.QueueId = ''
    self.QueueType = 0
    self.MessageID = 0
    self.Ses = 0
    self.Seq = 0
    self.Reference = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.QueueId = result[0]
    self.QueueType = result[1]
    self.MessageID = result[2]
    self.Ses = result[3]
    self.Seq = result[4]
    self.Reference = result[5]
    self.Status = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.QueueId, self.QueueType, self.MessageID, self.Ses, self.Seq, self.Reference, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'QueueId|QueueType|MessageID|Ses|Seq|Reference|Status|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('QueueRecoveryInsert', self._data())
    self._store(result)
  def runInsert(self, QueueId, QueueType, MessageID, Ses, Seq, Reference, Status, USId, Tmstamp):
    self.QueueId = QueueId
    self.QueueType = QueueType
    self.MessageID = MessageID
    self.Ses = Ses
    self.Seq = Seq
    self.Reference = Reference
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('QueueRecoveryUpdate', self._data())
    self._store(result)
  def runUpdate(self, QueueId, QueueType, MessageID, Ses, Seq, Reference, Status, USId, Tmstamp):
    self.QueueId = QueueId
    self.QueueType = QueueType
    self.MessageID = MessageID
    self.Ses = Ses
    self.Seq = Seq
    self.Reference = Reference
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('QueueRecoverySelectOne', self._data())
    self._store(result)
  def readSelectOne(self, QueueId):
    self.QueueId = QueueId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBQueueRecoveryExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'QueueId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.QueueId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.QueueId = result[1]
  def _data(self):
    return [self.Count, self.QueueId]
  def _fields(self):
    return 'Count|QueueId'.split('|')
  def execExists(self):
    result = self._connect.action('QueueRecoveryExists', self._data())
    self._store(result)
  def readExists(self, QueueId):
    self.QueueId = QueueId
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBQueueRecoveryCount(object):
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
    result = self._connect.action('QueueRecoveryCount', self._data())
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

class DBQueueRecoveryUpdStat(object):
  __slots__ = ['_connect', '_query', 'QueueId', 'MessageID', 'Seq', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.QueueId = ''
    self.MessageID = 0
    self.Seq = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.QueueId = result[0]
    self.MessageID = result[1]
    self.Seq = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.QueueId, self.MessageID, self.Seq, self.Status]
  def _fields(self):
    return 'QueueId|MessageID|Seq|Status'.split('|')
  def execUpdStat(self):
    result = self._connect.action('QueueRecoveryUpdStat', self._data())
    self._store(result)
  def runUpdStat(self, QueueId, MessageID, Seq, Status):
    self.QueueId = QueueId
    self.MessageID = MessageID
    self.Seq = Seq
    self.Status = Status
    self.execUpdStat()

