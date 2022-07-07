from INTRINSICS import *
### generated code from DBPortal ###

AccountTypeStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  }
class DBAccountType(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Status = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Id, self.Descr, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Descr|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AccountTypeInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Descr, Status, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AccountTypeUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Descr, Status, USId, TmStamp):
    self.Id = Id
    self.Descr = Descr
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AccountTypeSelectOne', self._data())
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

class DBAccountTypeDeleteOne(object):
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
    result = self._connect.action('AccountTypeDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

