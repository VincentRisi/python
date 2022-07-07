from INTRINSICS import *
### generated code from DBPortal ###

class DBTestPayment(object):
  __slots__ = ['_connect', '_query', 'TestMessageID', 'SourcesystemID', 'Referance', 'Message', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.TestMessageID = 0
    self.SourcesystemID = ''
    self.Referance = ''
    self.Message = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.TestMessageID = result[0]
    self.SourcesystemID = result[1]
    self.Referance = result[2]
    self.Message = result[3]
    self.USId = result[4]
    self.Tmstamp = result[5]
  def _data(self):
    return [self.TestMessageID, self.SourcesystemID, self.Referance, self.Message, self.USId, self.Tmstamp]
  def _fields(self):
    return 'TestMessageID|SourcesystemID|Referance|Message|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('TestPaymentInsert', self._data())
    self._store(result)
  def runInsert(self, TestMessageID, SourcesystemID, Referance, Message, USId, Tmstamp):
    self.TestMessageID = TestMessageID
    self.SourcesystemID = SourcesystemID
    self.Referance = Referance
    self.Message = Message
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('TestPaymentUpdate', self._data())
    self._store(result)
  def runUpdate(self, TestMessageID, SourcesystemID, Referance, Message, USId, Tmstamp):
    self.TestMessageID = TestMessageID
    self.SourcesystemID = SourcesystemID
    self.Referance = Referance
    self.Message = Message
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('TestPaymentSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, TestMessageID):
    self.TestMessageID = TestMessageID
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
    self._connect.action('TestPaymentDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('TestPaymentSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBTestPayment(self._connect)
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

class DBTestPaymentDeleteOne(object):
  __slots__ = ['_connect', '_query', 'TestMessageID']
  def __init__(self, connect=None):
    self._connect = connect
    self.TestMessageID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.TestMessageID = result[0]
  def _data(self):
    return [self.TestMessageID]
  def _fields(self):
    return 'TestMessageID'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('TestPaymentDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, TestMessageID):
    self.TestMessageID = TestMessageID
    self.execDeleteOne()

class DBTestPaymentExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'TestMessageID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.TestMessageID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.TestMessageID = result[1]
  def _data(self):
    return [self.Count, self.TestMessageID]
  def _fields(self):
    return 'Count|TestMessageID'.split('|')
  def execExists(self):
    result = self._connect.action('TestPaymentExists', self._data())
    self._store(result)
  def readExists(self, TestMessageID):
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

class DBTestPaymentCount(object):
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
    result = self._connect.action('TestPaymentCount', self._data())
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

