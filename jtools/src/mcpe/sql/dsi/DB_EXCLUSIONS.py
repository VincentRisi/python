from INTRINSICS import *
### generated code from DBPortal ###

class DBEXCLUSIONS(object):
  __slots__ = ['_connect', '_query', 'SWIFTADDRESS', 'ACCOUNTNO', 'BENCORRIND', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.SWIFTADDRESS = ''
    self.ACCOUNTNO = ''
    self.BENCORRIND = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SWIFTADDRESS = result[0]
    self.ACCOUNTNO = result[1]
    self.BENCORRIND = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.SWIFTADDRESS, self.ACCOUNTNO, self.BENCORRIND, self.USId, self.TmStamp]
  def _fields(self):
    return 'SWIFTADDRESS|ACCOUNTNO|BENCORRIND|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('EXCLUSIONSInsert', self._data())
    self._store(result)
  def runInsert(self, SWIFTADDRESS, ACCOUNTNO, BENCORRIND, USId, TmStamp):
    self.SWIFTADDRESS = SWIFTADDRESS
    self.ACCOUNTNO = ACCOUNTNO
    self.BENCORRIND = BENCORRIND
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('EXCLUSIONSUpdate', self._data())
    self._store(result)
  def runUpdate(self, SWIFTADDRESS, ACCOUNTNO, BENCORRIND, USId, TmStamp):
    self.SWIFTADDRESS = SWIFTADDRESS
    self.ACCOUNTNO = ACCOUNTNO
    self.BENCORRIND = BENCORRIND
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('EXCLUSIONSSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, SWIFTADDRESS, ACCOUNTNO):
    self.SWIFTADDRESS = SWIFTADDRESS
    self.ACCOUNTNO = ACCOUNTNO
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBEXCLUSIONSDeleteOne(object):
  __slots__ = ['_connect', '_query', 'SWIFTADDRESS', 'ACCOUNTNO']
  def __init__(self, connect=None):
    self._connect = connect
    self.SWIFTADDRESS = ''
    self.ACCOUNTNO = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SWIFTADDRESS = result[0]
    self.ACCOUNTNO = result[1]
  def _data(self):
    return [self.SWIFTADDRESS, self.ACCOUNTNO]
  def _fields(self):
    return 'SWIFTADDRESS|ACCOUNTNO'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('EXCLUSIONSDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, SWIFTADDRESS, ACCOUNTNO):
    self.SWIFTADDRESS = SWIFTADDRESS
    self.ACCOUNTNO = ACCOUNTNO
    self.execDeleteOne()

class DBEXCLUSIONSSelectExclusion(object):
  __slots__ = ['_connect', '_query', 'SWIFTADDRESS', 'ACCOUNTNO', 'BENCORRIND']
  def __init__(self, connect=None):
    self._connect = connect
    self.SWIFTADDRESS = ''
    self.ACCOUNTNO = ''
    self.BENCORRIND = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SWIFTADDRESS = result[0]
    self.ACCOUNTNO = result[1]
    self.BENCORRIND = result[2]
  def _data(self):
    return [self.SWIFTADDRESS, self.ACCOUNTNO, self.BENCORRIND]
  def _fields(self):
    return 'SWIFTADDRESS|ACCOUNTNO|BENCORRIND'.split('|')
  def querySelectExclusion(self):
    self._query = self._connect.query('EXCLUSIONSSelectExclusion', self._data())
  def fetchSelectExclusion(self):
    rc, result = self._connect.fetch(self._query)
    record = DBEXCLUSIONSSelectExclusion(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectExclusion(self):
    self._connect.cancel(self._query)
  def loadSelectExclusion(self):
    self.querySelectExclusion()
    result = []
    while 1:
      rc, rec = self.fetchSelectExclusion()
      if rc == 0:
        break
      result.append(rec)
    return result

