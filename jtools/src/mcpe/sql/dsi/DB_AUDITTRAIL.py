from INTRINSICS import *
### generated code from DBPortal ###

AudittrailActionConst = {
  'StatusChange' : 1, 1 : 'StatusChange',
  'Comment' : 2, 2 : 'Comment',
  }
AudittrailFromStatusConst = {
  'None' : 0, 0 : 'None',
  'Pending' : 1, 1 : 'Pending',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
AudittrailToStatusConst = {
  'None' : 0, 0 : 'None',
  'Pending' : 1, 1 : 'Pending',
  'Complete' : 2, 2 : 'Complete',
  'Error' : 3, 3 : 'Error',
  }
class DBAudittrail(object):
  __slots__ = ['_connect', '_query', 'ID', 'MessageID', 'Action', 'FromStatus', 'ToStatus', 'Comments', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.MessageID = 0
    self.Action = 0
    self.FromStatus = 0
    self.ToStatus = 0
    self.Comments = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.MessageID = result[1]
    self.Action = result[2]
    self.FromStatus = result[3]
    self.ToStatus = result[4]
    self.Comments = result[5]
    self.USId = result[6]
    self.Tmstamp = result[7]
  def _data(self):
    return [self.ID, self.MessageID, self.Action, self.FromStatus, self.ToStatus, self.Comments, self.USId, self.Tmstamp]
  def _fields(self):
    return 'ID|MessageID|Action|FromStatus|ToStatus|Comments|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AudittrailInsert', self._data())
    self._store(result)
  def runInsert(self, ID, MessageID, Action, FromStatus, ToStatus, Comments, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.Action = Action
    self.FromStatus = FromStatus
    self.ToStatus = ToStatus
    self.Comments = Comments
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AudittrailUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, MessageID, Action, FromStatus, ToStatus, Comments, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.Action = Action
    self.FromStatus = FromStatus
    self.ToStatus = ToStatus
    self.Comments = Comments
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AudittrailSelectOne', self._data())
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
    self._query = self._connect.query('AudittrailSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAudittrail(self._connect)
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

class DBAudittrailDeleteOne(object):
  __slots__ = ['_connect', '_query', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
  def _data(self):
    return [self.ID]
  def _fields(self):
    return 'ID'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('AudittrailDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ID):
    self.ID = ID
    self.execDeleteOne()

class DBAudittrailExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.ID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.ID = result[1]
  def _data(self):
    return [self.Count, self.ID]
  def _fields(self):
    return 'Count|ID'.split('|')
  def execExists(self):
    result = self._connect.action('AudittrailExists', self._data())
    self._store(result)
  def readExists(self, ID):
    self.ID = ID
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAudittrailCount(object):
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
    result = self._connect.action('AudittrailCount', self._data())
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

