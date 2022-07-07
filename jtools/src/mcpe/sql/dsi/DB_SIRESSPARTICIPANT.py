from INTRINSICS import *
### generated code from DBPortal ###

class DBSIRESSParticipants(object):
  __slots__ = ['_connect', '_query', 'ParticipantBIC', 'ParticipantBankName', 'CPLAccNo', 'RTLAccNo', 'CPLGLAccNo', 'RTLGLAccNo', 'SiressBIC', 'PayCode', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ParticipantBIC = ''
    self.ParticipantBankName = ''
    self.CPLAccNo = ''
    self.RTLAccNo = ''
    self.CPLGLAccNo = ''
    self.RTLGLAccNo = ''
    self.SiressBIC = ''
    self.PayCode = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ParticipantBIC = result[0]
    self.ParticipantBankName = result[1]
    self.CPLAccNo = result[2]
    self.RTLAccNo = result[3]
    self.CPLGLAccNo = result[4]
    self.RTLGLAccNo = result[5]
    self.SiressBIC = result[6]
    self.PayCode = result[7]
    self.USId = result[8]
    self.TmStamp = result[9]
  def _data(self):
    return [self.ParticipantBIC, self.ParticipantBankName, self.CPLAccNo, self.RTLAccNo, self.CPLGLAccNo, self.RTLGLAccNo, self.SiressBIC, self.PayCode, self.USId, self.TmStamp]
  def _fields(self):
    return 'ParticipantBIC|ParticipantBankName|CPLAccNo|RTLAccNo|CPLGLAccNo|RTLGLAccNo|SiressBIC|PayCode|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('SIRESSParticipantsInsert', self._data())
    self._store(result)
  def runInsert(self, ParticipantBIC, ParticipantBankName, CPLAccNo, RTLAccNo, CPLGLAccNo, RTLGLAccNo, SiressBIC, PayCode, USId, TmStamp):
    self.ParticipantBIC = ParticipantBIC
    self.ParticipantBankName = ParticipantBankName
    self.CPLAccNo = CPLAccNo
    self.RTLAccNo = RTLAccNo
    self.CPLGLAccNo = CPLGLAccNo
    self.RTLGLAccNo = RTLGLAccNo
    self.SiressBIC = SiressBIC
    self.PayCode = PayCode
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('SIRESSParticipantsUpdate', self._data())
    self._store(result)
  def runUpdate(self, ParticipantBIC, ParticipantBankName, CPLAccNo, RTLAccNo, CPLGLAccNo, RTLGLAccNo, SiressBIC, PayCode, USId, TmStamp):
    self.ParticipantBIC = ParticipantBIC
    self.ParticipantBankName = ParticipantBankName
    self.CPLAccNo = CPLAccNo
    self.RTLAccNo = RTLAccNo
    self.CPLGLAccNo = CPLGLAccNo
    self.RTLGLAccNo = RTLGLAccNo
    self.SiressBIC = SiressBIC
    self.PayCode = PayCode
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('SIRESSParticipantsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, ParticipantBIC):
    self.ParticipantBIC = ParticipantBIC
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSIRESSParticipantsDeleteOne(object):
  __slots__ = ['_connect', '_query', 'ParticipantBIC']
  def __init__(self, connect=None):
    self._connect = connect
    self.ParticipantBIC = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ParticipantBIC = result[0]
  def _data(self):
    return [self.ParticipantBIC]
  def _fields(self):
    return 'ParticipantBIC'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('SIRESSParticipantsDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ParticipantBIC):
    self.ParticipantBIC = ParticipantBIC
    self.execDeleteOne()

class DBSIRESSParticipantsExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'ParticipantBIC']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.ParticipantBIC = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.ParticipantBIC = result[1]
  def _data(self):
    return [self.Count, self.ParticipantBIC]
  def _fields(self):
    return 'Count|ParticipantBIC'.split('|')
  def execExists(self):
    result = self._connect.action('SIRESSParticipantsExists', self._data())
    self._store(result)
  def readExists(self, ParticipantBIC):
    self.ParticipantBIC = ParticipantBIC
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBSIRESSParticipantsSelParticipantForPartSwift(object):
  __slots__ = ['_connect', '_query', 'inParticipantBIC', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inParticipantBIC = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inParticipantBIC = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inParticipantBIC, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inParticipantBIC|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForPartSwift(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForPartSwift', self._data())
  def fetchSelParticipantForPartSwift(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForPartSwift(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForPartSwift(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForPartSwift(self):
    self.querySelParticipantForPartSwift()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForPartSwift()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBSIRESSParticipantsSelParticipantForFullSwift(object):
  __slots__ = ['_connect', '_query', 'inParticipantBIC', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inParticipantBIC = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inParticipantBIC = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inParticipantBIC, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inParticipantBIC|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForFullSwift(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForFullSwift', self._data())
  def fetchSelParticipantForFullSwift(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForFullSwift(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForFullSwift(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForFullSwift(self):
    self.querySelParticipantForFullSwift()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForFullSwift()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBSIRESSParticipantsSelParticipantForCPLAccNo(object):
  __slots__ = ['_connect', '_query', 'inCPLAccNo', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inCPLAccNo = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inCPLAccNo = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inCPLAccNo, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inCPLAccNo|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForCPLAccNo(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForCPLAccNo', self._data())
  def fetchSelParticipantForCPLAccNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForCPLAccNo(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForCPLAccNo(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForCPLAccNo(self):
    self.querySelParticipantForCPLAccNo()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForCPLAccNo()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBSIRESSParticipantsSelParticipantForRTLAccNo(object):
  __slots__ = ['_connect', '_query', 'inRTLAccNo', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inRTLAccNo = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inRTLAccNo = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inRTLAccNo, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inRTLAccNo|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForRTLAccNo(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForRTLAccNo', self._data())
  def fetchSelParticipantForRTLAccNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForRTLAccNo(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForRTLAccNo(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForRTLAccNo(self):
    self.querySelParticipantForRTLAccNo()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForRTLAccNo()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBSIRESSParticipantsSelParticipantForCPLGLAccNo(object):
  __slots__ = ['_connect', '_query', 'inCPLGLAccNo', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inCPLGLAccNo = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inCPLGLAccNo = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inCPLGLAccNo, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inCPLGLAccNo|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForCPLGLAccNo(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForCPLGLAccNo', self._data())
  def fetchSelParticipantForCPLGLAccNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForCPLGLAccNo(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForCPLGLAccNo(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForCPLGLAccNo(self):
    self.querySelParticipantForCPLGLAccNo()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForCPLGLAccNo()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBSIRESSParticipantsSelParticipantForRTLGLAccNo(object):
  __slots__ = ['_connect', '_query', 'inRTLGLAccNo', 'outParticipantBIC', 'outCPLAccNo', 'outRTLAccNo', 'outCPLGLAccNo', 'outRTLGLAccNo', 'outSiressBIC', 'outPayCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.inRTLGLAccNo = ''
    self.outParticipantBIC = ''
    self.outCPLAccNo = ''
    self.outRTLAccNo = ''
    self.outCPLGLAccNo = ''
    self.outRTLGLAccNo = ''
    self.outSiressBIC = ''
    self.outPayCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.inRTLGLAccNo = result[0]
    self.outParticipantBIC = result[1]
    self.outCPLAccNo = result[2]
    self.outRTLAccNo = result[3]
    self.outCPLGLAccNo = result[4]
    self.outRTLGLAccNo = result[5]
    self.outSiressBIC = result[6]
    self.outPayCode = result[7]
  def _data(self):
    return [self.inRTLGLAccNo, self.outParticipantBIC, self.outCPLAccNo, self.outRTLAccNo, self.outCPLGLAccNo, self.outRTLGLAccNo, self.outSiressBIC, self.outPayCode]
  def _fields(self):
    return 'inRTLGLAccNo|outParticipantBIC|outCPLAccNo|outRTLAccNo|outCPLGLAccNo|outRTLGLAccNo|outSiressBIC|outPayCode'.split('|')
  def querySelParticipantForRTLGLAccNo(self):
    self._query = self._connect.query('SIRESSParticipantsSelParticipantForRTLGLAccNo', self._data())
  def fetchSelParticipantForRTLGLAccNo(self):
    rc, result = self._connect.fetch(self._query)
    record = DBSIRESSParticipantsSelParticipantForRTLGLAccNo(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelParticipantForRTLGLAccNo(self):
    self._connect.cancel(self._query)
  def loadSelParticipantForRTLGLAccNo(self):
    self.querySelParticipantForRTLGLAccNo()
    result = []
    while 1:
      rc, rec = self.fetchSelParticipantForRTLGLAccNo()
      if rc == 0:
        break
      result.append(rec)
    return result

