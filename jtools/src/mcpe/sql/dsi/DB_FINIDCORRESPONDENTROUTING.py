from INTRINSICS import *
### generated code from DBPortal ###

FinidCorrespondentRoutingStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  }
class DBFinidCorrespondentRouting(object):
  __slots__ = ['_connect', '_query', 'FinId', 'Branchid', 'RouteFinId', 'RouteBranchid', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.Branchid = 0
    self.RouteFinId = 0
    self.RouteBranchid = 0
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.Branchid = result[1]
    self.RouteFinId = result[2]
    self.RouteBranchid = result[3]
    self.Status = result[4]
    self.USId = result[5]
    self.Tmstamp = result[6]
  def _data(self):
    return [self.FinId, self.Branchid, self.RouteFinId, self.RouteBranchid, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'FinId|Branchid|RouteFinId|RouteBranchid|Status|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FinidCorrespondentRoutingInsert', self._data())
    self._store(result)
  def runInsert(self, FinId, Branchid, RouteFinId, RouteBranchid, Status, USId, Tmstamp):
    self.FinId = FinId
    self.Branchid = Branchid
    self.RouteFinId = RouteFinId
    self.RouteBranchid = RouteBranchid
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('FinidCorrespondentRoutingUpdate', self._data())
    self._store(result)
  def runUpdate(self, FinId, Branchid, RouteFinId, RouteBranchid, Status, USId, Tmstamp):
    self.FinId = FinId
    self.Branchid = Branchid
    self.RouteFinId = RouteFinId
    self.RouteBranchid = RouteBranchid
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('FinidCorrespondentRoutingSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, FinId):
    self.FinId = FinId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBFinidCorrespondentRoutingDeleteOne(object):
  __slots__ = ['_connect', '_query', 'FinId']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
  def _data(self):
    return [self.FinId]
  def _fields(self):
    return 'FinId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('FinidCorrespondentRoutingDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, FinId):
    self.FinId = FinId
    self.execDeleteOne()

class DBFinidCorrespondentRoutingGet(object):
  __slots__ = ['_connect', '_query', 'FinId', 'RouteFinId']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.RouteFinId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.RouteFinId = result[1]
  def _data(self):
    return [self.FinId, self.RouteFinId]
  def _fields(self):
    return 'FinId|RouteFinId'.split('|')
  def execGet(self):
    result = self._connect.action('FinidCorrespondentRoutingGet', self._data())
    self._store(result)
  def readGet(self, FinId):
    self.FinId = FinId
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

