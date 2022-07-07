from INTRINSICS import *
### generated code from DBPortal ###

class DBBCurcyCurcy(object):
  __slots__ = ['_connect', '_query', 'Id', 'Descr', 'Comments', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Descr = ''
    self.Comments = ''
    self.Status = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Descr = result[1]
    self.Comments = result[2]
    self.Status = result[3]
  def _data(self):
    return [self.Id, self.Descr, self.Comments, self.Status]
  def _fields(self):
    return 'Id|Descr|Comments|Status'.split('|')
  def queryCurcy(self):
    self._query = self._connect.query('BCurcyCurcy', self._data())
  def fetchCurcy(self):
    rc, result = self._connect.fetch(self._query)
    record = DBBCurcyCurcy(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelCurcy(self):
    self._connect.cancel(self._query)
  def loadCurcy(self):
    self.queryCurcy()
    result = []
    while 1:
      rc, rec = self.fetchCurcy()
      if rc == 0:
        break
      result.append(rec)
    return result

