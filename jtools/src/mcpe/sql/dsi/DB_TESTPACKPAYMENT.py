from INTRINSICS import *
### generated code from DBPortal ###

class DBTestpackPayment(object):
  __slots__ = ['_connect', '_query', 'Testpackid', 'TestMessageID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Testpackid = ''
    self.TestMessageID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Testpackid = result[0]
    self.TestMessageID = result[1]
  def _data(self):
    return [self.Testpackid, self.TestMessageID]
  def _fields(self):
    return 'Testpackid|TestMessageID'.split('|')
  def execInsert(self):
    result = self._connect.action('TestpackPaymentInsert', self._data())
    self._store(result)
  def runInsert(self, Testpackid, TestMessageID):
    self.Testpackid = Testpackid
    self.TestMessageID = TestMessageID
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('TestpackPaymentUpdate', self._data())
    self._store(result)
  def runUpdate(self, Testpackid, TestMessageID):
    self.Testpackid = Testpackid
    self.TestMessageID = TestMessageID
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('TestpackPaymentSelectOne', self._data())
    self._store(result)
  def runSelectOne(self, Testpackid, TestMessageID):
    self.Testpackid = Testpackid
    self.TestMessageID = TestMessageID
    self.execSelectOne()
  def runDeleteAll(self):
    self._connect.action('TestpackPaymentDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('TestpackPaymentSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBTestpackPayment(self._connect)
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

class DBTestpackPaymentDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Testpackid', 'TestMessageID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Testpackid = ''
    self.TestMessageID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Testpackid = result[0]
    self.TestMessageID = result[1]
  def _data(self):
    return [self.Testpackid, self.TestMessageID]
  def _fields(self):
    return 'Testpackid|TestMessageID'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('TestpackPaymentDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Testpackid, TestMessageID):
    self.Testpackid = Testpackid
    self.TestMessageID = TestMessageID
    self.execDeleteOne()

class DBTestpackPaymentExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'Testpackid', 'TestMessageID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.Testpackid = ''
    self.TestMessageID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.Testpackid = result[1]
    self.TestMessageID = result[2]
  def _data(self):
    return [self.Count, self.Testpackid, self.TestMessageID]
  def _fields(self):
    return 'Count|Testpackid|TestMessageID'.split('|')
  def execExists(self):
    result = self._connect.action('TestpackPaymentExists', self._data())
    self._store(result)
  def readExists(self, Testpackid, TestMessageID):
    self.Testpackid = Testpackid
    self.TestMessageID = TestMessageID
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBTestpackPaymentCount(object):
  __slots__ = ['_connect', '_query', 'NoOf']
  def __init__(self, connect=None):
    self._connect = connect
    self.NoOf = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.NoOf = result[0]
  def _data(self):
    return [self.NoOf]
  def _fields(self):
    return 'NoOf'.split('|')
  def execCount(self):
    result = self._connect.action('TestpackPaymentCount', self._data())
    self._store(result)
  def readCount(self):
    try:
      self.execCount()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

