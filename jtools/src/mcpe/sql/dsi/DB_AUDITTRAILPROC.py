from INTRINSICS import *
### generated code from DBPortal ###

class DBAudittrailByMsgNo(object):
  __slots__ = ['_connect', '_query', 'InMessageID', 'ID', 'MessageID', 'Action', 'FromStatus', 'ToStatus', 'Comments', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InMessageID = 0
    self.ID = 0
    self.MessageID = 0
    self.Action = 0
    self.FromStatus = 0
    self.ToStatus = 0
    self.Comments = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InMessageID = result[0]
    self.ID = result[1]
    self.MessageID = result[2]
    self.Action = result[3]
    self.FromStatus = result[4]
    self.ToStatus = result[5]
    self.Comments = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.InMessageID, self.ID, self.MessageID, self.Action, self.FromStatus, self.ToStatus, self.Comments, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InMessageID|ID|MessageID|Action|FromStatus|ToStatus|Comments|USId|Tmstamp'.split('|')
  def queryByMsgNo(self):
    self._query = self._connect.query('AudittrailByMsgNo', self._data())
  def fetchByMsgNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBAudittrailByMsgNo(self._connect)
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

