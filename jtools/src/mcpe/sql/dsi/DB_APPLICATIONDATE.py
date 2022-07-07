from INTRINSICS import *
### generated code from DBPortal ###

class DBApplication_Date(object):
  __slots__ = ['_connect', '_query', 'Date_Type', 'Description', 'Current_Date', 'UserId', 'TMstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Date_Type = 0
    self.Description = ''
    self.Current_Date = ''
    self.UserId = ''
    self.TMstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Date_Type = result[0]
    self.Description = result[1]
    self.Current_Date = result[2]
    self.UserId = result[3]
    self.TMstamp = result[4]
  def _data(self):
    return [self.Date_Type, self.Description, self.Current_Date, self.UserId, self.TMstamp]
  def _fields(self):
    return 'Date_Type|Description|Current_Date|UserId|TMstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('Application_DateInsert', self._data())
    self._store(result)
  def runInsert(self, Date_Type, Description, Current_Date, UserId, TMstamp):
    self.Date_Type = Date_Type
    self.Description = Description
    self.Current_Date = Current_Date
    self.UserId = UserId
    self.TMstamp = TMstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('Application_DateUpdate', self._data())
    self._store(result)
  def runUpdate(self, Date_Type, Description, Current_Date, UserId, TMstamp):
    self.Date_Type = Date_Type
    self.Description = Description
    self.Current_Date = Current_Date
    self.UserId = UserId
    self.TMstamp = TMstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('Application_DateSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Date_Type):
    self.Date_Type = Date_Type
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('Application_DateSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBApplication_Date(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectAll(self):
    self._connect.cancel(self._query)
  def loadSelectAll(self):
    self.querySelectAll()
    result = []
    while 1:
      rc, rec = self.fetchSelectAll()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBApplication_DateExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Date_Type']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Date_Type = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Date_Type = result[1]
  def _data(self):
    return [self.Count, self.Date_Type]
  def _fields(self):
    return 'Count|Date_Type'.split('|')
  def execExists(self):
    result = self._connect.action('Application_DateExists', self._data())
    self._store(result)
  def readExists(self, Date_Type):
    self.Date_Type = Date_Type
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBApplication_DateGetSysDate(object):
  __slots__ = ['_connect', '_query', 'SystemDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.SystemDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SystemDate = result[0]
  def _data(self):
    return [self.SystemDate]
  def _fields(self):
    return 'SystemDate'.split('|')
  def execGetSysDate(self):
    result = self._connect.action('Application_DateGetSysDate', self._data())
    self._store(result)
  def readGetSysDate(self):
    try:
      self.execGetSysDate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBApplication_DateUpdSystemDate(object):
  __slots__ = ['_connect', '_query', 'SystemDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.SystemDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SystemDate = result[0]
  def _data(self):
    return [self.SystemDate]
  def _fields(self):
    return 'SystemDate'.split('|')
  def execUpdSystemDate(self):
    result = self._connect.action('Application_DateUpdSystemDate', self._data())
    self._store(result)
  def runUpdSystemDate(self, SystemDate):
    self.SystemDate = SystemDate
    self.execUpdSystemDate()

class DBApplication_DateInc(object):
  __slots__ = ['_connect', '_query', 'InDateType']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDateType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDateType = result[0]
  def _data(self):
    return [self.InDateType]
  def _fields(self):
    return 'InDateType'.split('|')
  def execInc(self):
    result = self._connect.action('Application_DateInc', self._data())
    self._store(result)
  def runInc(self, InDateType):
    self.InDateType = InDateType
    self.execInc()

class DBApplication_DateSet(object):
  __slots__ = ['_connect', '_query', 'InDateType', 'NewDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDateType = 0
    self.NewDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDateType = result[0]
    self.NewDate = result[1]
  def _data(self):
    return [self.InDateType, self.NewDate]
  def _fields(self):
    return 'InDateType|NewDate'.split('|')
  def execSet(self):
    result = self._connect.action('Application_DateSet', self._data())
    self._store(result)
  def runSet(self, InDateType, NewDate):
    self.InDateType = InDateType
    self.NewDate = NewDate
    self.execSet()

class DBApplication_DateDateSet(object):
  __slots__ = ['_connect', '_query', 'InDateType']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDateType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDateType = result[0]
  def _data(self):
    return [self.InDateType]
  def _fields(self):
    return 'InDateType'.split('|')
  def execDateSet(self):
    result = self._connect.action('Application_DateDateSet', self._data())
    self._store(result)
  def runDateSet(self, InDateType):
    self.InDateType = InDateType
    self.execDateSet()

class DBApplication_Date_Count(object):
  __slots__ = ['_connect', '_query', 'NoRecs']
  def __init__(self, connect=None):
    self._connect = connect
    self.NoRecs = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.NoRecs = result[0]
  def _data(self):
    return [self.NoRecs]
  def _fields(self):
    return 'NoRecs'.split('|')
  def exec_Count(self):
    result = self._connect.action('Application_Date_Count', self._data())
    self._store(result)
  def read_Count(self):
    try:
      self.exec_Count()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBApplication_Date_Table(object):
  __slots__ = ['_connect', '_query', 'Type', 'Current_Date']
  def __init__(self, connect=None):
    self._connect = connect
    self.Type = 0
    self.Current_Date = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Type = result[0]
    self.Current_Date = result[1]
  def _data(self):
    return [self.Type, self.Current_Date]
  def _fields(self):
    return 'Type|Current_Date'.split('|')
  def query_Table(self):
    self._query = self._connect.query('Application_Date_Table', self._data())
  def fetch_Table(self):
    rc, result = self._connect.fetch(self._query)
    record = DBApplication_Date_Table(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancel_Table(self):
    self._connect.cancel(self._query)
  def load_Table(self):
    self.query_Table()
    result = []
    while 1:
      rc, rec = self.fetch_Table()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBApplication_DateGet(object):
  __slots__ = ['_connect', '_query', 'Type', 'Current_Date']
  def __init__(self, connect=None):
    self._connect = connect
    self.Type = 0
    self.Current_Date = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Type = result[0]
    self.Current_Date = result[1]
  def _data(self):
    return [self.Type, self.Current_Date]
  def _fields(self):
    return 'Type|Current_Date'.split('|')
  def execGet(self):
    result = self._connect.action('Application_DateGet', self._data())
    self._store(result)
  def readGet(self, Type):
    self.Type = Type
    try:
      self.execGet()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBApplication_DateUpdShortDate(object):
  __slots__ = ['_connect', '_query', 'Type', 'NewDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.Type = 0
    self.NewDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Type = result[0]
    self.NewDate = result[1]
  def _data(self):
    return [self.Type, self.NewDate]
  def _fields(self):
    return 'Type|NewDate'.split('|')
  def execUpdShortDate(self):
    result = self._connect.action('Application_DateUpdShortDate', self._data())
    self._store(result)
  def runUpdShortDate(self, Type, NewDate):
    self.Type = Type
    self.NewDate = NewDate
    self.execUpdShortDate()

