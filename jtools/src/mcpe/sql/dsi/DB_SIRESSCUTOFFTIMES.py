from INTRINSICS import *
### generated code from DBPortal ###

class DBSIRESSCutOffTimes(object):
  __slots__ = ['_connect', '_query', 'CurrentDay', 'TradingDay', 'StartOfDay', 'CutOffTime', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.CurrentDay = ''
    self.TradingDay = ''
    self.StartOfDay = ''
    self.CutOffTime = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CurrentDay = result[0]
    self.TradingDay = result[1]
    self.StartOfDay = result[2]
    self.CutOffTime = result[3]
    self.USId = result[4]
    self.TmStamp = result[5]
  def _data(self):
    return [self.CurrentDay, self.TradingDay, self.StartOfDay, self.CutOffTime, self.USId, self.TmStamp]
  def _fields(self):
    return 'CurrentDay|TradingDay|StartOfDay|CutOffTime|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('SIRESSCutOffTimesInsert', self._data())
    self._store(result)
  def runInsert(self, CurrentDay, TradingDay, StartOfDay, CutOffTime, USId, TmStamp):
    self.CurrentDay = CurrentDay
    self.TradingDay = TradingDay
    self.StartOfDay = StartOfDay
    self.CutOffTime = CutOffTime
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('SIRESSCutOffTimesUpdate', self._data())
    self._store(result)
  def runUpdate(self, CurrentDay, TradingDay, StartOfDay, CutOffTime, USId, TmStamp):
    self.CurrentDay = CurrentDay
    self.TradingDay = TradingDay
    self.StartOfDay = StartOfDay
    self.CutOffTime = CutOffTime
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('SIRESSCutOffTimesSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, CurrentDay):
    self.CurrentDay = CurrentDay
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSIRESSCutOffTimesDeleteOne(object):
  __slots__ = ['_connect', '_query', 'CurrentDay']
  def __init__(self, connect=None):
    self._connect = connect
    self.CurrentDay = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CurrentDay = result[0]
  def _data(self):
    return [self.CurrentDay]
  def _fields(self):
    return 'CurrentDay'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('SIRESSCutOffTimesDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, CurrentDay):
    self.CurrentDay = CurrentDay
    self.execDeleteOne()

class DBSIRESSCutOffTimesSelTradingDay(object):
  __slots__ = ['_connect', '_query', 'inDay', 'outTradingDay', 'outStartOfDay', 'outCutOffTime']
  def __init__(self, connect=None):
    self._connect = connect
    self.inDay = ''
    self.outTradingDay = ''
    self.outStartOfDay = ''
    self.outCutOffTime = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inDay = result[0]
    self.outTradingDay = result[1]
    self.outStartOfDay = result[2]
    self.outCutOffTime = result[3]
  def _data(self):
    return [self.inDay, self.outTradingDay, self.outStartOfDay, self.outCutOffTime]
  def _fields(self):
    return 'inDay|outTradingDay|outStartOfDay|outCutOffTime'.split('|')
  def querySelTradingDay(self):
    self._query = self._connect.query('SIRESSCutOffTimesSelTradingDay', self._data())
  def fetchSelTradingDay(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSCutOffTimesSelTradingDay(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelTradingDay(self):
    self._connect.cancel(self._query)
  def loadSelTradingDay(self):
    self.querySelTradingDay()
    result = []
    while 1:
      rc, rec = self.fetchSelTradingDay()
      if rc == 0:
        break
      result.append(rec)
    return result

