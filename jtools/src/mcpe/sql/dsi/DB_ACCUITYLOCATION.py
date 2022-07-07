#use INTRINSICS
### generated code from DBPortal ###

AccuityLocationStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAccuityLocation(Proforma):
  def __init__(self, connect=None):
    Proforma.__init__(self, ['_connect', '_query', 'LocationId', 'CountryCode', 'InstitutionType', 'OfficeType', 'NameAbbrev', 'NameFull', 'BranchName', 'AddressLine1', 'AddressLine2', 'City', 'StateAbbr', 'StateFull', 'PostalCode', 'CountryName', 'EmployerTaxId', 'DateOfFinancial', 'CurrentAssets', 'HeadOfficeId', 'InstitutionId', 'CorrLocationType', 'CorrLocationId', 'Status', 'USId', 'TmStamp'])
    self._connect = connect
    self.LocationId = 0
    self.CountryCode = ''
    self.InstitutionType = ''
    self.OfficeType = ''
    self.NameAbbrev = ''
    self.NameFull = ''
    self.BranchName = ''
    self.AddressLine1 = ''
    self.AddressLine2 = ''
    self.City = ''
    self.StateAbbr = ''
    self.StateFull = ''
    self.PostalCode = ''
    self.CountryName = ''
    self.EmployerTaxId = ''
    self.DateOfFinancial = ''
    self.CurrentAssets = ''
    self.HeadOfficeId = 0
    self.InstitutionId = 0
    self.CorrLocationType = 0
    self.CorrLocationId = 0
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LocationId = result[0]
    self.CountryCode = result[1]
    self.InstitutionType = result[2]
    self.OfficeType = result[3]
    self.NameAbbrev = result[4]
    self.NameFull = result[5]
    self.BranchName = result[6]
    self.AddressLine1 = result[7]
    self.AddressLine2 = result[8]
    self.City = result[9]
    self.StateAbbr = result[10]
    self.StateFull = result[11]
    self.PostalCode = result[12]
    self.CountryName = result[13]
    self.EmployerTaxId = result[14]
    self.DateOfFinancial = result[15]
    self.CurrentAssets = result[16]
    self.HeadOfficeId = result[17]
    self.InstitutionId = result[18]
    self.CorrLocationType = result[19]
    self.CorrLocationId = result[20]
    self.Status = result[21]
    self.USId = result[22]
    self.TmStamp = result[23]
  def _data(self):
    return [self.LocationId, self.CountryCode, self.InstitutionType, self.OfficeType, self.NameAbbrev, self.NameFull, self.BranchName, self.AddressLine1, self.AddressLine2, self.City, self.StateAbbr, self.StateFull, self.PostalCode, self.CountryName, self.EmployerTaxId, self.DateOfFinancial, self.CurrentAssets, self.HeadOfficeId, self.InstitutionId, self.CorrLocationType, self.CorrLocationId, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'LocationId|CountryCode|InstitutionType|OfficeType|NameAbbrev|NameFull|BranchName|AddressLine1|AddressLine2|City|StateAbbr|StateFull|PostalCode|CountryName|EmployerTaxId|DateOfFinancial|CurrentAssets|HeadOfficeId|InstitutionId|CorrLocationType|CorrLocationId|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AccuityLocationInsert', self._data())
    self._store(result)
  def runInsert(self, LocationId, CountryCode, InstitutionType, OfficeType, NameAbbrev, NameFull, BranchName, AddressLine1, AddressLine2, City, StateAbbr, StateFull, PostalCode, CountryName, EmployerTaxId, DateOfFinancial, CurrentAssets, HeadOfficeId, InstitutionId, CorrLocationType, CorrLocationId, Status, USId, TmStamp):
    self.LocationId = LocationId
    self.CountryCode = CountryCode
    self.InstitutionType = InstitutionType
    self.OfficeType = OfficeType
    self.NameAbbrev = NameAbbrev
    self.NameFull = NameFull
    self.BranchName = BranchName
    self.AddressLine1 = AddressLine1
    self.AddressLine2 = AddressLine2
    self.City = City
    self.StateAbbr = StateAbbr
    self.StateFull = StateFull
    self.PostalCode = PostalCode
    self.CountryName = CountryName
    self.EmployerTaxId = EmployerTaxId
    self.DateOfFinancial = DateOfFinancial
    self.CurrentAssets = CurrentAssets
    self.HeadOfficeId = HeadOfficeId
    self.InstitutionId = InstitutionId
    self.CorrLocationType = CorrLocationType
    self.CorrLocationId = CorrLocationId
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AccuityLocationUpdate', self._data())
    self._store(result)
  def runUpdate(self, LocationId, CountryCode, InstitutionType, OfficeType, NameAbbrev, NameFull, BranchName, AddressLine1, AddressLine2, City, StateAbbr, StateFull, PostalCode, CountryName, EmployerTaxId, DateOfFinancial, CurrentAssets, HeadOfficeId, InstitutionId, CorrLocationType, CorrLocationId, Status, USId, TmStamp):
    self.LocationId = LocationId
    self.CountryCode = CountryCode
    self.InstitutionType = InstitutionType
    self.OfficeType = OfficeType
    self.NameAbbrev = NameAbbrev
    self.NameFull = NameFull
    self.BranchName = BranchName
    self.AddressLine1 = AddressLine1
    self.AddressLine2 = AddressLine2
    self.City = City
    self.StateAbbr = StateAbbr
    self.StateFull = StateFull
    self.PostalCode = PostalCode
    self.CountryName = CountryName
    self.EmployerTaxId = EmployerTaxId
    self.DateOfFinancial = DateOfFinancial
    self.CurrentAssets = CurrentAssets
    self.HeadOfficeId = HeadOfficeId
    self.InstitutionId = InstitutionId
    self.CorrLocationType = CorrLocationType
    self.CorrLocationId = CorrLocationId
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AccuityLocationSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, LocationId):
    self.LocationId = LocationId
    try:
      self.execSelectOne()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityLocationExists(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Count', 'LocationId'])
    self._connect = connect
    self.Count = 0
    self.LocationId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.LocationId = result[1]
  def _data(self):
    return [self.Count, self.LocationId]
  def _fields(self):
    return 'Count|LocationId'.split('|')
  def execExists(self):
    result = self._connect.action('AccuityLocationExists', self._data())
    self._store(result)
  def readExists(self, LocationId):
    self.LocationId = LocationId
    try:
      self.execExists()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityLocationGet(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'FinId', 'BankName', 'Town', 'Country', 'SwiftAddress', 'NationalBankCode', 'Status'])
    self._connect = connect
    self.FinId = 0
    self.BankName = ''
    self.Town = ''
    self.Country = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.BankName = result[1]
    self.Town = result[2]
    self.Country = result[3]
    self.SwiftAddress = result[4]
    self.NationalBankCode = result[5]
    self.Status = result[6]
  def _data(self):
    return [self.FinId, self.BankName, self.Town, self.Country, self.SwiftAddress, self.NationalBankCode, self.Status]
  def _fields(self):
    return 'FinId|BankName|Town|Country|SwiftAddress|NationalBankCode|Status'.split('|')
  def execGet(self):
    result = self._connect.action('AccuityLocationGet', self._data())
    self._store(result)
  def readGet(self, FinId):
    self.FinId = FinId
    try:
      self.execGet()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityLocationGetBankCode(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'FinId', 'NationalBankCode'])
    self._connect = connect
    self.FinId = 0
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.NationalBankCode = result[1]
  def _data(self):
    return [self.FinId, self.NationalBankCode]
  def _fields(self):
    return 'FinId|NationalBankCode'.split('|')
  def execGetBankCode(self):
    result = self._connect.action('AccuityLocationGetBankCode', self._data())
    self._store(result)
  def readGetBankCode(self, FinId):
    self.FinId = FinId
    try:
      self.execGetBankCode()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityLocationFinIdBankCodeCheck(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'FinId', 'NationalBankCode', 'MatchCount'])
    self._connect = connect
    self.FinId = 0
    self.NationalBankCode = ''
    self.MatchCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.NationalBankCode = result[1]
    self.MatchCount = result[2]
  def _data(self):
    return [self.FinId, self.NationalBankCode, self.MatchCount]
  def _fields(self):
    return 'FinId|NationalBankCode|MatchCount'.split('|')
  def execFinIdBankCodeCheck(self):
    result = self._connect.action('AccuityLocationFinIdBankCodeCheck', self._data())
    self._store(result)
  def readFinIdBankCodeCheck(self, FinId, NationalBankCode):
    self.FinId = FinId
    self.NationalBankCode = NationalBankCode
    try:
      self.execFinIdBankCodeCheck()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAccuityLocationSwiftLookup(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'SwiftAddress', 'Currency', 'SwiftAddressOut'])
    self._connect = connect
    self.SwiftAddress = ''
    self.Currency = ''
    self.SwiftAddressOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.Currency = result[1]
    self.SwiftAddressOut = result[2]
  def _data(self):
    return [self.SwiftAddress, self.Currency, self.SwiftAddressOut]
  def _fields(self):
    return 'SwiftAddress|Currency|SwiftAddressOut'.split('|')
  def querySwiftLookup(self):
    self._query = self._connect.query('AccuityLocationSwiftLookup', self._data())
  def fetchSwiftLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAccuityLocationSwiftLookup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSwiftLookup(self):
    self._connect.cancel(self._query)
  def loadSwiftLookup(self):
    self.querySwiftLookup()
    result = []
    while 1:
      rc, rec = self.fetchSwiftLookup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBAccuityLocationSwiftCountryLookup(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'SwiftAddress', 'Country', 'SwiftAddressOut'])
    self._connect = connect
    self.SwiftAddress = ''
    self.Country = ''
    self.SwiftAddressOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.Country = result[1]
    self.SwiftAddressOut = result[2]
  def _data(self):
    return [self.SwiftAddress, self.Country, self.SwiftAddressOut]
  def _fields(self):
    return 'SwiftAddress|Country|SwiftAddressOut'.split('|')
  def querySwiftCountryLookup(self):
    self._query = self._connect.query('AccuityLocationSwiftCountryLookup', self._data())
  def fetchSwiftCountryLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAccuityLocationSwiftCountryLookup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSwiftCountryLookup(self):
    self._connect.cancel(self._query)
  def loadSwiftCountryLookup(self):
    self.querySwiftCountryLookup()
    result = []
    while 1:
      rc, rec = self.fetchSwiftCountryLookup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBAccuityLocationFinIdLookup(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'SwiftAddress', 'FinId', 'BranchId'])
    self._connect = connect
    self.SwiftAddress = ''
    self.FinId = 0
    self.BranchId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.FinId = result[1]
    self.BranchId = result[2]
  def _data(self):
    return [self.SwiftAddress, self.FinId, self.BranchId]
  def _fields(self):
    return 'SwiftAddress|FinId|BranchId'.split('|')
  def queryFinIdLookup(self):
    self._query = self._connect.query('AccuityLocationFinIdLookup', self._data())
  def fetchFinIdLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAccuityLocationFinIdLookup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFinIdLookup(self):
    self._connect.cancel(self._query)
  def loadFinIdLookup(self):
    self.queryFinIdLookup()
    result = []
    while 1:
      rc, rec = self.fetchFinIdLookup()
      if rc == 0:
        break
      result.append(rec)
    return result

