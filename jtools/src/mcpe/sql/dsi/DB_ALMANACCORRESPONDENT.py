from INTRINSICS import *
### generated code from DBPortal ###

AlmanacCorrespondentStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }
class DBAlmanacCorrespondent(object):
  __slots__ = ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBranchId', 'CorrBankName', 'CorrTown', 'CorrCountry', 'CorrAccountNo', 'CorrSwiftAddress', 'PreferredInd', 'RBIInsertDate', 'RBIChangeDate', 'Status', 'USId', 'TmStamp']
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
    self.USId = ''
    self.TmStamp = ''
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
    self.USId = result[13]
    self.TmStamp = result[14]
  def _data(self):
    return [self.FinId, self.CorrCurrency, self.CorrFinId, self.CorrBranchId, self.CorrBankName, self.CorrTown, self.CorrCountry, self.CorrAccountNo, self.CorrSwiftAddress, self.PreferredInd, self.RBIInsertDate, self.RBIChangeDate, self.Status, self.USId, self.TmStamp]
  def _fields(self):
    return 'FinId|CorrCurrency|CorrFinId|CorrBranchId|CorrBankName|CorrTown|CorrCountry|CorrAccountNo|CorrSwiftAddress|PreferredInd|RBIInsertDate|RBIChangeDate|Status|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('AlmanacCorrespondentInsert', self._data())
    self._store(result)
  def runInsert(self, FinId, CorrCurrency, CorrFinId, CorrBranchId, CorrBankName, CorrTown, CorrCountry, CorrAccountNo, CorrSwiftAddress, PreferredInd, RBIInsertDate, RBIChangeDate, Status, USId, TmStamp):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    self.CorrFinId = CorrFinId
    self.CorrBranchId = CorrBranchId
    self.CorrBankName = CorrBankName
    self.CorrTown = CorrTown
    self.CorrCountry = CorrCountry
    self.CorrAccountNo = CorrAccountNo
    self.CorrSwiftAddress = CorrSwiftAddress
    self.PreferredInd = PreferredInd
    self.RBIInsertDate = RBIInsertDate
    self.RBIChangeDate = RBIChangeDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('AlmanacCorrespondentUpdate', self._data())
    self._store(result)
  def runUpdate(self, FinId, CorrCurrency, CorrFinId, CorrBranchId, CorrBankName, CorrTown, CorrCountry, CorrAccountNo, CorrSwiftAddress, PreferredInd, RBIInsertDate, RBIChangeDate, Status, USId, TmStamp):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    self.CorrFinId = CorrFinId
    self.CorrBranchId = CorrBranchId
    self.CorrBankName = CorrBankName
    self.CorrTown = CorrTown
    self.CorrCountry = CorrCountry
    self.CorrAccountNo = CorrAccountNo
    self.CorrSwiftAddress = CorrSwiftAddress
    self.PreferredInd = PreferredInd
    self.RBIInsertDate = RBIInsertDate
    self.RBIChangeDate = RBIChangeDate
    self.Status = Status
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('AlmanacCorrespondentSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, FinId, CorrCurrency, CorrFinId, CorrBranchId):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    self.CorrFinId = CorrFinId
    self.CorrBranchId = CorrBranchId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacCorrespondentDeleteOne(object):
  __slots__ = ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBranchId']
  def __init__(self, connect=None):
    self._connect = connect
    self.FinId = 0
    self.CorrCurrency = ''
    self.CorrFinId = 0
    self.CorrBranchId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.FinId = result[0]
    self.CorrCurrency = result[1]
    self.CorrFinId = result[2]
    self.CorrBranchId = result[3]
  def _data(self):
    return [self.FinId, self.CorrCurrency, self.CorrFinId, self.CorrBranchId]
  def _fields(self):
    return 'FinId|CorrCurrency|CorrFinId|CorrBranchId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('AlmanacCorrespondentDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, FinId, CorrCurrency, CorrFinId, CorrBranchId):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    self.CorrFinId = CorrFinId
    self.CorrBranchId = CorrBranchId
    self.execDeleteOne()

class DBAlmanacCorrespondentExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBranchId']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.FinId = 0
    self.CorrCurrency = ''
    self.CorrFinId = 0
    self.CorrBranchId = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.FinId = result[1]
    self.CorrCurrency = result[2]
    self.CorrFinId = result[3]
    self.CorrBranchId = result[4]
  def _data(self):
    return [self.Count, self.FinId, self.CorrCurrency, self.CorrFinId, self.CorrBranchId]
  def _fields(self):
    return 'Count|FinId|CorrCurrency|CorrFinId|CorrBranchId'.split('|')
  def execExists(self):
    result = self._connect.action('AlmanacCorrespondentExists', self._data())
    self._store(result)
  def readExists(self, FinId, CorrCurrency, CorrFinId, CorrBranchId):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    self.CorrFinId = CorrFinId
    self.CorrBranchId = CorrBranchId
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacCorrespondentUpdateAllStatus(object):
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
    result = self._connect.action('AlmanacCorrespondentUpdateAllStatus', self._data())
    self._store(result)
  def runUpdateAllStatus(self, Status, USId):
    self.Status = Status
    self.USId = USId
    self.execUpdateAllStatus()

class DBAlmanacCorrespondentGet(object):
  __slots__ = ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrFinId', 'CorrBankName', 'CorrTown', 'CorrCountry', 'CorrAccountNo', 'CorrSwiftAddress', 'PreferredInd', 'Status']
  def __init__(self, connect=None):
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
    result = self._connect.action('AlmanacCorrespondentGet', self._data())
    self._store(result)
  def readGet(self, FinId, CorrCurrency):
    self.FinId = FinId
    self.CorrCurrency = CorrCurrency
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBAlmanacCorrespondentGetSwiftList(object):
  __slots__ = ['_connect', '_query', 'FinId', 'CorrCurrency', 'CorrSwiftAddress', 'Status']
  def __init__(self, connect=None):
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
    self._query = self._connect.query('AlmanacCorrespondentGetSwiftList', self._data())
  def fetchGetSwiftList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAlmanacCorrespondentGetSwiftList(self._connect)
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

