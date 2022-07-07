from INTRINSICS import *
### generated code from DBPortal ###

class DBLookup(object):
  __slots__ = ['_connect', '_query', 'Name', 'Refs', 'Value', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Refs = ''
    self.Value = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
    self.Value = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Name, self.Refs, self.Value, self.USId, self.TmStamp]
  def _fields(self):
    return 'Name|Refs|Value|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('LookupInsert', self._data())
    self._store(result)
  def runInsert(self, Name, Refs, Value, USId, TmStamp):
    self.Name = Name
    self.Refs = Refs
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('LookupUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, Refs, Value, USId, TmStamp):
    self.Name = Name
    self.Refs = Refs
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('LookupSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name, Refs):
    self.Name = Name
    self.Refs = Refs
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def runDeleteAll(self):
    self._connect.action('LookupDeleteAll', [])

class DBLookupDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Name', 'Refs']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Refs = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
  def _data(self):
    return [self.Name, self.Refs]
  def _fields(self):
    return 'Name|Refs'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('LookupDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name, Refs):
    self.Name = Name
    self.Refs = Refs
    self.execDeleteOne()

class DBLookupSelectList(object):
  __slots__ = ['_connect', '_query', 'Name', 'Refs', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.Name = ''
    self.Refs = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Name, self.Refs, self.Value]
  def _fields(self):
    return 'Name|Refs|Value'.split('|')
  def querySelectList(self):
    self._query = self._connect.query('LookupSelectList', self._data())
  def fetchSelectList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupSelectList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectList(self):
    self._connect.cancel(self._query)
  def loadSelectList(self):
    self.querySelectList()
    result = []
    while 1:
      rc, rec = self.fetchSelectList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBLookupGet(object):
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
  def execGet(self):
    result = self._connect.action('LookupGet', self._data())
    self._store(result)
  def readGet(self, Name, Ref):
    self.Name = Name
    self.Ref = Ref
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBLookupNameList(object):
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
  def queryNameList(self):
    self._query = self._connect.query('LookupNameList', self._data())
  def fetchNameList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupNameList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelNameList(self):
    self._connect.cancel(self._query)
  def loadNameList(self):
    self.queryNameList()
    result = []
    while 1:
      rc, rec = self.fetchNameList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBLookupSelectIBAN(object):
  __slots__ = ['_connect', '_query', 'Ref', 'Name', 'Value']
  def __init__(self, connect=None):
    self._connect = connect
    self.Ref = ''
    self.Name = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Ref = result[0]
    self.Name = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Ref, self.Name, self.Value]
  def _fields(self):
    return 'Ref|Name|Value'.split('|')
  def querySelectIBAN(self):
    self._query = self._connect.query('LookupSelectIBAN', self._data())
  def fetchSelectIBAN(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupSelectIBAN(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectIBAN(self):
    self._connect.cancel(self._query)
  def loadSelectIBAN(self):
    self.querySelectIBAN()
    result = []
    while 1:
      rc, rec = self.fetchSelectIBAN()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBLookupSelectVatAccNumber(object):
  __slots__ = ['_connect', '_query', 'Ref', 'Value', 'USid', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Ref = ''
    self.Value = ''
    self.USid = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Ref = result[0]
    self.Value = result[1]
    self.USid = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.Ref, self.Value, self.USid, self.TmStamp]
  def _fields(self):
    return 'Ref|Value|USid|TmStamp'.split('|')
  def execSelectVatAccNumber(self):
    result = self._connect.action('LookupSelectVatAccNumber', self._data())
    self._store(result)
  def readSelectVatAccNumber(self, Ref):
    self.Ref = Ref
    try:
      self.execSelectVatAccNumber()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBLookupSelectAllVatAccNumber(object):
  __slots__ = ['_connect', '_query', 'Value', 'USid', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Value = ''
    self.USid = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Value = result[0]
    self.USid = result[1]
    self.TmStamp = result[2]
  def _data(self):
    return [self.Value, self.USid, self.TmStamp]
  def _fields(self):
    return 'Value|USid|TmStamp'.split('|')
  def querySelectAllVatAccNumber(self):
    self._query = self._connect.query('LookupSelectAllVatAccNumber', self._data())
  def fetchSelectAllVatAccNumber(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupSelectAllVatAccNumber(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectAllVatAccNumber(self):
    self._connect.cancel(self._query)
  def loadSelectAllVatAccNumber(self):
    self.querySelectAllVatAccNumber()
    result = []
    while 1:
      rc, rec = self.fetchSelectAllVatAccNumber()
      if rc == 0:
        break
      result.append(rec)
    return result

