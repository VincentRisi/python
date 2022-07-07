from INTRINSICS import *
### generated code from DBPortal ###

class DBBankFileBicAddress(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'MyCount']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.MyCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.MyCount = result[1]
  def _data(self):
    return [self.SwiftAddress, self.MyCount]
  def _fields(self):
    return 'SwiftAddress|MyCount'.split('|')
  def execBicAddress(self):
    result = self._connect.action('BankFileBicAddress', self._data())
    self._store(result)
  def readBicAddress(self, SwiftAddress):
    self.SwiftAddress = SwiftAddress
    try:
      self.execBicAddress()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBBankFileSetAllStatus(object):
  __slots__ = ['_connect', '_query', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Status = result[0]
  def _data(self):
    return [self.Status]
  def _fields(self):
    return 'Status'.split('|')
  def execSetAllStatus(self):
    result = self._connect.action('BankFileSetAllStatus', self._data())
    self._store(result)
  def runSetAllStatus(self, Status):
    self.Status = Status
    self.execSetAllStatus()

