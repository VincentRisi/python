from INTRINSICS import *
### generated code from DBPortal ###

class DBKeyValue(object):
  __slots__ = ['_connect', '_query', 'Topic', 'KeyId', 'ValueType', 'ValueLen', 'ValueData', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Topic = ''
    self.KeyId = ''
    self.ValueType = ''
    self.ValueLen = 0
    self.ValueData = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Topic = result[0]
    self.KeyId = result[1]
    self.ValueType = result[2]
    self.ValueLen = result[3]
    self.ValueData = result[4]
    self.USId = result[5]
    self.TmStamp = result[6]
  def _data(self):
    return [self.Topic, self.KeyId, self.ValueType, self.ValueLen, self.ValueData, self.USId, self.TmStamp]
  def _fields(self):
    return 'Topic|KeyId|ValueType|ValueLen|ValueData|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('KeyValueInsert', self._data())
    self._store(result)
  def runInsert(self, Topic, KeyId, ValueType, ValueLen, ValueData, USId, TmStamp):
    self.Topic = Topic
    self.KeyId = KeyId
    self.ValueType = ValueType
    self.ValueLen = ValueLen
    self.ValueData = ValueData
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('KeyValueUpdate', self._data())
    self._store(result)
  def runUpdate(self, Topic, KeyId, ValueType, ValueLen, ValueData, USId, TmStamp):
    self.Topic = Topic
    self.KeyId = KeyId
    self.ValueType = ValueType
    self.ValueLen = ValueLen
    self.ValueData = ValueData
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('KeyValueSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Topic, KeyId):
    self.Topic = Topic
    self.KeyId = KeyId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBKeyValueDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Topic', 'KeyId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Topic = ''
    self.KeyId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Topic = result[0]
    self.KeyId = result[1]
  def _data(self):
    return [self.Topic, self.KeyId]
  def _fields(self):
    return 'Topic|KeyId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('KeyValueDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Topic, KeyId):
    self.Topic = Topic
    self.KeyId = KeyId
    self.execDeleteOne()

