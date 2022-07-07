from INTRINSICS import *
### generated code from DBPortal ###

QueueQueueTypeConst = {
  'Message' : 0, 0 : 'Message',
  'Stream' : 1, 1 : 'Stream',
  'Response' : 2, 2 : 'Response',
  'Reply' : 3, 3 : 'Reply',
  }
QueueStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  }
class DBQueue(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Descr', 'InputDriver', 'OutputDriver', 'QueueType', 'Priority', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Descr = ''
    self.InputDriver = ''
    self.OutputDriver = ''
    self.QueueType = 0
    self.Priority = 0
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Descr = result[2]
    self.InputDriver = result[3]
    self.OutputDriver = result[4]
    self.QueueType = result[5]
    self.Priority = result[6]
    self.Status = result[7]
    self.USId = result[8]
    self.TmStamp = result[9]
  def _data(self):
    return [self.Id, self.Name, self.Descr, self.InputDriver, self.OutputDriver, self.QueueType, self.Priority, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Name|Descr|InputDriver|OutputDriver|QueueType|Priority|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('QueueInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Name, Descr, InputDriver, OutputDriver, QueueType, Priority, Status, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Descr = Descr
    self.InputDriver = InputDriver
    self.OutputDriver = OutputDriver
    self.QueueType = QueueType
    self.Priority = Priority
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('QueueUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Name, Descr, InputDriver, OutputDriver, QueueType, Priority, Status, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Descr = Descr
    self.InputDriver = InputDriver
    self.OutputDriver = OutputDriver
    self.QueueType = QueueType
    self.Priority = Priority
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('QueueSelectOne', self._data())
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
  def querySelectAll(self):
    self._query = self._connect.query('QueueSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBQueue(self._connect)
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

class DBQueueDeleteOne(object):
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
    result = self._connect.action('QueueDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBQueueExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Id = result[1]
  def _data(self):
    return [self.Count, self.Id]
  def _fields(self):
    return 'Count|Id'.split('|')
  def execExists(self):
    result = self._connect.action('QueueExists', self._data())
    self._store(result)
  def readExists(self, Id):
    self.Id = Id
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBQueueCount(object):
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
    result = self._connect.action('QueueCount', self._data())
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

class DBQueueGet(object):
  __slots__ = ['_connect', '_query', 'QueueName', 'Id', 'Descr', 'InputDriver', 'OutputDriver', 'QueueType', 'Priority', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.QueueName = ''
    self.Id = ''
    self.Descr = ''
    self.InputDriver = ''
    self.OutputDriver = ''
    self.QueueType = 0
    self.Priority = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.QueueName = result[0]
    self.Id = result[1]
    self.Descr = result[2]
    self.InputDriver = result[3]
    self.OutputDriver = result[4]
    self.QueueType = result[5]
    self.Priority = result[6]
    self.Status = result[7]
  def _data(self):
    return [self.QueueName, self.Id, self.Descr, self.InputDriver, self.OutputDriver, self.QueueType, self.Priority, self.Status]
  def _fields(self):
    return 'QueueName|Id|Descr|InputDriver|OutputDriver|QueueType|Priority|Status'.split('|')
  def execGet(self):
    result = self._connect.action('QueueGet', self._data())
    self._store(result)
  def readGet(self, QueueName):
    self.QueueName = QueueName
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

