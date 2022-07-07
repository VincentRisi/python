from INTRINSICS import *
### generated code from DBPortal ###

class DBTestPack(object):
  __slots__ = ['_connect', '_query', 'Name', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.USId = result[1]
    self.TMStamp = result[2]
  def _data(self):
    return [self.Name, self.USId, self.TMStamp]
  def _fields(self):
    return 'Name|USId|TMStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('TestPackInsert', self._data())
    self._store(result)
  def runInsert(self, Name, USId, TMStamp):
    self.Name = Name
    self.USId = USId
    self.TMStamp = TMStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('TestPackUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, USId, TMStamp):
    self.Name = Name
    self.USId = USId
    self.TMStamp = TMStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('TestPackSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name):
    self.Name = Name
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
    self._connect.action('TestPackDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('TestPackSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBTestPack(self._connect)
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

class DBTestPackDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
  def _data(self):
    return [self.Name]
  def _fields(self):
    return 'Name'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('TestPackDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name):
    self.Name = Name
    self.execDeleteOne()

class DBTestPackExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Name = result[1]
  def _data(self):
    return [self.Count, self.Name]
  def _fields(self):
    return 'Count|Name'.split('|')
  def execExists(self):
    result = self._connect.action('TestPackExists', self._data())
    self._store(result)
  def readExists(self, Name):
    self.Name = Name
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBTestPackCount(object):
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
    result = self._connect.action('TestPackCount', self._data())
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

class DBTestPackList(object):
  __slots__ = ['_connect', '_query', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
  def _data(self):
    return [self.Name]
  def _fields(self):
    return 'Name'.split('|')
  def queryList(self):
    self._query = self._connect.query('TestPackList', self._data())
  def fetchList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBTestPackList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelList(self):
    self._connect.cancel(self._query)
  def loadList(self):
    self.queryList()
    result = []
    while 1:
      rc, rec = self.fetchList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBTestPackByPack(object):
  __slots__ = ['_connect', '_query', 'PackName', 'Id', 'SourceSysid', 'Reference', 'QueueId', 'MessageType', 'Priority', 'Status', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.PackName = ''
    self.Id = 0
    self.SourceSysid = ''
    self.Reference = ''
    self.QueueId = ''
    self.MessageType = 0
    self.Priority = 0
    self.Status = 0
    self.DateCreated = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.PackName = result[0]
    self.Id = result[1]
    self.SourceSysid = result[2]
    self.Reference = result[3]
    self.QueueId = result[4]
    self.MessageType = result[5]
    self.Priority = result[6]
    self.Status = result[7]
    self.DateCreated = result[8]
  def _data(self):
    return [self.PackName, self.Id, self.SourceSysid, self.Reference, self.QueueId, self.MessageType, self.Priority, self.Status, self.DateCreated]
  def _fields(self):
    return 'PackName|Id|SourceSysid|Reference|QueueId|MessageType|Priority|Status|DateCreated'.split('|')
  def queryByPack(self):
    self._query = self._connect.query('TestPackByPack', self._data())
  def fetchByPack(self):
    rc, result = self._connect.fetch(self._query)
    record = DBTestPackByPack(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByPack(self):
    self._connect.cancel(self._query)
  def loadByPack(self):
    self.queryByPack()
    result = []
    while 1:
      rc, rec = self.fetchByPack()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBTestPackGetData(object):
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
    result = self._connect.action('TestPackGetData', self._data())
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

class DBTestPackFromMessage(object):
  __slots__ = ['_connect', '_query', 'MessageId', 'PackName', 'MessageData', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageId = 0
    self.PackName = ''
    self.MessageData = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageId = result[0]
    self.PackName = result[1]
    self.MessageData = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.MessageId, self.PackName, self.MessageData, self.USId, self.TmStamp]
  def _fields(self):
    return 'MessageId|PackName|MessageData|USId|TmStamp'.split('|')
  def execFromMessage(self):
    result = self._connect.action('TestPackFromMessage', self._data())
    self._store(result)
  def runFromMessage(self, MessageId, PackName, MessageData, USId, TmStamp):
    self.MessageId = MessageId
    self.PackName = PackName
    self.MessageData = MessageData
    self.USId = USId
    self.TmStamp = TmStamp
    self.execFromMessage()

class DBTestPackRemoveMessage(object):
  __slots__ = ['_connect', '_query', 'MessageId', 'PackName']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageId = 0
    self.PackName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageId = result[0]
    self.PackName = result[1]
  def _data(self):
    return [self.MessageId, self.PackName]
  def _fields(self):
    return 'MessageId|PackName'.split('|')
  def execRemoveMessage(self):
    result = self._connect.action('TestPackRemoveMessage', self._data())
    self._store(result)
  def runRemoveMessage(self, MessageId, PackName):
    self.MessageId = MessageId
    self.PackName = PackName
    self.execRemoveMessage()

