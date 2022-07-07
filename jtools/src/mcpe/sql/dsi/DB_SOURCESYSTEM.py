from INTRINSICS import *
### generated code from DBPortal ###

SourceSystemStatusConst = {
  'ACTIVE' : 0, 0 : 'ACTIVE',
  'INACTIVE' : 1, 1 : 'INACTIVE',
  'MARKDELETE' : 2, 2 : 'MARKDELETE',
  }
class DBSourceSystem(object):
  __slots__ = ['_connect', '_query', 'ID', 'Name', 'Decription', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = ''
    self.Name = ''
    self.Decription = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.Name = result[1]
    self.Decription = result[2]
    self.Status = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.ID, self.Name, self.Decription, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'ID|Name|Decription|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('SourceSystemInsert', self._data())
    self._store(result)
  def runInsert(self, ID, Name, Decription, Status, USId, TmStamp):
    self.ID = ID
    self.Name = Name
    self.Decription = Decription
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('SourceSystemUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, Name, Decription, Status, USId, TmStamp):
    self.ID = ID
    self.Name = Name
    self.Decription = Decription
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('SourceSystemSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, ID):
    self.ID = ID
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('SourceSystemSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSourceSystem(self._connect)
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

class DBSourceSystemDeleteOne(object):
  __slots__ = ['_connect', '_query', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
  def _data(self):
    return [self.ID]
  def _fields(self):
    return 'ID'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('SourceSystemDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ID):
    self.ID = ID
    self.execDeleteOne()

class DBSourceSystemByName(object):
  __slots__ = ['_connect', '_query', 'Name', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.ID = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.ID = result[1]
  def _data(self):
    return [self.Name, self.ID]
  def _fields(self):
    return 'Name|ID'.split('|')
  def execByName(self):
    result = self._connect.action('SourceSystemByName', self._data())
    self._store(result)
  def readByName(self, Name):
    self.Name = Name
    try:
      self.execByName()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

