#use INTRINSICS
### generated code from DBPortal ###

AccuityOfficerStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAccuityOfficer(Proforma):
  def __init__(self, connect=None):
    Proforma.__init__(self, ['_connect', '_query', 'Id', 'LocationId', 'Department', 'OfficerName', 'Status', 'USId', 'TmStamp'])
    self._connect = connect
    self.Id = 0
    self.LocationId = 0
    self.Department = ''
    self.OfficerName = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.LocationId = result[1]
    self.Department = result[2]
    self.OfficerName = result[3]
    self.Status = result[4]
    self.USId = result[5]
    self.TmStamp = result[6]
  def _data(self):
    return [self.Id, self.LocationId, self.Department, self.OfficerName, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|LocationId|Department|OfficerName|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AccuityOfficerInsert', self._data())
    self._store(result)
  def runInsert(self, Id, LocationId, Department, OfficerName, Status, USId, TmStamp):
    self.Id = Id
    self.LocationId = LocationId
    self.Department = Department
    self.OfficerName = OfficerName
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AccuityOfficerUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, LocationId, Department, OfficerName, Status, USId, TmStamp):
    self.Id = Id
    self.LocationId = LocationId
    self.Department = Department
    self.OfficerName = OfficerName
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AccuityOfficerSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id):
    self.Id = Id
    try:
      self.execSelectOne()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityOfficerExists(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Count', 'Id'])
    self._connect = connect
    self.Count = 0
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Id = result[1]
  def _data(self):
    return [self.Count, self.Id]
  def _fields(self):
    return 'Count|Id'.split('|')
  def execExists(self):
    result = self._connect.action('AccuityOfficerExists', self._data())
    self._store(result)
  def readExists(self, Id):
    self.Id = Id
    try:
      self.execExists()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

