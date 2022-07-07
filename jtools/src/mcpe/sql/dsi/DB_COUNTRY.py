from INTRINSICS import *
### generated code from DBPortal ###

CountryStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  }
class DBCountry(object):
  __slots__ = ['_connect', '_query', 'Id', 'CodeId', 'CurrId', 'Status', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.CodeId = ''
    self.CurrId = ''
    self.Status = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.CodeId = result[1]
    self.CurrId = result[2]
    self.Status = result[3]
    self.USId = result[4]
    self.Tmstamp = result[5]
  def _data(self):
    return [self.Id, self.CodeId, self.CurrId, self.Status, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Id|CodeId|CurrId|Status|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('CountryInsert', self._data())
    self._store(result)
  def runInsert(self, Id, CodeId, CurrId, Status, USId, Tmstamp):
    self.Id = Id
    self.CodeId = CodeId
    self.CurrId = CurrId
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('CountryUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, CodeId, CurrId, Status, USId, Tmstamp):
    self.Id = Id
    self.CodeId = CodeId
    self.CurrId = CurrId
    self.Status = Status
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('CountrySelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id):
    self.Id = Id
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBCountryDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
  def _data(self):
    return [self.Id]
  def _fields(self):
    return 'Id'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('CountryDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

class DBCountryGet(object):
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
  def execGet(self):
    result = self._connect.action('CountryGet', self._data())
    self._store(result)
  def readGet(self, Id):
    self.Id = Id
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBCountryGetByCurrency(object):
  __slots__ = ['_connect', '_query', 'CurrId', 'Id', 'CodeId', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.CurrId = ''
    self.Id = ''
    self.CodeId = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CurrId = result[0]
    self.Id = result[1]
    self.CodeId = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.CurrId, self.Id, self.CodeId, self.Status]
  def _fields(self):
    return 'CurrId|Id|CodeId|Status'.split('|')
  def execGetByCurrency(self):
    result = self._connect.action('CountryGetByCurrency', self._data())
    self._store(result)
  def readGetByCurrency(self, CurrId):
    self.CurrId = CurrId
    try:
      self.execGetByCurrency()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBCountryGetByCodeId(object):
  __slots__ = ['_connect', '_query', 'CodeId', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.CodeId = ''
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CodeId = result[0]
    self.Id = result[1]
  def _data(self):
    return [self.CodeId, self.Id]
  def _fields(self):
    return 'CodeId|Id'.split('|')
  def execGetByCodeId(self):
    result = self._connect.action('CountryGetByCodeId', self._data())
    self._store(result)
  def readGetByCodeId(self, CodeId):
    self.CodeId = CodeId
    try:
      self.execGetByCodeId()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

