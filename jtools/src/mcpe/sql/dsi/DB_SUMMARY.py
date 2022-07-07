from INTRINSICS import *
### generated code from DBPortal ###

SummarySummaryTypeConst = {
  'XML' : 0, 0 : 'XML',
  'Text' : 1, 1 : 'Text',
  }
class DBSummary(object):
  __slots__ = ['_connect', '_query', 'ID', 'MessageID', 'SummaryLen', 'SummaryData', 'SummaryType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.MessageID = 0
    self.SummaryLen = 0
    self.SummaryData = 0
    self.SummaryType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.MessageID = result[1]
    self.SummaryLen = result[2]
    self.SummaryData = result[3]
    self.SummaryType = result[4]
    self.USId = result[5]
    self.Tmstamp = result[6]
  def _data(self):
    return [self.ID, self.MessageID, self.SummaryLen, self.SummaryData, self.SummaryType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'ID|MessageID|SummaryLen|SummaryData|SummaryType|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('SummaryInsert', self._data())
    self._store(result)
  def runInsert(self, ID, MessageID, SummaryLen, SummaryData, SummaryType, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.SummaryLen = SummaryLen
    self.SummaryData = SummaryData
    self.SummaryType = SummaryType
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('SummaryUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, MessageID, SummaryLen, SummaryData, SummaryType, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.SummaryLen = SummaryLen
    self.SummaryData = SummaryData
    self.SummaryType = SummaryType
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('SummarySelectOne', self._data())
    self._store(result)
  def readSelectOne(self, ID):
    self.ID = ID
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
    self._connect.action('SummaryDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('SummarySelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSummary(self._connect)
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

class DBSummaryDeleteOne(object):
  __slots__ = ['_connect', '_query', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
  def _data(self):
    return [self.ID]
  def _fields(self):
    return 'ID'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('SummaryDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ID):
    self.ID = ID
    self.execDeleteOne()

class DBSummaryExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.ID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.ID = result[1]
  def _data(self):
    return [self.Count, self.ID]
  def _fields(self):
    return 'Count|ID'.split('|')
  def execExists(self):
    result = self._connect.action('SummaryExists', self._data())
    self._store(result)
  def readExists(self, ID):
    self.ID = ID
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSummaryCount(object):
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
    result = self._connect.action('SummaryCount', self._data())
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

class DBSummaryByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'ID', 'MessageID', 'SummaryLen', 'SummaryData', 'SummaryType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.ID = 0
    self.MessageID = 0
    self.SummaryLen = 0
    self.SummaryData = 0
    self.SummaryType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.ID = result[1]
    self.MessageID = result[2]
    self.SummaryLen = result[3]
    self.SummaryData = result[4]
    self.SummaryType = result[5]
    self.USId = result[6]
    self.Tmstamp = result[7]
  def _data(self):
    return [self.InID, self.ID, self.MessageID, self.SummaryLen, self.SummaryData, self.SummaryType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InID|ID|MessageID|SummaryLen|SummaryData|SummaryType|USId|Tmstamp'.split('|')
  def execByID(self):
    result = self._connect.action('SummaryByID', self._data())
    self._store(result)
  def readByID(self, InID):
    self.InID = InID
    try:
      self.execByID()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSummaryByDayAndQueueId(object):
  __slots__ = ['_connect', '_query', 'InDate', 'QueueId', 'ID', 'MessageID', 'SummaryLen', 'SummaryData', 'SummaryType', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InDate = ''
    self.QueueId = ''
    self.ID = 0
    self.MessageID = 0
    self.SummaryLen = 0
    self.SummaryData = 0
    self.SummaryType = 0
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InDate = result[0]
    self.QueueId = result[1]
    self.ID = result[2]
    self.MessageID = result[3]
    self.SummaryLen = result[4]
    self.SummaryData = result[5]
    self.SummaryType = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.InDate, self.QueueId, self.ID, self.MessageID, self.SummaryLen, self.SummaryData, self.SummaryType, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InDate|QueueId|ID|MessageID|SummaryLen|SummaryData|SummaryType|USId|Tmstamp'.split('|')
  def queryByDayAndQueueId(self):
    self._query = self._connect.query('SummaryByDayAndQueueId', self._data())
  def fetchByDayAndQueueId(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSummaryByDayAndQueueId(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByDayAndQueueId(self):
    self._connect.cancel(self._query)
  def loadByDayAndQueueId(self):
    self.queryByDayAndQueueId()
    result = []
    while 1:
      rc, rec = self.fetchByDayAndQueueId()
      if rc == 0:
        break
      result.append(rec)
    return result

