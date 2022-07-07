from INTRINSICS import *
### generated code from DBPortal ###

RoutingMessageTypeConst = {
  'Message' : 0, 0 : 'Message',
  'Stream' : 1, 1 : 'Stream',
  'Response' : 2, 2 : 'Response',
  'Reply' : 3, 3 : 'Reply',
  }
RoutingMethodConst = {
  'Auto' : 0, 0 : 'Auto',
  'Manual' : 1, 1 : 'Manual',
  }
class DBRouting(object):
  __slots__ = ['_connect', '_query', 'Id', 'MessageID', 'MessageType', 'Queuefrom', 'Queueto', 'Comments', 'Method', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.MessageID = 0
    self.MessageType = 0
    self.Queuefrom = ''
    self.Queueto = ''
    self.Comments = ''
    self.Method = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.MessageID = result[1]
    self.MessageType = result[2]
    self.Queuefrom = result[3]
    self.Queueto = result[4]
    self.Comments = result[5]
    self.Method = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.Id, self.MessageID, self.MessageType, self.Queuefrom, self.Queueto, self.Comments, self.Method, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Id|MessageID|MessageType|Queuefrom|Queueto|Comments|Method|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('RoutingInsert', self._data())
    self._store(result)
  def runInsert(self, Id, MessageID, MessageType, Queuefrom, Queueto, Comments, Method, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.MessageType = MessageType
    self.Queuefrom = Queuefrom
    self.Queueto = Queueto
    self.Comments = Comments
    self.Method = Method
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('RoutingUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, MessageID, MessageType, Queuefrom, Queueto, Comments, Method, USId, Tmstamp):
    self.Id = Id
    self.MessageID = MessageID
    self.MessageType = MessageType
    self.Queuefrom = Queuefrom
    self.Queueto = Queueto
    self.Comments = Comments
    self.Method = Method
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('RoutingSelectOne', self._data())
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
  def runDeleteAll(self):
    self._connect.action('RoutingDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('RoutingSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBRouting(self._connect)
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

class DBRoutingDeleteOne(object):
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
    result = self._connect.action('RoutingDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBRoutingExists(object):
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
    result = self._connect.action('RoutingExists', self._data())
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

class DBRoutingCount(object):
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
    result = self._connect.action('RoutingCount', self._data())
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

class DBRoutingByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'Id', 'MessageID', 'MessageType', 'Queuefrom', 'Queueto', 'Comments', 'Method', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.Id = 0
    self.MessageID = 0
    self.MessageType = 0
    self.Queuefrom = ''
    self.Queueto = ''
    self.Comments = ''
    self.Method = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.Id = result[1]
    self.MessageID = result[2]
    self.MessageType = result[3]
    self.Queuefrom = result[4]
    self.Queueto = result[5]
    self.Comments = result[6]
    self.Method = result[7]
    self.USId = result[8]
    self.Tmstamp = result[9]
  def _data(self):
    return [self.InID, self.Id, self.MessageID, self.MessageType, self.Queuefrom, self.Queueto, self.Comments, self.Method, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InID|Id|MessageID|MessageType|Queuefrom|Queueto|Comments|Method|USId|Tmstamp'.split('|')
  def execByID(self):
    result = self._connect.action('RoutingByID', self._data())
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

class DBRoutingByMessageID(object):
  __slots__ = ['_connect', '_query', 'InMessageId', 'InMessageType', 'Id', 'MessageID', 'MessageType', 'Queuefrom', 'Queueto', 'Comments', 'Method', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageId = 0
    self.InMessageType = 0
    self.Id = 0
    self.MessageID = 0
    self.MessageType = 0
    self.Queuefrom = ''
    self.Queueto = ''
    self.Comments = ''
    self.Method = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageId = result[0]
    self.InMessageType = result[1]
    self.Id = result[2]
    self.MessageID = result[3]
    self.MessageType = result[4]
    self.Queuefrom = result[5]
    self.Queueto = result[6]
    self.Comments = result[7]
    self.Method = result[8]
    self.USId = result[9]
    self.Tmstamp = result[10]
  def _data(self):
    return [self.InMessageId, self.InMessageType, self.Id, self.MessageID, self.MessageType, self.Queuefrom, self.Queueto, self.Comments, self.Method, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageId|InMessageType|Id|MessageID|MessageType|Queuefrom|Queueto|Comments|Method|USId|Tmstamp'.split('|')
  def queryByMessageID(self):
    self._query = self._connect.query('RoutingByMessageID', self._data())
  def fetchByMessageID(self):
    rc, result = self._connect.fetch(self._query)
    record = DBRoutingByMessageID(self._connect)
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

