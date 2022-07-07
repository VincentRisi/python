#use INTRINSICS
### generated code from DBPortal ###

AccuityCorrespondentStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAccuityCorrespondent(Proforma):
  def __init__(self, connect=None):
    Proforma.__init__(self, ['_connect', '_query', 'Id', 'LocationId', 'ClearingSystem', 'CurrencyCode', 'OwnerSwift', 'OwnerSwiftWOPadding', 'OwnerSSIAccountNo', 'ClearingAccuityId', 'ClearingSwift', 'ClearingSwiftWOPadding', 'HolderAccuityId', 'HolderSwift', 'HolderSwiftWOPadding', 'HolderSSIAccountNo', 'PreferredSSIInd', 'FurtherAccuityId', 'FurtherSwift', 'FurtherSwiftWOPadding', 'Further2AccuityId', 'Further2Swift', 'Further2SwiftWOPadding', 'CorrespondentEffectiveDate', 'CorrespondentDeactivationDate', 'CorrespondentUpdateDate', 'SSINotes', 'Status', 'USId', 'TmStamp'])
    self._connect = connect
    self.Id = 0
    self.LocationId = 0
    self.ClearingSystem = ''
    self.CurrencyCode = ''
    self.OwnerSwift = ''
    self.OwnerSwiftWOPadding = ''
    self.OwnerSSIAccountNo = ''
    self.ClearingAccuityId = ''
    self.ClearingSwift = ''
    self.ClearingSwiftWOPadding = ''
    self.HolderAccuityId = ''
    self.HolderSwift = ''
    self.HolderSwiftWOPadding = ''
    self.HolderSSIAccountNo = ''
    self.PreferredSSIInd = ''
    self.FurtherAccuityId = ''
    self.FurtherSwift = ''
    self.FurtherSwiftWOPadding = ''
    self.Further2AccuityId = ''
    self.Further2Swift = ''
    self.Further2SwiftWOPadding = ''
    self.CorrespondentEffectiveDate = ''
    self.CorrespondentDeactivationDate = ''
    self.CorrespondentUpdateDate = ''
    self.SSINotes = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.LocationId = result[1]
    self.ClearingSystem = result[2]
    self.CurrencyCode = result[3]
    self.OwnerSwift = result[4]
    self.OwnerSwiftWOPadding = result[5]
    self.OwnerSSIAccountNo = result[6]
    self.ClearingAccuityId = result[7]
    self.ClearingSwift = result[8]
    self.ClearingSwiftWOPadding = result[9]
    self.HolderAccuityId = result[10]
    self.HolderSwift = result[11]
    self.HolderSwiftWOPadding = result[12]
    self.HolderSSIAccountNo = result[13]
    self.PreferredSSIInd = result[14]
    self.FurtherAccuityId = result[15]
    self.FurtherSwift = result[16]
    self.FurtherSwiftWOPadding = result[17]
    self.Further2AccuityId = result[18]
    self.Further2Swift = result[19]
    self.Further2SwiftWOPadding = result[20]
    self.CorrespondentEffectiveDate = result[21]
    self.CorrespondentDeactivationDate = result[22]
    self.CorrespondentUpdateDate = result[23]
    self.SSINotes = result[24]
    self.Status = result[25]
    self.USId = result[26]
    self.TmStamp = result[27]
  def _data(self):
    return [self.Id, self.LocationId, self.ClearingSystem, self.CurrencyCode, self.OwnerSwift, self.OwnerSwiftWOPadding, self.OwnerSSIAccountNo, self.ClearingAccuityId, self.ClearingSwift, self.ClearingSwiftWOPadding, self.HolderAccuityId, self.HolderSwift, self.HolderSwiftWOPadding, self.HolderSSIAccountNo, self.PreferredSSIInd, self.FurtherAccuityId, self.FurtherSwift, self.FurtherSwiftWOPadding, self.Further2AccuityId, self.Further2Swift, self.Further2SwiftWOPadding, self.CorrespondentEffectiveDate, self.CorrespondentDeactivationDate, self.CorrespondentUpdateDate, self.SSINotes, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|LocationId|ClearingSystem|CurrencyCode|OwnerSwift|OwnerSwiftWOPadding|OwnerSSIAccountNo|ClearingAccuityId|ClearingSwift|ClearingSwiftWOPadding|HolderAccuityId|HolderSwift|HolderSwiftWOPadding|HolderSSIAccountNo|PreferredSSIInd|FurtherAccuityId|FurtherSwift|FurtherSwiftWOPadding|Further2AccuityId|Further2Swift|Further2SwiftWOPadding|CorrespondentEffectiveDate|CorrespondentDeactivationDate|CorrespondentUpdateDate|SSINotes|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AccuityCorrespondentInsert', self._data())
    self._store(result)
  def runInsert(self, Id, LocationId, ClearingSystem, CurrencyCode, OwnerSwift, OwnerSwiftWOPadding, OwnerSSIAccountNo, ClearingAccuityId, ClearingSwift, ClearingSwiftWOPadding, HolderAccuityId, HolderSwift, HolderSwiftWOPadding, HolderSSIAccountNo, PreferredSSIInd, FurtherAccuityId, FurtherSwift, FurtherSwiftWOPadding, Further2AccuityId, Further2Swift, Further2SwiftWOPadding, CorrespondentEffectiveDate, CorrespondentDeactivationDate, CorrespondentUpdateDate, SSINotes, Status, USId, TmStamp):
    self.Id = Id
    self.LocationId = LocationId
    self.ClearingSystem = ClearingSystem
    self.CurrencyCode = CurrencyCode
    self.OwnerSwift = OwnerSwift
    self.OwnerSwiftWOPadding = OwnerSwiftWOPadding
    self.OwnerSSIAccountNo = OwnerSSIAccountNo
    self.ClearingAccuityId = ClearingAccuityId
    self.ClearingSwift = ClearingSwift
    self.ClearingSwiftWOPadding = ClearingSwiftWOPadding
    self.HolderAccuityId = HolderAccuityId
    self.HolderSwift = HolderSwift
    self.HolderSwiftWOPadding = HolderSwiftWOPadding
    self.HolderSSIAccountNo = HolderSSIAccountNo
    self.PreferredSSIInd = PreferredSSIInd
    self.FurtherAccuityId = FurtherAccuityId
    self.FurtherSwift = FurtherSwift
    self.FurtherSwiftWOPadding = FurtherSwiftWOPadding
    self.Further2AccuityId = Further2AccuityId
    self.Further2Swift = Further2Swift
    self.Further2SwiftWOPadding = Further2SwiftWOPadding
    self.CorrespondentEffectiveDate = CorrespondentEffectiveDate
    self.CorrespondentDeactivationDate = CorrespondentDeactivationDate
    self.CorrespondentUpdateDate = CorrespondentUpdateDate
    self.SSINotes = SSINotes
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AccuityCorrespondentUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, LocationId, ClearingSystem, CurrencyCode, OwnerSwift, OwnerSwiftWOPadding, OwnerSSIAccountNo, ClearingAccuityId, ClearingSwift, ClearingSwiftWOPadding, HolderAccuityId, HolderSwift, HolderSwiftWOPadding, HolderSSIAccountNo, PreferredSSIInd, FurtherAccuityId, FurtherSwift, FurtherSwiftWOPadding, Further2AccuityId, Further2Swift, Further2SwiftWOPadding, CorrespondentEffectiveDate, CorrespondentDeactivationDate, CorrespondentUpdateDate, SSINotes, Status, USId, TmStamp):
    self.Id = Id
    self.LocationId = LocationId
    self.ClearingSystem = ClearingSystem
    self.CurrencyCode = CurrencyCode
    self.OwnerSwift = OwnerSwift
    self.OwnerSwiftWOPadding = OwnerSwiftWOPadding
    self.OwnerSSIAccountNo = OwnerSSIAccountNo
    self.ClearingAccuityId = ClearingAccuityId
    self.ClearingSwift = ClearingSwift
    self.ClearingSwiftWOPadding = ClearingSwiftWOPadding
    self.HolderAccuityId = HolderAccuityId
    self.HolderSwift = HolderSwift
    self.HolderSwiftWOPadding = HolderSwiftWOPadding
    self.HolderSSIAccountNo = HolderSSIAccountNo
    self.PreferredSSIInd = PreferredSSIInd
    self.FurtherAccuityId = FurtherAccuityId
    self.FurtherSwift = FurtherSwift
    self.FurtherSwiftWOPadding = FurtherSwiftWOPadding
    self.Further2AccuityId = Further2AccuityId
    self.Further2Swift = Further2Swift
    self.Further2SwiftWOPadding = Further2SwiftWOPadding
    self.CorrespondentEffectiveDate = CorrespondentEffectiveDate
    self.CorrespondentDeactivationDate = CorrespondentDeactivationDate
    self.CorrespondentUpdateDate = CorrespondentUpdateDate
    self.SSINotes = SSINotes
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AccuityCorrespondentSelectOne', self._data())
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

