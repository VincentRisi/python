from INTRINSICS import *
### generated code from DBPortal ###

AlmanacBankStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAlmanacBank(object):
  __slots__ = ['_connect', '_query', 'FinId', 'BranchId', 'BankName', 'Town', 'AddressLine1', 'AddressLine2', 'AddressLine3', 'AddressLine4', 'AddressLine5', 'Country', 'Telephone', 'Fax', 'Telex', 'SwiftAddress', 'NationalBankCode', 'RBIInsertDate', 'RBIChangeDate', 'Status', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.BranchId = 0
    self.BankName = ''
    self.Town = ''
    self.AddressLine1 = ''
    self.AddressLine2 = ''
    self.AddressLine3 = ''
    self.AddressLine4 = ''
    self.AddressLine5 = ''
    self.Country = ''
    self.Telephone = ''
    self.Fax = ''
    self.Telex = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
    self.RBIInsertDate = ''
    self.RBIChangeDate = ''
    self.Status = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.BranchId = result[1]
    self.BankName = result[2]
    self.Town = result[3]
    self.AddressLine1 = result[4]
    self.AddressLine2 = result[5]
    self.AddressLine3 = result[6]
    self.AddressLine4 = result[7]
    self.AddressLine5 = result[8]
    self.Country = result[9]
    self.Telephone = result[10]
    self.Fax = result[11]
    self.Telex = result[12]
    self.SwiftAddress = result[13]
    self.NationalBankCode = result[14]
    self.RBIInsertDate = result[15]
    self.RBIChangeDate = result[16]
    self.Status = result[17]
    self.USId = result[18]
    self.TmStamp = result[19]
  def _data(self):
    return [self.FinId, self.BranchId, self.BankName, self.Town, self.AddressLine1, self.AddressLine2, self.AddressLine3, self.AddressLine4, self.AddressLine5, self.Country, self.Telephone, self.Fax, self.Telex, self.SwiftAddress, self.NationalBankCode, self.RBIInsertDate, self.RBIChangeDate, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'FinId|BranchId|BankName|Town|AddressLine1|AddressLine2|AddressLine3|AddressLine4|AddressLine5|Country|Telephone|Fax|Telex|SwiftAddress|NationalBankCode|RBIInsertDate|RBIChangeDate|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AlmanacBankInsert', self._data())
    self._store(result)
  def runInsert(self, FinId, BranchId, BankName, Town, AddressLine1, AddressLine2, AddressLine3, AddressLine4, AddressLine5, Country, Telephone, Fax, Telex, SwiftAddress, NationalBankCode, RBIInsertDate, RBIChangeDate, Status, USId, TmStamp):
    self.FinId = FinId
    self.BranchId = BranchId
    self.BankName = BankName
    self.Town = Town
    self.AddressLine1 = AddressLine1
    self.AddressLine2 = AddressLine2
    self.AddressLine3 = AddressLine3
    self.AddressLine4 = AddressLine4
    self.AddressLine5 = AddressLine5
    self.Country = Country
    self.Telephone = Telephone
    self.Fax = Fax
    self.Telex = Telex
    self.SwiftAddress = SwiftAddress
    self.NationalBankCode = NationalBankCode
    self.RBIInsertDate = RBIInsertDate
    self.RBIChangeDate = RBIChangeDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AlmanacBankUpdate', self._data())
    self._store(result)
  def runUpdate(self, FinId, BranchId, BankName, Town, AddressLine1, AddressLine2, AddressLine3, AddressLine4, AddressLine5, Country, Telephone, Fax, Telex, SwiftAddress, NationalBankCode, RBIInsertDate, RBIChangeDate, Status, USId, TmStamp):
    self.FinId = FinId
    self.BranchId = BranchId
    self.BankName = BankName
    self.Town = Town
    self.AddressLine1 = AddressLine1
    self.AddressLine2 = AddressLine2
    self.AddressLine3 = AddressLine3
    self.AddressLine4 = AddressLine4
    self.AddressLine5 = AddressLine5
    self.Country = Country
    self.Telephone = Telephone
    self.Fax = Fax
    self.Telex = Telex
    self.SwiftAddress = SwiftAddress
    self.NationalBankCode = NationalBankCode
    self.RBIInsertDate = RBIInsertDate
    self.RBIChangeDate = RBIChangeDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AlmanacBankSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, FinId, BranchId):
    self.FinId = FinId
    self.BranchId = BranchId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacBankDeleteOne(object):
  __slots__ = ['_connect', '_query', 'FinId', 'BranchId']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.BranchId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.BranchId = result[1]
  def _data(self):
    return [self.FinId, self.BranchId]
  def _fields(self):
    return 'FinId|BranchId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('AlmanacBankDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, FinId, BranchId):
    self.FinId = FinId
    self.BranchId = BranchId
    self.execDeleteOne()

class DBAlmanacBankExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'FinId', 'BranchId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.FinId = 0
    self.BranchId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.FinId = result[1]
    self.BranchId = result[2]
  def _data(self):
    return [self.Count, self.FinId, self.BranchId]
  def _fields(self):
    return 'Count|FinId|BranchId'.split('|')
  def execExists(self):
    result = self._connect.action('AlmanacBankExists', self._data())
    self._store(result)
  def readExists(self, FinId, BranchId):
    self.FinId = FinId
    self.BranchId = BranchId
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacBankUpdateAllStatus(object):
  __slots__ = ['_connect', '_query', 'Status', 'USId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Status = 0
    self.USId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Status = result[0]
    self.USId = result[1]
  def _data(self):
    return [self.Status, self.USId]
  def _fields(self):
    return 'Status|USId'.split('|')
  def execUpdateAllStatus(self):
    result = self._connect.action('AlmanacBankUpdateAllStatus', self._data())
    self._store(result)
  def runUpdateAllStatus(self, Status, USId):
    self.Status = Status
    self.USId = USId
    self.execUpdateAllStatus()

class DBAlmanacBankGet(object):
  __slots__ = ['_connect', '_query', 'FinId', 'BranchId', 'BankName', 'Town', 'Country', 'SwiftAddress', 'NationalBankCode', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.BranchId = 0
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
    self.BranchId = result[1]
    self.BankName = result[2]
    self.Town = result[3]
    self.Country = result[4]
    self.SwiftAddress = result[5]
    self.NationalBankCode = result[6]
    self.Status = result[7]
  def _data(self):
    return [self.FinId, self.BranchId, self.BankName, self.Town, self.Country, self.SwiftAddress, self.NationalBankCode, self.Status]
  def _fields(self):
    return 'FinId|BranchId|BankName|Town|Country|SwiftAddress|NationalBankCode|Status'.split('|')
  def execGet(self):
    result = self._connect.action('AlmanacBankGet', self._data())
    self._store(result)
  def readGet(self, FinId, BranchId):
    self.FinId = FinId
    self.BranchId = BranchId
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacBankGetBankCode(object):
  __slots__ = ['_connect', '_query', 'FinId', 'BranchId', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.BranchId = 0
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.BranchId = result[1]
    self.NationalBankCode = result[2]
  def _data(self):
    return [self.FinId, self.BranchId, self.NationalBankCode]
  def _fields(self):
    return 'FinId|BranchId|NationalBankCode'.split('|')
  def execGetBankCode(self):
    result = self._connect.action('AlmanacBankGetBankCode', self._data())
    self._store(result)
  def readGetBankCode(self, FinId, BranchId):
    self.FinId = FinId
    self.BranchId = BranchId
    try:
      self.execGetBankCode()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacBankFinIdBankCodeCheck(object):
  __slots__ = ['_connect', '_query', 'FinId', 'NationalBankCode', 'MatchCount']
  def __init__(self, connect=None):
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
    result = self._connect.action('AlmanacBankFinIdBankCodeCheck', self._data())
    self._store(result)
  def readFinIdBankCodeCheck(self, FinId, NationalBankCode):
    self.FinId = FinId
    self.NationalBankCode = NationalBankCode
    try:
      self.execFinIdBankCodeCheck()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacBankSwiftLookup(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'Currency', 'SwiftAddressOut']
  def __init__(self, connect=None):
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
    self._query = self._connect.query('AlmanacBankSwiftLookup', self._data())
  def fetchSwiftLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAlmanacBankSwiftLookup(self._connect)
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

class DBAlmanacBankSwiftCountryLookup(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'Country', 'SwiftAddressOut']
  def __init__(self, connect=None):
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
    self._query = self._connect.query('AlmanacBankSwiftCountryLookup', self._data())
  def fetchSwiftCountryLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAlmanacBankSwiftCountryLookup(self._connect)
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

class DBAlmanacBankFinIdLookup(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'FinId', 'BranchId']
  def __init__(self, connect=None):
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
    self._query = self._connect.query('AlmanacBankFinIdLookup', self._data())
  def fetchFinIdLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAlmanacBankFinIdLookup(self._connect)
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

