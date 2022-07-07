from INTRINSICS import *
### generated code from DBPortal ###

PersistentTypeConst = {
  'StoreString' : 0, 0 : 'StoreString',
  'StoreInteger' : 1, 1 : 'StoreInteger',
  'StoreDouble' : 2, 2 : 'StoreDouble',
  }
class DBPersistent(object):
  __slots__ = ['_connect', '_query', 'Name', 'Ref', 'Type', 'Value', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Ref = ''
    self.Type = 0
    self.Value = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Ref = result[1]
    self.Type = result[2]
    self.Value = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.Name, self.Ref, self.Type, self.Value, self.USId, self.TmStamp]
  def _fields(self):
    return 'Name|Ref|Type|Value|USId|TmStamp'.split('|')
  def execSelectOne(self):
    result = self._connect.action('PersistentSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name, Ref):
    self.Name = Name
    self.Ref = Ref
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def execInsert(self):
    result = self._connect.action('PersistentInsert', self._data())
    self._store(result)
  def runInsert(self, Name, Ref, Type, Value, USId, TmStamp):
    self.Name = Name
    self.Ref = Ref
    self.Type = Type
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('PersistentUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, Ref, Type, Value, USId, TmStamp):
    self.Name = Name
    self.Ref = Ref
    self.Type = Type
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()

class DBPersistentDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Name', 'Ref']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Ref = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Ref = result[1]
  def _data(self):
    return [self.Name, self.Ref]
  def _fields(self):
    return 'Name|Ref'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('PersistentDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name, Ref):
    self.Name = Name
    self.Ref = Ref
    self.execDeleteOne()

class DBPersistentGetForUpdate(object):
  __slots__ = ['_connect', '_query', 'Name', 'Ref', 'Type', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Ref = ''
    self.Type = 0
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Ref = result[1]
    self.Type = result[2]
    self.Value = result[3]
  def _data(self):
    return [self.Name, self.Ref, self.Type, self.Value]
  def _fields(self):
    return 'Name|Ref|Type|Value'.split('|')
  def execGetForUpdate(self):
    result = self._connect.action('PersistentGetForUpdate', self._data())
    self._store(result)
  def readGetForUpdate(self, Name, Ref):
    self.Name = Name
    self.Ref = Ref
    try:
      self.execGetForUpdate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

