from INTRINSICS import *
### generated code from DBPortal ###

class DBBankAccount(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'AccountTypeId', 'AccountNo', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.AccountTypeId = ''
    self.AccountNo = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.AccountTypeId = result[2]
    self.AccountNo = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.AccountTypeId, self.AccountNo, self.USId, self.TmStamp]
  def _fields(self):
    return 'SwiftAddress|CurrId|AccountTypeId|AccountNo|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('BankAccountInsert', self._data())
    self._store(result)
  def runInsert(self, SwiftAddress, CurrId, AccountTypeId, AccountNo, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.AccountTypeId = AccountTypeId
    self.AccountNo = AccountNo
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('BankAccountUpdate', self._data())
    self._store(result)
  def runUpdate(self, SwiftAddress, CurrId, AccountTypeId, AccountNo, USId, TmStamp):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.AccountTypeId = AccountTypeId
    self.AccountNo = AccountNo
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('BankAccountSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, SwiftAddress, CurrId, AccountTypeId):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.AccountTypeId = AccountTypeId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBBankAccountDeleteOne(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'AccountTypeId']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.AccountTypeId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.AccountTypeId = result[2]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.AccountTypeId]
  def _fields(self):
    return 'SwiftAddress|CurrId|AccountTypeId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('BankAccountDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, SwiftAddress, CurrId, AccountTypeId):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.AccountTypeId = AccountTypeId
    self.execDeleteOne()

class DBBankAccountAccNoBySwift(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'CurrId', 'AccountNo', 'AccountTypeId']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.CurrId = ''
    self.AccountNo = ''
    self.AccountTypeId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.CurrId = result[1]
    self.AccountNo = result[2]
    self.AccountTypeId = result[3]
  def _data(self):
    return [self.SwiftAddress, self.CurrId, self.AccountNo, self.AccountTypeId]
  def _fields(self):
    return 'SwiftAddress|CurrId|AccountNo|AccountTypeId'.split('|')
  def queryAccNoBySwift(self):
    self._query = self._connect.query('BankAccountAccNoBySwift', self._data())
  def fetchAccNoBySwift(self):
    rc, result = self._connect.fetch(self._query)
    record = DBBankAccountAccNoBySwift(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelAccNoBySwift(self):
    self._connect.cancel(self._query)
  def loadAccNoBySwift(self):
    self.queryAccNoBySwift()
    result = []
    while 1:
      rc, rec = self.fetchAccNoBySwift()
      if rc == 0:
        break
      result.append(rec)
    return result

