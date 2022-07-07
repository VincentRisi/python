from INTRINSICS import *
### generated code from DBPortal ###

ReplyMessageTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  'File' : 2, 2 : 'File',
  }
ReplyStatusConst = {
  'None' : 0, 0 : 'None',
  'Sent' : 1, 1 : 'Sent',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
class DBReply(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageData', 'MessageType', 'DateCreated', 'UserCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.UserCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageID = result[1]
    self.QueueID = result[2]
    self.MessageLen = result[3]
    self.MessageData = result[4]
    self.MessageType = result[5]
    self.DateCreated = result[6]
    self.UserCreated = result[7]
    self.Status = result[8]
    self.USId = result[9]
    self.Tmstamp = result[10]
  def _data(self):
    return [self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageData, self.MessageType, self.DateCreated, self.UserCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Id|MessageID|QueueID|MessageLen|MessageData|MessageType|DateCreated|UserCreated|Status|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('ReplyInsert', self._data())
    self._store(result)
  def runInsert(self, Id, MessageID, QueueID, MessageLen, MessageData, MessageType, DateCreated, UserCreated, Status, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.QueueID = QueueID
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.DateCreated = DateCreated
    self.UserCreated = UserCreated
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('ReplyUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, MessageID, QueueID, MessageLen, MessageData, MessageType, DateCreated, UserCreated, Status, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.QueueID = QueueID
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.DateCreated = DateCreated
    self.UserCreated = UserCreated
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('ReplySelectOne', self._data())
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
    result = self._connect.action('ReplySelectOneUpd', self._data())
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
    self._query = self._connect.query('ReplySelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReply(self._connect)
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

class DBReplyDeleteOne(object):
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
    result = self._connect.action('ReplyDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBReplyExists(object):
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
    result = self._connect.action('ReplyExists', self._data())
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

class DBReplyCount(object):
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
    result = self._connect.action('ReplyCount', self._data())
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

class DBReplyGetById(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageID', 'MessageLen', 'MessageData', 'MessageType', 'Status', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageID = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Status = 0
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageID = result[1]
    self.MessageLen = result[2]
    self.MessageData = result[3]
    self.MessageType = result[4]
    self.Status = result[5]
    self.Reference = result[6]
  def _data(self):
    return [self.Id, self.MessageID, self.MessageLen, self.MessageData, self.MessageType, self.Status, self.Reference]
  def _fields(self):
    return 'Id|MessageID|MessageLen|MessageData|MessageType|Status|Reference'.split('|')
  def execGetById(self):
    result = self._connect.action('ReplyGetById', self._data())
    self._store(result)
  def readGetById(self, Id):
    self.Id = Id
    try:
      self.execGetById()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBReplyQueued(object):
  __slots__ = ['_connect', '_query', 'Queue', 'DayInterval', 'Status', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.DayInterval = 0
    self.Status = 0
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.DayInterval = result[1]
    self.Status = result[2]
    self.Id = result[3]
  def _data(self):
    return [self.Queue, self.DayInterval, self.Status, self.Id]
  def _fields(self):
    return 'Queue|DayInterval|Status|Id'.split('|')
  def queryQueued(self):
    self._query = self._connect.query('ReplyQueued', self._data())
  def fetchQueued(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyQueued(self._connect)
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

class DBReplyUpdateStatus(object):
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
    result = self._connect.action('ReplyUpdateStatus', self._data())
    self._store(result)
  def runUpdateStatus(self, Id, Status, USId):
    self.Id = Id
    self.Status = Status
    self.USId = USId
    self.execUpdateStatus()

class DBReplyByQueueDate(object):
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
    self._query = self._connect.query('ReplyByQueueDate', self._data())
  def fetchByQueueDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByQueueDate(self._connect)
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

class DBReplyByDate(object):
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
    self._query = self._connect.query('ReplyByDate', self._data())
  def fetchByDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByDate(self._connect)
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

class DBReplyQueues(object):
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
    self._query = self._connect.query('ReplyQueues', self._data())
  def fetchQueues(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyQueues(self._connect)
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

class DBReplyGetData(object):
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
    result = self._connect.action('ReplyGetData', self._data())
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

class DBReplyRoute(object):
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
    result = self._connect.action('ReplyRoute', self._data())
    self._store(result)
  def runRoute(self, Id, QueueId, USId):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.execRoute()

class DBReplyForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'MessageID', 'MessageLen', 'MessageData', 'MessageType', 'DateCreated', 'ResponseQueue', 'MessageReference']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.MessageID = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.ResponseQueue = ''
    self.MessageReference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.MessageID = result[3]
    self.MessageLen = result[4]
    self.MessageData = result[5]
    self.MessageType = result[6]
    self.DateCreated = result[7]
    self.ResponseQueue = result[8]
    self.MessageReference = result[9]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.MessageID, self.MessageLen, self.MessageData, self.MessageType, self.DateCreated, self.ResponseQueue, self.MessageReference]
  def _fields(self):
    return 'Id|QueueId|Status|MessageID|MessageLen|MessageData|MessageType|DateCreated|ResponseQueue|MessageReference'.split('|')
  def execForUpd(self):
    result = self._connect.action('ReplyForUpd', self._data())
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

class DBReplyForUpdeximbill(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'MessageID', 'MessageLen', 'MessageData', 'MessageType', 'DateCreated', 'ResponseQueue', 'MessageReference']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.MessageID = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.ResponseQueue = ''
    self.MessageReference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.MessageID = result[3]
    self.MessageLen = result[4]
    self.MessageData = result[5]
    self.MessageType = result[6]
    self.DateCreated = result[7]
    self.ResponseQueue = result[8]
    self.MessageReference = result[9]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.MessageID, self.MessageLen, self.MessageData, self.MessageType, self.DateCreated, self.ResponseQueue, self.MessageReference]
  def _fields(self):
    return 'Id|QueueId|Status|MessageID|MessageLen|MessageData|MessageType|DateCreated|ResponseQueue|MessageReference'.split('|')
  def execForUpdeximbill(self):
    result = self._connect.action('ReplyForUpdeximbill', self._data())
    self._store(result)
  def readForUpdeximbill(self, Id, QueueId, Status):
    self.Id = Id
    self.QueueId = QueueId
    self.Status = Status
    try:
      self.execForUpdeximbill()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBReplyUpdStatus(object):
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
  def execUpdStatus(self):
    result = self._connect.action('ReplyUpdStatus', self._data())
    self._store(result)
  def runUpdStatus(self, Id, Status, USId):
    self.Id = Id
    self.Status = Status
    self.USId = USId
    self.execUpdStatus()

class DBReplyByQueue(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InStatus', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageType', 'DateCreated', 'UserCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InStatus = 0
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.UserCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InStatus = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.MessageID = result[5]
    self.QueueID = result[6]
    self.MessageLen = result[7]
    self.MessageType = result[8]
    self.DateCreated = result[9]
    self.UserCreated = result[10]
    self.Status = result[11]
    self.USId = result[12]
    self.Tmstamp = result[13]
  def _data(self):
    return [self.InQueue, self.InStatus, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageType, self.DateCreated, self.UserCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InQueue|InStatus|InDateFrom|InDateTo|Id|MessageID|QueueID|MessageLen|MessageType|DateCreated|UserCreated|Status|USId|Tmstamp'.split('|')
  def queryByQueue(self):
    self._query = self._connect.query('ReplyByQueue', self._data())
  def fetchByQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByQueue(self._connect)
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

class DBReplyByQueueAll(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageType', 'DateCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageID = result[4]
    self.QueueID = result[5]
    self.MessageLen = result[6]
    self.MessageType = result[7]
    self.DateCreated = result[8]
    self.Status = result[9]
    self.USId = result[10]
    self.Tmstamp = result[11]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageType, self.DateCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|MessageID|QueueID|MessageLen|MessageType|DateCreated|Status|USId|Tmstamp'.split('|')
  def queryByQueueAll(self):
    self._query = self._connect.query('ReplyByQueueAll', self._data())
  def fetchByQueueAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByQueueAll(self._connect)
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

class DBReplyByMsgIDQueue(object):
  __slots__ = ['_connect', '_query', 'InMessageID', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageType', 'DateCreated', 'UserCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageID = 0
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.UserCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageID = result[0]
    self.InQueue = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.MessageID = result[5]
    self.QueueID = result[6]
    self.MessageLen = result[7]
    self.MessageType = result[8]
    self.DateCreated = result[9]
    self.UserCreated = result[10]
    self.Status = result[11]
    self.USId = result[12]
    self.Tmstamp = result[13]
  def _data(self):
    return [self.InMessageID, self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageType, self.DateCreated, self.UserCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageID|InQueue|InDateFrom|InDateTo|Id|MessageID|QueueID|MessageLen|MessageType|DateCreated|UserCreated|Status|USId|Tmstamp'.split('|')
  def queryByMsgIDQueue(self):
    self._query = self._connect.query('ReplyByMsgIDQueue', self._data())
  def fetchByMsgIDQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByMsgIDQueue(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMsgIDQueue(self):
    self._connect.cancel(self._query)
  def loadByMsgIDQueue(self):
    self.queryByMsgIDQueue()
    result = []
    while 1:
      rc, rec = self.fetchByMsgIDQueue()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBReplyStatusCount(object):
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
    result = self._connect.action('ReplyStatusCount', self._data())
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

class DBReplyStatusCountAll(object):
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
    result = self._connect.action('ReplyStatusCountAll', self._data())
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

class DBReplyByMessageID(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageType', 'DateCreated', 'UserCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.UserCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.QueueID = result[3]
    self.MessageLen = result[4]
    self.MessageType = result[5]
    self.DateCreated = result[6]
    self.UserCreated = result[7]
    self.Status = result[8]
    self.USId = result[9]
    self.Tmstamp = result[10]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageType, self.DateCreated, self.UserCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageId|Id|MessageID|QueueID|MessageLen|MessageType|DateCreated|UserCreated|Status|USId|Tmstamp'.split('|')
  def queryByMessageID(self):
    self._query = self._connect.query('ReplyByMessageID', self._data())
  def fetchByMessageID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByMessageID(self._connect)
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

class DBReplyByMessageIDData(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageData', 'MessageType', 'DateCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.QueueID = result[3]
    self.MessageLen = result[4]
    self.MessageData = result[5]
    self.MessageType = result[6]
    self.DateCreated = result[7]
    self.Status = result[8]
    self.USId = result[9]
    self.Tmstamp = result[10]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageData, self.MessageType, self.DateCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageId|Id|MessageID|QueueID|MessageLen|MessageData|MessageType|DateCreated|Status|USId|Tmstamp'.split('|')
  def queryByMessageIDData(self):
    self._query = self._connect.query('ReplyByMessageIDData', self._data())
  def fetchByMessageIDData(self):
    rc, result = self._connect.fetch(self._query)
    record = DBReplyByMessageIDData(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMessageIDData(self):
    self._connect.cancel(self._query)
  def loadByMessageIDData(self):
    self.queryByMessageIDData()
    result = []
    while 1:
      rc, rec = self.fetchByMessageIDData()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBReplyByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'Id', 'MessageID', 'QueueID', 'MessageLen', 'MessageData', 'MessageType', 'DateCreated', 'UserCreated', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.Id = 0
    self.MessageID = 0
    self.QueueID = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.DateCreated = ''
    self.UserCreated = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.QueueID = result[3]
    self.MessageLen = result[4]
    self.MessageData = result[5]
    self.MessageType = result[6]
    self.DateCreated = result[7]
    self.UserCreated = result[8]
    self.Status = result[9]
    self.USId = result[10]
    self.Tmstamp = result[11]
  def _data(self):
    return [self.InID, self.Id, self.MessageID, self.QueueID, self.MessageLen, self.MessageData, self.MessageType, self.DateCreated, self.UserCreated, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InID|Id|MessageID|QueueID|MessageLen|MessageData|MessageType|DateCreated|UserCreated|Status|USId|Tmstamp'.split('|')
  def execByID(self):
    result = self._connect.action('ReplyByID', self._data())
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

class DBReplyUpdQueue(object):
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
    result = self._connect.action('ReplyUpdQueue', self._data())
    self._store(result)
  def runUpdQueue(self, InMsgNo, InQueueID):
    self.InMsgNo = InMsgNo
    self.InQueueID = InQueueID
    self.execUpdQueue()

