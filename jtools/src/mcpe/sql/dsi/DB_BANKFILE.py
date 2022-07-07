from INTRINSICS import *
### generated code from DBPortal ###

BankFileStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBBankFile(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'BankName', 'BankTown', 'BankType', 'BranchName', 'PhysicalAddr1', 'PhysicalAddr2', 'PhysicalAddr3', 'PhysicalAddr4', 'PhysicalAddr5', 'PhysicalCountry', 'PostalAddr1', 'PostalAddr2', 'PostalAddr3', 'PostalAddr4', 'PostalCountry', 'Telephone', 'EMail', 'Info', 'AuthKeysExchd', 'TgTestKeysExchd', 'DeleteInd', 'Status', 'USId', 'TmStamp']
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
    self.USId = ''
    self.TmStamp = ''
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
    self.USId = result[23]
    self.TmStamp = result[24]
  def _data(self):
    return [self.SwiftAddress, self.BankName, self.BankTown, self.BankType, self.BranchName, self.PhysicalAddr1, self.PhysicalAddr2, self.PhysicalAddr3, self.PhysicalAddr4, self.PhysicalAddr5, self.PhysicalCountry, self.PostalAddr1, self.PostalAddr2, self.PostalAddr3, self.PostalAddr4, self.PostalCountry, self.Telephone, self.EMail, self.Info, self.AuthKeysExchd, self.TgTestKeysExchd, self.DeleteInd, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'SwiftAddress|BankName|BankTown|BankType|BranchName|PhysicalAddr1|PhysicalAddr2|PhysicalAddr3|PhysicalAddr4|PhysicalAddr5|PhysicalCountry|PostalAddr1|PostalAddr2|PostalAddr3|PostalAddr4|PostalCountry|Telephone|EMail|Info|AuthKeysExchd|TgTestKeysExchd|DeleteInd|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('BankFileInsert', self._data())
    self._store(result)
  def runInsert(self, SwiftAddress, BankName, BankTown, BankType, BranchName, PhysicalAddr1, PhysicalAddr2, PhysicalAddr3, PhysicalAddr4, PhysicalAddr5, PhysicalCountry, PostalAddr1, PostalAddr2, PostalAddr3, PostalAddr4, PostalCountry, Telephone, EMail, Info, AuthKeysExchd, TgTestKeysExchd, DeleteInd, Status, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.BankName = BankName
    self.BankTown = BankTown
    self.BankType = BankType
    self.BranchName = BranchName
    self.PhysicalAddr1 = PhysicalAddr1
    self.PhysicalAddr2 = PhysicalAddr2
    self.PhysicalAddr3 = PhysicalAddr3
    self.PhysicalAddr4 = PhysicalAddr4
    self.PhysicalAddr5 = PhysicalAddr5
    self.PhysicalCountry = PhysicalCountry
    self.PostalAddr1 = PostalAddr1
    self.PostalAddr2 = PostalAddr2
    self.PostalAddr3 = PostalAddr3
    self.PostalAddr4 = PostalAddr4
    self.PostalCountry = PostalCountry
    self.Telephone = Telephone
    self.EMail = EMail
    self.Info = Info
    self.AuthKeysExchd = AuthKeysExchd
    self.TgTestKeysExchd = TgTestKeysExchd
    self.DeleteInd = DeleteInd
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('BankFileUpdate', self._data())
    self._store(result)
  def runUpdate(self, SwiftAddress, BankName, BankTown, BankType, BranchName, PhysicalAddr1, PhysicalAddr2, PhysicalAddr3, PhysicalAddr4, PhysicalAddr5, PhysicalCountry, PostalAddr1, PostalAddr2, PostalAddr3, PostalAddr4, PostalCountry, Telephone, EMail, Info, AuthKeysExchd, TgTestKeysExchd, DeleteInd, Status, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.BankName = BankName
    self.BankTown = BankTown
    self.BankType = BankType
    self.BranchName = BranchName
    self.PhysicalAddr1 = PhysicalAddr1
    self.PhysicalAddr2 = PhysicalAddr2
    self.PhysicalAddr3 = PhysicalAddr3
    self.PhysicalAddr4 = PhysicalAddr4
    self.PhysicalAddr5 = PhysicalAddr5
    self.PhysicalCountry = PhysicalCountry
    self.PostalAddr1 = PostalAddr1
    self.PostalAddr2 = PostalAddr2
    self.PostalAddr3 = PostalAddr3
    self.PostalAddr4 = PostalAddr4
    self.PostalCountry = PostalCountry
    self.Telephone = Telephone
    self.EMail = EMail
    self.Info = Info
    self.AuthKeysExchd = AuthKeysExchd
    self.TgTestKeysExchd = TgTestKeysExchd
    self.DeleteInd = DeleteInd
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('BankFileSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, SwiftAddress):
    self.SwiftAddress = SwiftAddress
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBBankFileDeleteOne(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
  def _data(self):
    return [self.SwiftAddress]
  def _fields(self):
    return 'SwiftAddress'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('BankFileDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, SwiftAddress):
    self.SwiftAddress = SwiftAddress
    self.execDeleteOne()

class DBBankFileGetAuthKeys(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'AuthKeysExchd']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.AuthKeysExchd = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.AuthKeysExchd = result[1]
  def _data(self):
    return [self.SwiftAddress, self.AuthKeysExchd]
  def _fields(self):
    return 'SwiftAddress|AuthKeysExchd'.split('|')
  def execGetAuthKeys(self):
    result = self._connect.action('BankFileGetAuthKeys', self._data())
    self._store(result)
  def readGetAuthKeys(self, SwiftAddress):
    self.SwiftAddress = SwiftAddress
    try:
      self.execGetAuthKeys()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBBankFileUpd(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'BankName', 'BankTown', 'BankType', 'BranchName', 'PhysicalAddr1', 'PhysicalAddr2', 'PhysicalAddr3', 'PhysicalAddr4', 'PhysicalAddr5', 'PhysicalCountry', 'PostalAddr1', 'PostalAddr2', 'PostalAddr3', 'PostalAddr4', 'PostalCountry', 'Status', 'USId']
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
    self.Status = 0
    self.USId = ''
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
    self.Status = result[16]
    self.USId = result[17]
  def _data(self):
    return [self.SwiftAddress, self.BankName, self.BankTown, self.BankType, self.BranchName, self.PhysicalAddr1, self.PhysicalAddr2, self.PhysicalAddr3, self.PhysicalAddr4, self.PhysicalAddr5, self.PhysicalCountry, self.PostalAddr1, self.PostalAddr2, self.PostalAddr3, self.PostalAddr4, self.PostalCountry, self.Status, self.USId]
  def _fields(self):
    return 'SwiftAddress|BankName|BankTown|BankType|BranchName|PhysicalAddr1|PhysicalAddr2|PhysicalAddr3|PhysicalAddr4|PhysicalAddr5|PhysicalCountry|PostalAddr1|PostalAddr2|PostalAddr3|PostalAddr4|PostalCountry|Status|USId'.split('|')
  def execUpd(self):
    result = self._connect.action('BankFileUpd', self._data())
    self._store(result)
  def runUpd(self, SwiftAddress, BankName, BankTown, BankType, BranchName, PhysicalAddr1, PhysicalAddr2, PhysicalAddr3, PhysicalAddr4, PhysicalAddr5, PhysicalCountry, PostalAddr1, PostalAddr2, PostalAddr3, PostalAddr4, PostalCountry, Status, USId):
    self.SwiftAddress = SwiftAddress
    self.BankName = BankName
    self.BankTown = BankTown
    self.BankType = BankType
    self.BranchName = BranchName
    self.PhysicalAddr1 = PhysicalAddr1
    self.PhysicalAddr2 = PhysicalAddr2
    self.PhysicalAddr3 = PhysicalAddr3
    self.PhysicalAddr4 = PhysicalAddr4
    self.PhysicalAddr5 = PhysicalAddr5
    self.PhysicalCountry = PhysicalCountry
    self.PostalAddr1 = PostalAddr1
    self.PostalAddr2 = PostalAddr2
    self.PostalAddr3 = PostalAddr3
    self.PostalAddr4 = PostalAddr4
    self.PostalCountry = PostalCountry
    self.Status = Status
    self.USId = USId
    self.execUpd()

class DBBankFileBankFileEXT(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'BankName', 'BankTown', 'AccountNo', 'BankType', 'CurrId', 'AccountTypeId', 'Telephone', 'EMail', 'Info', 'AuthKeysExchd', 'TgTestKeysExchd', 'DeleteInd', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.BankName = ''
    self.BankTown = ''
    self.AccountNo = ''
    self.BankType = ''
    self.CurrId = ''
    self.AccountTypeId = ''
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
    self.AccountNo = result[3]
    self.BankType = result[4]
    self.CurrId = result[5]
    self.AccountTypeId = result[6]
    self.Telephone = result[7]
    self.EMail = result[8]
    self.Info = result[9]
    self.AuthKeysExchd = result[10]
    self.TgTestKeysExchd = result[11]
    self.DeleteInd = result[12]
    self.Status = result[13]
  def _data(self):
    return [self.SwiftAddress, self.BankName, self.BankTown, self.AccountNo, self.BankType, self.CurrId, self.AccountTypeId, self.Telephone, self.EMail, self.Info, self.AuthKeysExchd, self.TgTestKeysExchd, self.DeleteInd, self.Status]
  def _fields(self):
    return 'SwiftAddress|BankName|BankTown|AccountNo|BankType|CurrId|AccountTypeId|Telephone|EMail|Info|AuthKeysExchd|TgTestKeysExchd|DeleteInd|Status'.split('|')
  def queryBankFileEXT(self):
    self._query = self._connect.query('BankFileBankFileEXT', self._data())
  def fetchBankFileEXT(self):
    rc, result = self._connect.fetch(self._query)
    record = DBBankFileBankFileEXT(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelBankFileEXT(self):
    self._connect.cancel(self._query)
  def loadBankFileEXT(self):
    self.queryBankFileEXT()
    result = []
    while 1:
      rc, rec = self.fetchBankFileEXT()
      if rc == 0:
        break
      result.append(rec)
    return result

