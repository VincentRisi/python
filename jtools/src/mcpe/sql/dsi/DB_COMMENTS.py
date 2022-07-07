from INTRINSICS import *
### generated code from DBPortal ###

class DBComments(object):
  __slots__ = ['_connect', '_query', 'ID', 'MessageID', 'Text', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.MessageID = 0
    self.Text = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.MessageID = result[1]
    self.Text = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
  def _data(self):
    return [self.ID, self.MessageID, self.Text, self.USId, self.Tmstamp]
  def _fields(self):
    return 'ID|MessageID|Text|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('CommentsInsert', self._data())
    self._store(result)
  def runInsert(self, ID, MessageID, Text, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.Text = Text
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('CommentsUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, MessageID, Text, USId, Tmstamp):
    self.ID = ID
    self.MessageID = MessageID
    self.Text = Text
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('CommentsSelectOne', self._data())
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
    self._connect.action('CommentsDeleteAll', [])
  def querySelectAll(self):
    self._query = self._connect.query('CommentsSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBComments(self._connect)
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

class DBCommentsDeleteOne(object):
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
    result = self._connect.action('CommentsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ID):
    self.ID = ID
    self.execDeleteOne()

class DBCommentsExists(object):
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
    result = self._connect.action('CommentsExists', self._data())
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

class DBCommentsCount(object):
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
    result = self._connect.action('CommentsCount', self._data())
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

