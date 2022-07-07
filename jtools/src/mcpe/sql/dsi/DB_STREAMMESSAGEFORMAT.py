from INTRINSICS import *
### generated code from DBPortal ###

class DBStreamMessageFormat(object):
  __slots__ = ['_connect', '_query', 'Id', 'Format', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Format = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Format = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.Id, self.Format, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Format|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StreamMessageFormatInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Format, USId, TmStamp):
    self.Id = Id
    self.Format = Format
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StreamMessageFormatUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Format, USId, TmStamp):
    self.Id = Id
    self.Format = Format
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StreamMessageFormatSelectOne', self._data())
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

class DBStreamMessageFormatDeleteOne(object):
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
    result = self._connect.action('StreamMessageFormatDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

