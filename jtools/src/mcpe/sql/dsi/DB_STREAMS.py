from INTRINSICS import *
### generated code from DBPortal ###

StreamsMessageTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  'File' : 2, 2 : 'File',
  'Swift' : 3, 3 : 'Swift',
  'Json' : 4, 4 : 'Json',
  'Yaml' : 5, 5 : 'Yaml',
  }
StreamsStatusConst = {
  'None' : 0, 0 : 'None',
  'Sent' : 1, 1 : 'Sent',
  'Ack' : 2, 2 : 'Ack',
  'Nak' : 3, 3 : 'Nak',
  }
class DBStreams(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageId = result[1]
    self.QueueId = result[2]
    self.EventQueueId = result[3]
    self.StreamRef = result[4]
    self.StreamType = result[5]
    self.StreamDescr = result[6]
    self.MessageLen = result[7]
    self.MessageData = result[8]
    self.MessageType = result[9]
    self.Priority = result[10]
    self.Status = result[11]
    self.DateCreated = result[12]
    self.USId = result[13]
    self.TmStamp = result[14]
  def _data(self):
    return [self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageData|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StreamsInsert', self._data())
    self._store(result)
  def runInsert(self, Id, MessageId, QueueId, EventQueueId, StreamRef, StreamType, StreamDescr, MessageLen, MessageData, MessageType, Priority, Status, DateCreated, USId, TmStamp):
    self.Id = Id
    self.MessageId = MessageId
    self.QueueId = QueueId
    self.EventQueueId = EventQueueId
    self.StreamRef = StreamRef
    self.StreamType = StreamType
    self.StreamDescr = StreamDescr
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.Priority = Priority
    self.Status = Status
    self.DateCreated = DateCreated
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StreamsUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, MessageId, QueueId, EventQueueId, StreamRef, StreamType, StreamDescr, MessageLen, MessageData, MessageType, Priority, Status, DateCreated, USId, TmStamp):
    self.Id = Id
    self.MessageId = MessageId
    self.QueueId = QueueId
    self.EventQueueId = EventQueueId
    self.StreamRef = StreamRef
    self.StreamType = StreamType
    self.StreamDescr = StreamDescr
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.Priority = Priority
    self.Status = Status
    self.DateCreated = DateCreated
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StreamsSelectOne', self._data())
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
    result = self._connect.action('StreamsSelectOneUpd', self._data())
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
    self._query = self._connect.query('StreamsSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreams(self._connect)
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

class DBStreamsDeleteOne(object):
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
    result = self._connect.action('StreamsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBStreamsExists(object):
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
    result = self._connect.action('StreamsExists', self._data())
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

class DBStreamsCount(object):
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
    result = self._connect.action('StreamsCount', self._data())
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

class DBStreamsQueued(object):
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
    self._query = self._connect.query('StreamsQueued', self._data())
  def fetchQueued(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsQueued(self._connect)
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

class DBStreamsQueuedEx(object):
  __slots__ = ['_connect', '_query', 'Queue', 'DayInterval', 'Status', 'Id', 'StreamRef']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.DayInterval = 0
    self.Status = 0
    self.Id = 0
    self.StreamRef = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.DayInterval = result[1]
    self.Status = result[2]
    self.Id = result[3]
    self.StreamRef = result[4]
  def _data(self):
    return [self.Queue, self.DayInterval, self.Status, self.Id, self.StreamRef]
  def _fields(self):
    return 'Queue|DayInterval|Status|Id|StreamRef'.split('|')
  def queryQueuedEx(self):
    self._query = self._connect.query('StreamsQueuedEx', self._data())
  def fetchQueuedEx(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsQueuedEx(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueuedEx(self):
    self._connect.cancel(self._query)
  def loadQueuedEx(self):
    self.queryQueuedEx()
    result = []
    while 1:
      rc, rec = self.fetchQueuedEx()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByStatusQueueDate(object):
  __slots__ = ['_connect', '_query', 'Queue', 'Status', 'DateFrom', 'Id', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.Status = 0
    self.DateFrom = ''
    self.Id = 0
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.Status = result[1]
    self.DateFrom = result[2]
    self.Id = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Queue, self.Status, self.DateFrom, self.Id, self.TmStamp]
  def _fields(self):
    return 'Queue|Status|DateFrom|Id|TmStamp'.split('|')
  def queryByStatusQueueDate(self):
    self._query = self._connect.query('StreamsByStatusQueueDate', self._data())
  def fetchByStatusQueueDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByStatusQueueDate(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByStatusQueueDate(self):
    self._connect.cancel(self._query)
  def loadByStatusQueueDate(self):
    self.queryByStatusQueueDate()
    result = []
    while 1:
      rc, rec = self.fetchByStatusQueueDate()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsRevertStatusToNone(object):
  __slots__ = ['_connect', '_query', 'Queue', 'StatusNone', 'StatusSent']
  def __init__(self, connect=None):
    self._connect = connect
    self.Queue = ''
    self.StatusNone = 0
    self.StatusSent = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Queue = result[0]
    self.StatusNone = result[1]
    self.StatusSent = result[2]
  def _data(self):
    return [self.Queue, self.StatusNone, self.StatusSent]
  def _fields(self):
    return 'Queue|StatusNone|StatusSent'.split('|')
  def execRevertStatusToNone(self):
    result = self._connect.action('StreamsRevertStatusToNone', self._data())
    self._store(result)
  def runRevertStatusToNone(self, Queue, StatusNone, StatusSent):
    self.Queue = Queue
    self.StatusNone = StatusNone
    self.StatusSent = StatusSent
    self.execRevertStatusToNone()

class DBStreamsUpdateStatus(object):
  __slots__ = ['_connect', '_query', 'Id', 'StreamRef', 'Status', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.StreamRef = ''
    self.Status = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.StreamRef = result[1]
    self.Status = result[2]
    self.USId = result[3]
  def _data(self):
    return [self.Id, self.StreamRef, self.Status, self.USId]
  def _fields(self):
    return 'Id|StreamRef|Status|USId'.split('|')
  def execUpdateStatus(self):
    result = self._connect.action('StreamsUpdateStatus', self._data())
    self._store(result)
  def runUpdateStatus(self, Id, StreamRef, Status, USId):
    self.Id = Id
    self.StreamRef = StreamRef
    self.Status = Status
    self.USId = USId
    self.execUpdateStatus()

class DBStreamsForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'EventQueueID', 'StreamRef', 'MessageLen', 'MessageData', 'MessageType', 'Priority']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.EventQueueID = ''
    self.StreamRef = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.EventQueueID = result[3]
    self.StreamRef = result[4]
    self.MessageLen = result[5]
    self.MessageData = result[6]
    self.MessageType = result[7]
    self.Priority = result[8]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.EventQueueID, self.StreamRef, self.MessageLen, self.MessageData, self.MessageType, self.Priority]
  def _fields(self):
    return 'Id|QueueId|Status|EventQueueID|StreamRef|MessageLen|MessageData|MessageType|Priority'.split('|')
  def execForUpd(self):
    result = self._connect.action('StreamsForUpd', self._data())
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

class DBStreamsGetByRef(object):
  __slots__ = ['_connect', '_query', 'StreamRef', 'ID', 'MessageID', 'EventQueueID', 'ReplyQueueID', 'StreamCount']
  def __init__(self, connect=None):
    self._connect = connect
    self.StreamRef = ''
    self.ID = 0
    self.MessageID = 0
    self.EventQueueID = ''
    self.ReplyQueueID = ''
    self.StreamCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StreamRef = result[0]
    self.ID = result[1]
    self.MessageID = result[2]
    self.EventQueueID = result[3]
    self.ReplyQueueID = result[4]
    self.StreamCount = result[5]
  def _data(self):
    return [self.StreamRef, self.ID, self.MessageID, self.EventQueueID, self.ReplyQueueID, self.StreamCount]
  def _fields(self):
    return 'StreamRef|ID|MessageID|EventQueueID|ReplyQueueID|StreamCount'.split('|')
  def execGetByRef(self):
    result = self._connect.action('StreamsGetByRef', self._data())
    self._store(result)
  def runGetByRef(self, StreamRef, ID, MessageID, EventQueueID, ReplyQueueID, StreamCount):
    self.StreamRef = StreamRef
    self.ID = ID
    self.MessageID = MessageID
    self.EventQueueID = EventQueueID
    self.ReplyQueueID = ReplyQueueID
    self.StreamCount = StreamCount
    self.execGetByRef()

class DBStreamsGetByQRef(object):
  __slots__ = ['_connect', '_query', 'StreamRef', 'QueueId', 'Status', 'ID', 'MessageID', 'EventQueueID', 'ReplyQueueID', 'ReplyQueue', 'StreamCount']
  def __init__(self, connect=None):
    self._connect = connect
    self.StreamRef = ''
    self.QueueId = ''
    self.Status = 0
    self.ID = 0
    self.MessageID = 0
    self.EventQueueID = ''
    self.ReplyQueueID = ''
    self.ReplyQueue = ''
    self.StreamCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StreamRef = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.ID = result[3]
    self.MessageID = result[4]
    self.EventQueueID = result[5]
    self.ReplyQueueID = result[6]
    self.ReplyQueue = result[7]
    self.StreamCount = result[8]
  def _data(self):
    return [self.StreamRef, self.QueueId, self.Status, self.ID, self.MessageID, self.EventQueueID, self.ReplyQueueID, self.ReplyQueue, self.StreamCount]
  def _fields(self):
    return 'StreamRef|QueueId|Status|ID|MessageID|EventQueueID|ReplyQueueID|ReplyQueue|StreamCount'.split('|')
  def execGetByQRef(self):
    result = self._connect.action('StreamsGetByQRef', self._data())
    self._store(result)
  def runGetByQRef(self, StreamRef, QueueId, Status, ID, MessageID, EventQueueID, ReplyQueueID, ReplyQueue, StreamCount):
    self.StreamRef = StreamRef
    self.QueueId = QueueId
    self.Status = Status
    self.ID = ID
    self.MessageID = MessageID
    self.EventQueueID = EventQueueID
    self.ReplyQueueID = ReplyQueueID
    self.ReplyQueue = ReplyQueue
    self.StreamCount = StreamCount
    self.execGetByQRef()

class DBStreamsGetById(object):
  __slots__ = ['_connect', '_query', 'ID', 'MessageID', 'EventQueueID', 'StreamRef', 'StreamCount', 'ReplyQueueID', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.MessageID = 0
    self.EventQueueID = ''
    self.StreamRef = ''
    self.StreamCount = 0
    self.ReplyQueueID = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.MessageID = result[1]
    self.EventQueueID = result[2]
    self.StreamRef = result[3]
    self.StreamCount = result[4]
    self.ReplyQueueID = result[5]
    self.Status = result[6]
  def _data(self):
    return [self.ID, self.MessageID, self.EventQueueID, self.StreamRef, self.StreamCount, self.ReplyQueueID, self.Status]
  def _fields(self):
    return 'ID|MessageID|EventQueueID|StreamRef|StreamCount|ReplyQueueID|Status'.split('|')
  def execGetById(self):
    result = self._connect.action('StreamsGetById', self._data())
    self._store(result)
  def readGetById(self, ID):
    self.ID = ID
    try:
      self.execGetById()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsGetMsgStatus(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'MyCount', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.MyCount = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.MyCount = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.MessageID, self.MyCount, self.Status]
  def _fields(self):
    return 'MessageID|MyCount|Status'.split('|')
  def queryGetMsgStatus(self):
    self._query = self._connect.query('StreamsGetMsgStatus', self._data())
  def fetchGetMsgStatus(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsGetMsgStatus(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetMsgStatus(self):
    self._connect.cancel(self._query)
  def loadGetMsgStatus(self):
    self.queryGetMsgStatus()
    result = []
    while 1:
      rc, rec = self.fetchGetMsgStatus()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsCountMsgStatus(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'Status', 'MyCount']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.Status = 0
    self.MyCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.Status = result[1]
    self.MyCount = result[2]
  def _data(self):
    return [self.MessageID, self.Status, self.MyCount]
  def _fields(self):
    return 'MessageID|Status|MyCount'.split('|')
  def execCountMsgStatus(self):
    result = self._connect.action('StreamsCountMsgStatus', self._data())
    self._store(result)
  def readCountMsgStatus(self, MessageID, Status):
    self.MessageID = MessageID
    self.Status = Status
    try:
      self.execCountMsgStatus()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsCountMsgStatusMultiple(object):
  __slots__ = ['_connect', '_query', 'StreamID', 'Status1', 'Status2', 'MyCount1', 'MyCount2', 'StreamCount', 'MessageID', 'ReplyQueueID']
  def __init__(self, connect=None):
    self._connect = connect
    self.StreamID = 0
    self.Status1 = 0
    self.Status2 = 0
    self.MyCount1 = 0
    self.MyCount2 = 0
    self.StreamCount = 0
    self.MessageID = 0
    self.ReplyQueueID = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StreamID = result[0]
    self.Status1 = result[1]
    self.Status2 = result[2]
    self.MyCount1 = result[3]
    self.MyCount2 = result[4]
    self.StreamCount = result[5]
    self.MessageID = result[6]
    self.ReplyQueueID = result[7]
  def _data(self):
    return [self.StreamID, self.Status1, self.Status2, self.MyCount1, self.MyCount2, self.StreamCount, self.MessageID, self.ReplyQueueID]
  def _fields(self):
    return 'StreamID|Status1|Status2|MyCount1|MyCount2|StreamCount|MessageID|ReplyQueueID'.split('|')
  def execCountMsgStatusMultiple(self):
    result = self._connect.action('StreamsCountMsgStatusMultiple', self._data())
    self._store(result)
  def readCountMsgStatusMultiple(self, StreamID, Status1, Status2):
    self.StreamID = StreamID
    self.Status1 = Status1
    self.Status2 = Status2
    try:
      self.execCountMsgStatusMultiple()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsByQueueDate(object):
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
    self._query = self._connect.query('StreamsByQueueDate', self._data())
  def fetchByQueueDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByQueueDate(self._connect)
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

class DBStreamsByDate(object):
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
    self._query = self._connect.query('StreamsByDate', self._data())
  def fetchByDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByDate(self._connect)
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

class DBStreamsQueues(object):
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
    self._query = self._connect.query('StreamsQueues', self._data())
  def fetchQueues(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsQueues(self._connect)
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

class DBStreamsGetData(object):
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
    result = self._connect.action('StreamsGetData', self._data())
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

class DBStreamsRouterForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'MessageId', 'EventQueueId', 'StreamRef', 'MessageLen', 'MessageData', 'MessageType', 'Priority']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.MessageId = 0
    self.EventQueueId = ''
    self.StreamRef = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.MessageId = result[3]
    self.EventQueueId = result[4]
    self.StreamRef = result[5]
    self.MessageLen = result[6]
    self.MessageData = result[7]
    self.MessageType = result[8]
    self.Priority = result[9]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.MessageId, self.EventQueueId, self.StreamRef, self.MessageLen, self.MessageData, self.MessageType, self.Priority]
  def _fields(self):
    return 'Id|QueueId|Status|MessageId|EventQueueId|StreamRef|MessageLen|MessageData|MessageType|Priority'.split('|')
  def execRouterForUpd(self):
    result = self._connect.action('StreamsRouterForUpd', self._data())
    self._store(result)
  def readRouterForUpd(self, Id, QueueId, Status):
    self.Id = Id
    self.QueueId = QueueId
    self.Status = Status
    try:
      self.execRouterForUpd()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsRoute(object):
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
    result = self._connect.action('StreamsRoute', self._data())
    self._store(result)
  def runRoute(self, Id, QueueId, USId):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.execRoute()

class DBStreamsByMessageID(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageId = result[2]
    self.QueueId = result[3]
    self.EventQueueId = result[4]
    self.StreamRef = result[5]
    self.StreamType = result[6]
    self.StreamDescr = result[7]
    self.MessageLen = result[8]
    self.MessageType = result[9]
    self.Priority = result[10]
    self.Status = result[11]
    self.DateCreated = result[12]
    self.USId = result[13]
    self.TmStamp = result[14]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InMessageId|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByMessageID(self):
    self._query = self._connect.query('StreamsByMessageID', self._data())
  def fetchByMessageID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByMessageID(self._connect)
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

class DBStreamsByMessageIdStreamType(object):
  __slots__ = ['_connect', '_query', 'MessageId', 'StreamType', 'Id', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageId = 0
    self.StreamType = ''
    self.Id = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageId = result[0]
    self.StreamType = result[1]
    self.Id = result[2]
    self.QueueId = result[3]
    self.EventQueueId = result[4]
    self.StreamRef = result[5]
    self.StreamDescr = result[6]
    self.MessageLen = result[7]
    self.MessageType = result[8]
    self.Priority = result[9]
    self.Status = result[10]
    self.DateCreated = result[11]
    self.USId = result[12]
    self.TmStamp = result[13]
  def _data(self):
    return [self.MessageId, self.StreamType, self.Id, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'MessageId|StreamType|Id|QueueId|EventQueueId|StreamRef|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByMessageIdStreamType(self):
    self._query = self._connect.query('StreamsByMessageIdStreamType', self._data())
  def fetchByMessageIdStreamType(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByMessageIdStreamType(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMessageIdStreamType(self):
    self._connect.cancel(self._query)
  def loadByMessageIdStreamType(self):
    self.queryByMessageIdStreamType()
    result = []
    while 1:
      rc, rec = self.fetchByMessageIdStreamType()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByMessageIDData(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp', 'MessageData']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
    self.MessageData = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageId = result[2]
    self.QueueId = result[3]
    self.EventQueueId = result[4]
    self.StreamRef = result[5]
    self.StreamType = result[6]
    self.StreamDescr = result[7]
    self.MessageLen = result[8]
    self.MessageType = result[9]
    self.Priority = result[10]
    self.Status = result[11]
    self.DateCreated = result[12]
    self.USId = result[13]
    self.TmStamp = result[14]
    self.MessageData = result[15]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp, self.MessageData]
  def _fields(self):
    return 'InMessageId|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp|MessageData'.split('|')
  def queryByMessageIDData(self):
    self._query = self._connect.query('StreamsByMessageIDData', self._data())
  def fetchByMessageIDData(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByMessageIDData(self._connect)
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

class DBStreamsUpdStatus(object):
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
    result = self._connect.action('StreamsUpdStatus', self._data())
    self._store(result)
  def runUpdStatus(self, Id, Status, USId):
    self.Id = Id
    self.Status = Status
    self.USId = USId
    self.execUpdStatus()

class DBStreamsByQueue(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InStatus', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InStatus = 0
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InStatus = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.MessageId = result[5]
    self.QueueId = result[6]
    self.EventQueueId = result[7]
    self.StreamRef = result[8]
    self.StreamType = result[9]
    self.StreamDescr = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.Priority = result[13]
    self.Status = result[14]
    self.DateCreated = result[15]
    self.USId = result[16]
    self.TmStamp = result[17]
  def _data(self):
    return [self.InQueue, self.InStatus, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InQueue|InStatus|InDateFrom|InDateTo|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByQueue(self):
    self._query = self._connect.query('StreamsByQueue', self._data())
  def fetchByQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByQueue(self._connect)
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

class DBStreamsByQueueAll(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageId = result[4]
    self.QueueId = result[5]
    self.EventQueueId = result[6]
    self.StreamRef = result[7]
    self.StreamType = result[8]
    self.StreamDescr = result[9]
    self.MessageLen = result[10]
    self.MessageType = result[11]
    self.Priority = result[12]
    self.Status = result[13]
    self.DateCreated = result[14]
    self.USId = result[15]
    self.TmStamp = result[16]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByQueueAll(self):
    self._query = self._connect.query('StreamsByQueueAll', self._data())
  def fetchByQueueAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByQueueAll(self._connect)
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

class DBStreamsByQueueAlli3Batch(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'Sourcesysid', 'Reference', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.Sourcesysid = ''
    self.Reference = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageId = result[4]
    self.QueueId = result[5]
    self.Sourcesysid = result[6]
    self.Reference = result[7]
    self.EventQueueId = result[8]
    self.StreamRef = result[9]
    self.StreamType = result[10]
    self.StreamDescr = result[11]
    self.MessageLen = result[12]
    self.MessageType = result[13]
    self.Priority = result[14]
    self.Status = result[15]
    self.DateCreated = result[16]
    self.USId = result[17]
    self.TmStamp = result[18]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.Sourcesysid, self.Reference, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|MessageId|QueueId|Sourcesysid|Reference|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByQueueAlli3Batch(self):
    self._query = self._connect.query('StreamsByQueueAlli3Batch', self._data())
  def fetchByQueueAlli3Batch(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByQueueAlli3Batch(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByQueueAlli3Batch(self):
    self._connect.cancel(self._query)
  def loadByQueueAlli3Batch(self):
    self.queryByQueueAlli3Batch()
    result = []
    while 1:
      rc, rec = self.fetchByQueueAlli3Batch()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByStreamRef(object):
  __slots__ = ['_connect', '_query', 'InStreamRef', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStreamRef = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStreamRef = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageId = result[4]
    self.QueueId = result[5]
    self.EventQueueId = result[6]
    self.StreamRef = result[7]
    self.StreamType = result[8]
    self.StreamDescr = result[9]
    self.MessageLen = result[10]
    self.MessageType = result[11]
    self.Priority = result[12]
    self.Status = result[13]
    self.DateCreated = result[14]
    self.USId = result[15]
    self.TmStamp = result[16]
  def _data(self):
    return [self.InStreamRef, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InStreamRef|InDateFrom|InDateTo|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByStreamRef(self):
    self._query = self._connect.query('StreamsByStreamRef', self._data())
  def fetchByStreamRef(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByStreamRef(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByStreamRef(self):
    self._connect.cancel(self._query)
  def loadByStreamRef(self):
    self.queryByStreamRef()
    result = []
    while 1:
      rc, rec = self.fetchByStreamRef()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByQStreamRef(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InStreamRef', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InStreamRef = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InStreamRef = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.MessageId = result[5]
    self.QueueId = result[6]
    self.EventQueueId = result[7]
    self.StreamRef = result[8]
    self.StreamType = result[9]
    self.StreamDescr = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.Priority = result[13]
    self.Status = result[14]
    self.DateCreated = result[15]
    self.USId = result[16]
    self.TmStamp = result[17]
  def _data(self):
    return [self.InQueue, self.InStreamRef, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InQueue|InStreamRef|InDateFrom|InDateTo|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryByQStreamRef(self):
    self._query = self._connect.query('StreamsByQStreamRef', self._data())
  def fetchByQStreamRef(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByQStreamRef(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByQStreamRef(self):
    self._connect.cancel(self._query)
  def loadByQStreamRef(self):
    self.queryByQStreamRef()
    result = []
    while 1:
      rc, rec = self.fetchByQStreamRef()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsStatusCount(object):
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
    result = self._connect.action('StreamsStatusCount', self._data())
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

class DBStreamsStatusCountAll(object):
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
    result = self._connect.action('StreamsStatusCountAll', self._data())
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

class DBStreamsByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'Id', 'MessageId', 'QueueId', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.Id = result[1]
    self.MessageId = result[2]
    self.QueueId = result[3]
    self.EventQueueId = result[4]
    self.StreamRef = result[5]
    self.StreamType = result[6]
    self.StreamDescr = result[7]
    self.MessageLen = result[8]
    self.MessageData = result[9]
    self.MessageType = result[10]
    self.Priority = result[11]
    self.Status = result[12]
    self.DateCreated = result[13]
    self.USId = result[14]
    self.TmStamp = result[15]
  def _data(self):
    return [self.InID, self.Id, self.MessageId, self.QueueId, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InID|Id|MessageId|QueueId|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageData|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def execByID(self):
    result = self._connect.action('StreamsByID', self._data())
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

class DBStreamsUpdQueue(object):
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
    result = self._connect.action('StreamsUpdQueue', self._data())
    self._store(result)
  def runUpdQueue(self, InMsgNo, InQueueID):
    self.InMsgNo = InMsgNo
    self.InQueueID = InQueueID
    self.execUpdQueue()

class DBStreamsFilemqForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'MessageID', 'EventQueueID', 'StreamRef', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'StreamCount', 'ReplyQueueID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.MessageID = 0
    self.EventQueueID = ''
    self.StreamRef = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.Priority = 0
    self.StreamCount = 0
    self.ReplyQueueID = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.MessageID = result[3]
    self.EventQueueID = result[4]
    self.StreamRef = result[5]
    self.MessageLen = result[6]
    self.MessageData = result[7]
    self.MessageType = result[8]
    self.Priority = result[9]
    self.StreamCount = result[10]
    self.ReplyQueueID = result[11]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.MessageID, self.EventQueueID, self.StreamRef, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.StreamCount, self.ReplyQueueID]
  def _fields(self):
    return 'Id|QueueId|Status|MessageID|EventQueueID|StreamRef|MessageLen|MessageData|MessageType|Priority|StreamCount|ReplyQueueID'.split('|')
  def execFilemqForUpd(self):
    result = self._connect.action('StreamsFilemqForUpd', self._data())
    self._store(result)
  def readFilemqForUpd(self, Id, QueueId, Status):
    self.Id = Id
    self.QueueId = QueueId
    self.Status = Status
    try:
      self.execFilemqForUpd()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsUpdateStreamRef(object):
  __slots__ = ['_connect', '_query', 'Id', 'StreamRef', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.StreamRef = ''
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.StreamRef = result[1]
    self.USId = result[2]
  def _data(self):
    return [self.Id, self.StreamRef, self.USId]
  def _fields(self):
    return 'Id|StreamRef|USId'.split('|')
  def execUpdateStreamRef(self):
    result = self._connect.action('StreamsUpdateStreamRef', self._data())
    self._store(result)
  def runUpdateStreamRef(self, Id, StreamRef, USId):
    self.Id = Id
    self.StreamRef = StreamRef
    self.USId = USId
    self.execUpdateStreamRef()

class DBStreamsBySourceAlli3BatchRTGS(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageId', 'QueueId', 'Sourcesysid', 'Reference', 'EventQueueId', 'StreamRef', 'StreamType', 'StreamDescr', 'MessageLen', 'MessageType', 'Priority', 'Status', 'DateCreated', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageId = 0
    self.QueueId = ''
    self.Sourcesysid = ''
    self.Reference = ''
    self.EventQueueId = ''
    self.StreamRef = ''
    self.StreamType = ''
    self.StreamDescr = ''
    self.MessageLen = 0
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageId = result[4]
    self.QueueId = result[5]
    self.Sourcesysid = result[6]
    self.Reference = result[7]
    self.EventQueueId = result[8]
    self.StreamRef = result[9]
    self.StreamType = result[10]
    self.StreamDescr = result[11]
    self.MessageLen = result[12]
    self.MessageType = result[13]
    self.Priority = result[14]
    self.Status = result[15]
    self.DateCreated = result[16]
    self.USId = result[17]
    self.TmStamp = result[18]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageId, self.QueueId, self.Sourcesysid, self.Reference, self.EventQueueId, self.StreamRef, self.StreamType, self.StreamDescr, self.MessageLen, self.MessageType, self.Priority, self.Status, self.DateCreated, self.USId, self.TmStamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|MessageId|QueueId|Sourcesysid|Reference|EventQueueId|StreamRef|StreamType|StreamDescr|MessageLen|MessageType|Priority|Status|DateCreated|USId|TmStamp'.split('|')
  def queryBySourceAlli3BatchRTGS(self):
    self._query = self._connect.query('StreamsBySourceAlli3BatchRTGS', self._data())
  def fetchBySourceAlli3BatchRTGS(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsBySourceAlli3BatchRTGS(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBySourceAlli3BatchRTGS(self):
    self._connect.cancel(self._query)
  def loadBySourceAlli3BatchRTGS(self):
    self.queryBySourceAlli3BatchRTGS()
    result = []
    while 1:
      rc, rec = self.fetchBySourceAlli3BatchRTGS()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByIDGetReference(object):
  __slots__ = ['_connect', '_query', 'MessageId', 'content']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageId = 0
    self.content = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageId = result[0]
    self.content = result[1]
  def _data(self):
    return [self.MessageId, self.content]
  def _fields(self):
    return 'MessageId|content'.split('|')
  def execByIDGetReference(self):
    result = self._connect.action('StreamsByIDGetReference', self._data())
    self._store(result)
  def readByIDGetReference(self, MessageId):
    self.MessageId = MessageId
    try:
      self.execByIDGetReference()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamsByMessageExclusionsi3Batch(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InQueue = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Reference = result[3]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Reference]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Reference'.split('|')
  def queryByMessageExclusionsi3Batch(self):
    self._query = self._connect.query('StreamsByMessageExclusionsi3Batch', self._data())
  def fetchByMessageExclusionsi3Batch(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByMessageExclusionsi3Batch(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMessageExclusionsi3Batch(self):
    self._connect.cancel(self._query)
  def loadByMessageExclusionsi3Batch(self):
    self.queryByMessageExclusionsi3Batch()
    result = []
    while 1:
      rc, rec = self.fetchByMessageExclusionsi3Batch()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsByReplyGetCorrBanks(object):
  __slots__ = ['_connect', '_query', 'InDateFrom', 'InDateTo', 'Reference', 'MessageData', 'MessageLen']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Reference = ''
    self.MessageData = 0
    self.MessageLen = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDateFrom = result[0]
    self.InDateTo = result[1]
    self.Reference = result[2]
    self.MessageData = result[3]
    self.MessageLen = result[4]
  def _data(self):
    return [self.InDateFrom, self.InDateTo, self.Reference, self.MessageData, self.MessageLen]
  def _fields(self):
    return 'InDateFrom|InDateTo|Reference|MessageData|MessageLen'.split('|')
  def queryByReplyGetCorrBanks(self):
    self._query = self._connect.query('StreamsByReplyGetCorrBanks', self._data())
  def fetchByReplyGetCorrBanks(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStreamsByReplyGetCorrBanks(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByReplyGetCorrBanks(self):
    self._connect.cancel(self._query)
  def loadByReplyGetCorrBanks(self):
    self.queryByReplyGetCorrBanks()
    result = []
    while 1:
      rc, rec = self.fetchByReplyGetCorrBanks()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStreamsForUpdate(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'Messageid', 'EventQueueID', 'StreamRef', 'MessageLen', 'MessageData', 'MessageType', 'Priority', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.Messageid = 0
    self.EventQueueID = ''
    self.StreamRef = ''
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
    self.Messageid = result[3]
    self.EventQueueID = result[4]
    self.StreamRef = result[5]
    self.MessageLen = result[6]
    self.MessageData = result[7]
    self.MessageType = result[8]
    self.Priority = result[9]
    self.DateCreated = result[10]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.Messageid, self.EventQueueID, self.StreamRef, self.MessageLen, self.MessageData, self.MessageType, self.Priority, self.DateCreated]
  def _fields(self):
    return 'Id|QueueId|Status|Messageid|EventQueueID|StreamRef|MessageLen|MessageData|MessageType|Priority|DateCreated'.split('|')
  def execForUpdate(self):
    result = self._connect.action('StreamsForUpdate', self._data())
    self._store(result)
  def readForUpdate(self, Id, QueueId, Status):
    self.Id = Id
    self.QueueId = QueueId
    self.Status = Status
    try:
      self.execForUpdate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

