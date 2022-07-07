#use INTRINSICS
### generated code from DBPortal ###

AccuityRoutingAttStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAccuityRoutingAtt(Proforma):
  def __init__(self, connect=None):
    Proforma.__init__(self, ['_connect', '_query', 'Id', 'RoutingType', 'RoutingCode', 'RoutingCodeAlt', 'OverrideRoutingCode', 'OverrideRoutingCodeAlt', 'ClearingSystem', 'MembershipType', 'RoutingTypeInfo', 'RoutingCodeStatus', 'ACHFlag', 'FedwireFundStatus', 'FedwireSecurityStatus', 'WireTranCode', 'EffectiveDate', 'DeactivatedDate', 'Status', 'USId', 'TmStamp'])
    self._connect = connect
    self.Id = 0
    self.RoutingType = ''
    self.RoutingCode = ''
    self.RoutingCodeAlt = ''
    self.OverrideRoutingCode = ''
    self.OverrideRoutingCodeAlt = ''
    self.ClearingSystem = ''
    self.MembershipType = ''
    self.RoutingTypeInfo = ''
    self.RoutingCodeStatus = ''
    self.ACHFlag = ''
    self.FedwireFundStatus = ''
    self.FedwireSecurityStatus = ''
    self.WireTranCode = ''
    self.EffectiveDate = ''
    self.DeactivatedDate = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.RoutingType = result[1]
    self.RoutingCode = result[2]
    self.RoutingCodeAlt = result[3]
    self.OverrideRoutingCode = result[4]
    self.OverrideRoutingCodeAlt = result[5]
    self.ClearingSystem = result[6]
    self.MembershipType = result[7]
    self.RoutingTypeInfo = result[8]
    self.RoutingCodeStatus = result[9]
    self.ACHFlag = result[10]
    self.FedwireFundStatus = result[11]
    self.FedwireSecurityStatus = result[12]
    self.WireTranCode = result[13]
    self.EffectiveDate = result[14]
    self.DeactivatedDate = result[15]
    self.Status = result[16]
    self.USId = result[17]
    self.TmStamp = result[18]
  def _data(self):
    return [self.Id, self.RoutingType, self.RoutingCode, self.RoutingCodeAlt, self.OverrideRoutingCode, self.OverrideRoutingCodeAlt, self.ClearingSystem, self.MembershipType, self.RoutingTypeInfo, self.RoutingCodeStatus, self.ACHFlag, self.FedwireFundStatus, self.FedwireSecurityStatus, self.WireTranCode, self.EffectiveDate, self.DeactivatedDate, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|RoutingType|RoutingCode|RoutingCodeAlt|OverrideRoutingCode|OverrideRoutingCodeAlt|ClearingSystem|MembershipType|RoutingTypeInfo|RoutingCodeStatus|ACHFlag|FedwireFundStatus|FedwireSecurityStatus|WireTranCode|EffectiveDate|DeactivatedDate|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AccuityRoutingAttInsert', self._data())
    self._store(result)
  def runInsert(self, Id, RoutingType, RoutingCode, RoutingCodeAlt, OverrideRoutingCode, OverrideRoutingCodeAlt, ClearingSystem, MembershipType, RoutingTypeInfo, RoutingCodeStatus, ACHFlag, FedwireFundStatus, FedwireSecurityStatus, WireTranCode, EffectiveDate, DeactivatedDate, Status, USId, TmStamp):
    self.Id = Id
    self.RoutingType = RoutingType
    self.RoutingCode = RoutingCode
    self.RoutingCodeAlt = RoutingCodeAlt
    self.OverrideRoutingCode = OverrideRoutingCode
    self.OverrideRoutingCodeAlt = OverrideRoutingCodeAlt
    self.ClearingSystem = ClearingSystem
    self.MembershipType = MembershipType
    self.RoutingTypeInfo = RoutingTypeInfo
    self.RoutingCodeStatus = RoutingCodeStatus
    self.ACHFlag = ACHFlag
    self.FedwireFundStatus = FedwireFundStatus
    self.FedwireSecurityStatus = FedwireSecurityStatus
    self.WireTranCode = WireTranCode
    self.EffectiveDate = EffectiveDate
    self.DeactivatedDate = DeactivatedDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AccuityRoutingAttUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, RoutingType, RoutingCode, RoutingCodeAlt, OverrideRoutingCode, OverrideRoutingCodeAlt, ClearingSystem, MembershipType, RoutingTypeInfo, RoutingCodeStatus, ACHFlag, FedwireFundStatus, FedwireSecurityStatus, WireTranCode, EffectiveDate, DeactivatedDate, Status, USId, TmStamp):
    self.Id = Id
    self.RoutingType = RoutingType
    self.RoutingCode = RoutingCode
    self.RoutingCodeAlt = RoutingCodeAlt
    self.OverrideRoutingCode = OverrideRoutingCode
    self.OverrideRoutingCodeAlt = OverrideRoutingCodeAlt
    self.ClearingSystem = ClearingSystem
    self.MembershipType = MembershipType
    self.RoutingTypeInfo = RoutingTypeInfo
    self.RoutingCodeStatus = RoutingCodeStatus
    self.ACHFlag = ACHFlag
    self.FedwireFundStatus = FedwireFundStatus
    self.FedwireSecurityStatus = FedwireSecurityStatus
    self.WireTranCode = WireTranCode
    self.EffectiveDate = EffectiveDate
    self.DeactivatedDate = DeactivatedDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AccuityRoutingAttSelectOne', self._data())
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

class DBAccuityRoutingAttExists(Proforma):
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
    result = self._connect.action('AccuityRoutingAttExists', self._data())
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

