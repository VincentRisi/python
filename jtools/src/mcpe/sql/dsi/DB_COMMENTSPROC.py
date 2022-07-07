from INTRINSICS import *
### generated code from DBPortal ###

class DBCommentsByMsgNo(object):
  __slots__ = ['_connect', '_query', 'InMessageID', 'ID', 'Text', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageID = 0
    self.ID = 0
    self.Text = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageID = result[0]
    self.ID = result[1]
    self.Text = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
  def _data(self):
    return [self.InMessageID, self.ID, self.Text, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageID|ID|Text|USId|Tmstamp'.split('|')
  def queryByMsgNo(self):
    self._query = self._connect.query('CommentsByMsgNo', self._data())
  def fetchByMsgNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBCommentsByMsgNo(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByMsgNo(self):
    self._connect.cancel(self._query)
  def loadByMsgNo(self):
    self.queryByMsgNo()
    result = []
    while 1:
      rc, rec = self.fetchByMsgNo()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBCommentsByID(object):
  __slots__ = ['_connect', '_query', 'InID', 'MessageID', 'Text', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InID = 0
    self.MessageID = 0
    self.Text = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InID = result[0]
    self.MessageID = result[1]
    self.Text = result[2]
    self.USId = result[3]
    self.Tmstamp = result[4]
  def _data(self):
    return [self.InID, self.MessageID, self.Text, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InID|MessageID|Text|USId|Tmstamp'.split('|')
  def execByID(self):
    result = self._connect.action('CommentsByID', self._data())
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

