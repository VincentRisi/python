from INTRINSICS import *
### generated code from DBPortal ###

MessageMessageTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  'File' : 2, 2 : 'File',
  }
MessageStatusConst = {
  'None' : 0, 0 : 'None',
  'Pending' : 1, 1 : 'Pending',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
class DBMessage(object):
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
  def execInsert(self):
    result = self._connect.action('MessageInsert', self._data())
    self._store(result)
  def runInsert(self, Id, SourceSysid, Reference, SourceQueue, QueueID, ResponseQueue, EventQueueID, StreamCount, MessageLen, MessageData, MessageType, Priority, Status, DateCreated, USId, TMStamp):
    self.Id = Id
    self.SourceSysid = SourceSysid
    self.Reference = Reference
    self.SourceQueue = SourceQueue
    self.QueueID = QueueID
    self.ResponseQueue = ResponseQueue
    self.EventQueueID = EventQueueID
    self.StreamCount = StreamCount
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.Priority = Priority
    self.Status = Status
    self.DateCreated = DateCreated
    self.USId = USId
    self.TMStamp = TMStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('MessageUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, SourceSysid, Reference, SourceQueue, QueueID, ResponseQueue, EventQueueID, StreamCount, MessageLen, MessageData, MessageType, Priority, Status, DateCreated, USId, TMStamp):
    self.Id = Id
    self.SourceSysid = SourceSysid
    self.Reference = Reference
    self.SourceQueue = SourceQueue
    self.QueueID = QueueID
    self.ResponseQueue = ResponseQueue
    self.EventQueueID = EventQueueID
    self.StreamCount = StreamCount
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.Priority = Priority
    self.Status = Status
    self.DateCreated = DateCreated
    self.USId = USId
    self.TMStamp = TMStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('MessageSelectOne', self._data())
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
  def execSelectOneUpd(self):
    result = self._connect.action('MessageSelectOneUpd', self._data())
    self._store(result)
  def readSelectOneUpd(self, Id):
    self.Id = Id
    try:
      self.execSelectOneUpd()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('MessageSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessage(self._connect)
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

class DBMessageDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
  def _data(self):
    return [self.Id]
  def _fields(self):
    return 'Id'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('MessageDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBMessageExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Id = 0
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
    result = self._connect.action('MessageExists', self._data())
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

class DBMessageCount(object):
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
    result = self._connect.action('MessageCount', self._data())
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

class DBMessageQueued(object):
  __slots__ = ['_connect', '_query', 'Queue', 'Status', 'BackDays', 'Id', 'TableName']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.Status = 0
    self.BackDays = 0
    self.Id = 0
    self.TableName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.Status = result[1]
    self.BackDays = result[2]
    self.Id = result[3]
    self.TableName = result[4]
  def _data(self):
    return [self.Queue, self.Status, self.BackDays, self.Id, self.TableName]
  def _fields(self):
    return 'Queue|Status|BackDays|Id|TableName'.split('|')
  def queryQueued(self):
    self._query = self._connect.query('MessageQueued', self._data())
  def fetchQueued(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageQueued(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueued(self):
    self._connect.cancel(self._query)
  def loadQueued(self):
    self.queryQueued()
    result = []
    while 1:
      rc, rec = self.fetchQueued()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageQueued3(object):
  __slots__ = ['_connect', '_query', 'Queue', 'Status', 'BackDays', 'Id', 'TableName']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.Status = 0
    self.BackDays = 0
    self.Id = 0
    self.TableName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.Status = result[1]
    self.BackDays = result[2]
    self.Id = result[3]
    self.TableName = result[4]
  def _data(self):
    return [self.Queue, self.Status, self.BackDays, self.Id, self.TableName]
  def _fields(self):
    return 'Queue|Status|BackDays|Id|TableName'.split('|')
  def queryQueued3(self):
    self._query = self._connect.query('MessageQueued3', self._data())
  def fetchQueued3(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageQueued3(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueued3(self):
    self._connect.cancel(self._query)
  def loadQueued3(self):
    self.queryQueued3()
    result = []
    while 1:
      rc, rec = self.fetchQueued3()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageUpdStatus(object):
  __slots__ = ['_connect', '_query', 'Id', 'StreamCount', 'Status', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.StreamCount = 0
    self.Status = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.StreamCount = result[1]
    self.Status = result[2]
    self.USId = result[3]
  def _data(self):
    return [self.Id, self.StreamCount, self.Status, self.USId]
  def _fields(self):
    return 'Id|StreamCount|Status|USId'.split('|')
  def execUpdStatus(self):
    result = self._connect.action('MessageUpdStatus', self._data())
    self._store(result)
  def runUpdStatus(self, Id, StreamCount, Status, USId):
    self.Id = Id
    self.StreamCount = StreamCount
    self.Status = Status
    self.USId = USId
    self.execUpdStatus()

class DBMessageForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'SourceSysId', 'Reference', 'SourceQueue', 'ResponseQueue', 'EventQueueId', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.SourceSysId = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.ResponseQueue = ''
    self.EventQueueId = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
    self.DateCreated = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.SourceSysId = result[3]
    self.Reference = result[4]
    self.SourceQueue = result[5]
    self.ResponseQueue = result[6]
    self.EventQueueId = result[7]
    self.MessageLen = result[8]
    self.MessageData = result[9]
    self.MessageType = result[10]
    self.Priority = result[11]
    self.DateCreated = result[12]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.SourceSysId, self.Reference, self.SourceQueue, self.ResponseQueue, self.EventQueueId, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.DateCreated]
  def _fields(self):
    return 'Id|QueueId|Status|SourceSysId|Reference|SourceQueue|ResponseQueue|EventQueueId|MessageLen|MessageData|MessageType|Priority|DateCreated'.split('|')
  def execForUpd(self):
    result = self._connect.action('MessageForUpd', self._data())
    self._store(result)
  def readForUpd(self, Id, QueueId, Status):
    self.Id = Id
    self.QueueId = QueueId
    self.Status = Status
    try:
      self.execForUpd()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageByQueue(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InStatus', 'InDateFrom', 'InDateTo', 'Id', 'SourceSysid', 'Reference', 'QueueId', 'Status', 'DateCreated', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InStatus = 0
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.QueueId = ''
    self.Status = 0
    self.DateCreated = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InStatus = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.SourceSysid = result[5]
    self.Reference = result[6]
    self.QueueId = result[7]
    self.Status = result[8]
    self.DateCreated = result[9]
    self.TMStamp = result[10]
  def _data(self):
    return [self.InQueue, self.InStatus, self.InDateFrom, self.InDateTo, self.Id, self.SourceSysid, self.Reference, self.QueueId, self.Status, self.DateCreated, self.TMStamp]
  def _fields(self):
    return 'InQueue|InStatus|InDateFrom|InDateTo|Id|SourceSysid|Reference|QueueId|Status|DateCreated|TMStamp'.split('|')
  def queryByQueue(self):
    self._query = self._connect.query('MessageByQueue', self._data())
  def fetchByQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByQueue(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByQueue(self):
    self._connect.cancel(self._query)
  def loadByQueue(self):
    self.queryByQueue()
    result = []
    while 1:
      rc, rec = self.fetchByQueue()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByQueueAll(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'SourceSysid', 'Reference', 'QueueId', 'Status', 'DateCreated', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.QueueId = ''
    self.Status = 0
    self.DateCreated = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.SourceSysid = result[4]
    self.Reference = result[5]
    self.QueueId = result[6]
    self.Status = result[7]
    self.DateCreated = result[8]
    self.TMStamp = result[9]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.SourceSysid, self.Reference, self.QueueId, self.Status, self.DateCreated, self.TMStamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|SourceSysid|Reference|QueueId|Status|DateCreated|TMStamp'.split('|')
  def queryByQueueAll(self):
    self._query = self._connect.query('MessageByQueueAll', self._data())
  def fetchByQueueAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByQueueAll(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByQueueAll(self):
    self._connect.cancel(self._query)
  def loadByQueueAll(self):
    self.queryByQueueAll()
    result = []
    while 1:
      rc, rec = self.fetchByQueueAll()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageModifyQueue(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.USId = result[2]
    self.TMStamp = result[3]
  def _data(self):
    return [self.Id, self.QueueId, self.USId, self.TMStamp]
  def _fields(self):
    return 'Id|QueueId|USId|TMStamp'.split('|')
  def execModifyQueue(self):
    result = self._connect.action('MessageModifyQueue', self._data())
    self._store(result)
  def runModifyQueue(self, Id, QueueId, USId, TMStamp):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.TMStamp = TMStamp
    self.execModifyQueue()

class DBMessageRoute(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.USId = result[2]
  def _data(self):
    return [self.Id, self.QueueId, self.USId]
  def _fields(self):
    return 'Id|QueueId|USId'.split('|')
  def execRoute(self):
    result = self._connect.action('MessageRoute', self._data())
    self._store(result)
  def runRoute(self, Id, QueueId, USId):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.execRoute()

class DBMessageByQueueDate(object):
  __slots__ = ['_connect', '_query', 'QueueId', 'DateFrom', 'DateTo', 'MaxRows', 'Id', 'SourceSysid', 'Reference', 'MessageType', 'DateCreated', 'Priority', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.QueueId = ''
    self.DateFrom = ''
    self.DateTo = ''
    self.MaxRows = 0
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.MessageType = 0
    self.DateCreated = ''
    self.Priority = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.QueueId = result[0]
    self.DateFrom = result[1]
    self.DateTo = result[2]
    self.MaxRows = result[3]
    self.Id = result[4]
    self.SourceSysid = result[5]
    self.Reference = result[6]
    self.MessageType = result[7]
    self.DateCreated = result[8]
    self.Priority = result[9]
    self.Status = result[10]
  def _data(self):
    return [self.QueueId, self.DateFrom, self.DateTo, self.MaxRows, self.Id, self.SourceSysid, self.Reference, self.MessageType, self.DateCreated, self.Priority, self.Status]
  def _fields(self):
    return 'QueueId|DateFrom|DateTo|MaxRows|Id|SourceSysid|Reference|MessageType|DateCreated|Priority|Status'.split('|')
  def queryByQueueDate(self):
    self._query = self._connect.query('MessageByQueueDate', self._data())
  def fetchByQueueDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByQueueDate(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByQueueDate(self):
    self._connect.cancel(self._query)
  def loadByQueueDate(self):
    self.queryByQueueDate()
    result = []
    while 1:
      rc, rec = self.fetchByQueueDate()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByDate(object):
  __slots__ = ['_connect', '_query', 'DateFrom', 'DateTo', 'MaxRows', 'Id', 'QueueId', 'SourceSysid', 'Reference', 'MessageType', 'DateCreated', 'Priority', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateFrom = ''
    self.DateTo = ''
    self.MaxRows = 0
    self.Id = 0
    self.QueueId = ''
    self.SourceSysid = ''
    self.Reference = ''
    self.MessageType = 0
    self.DateCreated = ''
    self.Priority = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateFrom = result[0]
    self.DateTo = result[1]
    self.MaxRows = result[2]
    self.Id = result[3]
    self.QueueId = result[4]
    self.SourceSysid = result[5]
    self.Reference = result[6]
    self.MessageType = result[7]
    self.DateCreated = result[8]
    self.Priority = result[9]
    self.Status = result[10]
  def _data(self):
    return [self.DateFrom, self.DateTo, self.MaxRows, self.Id, self.QueueId, self.SourceSysid, self.Reference, self.MessageType, self.DateCreated, self.Priority, self.Status]
  def _fields(self):
    return 'DateFrom|DateTo|MaxRows|Id|QueueId|SourceSysid|Reference|MessageType|DateCreated|Priority|Status'.split('|')
  def queryByDate(self):
    self._query = self._connect.query('MessageByDate', self._data())
  def fetchByDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByDate(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByDate(self):
    self._connect.cancel(self._query)
  def loadByDate(self):
    self.queryByDate()
    result = []
    while 1:
      rc, rec = self.fetchByDate()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageQueues(object):
  __slots__ = ['_connect', '_query', 'DateFrom', 'DateTo', 'Id', 'Name', 'Descr', 'NoOf']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateFrom = ''
    self.DateTo = ''
    self.Id = ''
    self.Name = ''
    self.Descr = ''
    self.NoOf = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateFrom = result[0]
    self.DateTo = result[1]
    self.Id = result[2]
    self.Name = result[3]
    self.Descr = result[4]
    self.NoOf = result[5]
  def _data(self):
    return [self.DateFrom, self.DateTo, self.Id, self.Name, self.Descr, self.NoOf]
  def _fields(self):
    return 'DateFrom|DateTo|Id|Name|Descr|NoOf'.split('|')
  def queryQueues(self):
    self._query = self._connect.query('MessageQueues', self._data())
  def fetchQueues(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageQueues(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueues(self):
    self._connect.cancel(self._query)
  def loadQueues(self):
    self.queryQueues()
    result = []
    while 1:
      rc, rec = self.fetchQueues()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageGetData(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageType', 'MessageLen', 'MessageData']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageType = 0
    self.MessageLen = 0
    self.MessageData = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageType = result[1]
    self.MessageLen = result[2]
    self.MessageData = result[3]
  def _data(self):
    return [self.Id, self.MessageType, self.MessageLen, self.MessageData]
  def _fields(self):
    return 'Id|MessageType|MessageLen|MessageData'.split('|')
  def execGetData(self):
    result = self._connect.action('MessageGetData', self._data())
    self._store(result)
  def readGetData(self, Id):
    self.Id = Id
    try:
      self.execGetData()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageUpdQueue(object):
  __slots__ = ['_connect', '_query', 'InMsgNo', 'InQueueID']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMsgNo = 0
    self.InQueueID = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMsgNo = result[0]
    self.InQueueID = result[1]
  def _data(self):
    return [self.InMsgNo, self.InQueueID]
  def _fields(self):
    return 'InMsgNo|InQueueID'.split('|')
  def execUpdQueue(self):
    result = self._connect.action('MessageUpdQueue', self._data())
    self._store(result)
  def runUpdQueue(self, InMsgNo, InQueueID):
    self.InMsgNo = InMsgNo
    self.InQueueID = InQueueID
    self.execUpdQueue()

class DBMessageByMessageID(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.SourceSysid = result[2]
    self.Reference = result[3]
    self.SourceQueue = result[4]
    self.QueueID = result[5]
    self.ResponseQueue = result[6]
    self.EventQueueID = result[7]
    self.StreamCount = result[8]
    self.MessageLen = result[9]
    self.MessageType = result[10]
    self.Priority = result[11]
    self.Status = result[12]
    self.DateCreated = result[13]
    self.USId = result[14]
    self.TMStamp = result[15]
  def _data(self):
    return [self.InMessageId, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InMessageId|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryByMessageID(self):
    self._query = self._connect.query('MessageByMessageID', self._data())
  def fetchByMessageID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByMessageID(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMessageID(self):
    self._connect.cancel(self._query)
  def loadByMessageID(self):
    self.queryByMessageID()
    result = []
    while 1:
      rc, rec = self.fetchByMessageID()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByReference(object):
  __slots__ = ['_connect', '_query', 'InReference', 'InDateFrom', 'InDateTo', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InReference = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InReference = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.SourceSysid = result[4]
    self.Reference = result[5]
    self.SourceQueue = result[6]
    self.QueueID = result[7]
    self.ResponseQueue = result[8]
    self.EventQueueID = result[9]
    self.StreamCount = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.Priority = result[13]
    self.Status = result[14]
    self.DateCreated = result[15]
    self.USId = result[16]
    self.TMStamp = result[17]
  def _data(self):
    return [self.InReference, self.InDateFrom, self.InDateTo, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InReference|InDateFrom|InDateTo|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryByReference(self):
    self._query = self._connect.query('MessageByReference', self._data())
  def fetchByReference(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByReference(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByReference(self):
    self._connect.cancel(self._query)
  def loadByReference(self):
    self.queryByReference()
    result = []
    while 1:
      rc, rec = self.fetchByReference()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByReferenceSourceSysId(object):
  __slots__ = ['_connect', '_query', 'Reference', 'SourceSysid', 'Id', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.SourceSysid = ''
    self.Id = 0
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.SourceSysid = result[1]
    self.Id = result[2]
    self.SourceQueue = result[3]
    self.QueueID = result[4]
    self.ResponseQueue = result[5]
    self.EventQueueID = result[6]
    self.StreamCount = result[7]
    self.MessageLen = result[8]
    self.MessageType = result[9]
    self.Priority = result[10]
    self.Status = result[11]
    self.DateCreated = result[12]
    self.USId = result[13]
    self.TMStamp = result[14]
  def _data(self):
    return [self.Reference, self.SourceSysid, self.Id, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'Reference|SourceSysid|Id|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryByReferenceSourceSysId(self):
    self._query = self._connect.query('MessageByReferenceSourceSysId', self._data())
  def fetchByReferenceSourceSysId(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByReferenceSourceSysId(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByReferenceSourceSysId(self):
    self._connect.cancel(self._query)
  def loadByReferenceSourceSysId(self):
    self.queryByReferenceSourceSysId()
    result = []
    while 1:
      rc, rec = self.fetchByReferenceSourceSysId()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageBySourceQ(object):
  __slots__ = ['_connect', '_query', 'InSourceQ', 'InDateFrom', 'InDateTo', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InSourceQ = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InSourceQ = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.SourceSysid = result[4]
    self.Reference = result[5]
    self.SourceQueue = result[6]
    self.QueueID = result[7]
    self.ResponseQueue = result[8]
    self.EventQueueID = result[9]
    self.StreamCount = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.Priority = result[13]
    self.Status = result[14]
    self.DateCreated = result[15]
    self.USId = result[16]
    self.TMStamp = result[17]
  def _data(self):
    return [self.InSourceQ, self.InDateFrom, self.InDateTo, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InSourceQ|InDateFrom|InDateTo|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryBySourceQ(self):
    self._query = self._connect.query('MessageBySourceQ', self._data())
  def fetchBySourceQ(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageBySourceQ(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBySourceQ(self):
    self._connect.cancel(self._query)
  def loadBySourceQ(self):
    self.queryBySourceQ()
    result = []
    while 1:
      rc, rec = self.fetchBySourceQ()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByRefSourceQ(object):
  __slots__ = ['_connect', '_query', 'InReference', 'InSourceQueue', 'InDateFrom', 'InDateTo', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InReference = ''
    self.InSourceQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InReference = result[0]
    self.InSourceQueue = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.SourceSysid = result[5]
    self.Reference = result[6]
    self.SourceQueue = result[7]
    self.QueueID = result[8]
    self.ResponseQueue = result[9]
    self.EventQueueID = result[10]
    self.StreamCount = result[11]
    self.MessageLen = result[12]
    self.MessageType = result[13]
    self.Priority = result[14]
    self.Status = result[15]
    self.DateCreated = result[16]
    self.USId = result[17]
    self.TMStamp = result[18]
  def _data(self):
    return [self.InReference, self.InSourceQueue, self.InDateFrom, self.InDateTo, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InReference|InSourceQueue|InDateFrom|InDateTo|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryByRefSourceQ(self):
    self._query = self._connect.query('MessageByRefSourceQ', self._data())
  def fetchByRefSourceQ(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByRefSourceQ(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByRefSourceQ(self):
    self._connect.cancel(self._query)
  def loadByRefSourceQ(self):
    self.queryByRefSourceQ()
    result = []
    while 1:
      rc, rec = self.fetchByRefSourceQ()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageStatusCount(object):
  __slots__ = ['_connect', '_query', 'InStatus', 'InQueueID', 'InDateFrom', 'InDateTo', 'Cnt']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStatus = 0
    self.InQueueID = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Cnt = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStatus = result[0]
    self.InQueueID = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Cnt = result[4]
  def _data(self):
    return [self.InStatus, self.InQueueID, self.InDateFrom, self.InDateTo, self.Cnt]
  def _fields(self):
    return 'InStatus|InQueueID|InDateFrom|InDateTo|Cnt'.split('|')
  def execStatusCount(self):
    result = self._connect.action('MessageStatusCount', self._data())
    self._store(result)
  def readStatusCount(self, InStatus, InQueueID, InDateFrom, InDateTo):
    self.InStatus = InStatus
    self.InQueueID = InQueueID
    self.InDateFrom = InDateFrom
    self.InDateTo = InDateTo
    try:
      self.execStatusCount()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageStatusCountAll(object):
  __slots__ = ['_connect', '_query', 'InQueueID', 'InDateFrom', 'InDateTo', 'Cnt']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueueID = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Cnt = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueueID = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Cnt = result[3]
  def _data(self):
    return [self.InQueueID, self.InDateFrom, self.InDateTo, self.Cnt]
  def _fields(self):
    return 'InQueueID|InDateFrom|InDateTo|Cnt'.split('|')
  def execStatusCountAll(self):
    result = self._connect.action('MessageStatusCountAll', self._data())
    self._store(result)
  def readStatusCountAll(self, InQueueID, InDateFrom, InDateTo):
    self.InQueueID = InQueueID
    self.InDateFrom = InDateFrom
    self.InDateTo = InDateTo
    try:
      self.execStatusCountAll()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
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
    self.InID = result[0]
    self.Id = result[1]
    self.SourceSysid = result[2]
    self.Reference = result[3]
    self.SourceQueue = result[4]
    self.QueueID = result[5]
    self.ResponseQueue = result[6]
    self.EventQueueID = result[7]
    self.StreamCount = result[8]
    self.MessageLen = result[9]
    self.MessageData = result[10]
    self.MessageType = result[11]
    self.Priority = result[12]
    self.Status = result[13]
    self.DateCreated = result[14]
    self.USId = result[15]
    self.TMStamp = result[16]
  def _data(self):
    return [self.InID, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InID|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageData|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def execByID(self):
    result = self._connect.action('MessageByID', self._data())
    self._store(result)
  def readByID(self, InID):
    self.InID = InID
    try:
      self.execByID()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageDriverPrompt(object):
  __slots__ = ['_connect', '_query', 'InMsgNo', 'Id', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMsgNo = 0
    self.Id = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMsgNo = result[0]
    self.Id = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.InMsgNo, self.Id, self.Status]
  def _fields(self):
    return 'InMsgNo|Id|Status'.split('|')
  def execDriverPrompt(self):
    result = self._connect.action('MessageDriverPrompt', self._data())
    self._store(result)
  def readDriverPrompt(self, InMsgNo):
    self.InMsgNo = InMsgNo
    try:
      self.execDriverPrompt()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageBrnClean(object):
  __slots__ = ['_connect', '_query', 'InId', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InId = 0
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
    self.InId = result[0]
    self.Id = result[1]
    self.SourceSysid = result[2]
    self.Reference = result[3]
    self.SourceQueue = result[4]
    self.QueueID = result[5]
    self.ResponseQueue = result[6]
    self.EventQueueID = result[7]
    self.StreamCount = result[8]
    self.MessageLen = result[9]
    self.MessageData = result[10]
    self.MessageType = result[11]
    self.Priority = result[12]
    self.Status = result[13]
    self.DateCreated = result[14]
    self.USId = result[15]
    self.TMStamp = result[16]
  def _data(self):
    return [self.InId, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp]
  def _fields(self):
    return 'InId|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageLen|MessageData|MessageType|Priority|Status|DateCreated|USId|TMStamp'.split('|')
  def queryBrnClean(self):
    self._query = self._connect.query('MessageBrnClean', self._data())
  def fetchBrnClean(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageBrnClean(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBrnClean(self):
    self._connect.cancel(self._query)
  def loadBrnClean(self):
    self.queryBrnClean()
    result = []
    while 1:
      rc, rec = self.fetchBrnClean()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageByCriteria(object):
  __slots__ = ['_connect', '_query', 'InDateFrom', 'InDateTo', 'InStatus', 'Id', 'SourceSysid', 'Reference', 'SourceQueue', 'QueueID', 'ResponseQueue', 'EventQueueID', 'StreamCount', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TMStamp', 'MSGCOND']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDateFrom = ''
    self.InDateTo = ''
    self.InStatus = 0
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.SourceQueue = ''
    self.QueueID = ''
    self.ResponseQueue = ''
    self.EventQueueID = ''
    self.StreamCount = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TMStamp = ''
    self.MSGCOND = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDateFrom = result[0]
    self.InDateTo = result[1]
    self.InStatus = result[2]
    self.Id = result[3]
    self.SourceSysid = result[4]
    self.Reference = result[5]
    self.SourceQueue = result[6]
    self.QueueID = result[7]
    self.ResponseQueue = result[8]
    self.EventQueueID = result[9]
    self.StreamCount = result[10]
    self.MessageType = result[11]
    self.Priority = result[12]
    self.Status = result[13]
    self.DateCreated = result[14]
    self.USId = result[15]
    self.TMStamp = result[16]
    self.MSGCOND = result[17]
  def _data(self):
    return [self.InDateFrom, self.InDateTo, self.InStatus, self.Id, self.SourceSysid, self.Reference, self.SourceQueue, self.QueueID, self.ResponseQueue, self.EventQueueID, self.StreamCount, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TMStamp, self.MSGCOND]
  def _fields(self):
    return 'InDateFrom|InDateTo|InStatus|Id|SourceSysid|Reference|SourceQueue|QueueID|ResponseQueue|EventQueueID|StreamCount|MessageType|Priority|Status|DateCreated|USId|TMStamp|MSGCOND'.split('|')
  def queryByCriteria(self):
    self._query = self._connect.query('MessageByCriteria', self._data())
  def fetchByCriteria(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageByCriteria(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByCriteria(self):
    self._connect.cancel(self._query)
  def loadByCriteria(self):
    self.queryByCriteria()
    result = []
    while 1:
      rc, rec = self.fetchByCriteria()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageCleanup(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.Id = result[1]
  def _data(self):
    return [self.DateCreated, self.Id]
  def _fields(self):
    return 'DateCreated|Id'.split('|')
  def queryCleanup(self):
    self._query = self._connect.query('MessageCleanup', self._data())
  def fetchCleanup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageCleanup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelCleanup(self):
    self._connect.cancel(self._query)
  def loadCleanup(self):
    self.queryCleanup()
    result = []
    while 1:
      rc, rec = self.fetchCleanup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageRemoveFromTable(object):
  __slots__ = ['_connect', '_query', 'Table', 'IdList']
  def __init__(self, connect=None):
    self._connect = connect
    self.Table = ''
    self.IdList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Table = result[0]
    self.IdList = result[1]
  def _data(self):
    return [self.Table, self.IdList]
  def _fields(self):
    return 'Table|IdList'.split('|')
  def execRemoveFromTable(self):
    result = self._connect.action('MessageRemoveFromTable', self._data())
    self._store(result)
  def runRemoveFromTable(self, Table, IdList):
    self.Table = Table
    self.IdList = IdList
    self.execRemoveFromTable()

class DBMessageMsgIdByRefSourceQ(object):
  __slots__ = ['_connect', '_query', 'InReference', 'InSourceSystem', 'DayRange', 'MsgId']
  def __init__(self, connect=None):
    self._connect = connect
    self.InReference = ''
    self.InSourceSystem = ''
    self.DayRange = 0
    self.MsgId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InReference = result[0]
    self.InSourceSystem = result[1]
    self.DayRange = result[2]
    self.MsgId = result[3]
  def _data(self):
    return [self.InReference, self.InSourceSystem, self.DayRange, self.MsgId]
  def _fields(self):
    return 'InReference|InSourceSystem|DayRange|MsgId'.split('|')
  def queryMsgIdByRefSourceQ(self):
    self._query = self._connect.query('MessageMsgIdByRefSourceQ', self._data())
  def fetchMsgIdByRefSourceQ(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMessageMsgIdByRefSourceQ(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelMsgIdByRefSourceQ(self):
    self._connect.cancel(self._query)
  def loadMsgIdByRefSourceQ(self):
    self.queryMsgIdByRefSourceQ()
    result = []
    while 1:
      rc, rec = self.fetchMsgIdByRefSourceQ()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMessageDuplicate(object):
  __slots__ = ['_connect', '_query', 'Reference', 'QueueID', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.QueueID = ''
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.QueueID = result[1]
    self.Id = result[2]
  def _data(self):
    return [self.Reference, self.QueueID, self.Id]
  def _fields(self):
    return 'Reference|QueueID|Id'.split('|')
  def execDuplicate(self):
    result = self._connect.action('MessageDuplicate', self._data())
    self._store(result)
  def readDuplicate(self, Reference, QueueID):
    self.Reference = Reference
    self.QueueID = QueueID
    try:
      self.execDuplicate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageDuplicateCnt(object):
  __slots__ = ['_connect', '_query', 'Reference', 'QueueID', 'Cnt']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.QueueID = ''
    self.Cnt = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.QueueID = result[1]
    self.Cnt = result[2]
  def _data(self):
    return [self.Reference, self.QueueID, self.Cnt]
  def _fields(self):
    return 'Reference|QueueID|Cnt'.split('|')
  def execDuplicateCnt(self):
    result = self._connect.action('MessageDuplicateCnt', self._data())
    self._store(result)
  def readDuplicateCnt(self, Reference, QueueID):
    self.Reference = Reference
    self.QueueID = QueueID
    try:
      self.execDuplicateCnt()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageGetDuplicateByRefSrcSys(object):
  __slots__ = ['_connect', '_query', 'Reference', 'SourceSysName', 'Id', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.SourceSysName = ''
    self.Id = 0
    self.DateCreated = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.SourceSysName = result[1]
    self.Id = result[2]
    self.DateCreated = result[3]
  def _data(self):
    return [self.Reference, self.SourceSysName, self.Id, self.DateCreated]
  def _fields(self):
    return 'Reference|SourceSysName|Id|DateCreated'.split('|')
  def execGetDuplicateByRefSrcSys(self):
    result = self._connect.action('MessageGetDuplicateByRefSrcSys', self._data())
    self._store(result)
  def readGetDuplicateByRefSrcSys(self, Reference, SourceSysName):
    self.Reference = Reference
    self.SourceSysName = SourceSysName
    try:
      self.execGetDuplicateByRefSrcSys()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageDuplicateByRefSrcSys(object):
  __slots__ = ['_connect', '_query', 'Reference', 'SourceSysName', 'Cnt']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.SourceSysName = ''
    self.Cnt = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.SourceSysName = result[1]
    self.Cnt = result[2]
  def _data(self):
    return [self.Reference, self.SourceSysName, self.Cnt]
  def _fields(self):
    return 'Reference|SourceSysName|Cnt'.split('|')
  def execDuplicateByRefSrcSys(self):
    result = self._connect.action('MessageDuplicateByRefSrcSys', self._data())
    self._store(result)
  def readDuplicateByRefSrcSys(self, Reference, SourceSysName):
    self.Reference = Reference
    self.SourceSysName = SourceSysName
    try:
      self.execDuplicateByRefSrcSys()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageDupByRefSrcSys(object):
  __slots__ = ['_connect', '_query', 'Reference', 'SourceQueueID', 'SourceSysName', 'Id', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.SourceQueueID = ''
    self.SourceSysName = ''
    self.Id = 0
    self.DateCreated = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.SourceQueueID = result[1]
    self.SourceSysName = result[2]
    self.Id = result[3]
    self.DateCreated = result[4]
  def _data(self):
    return [self.Reference, self.SourceQueueID, self.SourceSysName, self.Id, self.DateCreated]
  def _fields(self):
    return 'Reference|SourceQueueID|SourceSysName|Id|DateCreated'.split('|')
  def execDupByRefSrcSys(self):
    result = self._connect.action('MessageDupByRefSrcSys', self._data())
    self._store(result)
  def readDupByRefSrcSys(self, Reference, SourceQueueID, SourceSysName):
    self.Reference = Reference
    self.SourceQueueID = SourceQueueID
    self.SourceSysName = SourceSysName
    try:
      self.execDupByRefSrcSys()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageWachoviaDuplicate(object):
  __slots__ = ['_connect', '_query', 'Reference', 'QueueID', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Reference = ''
    self.QueueID = ''
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Reference = result[0]
    self.QueueID = result[1]
    self.Id = result[2]
  def _data(self):
    return [self.Reference, self.QueueID, self.Id]
  def _fields(self):
    return 'Reference|QueueID|Id'.split('|')
  def execWachoviaDuplicate(self):
    result = self._connect.action('MessageWachoviaDuplicate', self._data())
    self._store(result)
  def readWachoviaDuplicate(self, Reference, QueueID):
    self.Reference = Reference
    self.QueueID = QueueID
    try:
      self.execWachoviaDuplicate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageGetSourceSysid(object):
  __slots__ = ['_connect', '_query', 'Id', 'SourceSysid', 'Priority']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.SourceSysid = ''
    self.Priority = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.SourceSysid = result[1]
    self.Priority = result[2]
  def _data(self):
    return [self.Id, self.SourceSysid, self.Priority]
  def _fields(self):
    return 'Id|SourceSysid|Priority'.split('|')
  def execGetSourceSysid(self):
    result = self._connect.action('MessageGetSourceSysid', self._data())
    self._store(result)
  def readGetSourceSysid(self, Id):
    self.Id = Id
    try:
      self.execGetSourceSysid()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMessageUpdateStatus(object):
  __slots__ = ['_connect', '_query', 'Id', 'Status', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.Status = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Status = result[1]
    self.USId = result[2]
  def _data(self):
    return [self.Id, self.Status, self.USId]
  def _fields(self):
    return 'Id|Status|USId'.split('|')
  def execUpdateStatus(self):
    result = self._connect.action('MessageUpdateStatus', self._data())
    self._store(result)
  def runUpdateStatus(self, Id, Status, USId):
    self.Id = Id
    self.Status = Status
    self.USId = USId
    self.execUpdateStatus()

