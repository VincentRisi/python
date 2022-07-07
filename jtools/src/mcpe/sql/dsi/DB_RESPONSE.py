from INTRINSICS import *
### generated code from DBPortal ###

ResponseStatusConst = {
  'Idle' : 0, 0 : 'Idle',
  'Sent' : 1, 1 : 'Sent',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
ResponseMessageTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  'File' : 2, 2 : 'File',
  }
class DBResponse(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageData', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageID = result[1]
    self.Streamid = result[2]
    self.Streamref = result[3]
    self.Sourcequeue = result[4]
    self.QueueID = result[5]
    self.DateCreated = result[6]
    self.Status = result[7]
    self.MessageLen = result[8]
    self.MessageData = result[9]
    self.MessageType = result[10]
    self.USId = result[11]
    self.Tmstamp = result[12]
  def _data(self):
    return [self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageData, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageData|MessageType|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('ResponseInsert', self._data())
    self._store(result)
  def runInsert(self, Id, MessageID, Streamid, Streamref, Sourcequeue, QueueID, DateCreated, Status, MessageLen, MessageData, MessageType, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.Streamid = Streamid
    self.Streamref = Streamref
    self.Sourcequeue = Sourcequeue
    self.QueueID = QueueID
    self.DateCreated = DateCreated
    self.Status = Status
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('ResponseUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, MessageID, Streamid, Streamref, Sourcequeue, QueueID, DateCreated, Status, MessageLen, MessageData, MessageType, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.Streamid = Streamid
    self.Streamref = Streamref
    self.Sourcequeue = Sourcequeue
    self.QueueID = QueueID
    self.DateCreated = DateCreated
    self.Status = Status
    self.MessageLen = MessageLen
    self.MessageData = MessageData
    self.MessageType = MessageType
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('ResponseSelectOne', self._data())
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
    result = self._connect.action('ResponseSelectOneUpd', self._data())
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
    self._query = self._connect.query('ResponseSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponse(self._connect)
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

class DBResponseDeleteOne(object):
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
    result = self._connect.action('ResponseDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBResponseExists(object):
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
    result = self._connect.action('ResponseExists', self._data())
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

class DBResponseCount(object):
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
    result = self._connect.action('ResponseCount', self._data())
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

class DBResponseByQueueDate(object):
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
    self._query = self._connect.query('ResponseByQueueDate', self._data())
  def fetchByQueueDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByQueueDate(self._connect)
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

class DBResponseByDate(object):
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
    self._query = self._connect.query('ResponseByDate', self._data())
  def fetchByDate(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByDate(self._connect)
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

class DBResponseQueues(object):
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
    self._query = self._connect.query('ResponseQueues', self._data())
  def fetchQueues(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseQueues(self._connect)
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

class DBResponseGetData(object):
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
    result = self._connect.action('ResponseGetData', self._data())
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

class DBResponseByMessageID(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.Streamid = result[3]
    self.Streamref = result[4]
    self.Sourcequeue = result[5]
    self.QueueID = result[6]
    self.DateCreated = result[7]
    self.Status = result[8]
    self.MessageLen = result[9]
    self.MessageType = result[10]
    self.USId = result[11]
    self.Tmstamp = result[12]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageId|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageType|USId|Tmstamp'.split('|')
  def queryByMessageID(self):
    self._query = self._connect.query('ResponseByMessageID', self._data())
  def fetchByMessageID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByMessageID(self._connect)
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

class DBResponseByMessageIDData(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageData', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.Streamid = result[3]
    self.Streamref = result[4]
    self.Sourcequeue = result[5]
    self.QueueID = result[6]
    self.DateCreated = result[7]
    self.Status = result[8]
    self.MessageLen = result[9]
    self.MessageData = result[10]
    self.MessageType = result[11]
    self.USId = result[12]
    self.Tmstamp = result[13]
  def _data(self):
    return [self.InMessageId, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageData, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageId|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageData|MessageType|USId|Tmstamp'.split('|')
  def queryByMessageIDData(self):
    self._query = self._connect.query('ResponseByMessageIDData', self._data())
  def fetchByMessageIDData(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByMessageIDData(self._connect)
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

class DBResponseResponse(object):
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
  def execResponse(self):
    result = self._connect.action('ResponseResponse', self._data())
    self._store(result)
  def runResponse(self, Id, QueueId, USId):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.execResponse()

class DBResponseForUpd(object):
  __slots__ = ['_connect', '_query', 'Id', 'QueueId', 'Status', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'DateCreated', 'MessageLen', 'MessageData', 'MessageType', 'ResponseQueue']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.QueueId = ''
    self.Status = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.DateCreated = ''
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.ResponseQueue = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
    self.MessageID = result[3]
    self.Streamid = result[4]
    self.Streamref = result[5]
    self.Sourcequeue = result[6]
    self.DateCreated = result[7]
    self.MessageLen = result[8]
    self.MessageData = result[9]
    self.MessageType = result[10]
    self.ResponseQueue = result[11]
  def _data(self):
    return [self.Id, self.QueueId, self.Status, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.DateCreated, self.MessageLen, self.MessageData, self.MessageType, self.ResponseQueue]
  def _fields(self):
    return 'Id|QueueId|Status|MessageID|Streamid|Streamref|Sourcequeue|DateCreated|MessageLen|MessageData|MessageType|ResponseQueue'.split('|')
  def execForUpd(self):
    result = self._connect.action('ResponseForUpd', self._data())
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

class DBResponseRoute(object):
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
    result = self._connect.action('ResponseRoute', self._data())
    self._store(result)
  def runRoute(self, Id, QueueId, USId):
    self.Id = Id
    self.QueueId = QueueId
    self.USId = USId
    self.execRoute()

class DBResponseUpdStatus(object):
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
    result = self._connect.action('ResponseUpdStatus', self._data())
    self._store(result)
  def runUpdStatus(self, Id, Status, USId):
    self.Id = Id
    self.Status = Status
    self.USId = USId
    self.execUpdStatus()

class DBResponseByQueue(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InStatus', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InStatus = 0
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageType = 0
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
    self.Streamid = result[6]
    self.Streamref = result[7]
    self.Sourcequeue = result[8]
    self.QueueID = result[9]
    self.DateCreated = result[10]
    self.Status = result[11]
    self.MessageLen = result[12]
    self.MessageType = result[13]
    self.USId = result[14]
    self.Tmstamp = result[15]
  def _data(self):
    return [self.InQueue, self.InStatus, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InQueue|InStatus|InDateFrom|InDateTo|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageType|USId|Tmstamp'.split('|')
  def queryByQueue(self):
    self._query = self._connect.query('ResponseByQueue', self._data())
  def fetchByQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByQueue(self._connect)
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

class DBResponseByQueueAll(object):
  __slots__ = ['_connect', '_query', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageType = 0
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
    self.Streamid = result[5]
    self.Streamref = result[6]
    self.Sourcequeue = result[7]
    self.QueueID = result[8]
    self.DateCreated = result[9]
    self.Status = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.USId = result[13]
    self.Tmstamp = result[14]
  def _data(self):
    return [self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InQueue|InDateFrom|InDateTo|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageType|USId|Tmstamp'.split('|')
  def queryByQueueAll(self):
    self._query = self._connect.query('ResponseByQueueAll', self._data())
  def fetchByQueueAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByQueueAll(self._connect)
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

class DBResponseByStreamRefQueue(object):
  __slots__ = ['_connect', '_query', 'InStreamRef', 'InQueue', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStreamRef = ''
    self.InQueue = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStreamRef = result[0]
    self.InQueue = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.Id = result[4]
    self.MessageID = result[5]
    self.Streamid = result[6]
    self.Streamref = result[7]
    self.Sourcequeue = result[8]
    self.QueueID = result[9]
    self.DateCreated = result[10]
    self.Status = result[11]
    self.MessageLen = result[12]
    self.MessageType = result[13]
    self.USId = result[14]
    self.Tmstamp = result[15]
  def _data(self):
    return [self.InStreamRef, self.InQueue, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InStreamRef|InQueue|InDateFrom|InDateTo|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageType|USId|Tmstamp'.split('|')
  def queryByStreamRefQueue(self):
    self._query = self._connect.query('ResponseByStreamRefQueue', self._data())
  def fetchByStreamRefQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByStreamRefQueue(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByStreamRefQueue(self):
    self._connect.cancel(self._query)
  def loadByStreamRefQueue(self):
    self.queryByStreamRefQueue()
    result = []
    while 1:
      rc, rec = self.fetchByStreamRefQueue()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBResponseByStreamRef(object):
  __slots__ = ['_connect', '_query', 'InStreamRef', 'InDateFrom', 'InDateTo', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStreamRef = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStreamRef = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.Id = result[3]
    self.MessageID = result[4]
    self.Streamid = result[5]
    self.Streamref = result[6]
    self.Sourcequeue = result[7]
    self.QueueID = result[8]
    self.DateCreated = result[9]
    self.Status = result[10]
    self.MessageLen = result[11]
    self.MessageType = result[12]
    self.USId = result[13]
    self.Tmstamp = result[14]
  def _data(self):
    return [self.InStreamRef, self.InDateFrom, self.InDateTo, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InStreamRef|InDateFrom|InDateTo|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageType|USId|Tmstamp'.split('|')
  def queryByStreamRef(self):
    self._query = self._connect.query('ResponseByStreamRef', self._data())
  def fetchByStreamRef(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByStreamRef(self._connect)
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

class DBResponseStatusCount(object):
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
    result = self._connect.action('ResponseStatusCount', self._data())
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

class DBResponseStatusCountAll(object):
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
    result = self._connect.action('ResponseStatusCountAll', self._data())
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

class DBResponseByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageData', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.Streamid = result[3]
    self.Streamref = result[4]
    self.Sourcequeue = result[5]
    self.QueueID = result[6]
    self.DateCreated = result[7]
    self.Status = result[8]
    self.MessageLen = result[9]
    self.MessageData = result[10]
    self.MessageType = result[11]
    self.USId = result[12]
    self.Tmstamp = result[13]
  def _data(self):
    return [self.InID, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageData, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InID|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageData|MessageType|USId|Tmstamp'.split('|')
  def execByID(self):
    result = self._connect.action('ResponseByID', self._data())
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

class DBResponseUpdQueue(object):
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
    result = self._connect.action('ResponseUpdQueue', self._data())
    self._store(result)
  def runUpdQueue(self, InMsgNo, InQueueID):
    self.InMsgNo = InMsgNo
    self.InQueueID = InQueueID
    self.execUpdQueue()

class DBResponseByStreamID(object):
  __slots__ = ['_connect', '_query', 'InStreamID', 'Id', 'MessageID', 'Streamid', 'Streamref', 'Sourcequeue', 'QueueID', 'DateCreated', 'Status', 'MessageLen', 'MessageData', 'MessageType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InStreamID = 0
    self.Id = 0
    self.MessageID = 0
    self.Streamid = 0
    self.Streamref = ''
    self.Sourcequeue = ''
    self.QueueID = ''
    self.DateCreated = ''
    self.Status = 0
    self.MessageLen = 0
    self.MessageData = 0
    self.MessageType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InStreamID = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.Streamid = result[3]
    self.Streamref = result[4]
    self.Sourcequeue = result[5]
    self.QueueID = result[6]
    self.DateCreated = result[7]
    self.Status = result[8]
    self.MessageLen = result[9]
    self.MessageData = result[10]
    self.MessageType = result[11]
    self.USId = result[12]
    self.Tmstamp = result[13]
  def _data(self):
    return [self.InStreamID, self.Id, self.MessageID, self.Streamid, self.Streamref, self.Sourcequeue, self.QueueID, self.DateCreated, self.Status, self.MessageLen, self.MessageData, self.MessageType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InStreamID|Id|MessageID|Streamid|Streamref|Sourcequeue|QueueID|DateCreated|Status|MessageLen|MessageData|MessageType|USId|Tmstamp'.split('|')
  def queryByStreamID(self):
    self._query = self._connect.query('ResponseByStreamID', self._data())
  def fetchByStreamID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseByStreamID(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByStreamID(self):
    self._connect.cancel(self._query)
  def loadByStreamID(self):
    self.queryByStreamID()
    result = []
    while 1:
      rc, rec = self.fetchByStreamID()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBResponseTVSlurpIDs(object):
  __slots__ = ['_connect', '_query', 'Id', 'Reference', 'WhereClause']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.Reference = ''
    self.WhereClause = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Reference = result[1]
    self.WhereClause = result[2]
  def _data(self):
    return [self.Id, self.Reference, self.WhereClause]
  def _fields(self):
    return 'Id|Reference|WhereClause'.split('|')
  def queryTVSlurpIDs(self):
    self._query = self._connect.query('ResponseTVSlurpIDs', self._data())
  def fetchTVSlurpIDs(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseTVSlurpIDs(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelTVSlurpIDs(self):
    self._connect.cancel(self._query)
  def loadTVSlurpIDs(self):
    self.queryTVSlurpIDs()
    result = []
    while 1:
      rc, rec = self.fetchTVSlurpIDs()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBResponseTVCount(object):
  __slots__ = ['_connect', '_query', 'ans', 'WhereClause']
  def __init__(self, connect=None):
    self._connect = connect
    self.ans = 0
    self.WhereClause = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ans = result[0]
    self.WhereClause = result[1]
  def _data(self):
    return [self.ans, self.WhereClause]
  def _fields(self):
    return 'ans|WhereClause'.split('|')
  def execTVCount(self):
    result = self._connect.action('ResponseTVCount', self._data())
    self._store(result)
  def readTVCount(self, WhereClause):
    self.WhereClause = WhereClause
    try:
      self.execTVCount()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBResponseGetByMsgID(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'MessageType', 'MessageLen', 'MessageData']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.MessageType = 0
    self.MessageLen = 0
    self.MessageData = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.MessageType = result[1]
    self.MessageLen = result[2]
    self.MessageData = result[3]
  def _data(self):
    return [self.MessageID, self.MessageType, self.MessageLen, self.MessageData]
  def _fields(self):
    return 'MessageID|MessageType|MessageLen|MessageData'.split('|')
  def queryGetByMsgID(self):
    self._query = self._connect.query('ResponseGetByMsgID', self._data())
  def fetchGetByMsgID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBResponseGetByMsgID(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetByMsgID(self):
    self._connect.cancel(self._query)
  def loadGetByMsgID(self):
    self.queryGetByMsgID()
    result = []
    while 1:
      rc, rec = self.fetchGetByMsgID()
      if rc == 0:
        break
      result.append(rec)
    return result

