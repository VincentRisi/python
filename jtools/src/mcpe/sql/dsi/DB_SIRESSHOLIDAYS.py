from INTRINSICS import *
### generated code from DBPortal ###

class DBSIRESSHolidays(object):
  __slots__ = ['_connect', '_query', 'HoliDayDate', 'Description', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.HoliDayDate = ''
    self.Description = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.HoliDayDate = result[0]
    self.Description = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.HoliDayDate, self.Description, self.USId, self.TmStamp]
  def _fields(self):
    return 'HoliDayDate|Description|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('SIRESSHolidaysInsert', self._data())
    self._store(result)
  def runInsert(self, HoliDayDate, Description, USId, TmStamp):
    self.HoliDayDate = HoliDayDate
    self.Description = Description
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('SIRESSHolidaysUpdate', self._data())
    self._store(result)
  def runUpdate(self, HoliDayDate, Description, USId, TmStamp):
    self.HoliDayDate = HoliDayDate
    self.Description = Description
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('SIRESSHolidaysSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, HoliDayDate):
    self.HoliDayDate = HoliDayDate
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSIRESSHolidaysDeleteOne(object):
  __slots__ = ['_connect', '_query', 'HoliDayDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.HoliDayDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.HoliDayDate = result[0]
  def _data(self):
    return [self.HoliDayDate]
  def _fields(self):
    return 'HoliDayDate'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('SIRESSHolidaysDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, HoliDayDate):
    self.HoliDayDate = HoliDayDate
    self.execDeleteOne()

class DBSIRESSHolidaysSelectHoliday(object):
  __slots__ = ['_connect', '_query', 'inDate', 'outHoliDayDate']
  def __init__(self, connect=None):
    self._connect = connect
    self.inDate = ''
    self.outHoliDayDate = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inDate = result[0]
    self.outHoliDayDate = result[1]
  def _data(self):
    return [self.inDate, self.outHoliDayDate]
  def _fields(self):
    return 'inDate|outHoliDayDate'.split('|')
  def querySelectHoliday(self):
    self._query = self._connect.query('SIRESSHolidaysSelectHoliday', self._data())
  def fetchSelectHoliday(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSHolidaysSelectHoliday(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectHoliday(self):
    self._connect.cancel(self._query)
  def loadSelectHoliday(self):
    self.querySelectHoliday()
    result = []
    while 1:
      rc, rec = self.fetchSelectHoliday()
      if rc == 0:
        break
      result.append(rec)
    return result

