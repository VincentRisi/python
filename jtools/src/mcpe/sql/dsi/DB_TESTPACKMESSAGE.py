from INTRINSICS import *
### generated code from DBPortal ###

class DBTestPackMessage(object):
  __slots__ = ['_connect', '_query', 'MessageId', 'PackName', 'USId', 'TMStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageId = 0
    self.PackName = ''
    self.USId = ''
    self.TMStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageId = result[0]
    self.PackName = result[1]
    self.USId = result[2]
    self.TMStamp = result[3]
  def _data(self):
    return [self.MessageId, self.PackName, self.USId, self.TMStamp]
  def _fields(self):
    return 'MessageId|PackName|USId|TMStamp'.split('|')