class DBAccuityCorrespondentExists(Proforma):
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
    result = self._connect.action('AccuityCorrespondentExists', self._data())
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

class DBAccuityCorrespondentGet(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBankName', 'CorrTown', 'CorrCountry', 'CorrAccountNo', 'CorrSwiftAddress', 'PreferredInd', 'Status'])
    self._connect = connect
    self.FinId = 0
    self.CorrCurrency = ''
    self.CorrFinId = 0
    self.CorrBankName = ''
    self.CorrTown = ''
    self.CorrCountry = ''
    self.CorrAccountNo = ''
    self.CorrSwiftAddress = ''
    self.PreferredInd = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.CorrCurrency = result[1]
    self.CorrFinId = result[2]
    self.CorrBankName = result[3]
    self.CorrTown = result[4]
    self.CorrCountry = result[5]
    self.CorrAccountNo = result[6]
    self.CorrSwiftAddress = result[7]
    self.PreferredInd = result[8]
    self.Status = result[9]
  def _data(self):
    return [self.FinId, self.CorrCurrency, self.CorrFinId, self.CorrBankName, self.CorrTown, self.CorrCountry, self.CorrAccountNo, self.CorrSwiftAddress, self.PreferredInd, self.Status]
  def _fields(self):
    return 'FinId|CorrCurrency|CorrFinId|CorrBankName|CorrTown|CorrCountry|CorrAccountNo|CorrSwiftAddress|PreferredInd|Status'.split('|')
  def execGet(self):
    result = self._connect.action('AccuityCorrespondentGet', self._data())
    self._store(result)
  def readGet(self, FinId, CorrCurrency):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    try:
      self.execGet()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityCorrespondentGetSwiftList(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrSwiftAddress', 'Status'])
    self._connect = connect
    self.FinId = 0
    self.CorrCurrency = ''
    self.CorrSwiftAddress = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.CorrCurrency = result[1]
    self.CorrSwiftAddress = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.FinId, self.CorrCurrency, self.CorrSwiftAddress, self.Status]
  def _fields(self):
    return 'FinId|CorrCurrency|CorrSwiftAddress|Status'.split('|')
  def queryGetSwiftList(self):
    self._query = self._connect.query('AccuityCorrespondentGetSwiftList', self._data())
  def fetchGetSwiftList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAccuityCorrespondentGetSwiftList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGetSwiftList(self):
    self._connect.cancel(self._query)
  def loadGetSwiftList(self):
    self.queryGetSwiftList()
    result = []
    while 1:
      rc, rec = self.fetchGetSwiftList()
      if rc == 0:
        break
      result.append(rec)
    return result

