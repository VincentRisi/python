from INTRINSICS import *
### generated code from DBPortal ###

class DBStreamFieldMsgRel(object):
  __slots__ = ['_connect', '_query', 'FieldId', 'StreamId', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.FieldId = ''
    self.StreamId = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FieldId = result[0]
    self.StreamId = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.FieldId, self.StreamId, self.USId, self.TmStamp]
  def _fields(self):
    return 'FieldId|StreamId|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StreamFieldMsgRelInsert', self._data())
    self._store(result)
  def runInsert(self, FieldId, StreamId, USId, TmStamp):
    self.FieldId = FieldId
    self.StreamId = StreamId
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()

class DBStreamFieldMsgRelDeleteOne(object):
  __slots__ = ['_connect', '_query', 'FieldId', 'StreamId']
  def __init__(self, connect=None):
    self._connect = connect
    self.FieldId = ''
    self.StreamId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FieldId = result[0]
    self.StreamId = result[1]
  def _data(self):
    return [self.FieldId, self.StreamId]
  def _fields(self):
    return 'FieldId|StreamId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StreamFieldMsgRelDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, FieldId, StreamId):
    self.FieldId = FieldId
    self.StreamId = StreamId
    self.execDeleteOne()

