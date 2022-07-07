from INTRINSICS import *
### generated code from DBPortal ###

class DBBankAccountFromLT(object):
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
  def execFromLT(self):
    result = self._connect.action('BankAccountFromLT', self._data())
    self._store(result)
  def readFromLT(self, SwiftAddress, CurrId, AccountTypeId):
    self.SwiftAddress = SwiftAddress
    self.CurrId = CurrId
    self.AccountTypeId = AccountTypeId
    try:
      self.execFromLT()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

