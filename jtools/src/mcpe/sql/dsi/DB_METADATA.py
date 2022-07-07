from INTRINSICS import *
### generated code from DBPortal ###

MetaDataTagConst = {
  'MQ_REPORT_FLAG' : 0, 0 : 'MQ_REPORT_FLAG',
  'MQ_CORELLID' : 1, 1 : 'MQ_CORELLID',
  'MQ_MESSAGEID' : 2, 2 : 'MQ_MESSAGEID',
  'MQ_REPLY_QUEUE' : 3, 3 : 'MQ_REPLY_QUEUE',
  }
MetaDataDataTypeConst = {
  'StringType' : 1, 1 : 'StringType',
  'IntegerType' : 2, 2 : 'IntegerType',
  'DoubleType' : 3, 3 : 'DoubleType',
  'DateType' : 4, 4 : 'DateType',
  }
class DBMetaData(object):
  __slots__ = ['_connect', '_query', 'ID', 'MessageID', 'ChildID', 'Tag', 'Value', 'DataType', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.MessageID = 0
    self.ChildID = 0
    self.Tag = ''
    self.Value = ''
    self.DataType = 0
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.MessageID = result[1]
    self.ChildID = result[2]
    self.Tag = result[3]
    self.Value = result[4]
    self.DataType = result[5]
    self.USId = result[6]
    self.TMStamp = result[7]
  def _data(self):
    return [self.ID, self.MessageID, self.ChildID, self.Tag, self.Value, self.DataType, self.USId, self.TMStamp]
  def _fields(self):
    return 'ID|MessageID|ChildID|Tag|Value|DataType|USId|TMStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('MetaDataInsert', self._data())
    self._store(result)
  def runInsert(self, ID, MessageID, ChildID, Tag, Value, DataType, USId, TMStamp):
    self.ID = ID
    self.MessageID = MessageID
    self.ChildID = ChildID
    self.Tag = Tag
    self.Value = Value
    self.DataType = DataType
    self.USId = USId
    self.TMStamp = TMStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('MetaDataUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, MessageID, ChildID, Tag, Value, DataType, USId, TMStamp):
    self.ID = ID
    self.MessageID = MessageID
    self.ChildID = ChildID
    self.Tag = Tag
    self.Value = Value
    self.DataType = DataType
    self.USId = USId
    self.TMStamp = TMStamp
    self.execUpdate()

class DBMetaDataGetByMessage(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'ID', 'Tag', 'Value', 'DataType']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.ID = 0
    self.Tag = ''
    self.Value = ''
    self.DataType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.ID = result[1]
    self.Tag = result[2]
    self.Value = result[3]
    self.DataType = result[4]
  def _data(self):
    return [self.MessageID, self.ID, self.Tag, self.Value, self.DataType]
  def _fields(self):
    return 'MessageID|ID|Tag|Value|DataType'.split('|')
  def queryGetByMessage(self):
    self._query = self._connect.query('MetaDataGetByMessage', self._data())
  def fetchGetByMessage(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMetaDataGetByMessage(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetByMessage(self):
    self._connect.cancel(self._query)
  def loadGetByMessage(self):
    self.queryGetByMessage()
    result = []
    while 1:
      rc, rec = self.fetchGetByMessage()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMetaDataGetByMessageTag(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'Tag', 'Value', 'DataType']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.Tag = ''
    self.Value = ''
    self.DataType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.Tag = result[1]
    self.Value = result[2]
    self.DataType = result[3]
  def _data(self):
    return [self.MessageID, self.Tag, self.Value, self.DataType]
  def _fields(self):
    return 'MessageID|Tag|Value|DataType'.split('|')
  def execGetByMessageTag(self):
    result = self._connect.action('MetaDataGetByMessageTag', self._data())
    self._store(result)
  def readGetByMessageTag(self, MessageID, Tag):
    self.MessageID = MessageID
    self.Tag = Tag
    try:
      self.execGetByMessageTag()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBMetaDataGetByMessageTags(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'Tag', 'Value', 'DataType', 'Tags']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.Tag = ''
    self.Value = ''
    self.DataType = 0
    self.Tags = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.Tag = result[1]
    self.Value = result[2]
    self.DataType = result[3]
    self.Tags = result[4]
  def _data(self):
    return [self.MessageID, self.Tag, self.Value, self.DataType, self.Tags]
  def _fields(self):
    return 'MessageID|Tag|Value|DataType|Tags'.split('|')
  def queryGetByMessageTags(self):
    self._query = self._connect.query('MetaDataGetByMessageTags', self._data())
  def fetchGetByMessageTags(self):
    rc, result = self._connect.fetch(self._query)
    record = DBMetaDataGetByMessageTags(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetByMessageTags(self):
    self._connect.cancel(self._query)
  def loadGetByMessageTags(self):
    self.queryGetByMessageTags()
    result = []
    while 1:
      rc, rec = self.fetchGetByMessageTags()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBMetaDataGetByMessageTagInt(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'Tag', 'Value', 'DataType']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.Tag = ''
    self.Value = 0
    self.DataType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.Tag = result[1]
    self.Value = result[2]
    self.DataType = result[3]
  def _data(self):
    return [self.MessageID, self.Tag, self.Value, self.DataType]
  def _fields(self):
    return 'MessageID|Tag|Value|DataType'.split('|')
  def execGetByMessageTagInt(self):
    result = self._connect.action('MetaDataGetByMessageTagInt', self._data())
    self._store(result)
  def readGetByMessageTagInt(self, MessageID, Tag):
    self.MessageID = MessageID
    self.Tag = Tag
    try:
      self.execGetByMessageTagInt()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

