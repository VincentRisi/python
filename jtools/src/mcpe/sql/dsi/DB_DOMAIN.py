from INTRINSICS import *
### generated code from DBPortal ###

class DBDomainAccountType(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.Id, self.Descr, self.Status]
  def _fields(self):
    return 'Id|Descr|Status'.split('|')
  def queryAccountType(self):
    self._query = self._connect.query('DomainAccountType', self._data())
  def fetchAccountType(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainAccountType(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAccountType(self):
    self._connect.cancel(self._query)
  def loadAccountType(self):
    self.queryAccountType()
    result = []
    while 1:
      rc, rec = self.fetchAccountType()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainBankFile(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'BankName', 'BankTown', 'BankType', 'BranchName', 'PhysicalAddr1', 'PhysicalAddr2', 'PhysicalAddr3', 'PhysicalAddr4', 'PhysicalAddr5', 'PhysicalCountry', 'PostalAddr1', 'PostalAddr2', 'PostalAddr3', 'PostalAddr4', 'PostalCountry', 'Telephone', 'EMail', 'Info', 'AuthKeysExchd', 'TgTestKeysExchd', 'DeleteInd', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.BankName = ''
    self.BankTown = ''
    self.BankType = ''
    self.BranchName = ''
    self.PhysicalAddr1 = ''
    self.PhysicalAddr2 = ''
    self.PhysicalAddr3 = ''
    self.PhysicalAddr4 = ''
    self.PhysicalAddr5 = ''
    self.PhysicalCountry = ''
    self.PostalAddr1 = ''
    self.PostalAddr2 = ''
    self.PostalAddr3 = ''
    self.PostalAddr4 = ''
    self.PostalCountry = ''
    self.Telephone = ''
    self.EMail = ''
    self.Info = ''
    self.AuthKeysExchd = ''
    self.TgTestKeysExchd = ''
    self.DeleteInd = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.BankName = result[1]
    self.BankTown = result[2]
    self.BankType = result[3]
    self.BranchName = result[4]
    self.PhysicalAddr1 = result[5]
    self.PhysicalAddr2 = result[6]
    self.PhysicalAddr3 = result[7]
    self.PhysicalAddr4 = result[8]
    self.PhysicalAddr5 = result[9]
    self.PhysicalCountry = result[10]
    self.PostalAddr1 = result[11]
    self.PostalAddr2 = result[12]
    self.PostalAddr3 = result[13]
    self.PostalAddr4 = result[14]
    self.PostalCountry = result[15]
    self.Telephone = result[16]
    self.EMail = result[17]
    self.Info = result[18]
    self.AuthKeysExchd = result[19]
    self.TgTestKeysExchd = result[20]
    self.DeleteInd = result[21]
    self.Status = result[22]
  def _data(self):
    return [self.SwiftAddress, self.BankName, self.BankTown, self.BankType, self.BranchName, self.PhysicalAddr1, self.PhysicalAddr2, self.PhysicalAddr3, self.PhysicalAddr4, self.PhysicalAddr5, self.PhysicalCountry, self.PostalAddr1, self.PostalAddr2, self.PostalAddr3, self.PostalAddr4, self.PostalCountry, self.Telephone, self.EMail, self.Info, self.AuthKeysExchd, self.TgTestKeysExchd, self.DeleteInd, self.Status]
  def _fields(self):
    return 'SwiftAddress|BankName|BankTown|BankType|BranchName|PhysicalAddr1|PhysicalAddr2|PhysicalAddr3|PhysicalAddr4|PhysicalAddr5|PhysicalCountry|PostalAddr1|PostalAddr2|PostalAddr3|PostalAddr4|PostalCountry|Telephone|EMail|Info|AuthKeysExchd|TgTestKeysExchd|DeleteInd|Status'.split('|')
  def queryBankFile(self):
    self._query = self._connect.query('DomainBankFile', self._data())
  def fetchBankFile(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainBankFile(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBankFile(self):
    self._connect.cancel(self._query)
  def loadBankFile(self):
    self.queryBankFile()
    result = []
    while 1:
      rc, rec = self.fetchBankFile()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainAlmanacBank(object):
  __slots__ = ['_connect', '_query', 'FinId', 'BranchId', 'BankName', 'Town', 'AddressLine1', 'AddressLine2', 'AddressLine3', 'AddressLine4', 'AddressLine5', 'Country', 'Telephone', 'Fax', 'Telex', 'SwiftAddress', 'NationalBankCode', 'RBIInsertDate', 'RBIChangeDate', 'Status']
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
  def _data(self):
    return [self.FinId, self.BranchId, self.BankName, self.Town, self.AddressLine1, self.AddressLine2, self.AddressLine3, self.AddressLine4, self.AddressLine5, self.Country, self.Telephone, self.Fax, self.Telex, self.SwiftAddress, self.NationalBankCode, self.RBIInsertDate, self.RBIChangeDate, self.Status]
  def _fields(self):
    return 'FinId|BranchId|BankName|Town|AddressLine1|AddressLine2|AddressLine3|AddressLine4|AddressLine5|Country|Telephone|Fax|Telex|SwiftAddress|NationalBankCode|RBIInsertDate|RBIChangeDate|Status'.split('|')
  def queryAlmanacBank(self):
    self._query = self._connect.query('DomainAlmanacBank', self._data())
  def fetchAlmanacBank(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainAlmanacBank(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAlmanacBank(self):
    self._connect.cancel(self._query)
  def loadAlmanacBank(self):
    self.queryAlmanacBank()
    result = []
    while 1:
      rc, rec = self.fetchAlmanacBank()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainAlmanacCorrespondent(object):
  __slots__ = ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBranchId', 'CorrBankName', 'CorrTown', 'CorrCountry', 'CorrAccountNo', 'CorrSwiftAddress', 'PreferredInd', 'RBIInsertDate', 'RBIChangeDate', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.CorrCurrency = ''
    self.CorrFinId = 0
    self.CorrBranchId = 0
    self.CorrBankName = ''
    self.CorrTown = ''
    self.CorrCountry = ''
    self.CorrAccountNo = ''
    self.CorrSwiftAddress = ''
    self.PreferredInd = ''
    self.RBIInsertDate = ''
    self.RBIChangeDate = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.CorrCurrency = result[1]
    self.CorrFinId = result[2]
    self.CorrBranchId = result[3]
    self.CorrBankName = result[4]
    self.CorrTown = result[5]
    self.CorrCountry = result[6]
    self.CorrAccountNo = result[7]
    self.CorrSwiftAddress = result[8]
    self.PreferredInd = result[9]
    self.RBIInsertDate = result[10]
    self.RBIChangeDate = result[11]
    self.Status = result[12]
  def _data(self):
    return [self.FinId, self.CorrCurrency, self.CorrFinId, self.CorrBranchId, self.CorrBankName, self.CorrTown, self.CorrCountry, self.CorrAccountNo, self.CorrSwiftAddress, self.PreferredInd, self.RBIInsertDate, self.RBIChangeDate, self.Status]
  def _fields(self):
    return 'FinId|CorrCurrency|CorrFinId|CorrBranchId|CorrBankName|CorrTown|CorrCountry|CorrAccountNo|CorrSwiftAddress|PreferredInd|RBIInsertDate|RBIChangeDate|Status'.split('|')
  def queryAlmanacCorrespondent(self):
    self._query = self._connect.query('DomainAlmanacCorrespondent', self._data())
  def fetchAlmanacCorrespondent(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainAlmanacCorrespondent(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAlmanacCorrespondent(self):
    self._connect.cancel(self._query)
  def loadAlmanacCorrespondent(self):
    self.queryAlmanacCorrespondent()
    result = []
    while 1:
      rc, rec = self.fetchAlmanacCorrespondent()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainCurrency(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Comments', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Comments = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Comments = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.Id, self.Descr, self.Comments, self.Status]
  def _fields(self):
    return 'Id|Descr|Comments|Status'.split('|')
  def queryCurrency(self):
    self._query = self._connect.query('DomainCurrency', self._data())
  def fetchCurrency(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainCurrency(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelCurrency(self):
    self._connect.cancel(self._query)
  def loadCurrency(self):
    self.queryCurrency()
    result = []
    while 1:
      rc, rec = self.fetchCurrency()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainBankAccount(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'AccountTypeId', 'AccountNo']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.AccountTypeId = ''
    self.AccountNo = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.AccountTypeId = result[2]
    self.AccountNo = result[3]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.AccountTypeId, self.AccountNo]
  def _fields(self):
    return 'SwiftAddress|CurrId|AccountTypeId|AccountNo'.split('|')
  def queryBankAccount(self):
    self._query = self._connect.query('DomainBankAccount', self._data())
  def fetchBankAccount(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainBankAccount(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBankAccount(self):
    self._connect.cancel(self._query)
  def loadBankAccount(self):
    self.queryBankAccount()
    result = []
    while 1:
      rc, rec = self.fetchBankAccount()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainBankCorrespondents(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'Correspondent', 'CreateDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.Correspondent = ''
    self.CreateDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.Correspondent = result[2]
    self.CreateDate = result[3]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.Correspondent, self.CreateDate]
  def _fields(self):
    return 'SwiftAddress|CurrId|Correspondent|CreateDate'.split('|')
  def queryBankCorrespondents(self):
    self._query = self._connect.query('DomainBankCorrespondents', self._data())
  def fetchBankCorrespondents(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainBankCorrespondents(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBankCorrespondents(self):
    self._connect.cancel(self._query)
  def loadBankCorrespondents(self):
    self.queryBankCorrespondents()
    result = []
    while 1:
      rc, rec = self.fetchBankCorrespondents()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainCountry(object):
  __slots__ = ['_connect', '_query', 'Id', 'CodeId', 'CurrId', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.CodeId = ''
    self.CurrId = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.CodeId = result[1]
    self.CurrId = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.Id, self.CodeId, self.CurrId, self.Status]
  def _fields(self):
    return 'Id|CodeId|CurrId|Status'.split('|')
  def queryCountry(self):
    self._query = self._connect.query('DomainCountry', self._data())
  def fetchCountry(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainCountry(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelCountry(self):
    self._connect.cancel(self._query)
  def loadCountry(self):
    self.queryCountry()
    result = []
    while 1:
      rc, rec = self.fetchCountry()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainDates(object):
  __slots__ = ['_connect', '_query', 'DateType', 'Description', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateType = 0
    self.Description = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateType = result[0]
    self.Description = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.DateType, self.Description, self.Value]
  def _fields(self):
    return 'DateType|Description|Value'.split('|')
  def queryDates(self):
    self._query = self._connect.query('DomainDates', self._data())
  def fetchDates(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainDates(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelDates(self):
    self._connect.cancel(self._query)
  def loadDates(self):
    self.queryDates()
    result = []
    while 1:
      rc, rec = self.fetchDates()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainDrivers(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.Id, self.Descr, self.Status]
  def _fields(self):
    return 'Id|Descr|Status'.split('|')
  def queryDrivers(self):
    self._query = self._connect.query('DomainDrivers', self._data())
  def fetchDrivers(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainDrivers(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelDrivers(self):
    self._connect.cancel(self._query)
  def loadDrivers(self):
    self.queryDrivers()
    result = []
    while 1:
      rc, rec = self.fetchDrivers()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainFieldSearchDef(object):
  __slots__ = ['_connect', '_query', 'Id', 'Tag']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Tag = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Tag = result[1]
  def _data(self):
    return [self.Id, self.Tag]
  def _fields(self):
    return 'Id|Tag'.split('|')
  def queryFieldSearchDef(self):
    self._query = self._connect.query('DomainFieldSearchDef', self._data())
  def fetchFieldSearchDef(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainFieldSearchDef(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFieldSearchDef(self):
    self._connect.cancel(self._query)
  def loadFieldSearchDef(self):
    self.queryFieldSearchDef()
    result = []
    while 1:
      rc, rec = self.fetchFieldSearchDef()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainFigCorrespondentBank(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrId', 'RankType', 'Rank', 'SwiftAddress', 'Frequency', 'Counter', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrId = ''
    self.RankType = ''
    self.Rank = 0
    self.SwiftAddress = ''
    self.Frequency = 0
    self.Counter = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrId = result[1]
    self.RankType = result[2]
    self.Rank = result[3]
    self.SwiftAddress = result[4]
    self.Frequency = result[5]
    self.Counter = result[6]
    self.Status = result[7]
  def _data(self):
    return [self.Country, self.CurrId, self.RankType, self.Rank, self.SwiftAddress, self.Frequency, self.Counter, self.Status]
  def _fields(self):
    return 'Country|CurrId|RankType|Rank|SwiftAddress|Frequency|Counter|Status'.split('|')
  def queryFigCorrespondentBank(self):
    self._query = self._connect.query('DomainFigCorrespondentBank', self._data())
  def fetchFigCorrespondentBank(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainFigCorrespondentBank(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFigCorrespondentBank(self):
    self._connect.cancel(self._query)
  def loadFigCorrespondentBank(self):
    self.queryFigCorrespondentBank()
    result = []
    while 1:
      rc, rec = self.fetchFigCorrespondentBank()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainFinidCorrespondentRouting(object):
  __slots__ = ['_connect', '_query', 'FinId', 'Branchid', 'RouteFinId', 'RouteBranchid', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.Branchid = 0
    self.RouteFinId = 0
    self.RouteBranchid = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.Branchid = result[1]
    self.RouteFinId = result[2]
    self.RouteBranchid = result[3]
    self.Status = result[4]
  def _data(self):
    return [self.FinId, self.Branchid, self.RouteFinId, self.RouteBranchid, self.Status]
  def _fields(self):
    return 'FinId|Branchid|RouteFinId|RouteBranchid|Status'.split('|')
  def queryFinidCorrespondentRouting(self):
    self._query = self._connect.query('DomainFinidCorrespondentRouting', self._data())
  def fetchFinidCorrespondentRouting(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainFinidCorrespondentRouting(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFinidCorrespondentRouting(self):
    self._connect.cancel(self._query)
  def loadFinidCorrespondentRouting(self):
    self.queryFinidCorrespondentRouting()
    result = []
    while 1:
      rc, rec = self.fetchFinidCorrespondentRouting()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainGrps(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.Name = result[1]
  def _data(self):
    return [self.GroupId, self.Name]
  def _fields(self):
    return 'GroupId|Name'.split('|')
  def queryGrps(self):
    self._query = self._connect.query('DomainGrps', self._data())
  def fetchGrps(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainGrps(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelGrps(self):
    self._connect.cancel(self._query)
  def loadGrps(self):
    self.queryGrps()
    result = []
    while 1:
      rc, rec = self.fetchGrps()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainLookup(object):
  __slots__ = ['_connect', '_query', 'Name', 'Ref', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Ref = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Ref = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Name, self.Ref, self.Value]
  def _fields(self):
    return 'Name|Ref|Value'.split('|')
  def queryLookup(self):
    self._query = self._connect.query('DomainLookup', self._data())
  def fetchLookup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainLookup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelLookup(self):
    self._connect.cancel(self._query)
  def loadLookup(self):
    self.queryLookup()
    result = []
    while 1:
      rc, rec = self.fetchLookup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainMT103Direct(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrencyID', 'DirectFlag']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrencyID = ''
    self.DirectFlag = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrencyID = result[1]
    self.DirectFlag = result[2]
  def _data(self):
    return [self.Country, self.CurrencyID, self.DirectFlag]
  def _fields(self):
    return 'Country|CurrencyID|DirectFlag'.split('|')
  def queryMT103Direct(self):
    self._query = self._connect.query('DomainMT103Direct', self._data())
  def fetchMT103Direct(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainMT103Direct(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelMT103Direct(self):
    self._connect.cancel(self._query)
  def loadMT103Direct(self):
    self.queryMT103Direct()
    result = []
    while 1:
      rc, rec = self.fetchMT103Direct()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainMT103DirectExceptions(object):
  __slots__ = ['_connect', '_query', 'Country', 'CurrencyID', 'BankName']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CurrencyID = ''
    self.BankName = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CurrencyID = result[1]
    self.BankName = result[2]
  def _data(self):
    return [self.Country, self.CurrencyID, self.BankName]
  def _fields(self):
    return 'Country|CurrencyID|BankName'.split('|')
  def queryMT103DirectExceptions(self):
    self._query = self._connect.query('DomainMT103DirectExceptions', self._data())
  def fetchMT103DirectExceptions(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainMT103DirectExceptions(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelMT103DirectExceptions(self):
    self._connect.cancel(self._query)
  def loadMT103DirectExceptions(self):
    self.queryMT103DirectExceptions()
    result = []
    while 1:
      rc, rec = self.fetchMT103DirectExceptions()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainQueueType(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Descr', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.Name = ''
    self.Descr = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Descr = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.Id, self.Name, self.Descr, self.Status]
  def _fields(self):
    return 'Id|Name|Descr|Status'.split('|')
  def queryQueueType(self):
    self._query = self._connect.query('DomainQueueType', self._data())
  def fetchQueueType(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainQueueType(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueueType(self):
    self._connect.cancel(self._query)
  def loadQueueType(self):
    self.queryQueueType()
    result = []
    while 1:
      rc, rec = self.fetchQueueType()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainQueue(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Descr', 'InputDriver', 'OutputDriver', 'QueueType', 'Priority', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Descr = ''
    self.InputDriver = ''
    self.OutputDriver = ''
    self.QueueType = 0
    self.Priority = 0
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Descr = result[2]
    self.InputDriver = result[3]
    self.OutputDriver = result[4]
    self.QueueType = result[5]
    self.Priority = result[6]
    self.Status = result[7]
  def _data(self):
    return [self.Id, self.Name, self.Descr, self.InputDriver, self.OutputDriver, self.QueueType, self.Priority, self.Status]
  def _fields(self):
    return 'Id|Name|Descr|InputDriver|OutputDriver|QueueType|Priority|Status'.split('|')
  def queryQueue(self):
    self._query = self._connect.query('DomainQueue', self._data())
  def fetchQueue(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainQueue(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelQueue(self):
    self._connect.cancel(self._query)
  def loadQueue(self):
    self.queryQueue()
    result = []
    while 1:
      rc, rec = self.fetchQueue()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainScriptGroup(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'GroupId', 'AccessType']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.GroupId = ''
    self.AccessType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.GroupId = result[1]
    self.AccessType = result[2]
  def _data(self):
    return [self.ScriptName, self.GroupId, self.AccessType]
  def _fields(self):
    return 'ScriptName|GroupId|AccessType'.split('|')
  def queryScriptGroup(self):
    self._query = self._connect.query('DomainScriptGroup', self._data())
  def fetchScriptGroup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainScriptGroup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelScriptGroup(self):
    self._connect.cancel(self._query)
  def loadScriptGroup(self):
    self.queryScriptGroup()
    result = []
    while 1:
      rc, rec = self.fetchScriptGroup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainSourceSystem(object):
  __slots__ = ['_connect', '_query', 'ID', 'Name', 'Decription', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = ''
    self.Name = ''
    self.Decription = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.Name = result[1]
    self.Decription = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.ID, self.Name, self.Decription, self.Status]
  def _fields(self):
    return 'ID|Name|Decription|Status'.split('|')
  def querySourceSystem(self):
    self._query = self._connect.query('DomainSourceSystem', self._data())
  def fetchSourceSystem(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainSourceSystem(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSourceSystem(self):
    self._connect.cancel(self._query)
  def loadSourceSystem(self):
    self.querySourceSystem()
    result = []
    while 1:
      rc, rec = self.fetchSourceSystem()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStaff(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Description']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Description = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Description = result[2]
  def _data(self):
    return [self.Id, self.Name, self.Description]
  def _fields(self):
    return 'Id|Name|Description'.split('|')
  def queryStaff(self):
    self._query = self._connect.query('DomainStaff', self._data())
  def fetchStaff(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStaff(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStaff(self):
    self._connect.cancel(self._query)
  def loadStaff(self):
    self.queryStaff()
    result = []
    while 1:
      rc, rec = self.fetchStaff()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStaffGroup(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
  def _data(self):
    return [self.StaffId, self.GroupId]
  def _fields(self):
    return 'StaffId|GroupId'.split('|')
  def queryStaffGroup(self):
    self._query = self._connect.query('DomainStaffGroup', self._data())
  def fetchStaffGroup(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStaffGroup(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStaffGroup(self):
    self._connect.cancel(self._query)
  def loadStaffGroup(self):
    self.queryStaffGroup()
    result = []
    while 1:
      rc, rec = self.fetchStaffGroup()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStaffQueuePerm(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'QueueId', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.QueueId = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.QueueId = result[1]
    self.Status = result[2]
  def _data(self):
    return [self.StaffId, self.QueueId, self.Status]
  def _fields(self):
    return 'StaffId|QueueId|Status'.split('|')
  def queryStaffQueuePerm(self):
    self._query = self._connect.query('DomainStaffQueuePerm', self._data())
  def fetchStaffQueuePerm(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStaffQueuePerm(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStaffQueuePerm(self):
    self._connect.cancel(self._query)
  def loadStaffQueuePerm(self):
    self.queryStaffQueuePerm()
    result = []
    while 1:
      rc, rec = self.fetchStaffQueuePerm()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStreamFieldsDef(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Descr', 'Length', 'Format', 'DefaultValue', 'Mandatory']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Descr = ''
    self.Length = 0
    self.Format = ''
    self.DefaultValue = ''
    self.Mandatory = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Descr = result[2]
    self.Length = result[3]
    self.Format = result[4]
    self.DefaultValue = result[5]
    self.Mandatory = result[6]
  def _data(self):
    return [self.Id, self.Name, self.Descr, self.Length, self.Format, self.DefaultValue, self.Mandatory]
  def _fields(self):
    return 'Id|Name|Descr|Length|Format|DefaultValue|Mandatory'.split('|')
  def queryStreamFieldsDef(self):
    self._query = self._connect.query('DomainStreamFieldsDef', self._data())
  def fetchStreamFieldsDef(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStreamFieldsDef(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStreamFieldsDef(self):
    self._connect.cancel(self._query)
  def loadStreamFieldsDef(self):
    self.queryStreamFieldsDef()
    result = []
    while 1:
      rc, rec = self.fetchStreamFieldsDef()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStreamMessageFormat(object):
  __slots__ = ['_connect', '_query', 'Id', 'Format']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Format = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Format = result[1]
  def _data(self):
    return [self.Id, self.Format]
  def _fields(self):
    return 'Id|Format'.split('|')
  def queryStreamMessageFormat(self):
    self._query = self._connect.query('DomainStreamMessageFormat', self._data())
  def fetchStreamMessageFormat(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStreamMessageFormat(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStreamMessageFormat(self):
    self._connect.cancel(self._query)
  def loadStreamMessageFormat(self):
    self.queryStreamMessageFormat()
    result = []
    while 1:
      rc, rec = self.fetchStreamMessageFormat()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainStreamType(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
  def _data(self):
    return [self.Id, self.Descr]
  def _fields(self):
    return 'Id|Descr'.split('|')
  def queryStreamType(self):
    self._query = self._connect.query('DomainStreamType', self._data())
  def fetchStreamType(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainStreamType(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelStreamType(self):
    self._connect.cancel(self._query)
  def loadStreamType(self):
    self.queryStreamType()
    result = []
    while 1:
      rc, rec = self.fetchStreamType()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBDomainTestPack(object):
  __slots__ = ['_connect', '_query', 'Name']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
  def _data(self):
    return [self.Name]
  def _fields(self):
    return 'Name'.split('|')
  def queryTestPack(self):
    self._query = self._connect.query('DomainTestPack', self._data())
  def fetchTestPack(self):
    rc, result = self._connect.fetch(self._query)
    record = DBDomainTestPack(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelTestPack(self):
    self._connect.cancel(self._query)
  def loadTestPack(self):
    self.queryTestPack()
    result = []
    while 1:
      rc, rec = self.fetchTestPack()
      if rc == 0:
        break
      result.append(rec)
    return result

