from INTRINSICS import *
### generated code from DBPortal ###

class DBAudits(object):
  __slots__ = ['_connect', '_query', 'Id', 'TableName', 'Action', 'Old', 'New', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.TableName = ''
    self.Action = ''
    self.Old = ''
    self.New = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.TableName = result[1]
    self.Action = result[2]
    self.Old = result[3]
    self.New = result[4]
    self.USId = result[5]
    self.TmStamp = result[6]
  def _data(self):
    return [self.Id, self.TableName, self.Action, self.Old, self.New, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|TableName|Action|Old|New|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AuditsInsert', self._data())
    self._store(result)
  def runInsert(self, Id, TableName, Action, Old, New, USId, TmStamp):
    self.Id = Id
    self.TableName = TableName
    self.Action = Action
    self.Old = Old
    self.New = New
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AuditsUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, TableName, Action, Old, New, USId, TmStamp):
    self.Id = Id
    self.TableName = TableName
    self.Action = Action
    self.Old = Old
    self.New = New
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AuditsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id, TableName):
    self.Id = Id
    self.TableName = TableName
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAuditsDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id', 'TableName']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.TableName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.TableName = result[1]
  def _data(self):
    return [self.Id, self.TableName]
  def _fields(self):
    return 'Id|TableName'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('AuditsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id, TableName):
    self.Id = Id
    self.TableName = TableName
    self.execDeleteOne()

