from INTRINSICS import *
### generated code from DBPortal ###

class DBWasteLog(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranNo', 'TranCode', 'SystemCode', 'LogSeq', 'ParentSeq', 'LinkSeq', 'ExtRef', 'Status', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
    self.LogSeq = 0
    self.ParentSeq = 0
    self.LinkSeq = 0
    self.ExtRef = ''
    self.Status = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranNo = result[1]
    self.TranCode = result[2]
    self.SystemCode = result[3]
    self.LogSeq = result[4]
    self.ParentSeq = result[5]
    self.LinkSeq = result[6]
    self.ExtRef = result[7]
    self.Status = result[8]
    self.Msg = result[9]
    self.MsgSize = result[10]
    self.TMStampIn = result[11]
    self.TMStampOut = result[12]
  def _data(self):
    return [self.RunDate, self.TranNo, self.TranCode, self.SystemCode, self.LogSeq, self.ParentSeq, self.LinkSeq, self.ExtRef, self.Status, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'RunDate|TranNo|TranCode|SystemCode|LogSeq|ParentSeq|LinkSeq|ExtRef|Status|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def execInsert(self):
    result = self._connect.action('WasteLogInsert', self._data())
    self._store(result)
  def runInsert(self, RunDate, TranNo, TranCode, SystemCode, LogSeq, ParentSeq, LinkSeq, ExtRef, Status, Msg, MsgSize, TMStampIn, TMStampOut):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.LogSeq = LogSeq
    self.ParentSeq = ParentSeq
    self.LinkSeq = LinkSeq
    self.ExtRef = ExtRef
    self.Status = Status
    self.Msg = Msg
    self.MsgSize = MsgSize
    self.TMStampIn = TMStampIn
    self.TMStampOut = TMStampOut
    self.execInsert()
  def execSelectOne(self):
    result = self._connect.action('WasteLogSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, RunDate, TranNo, TranCode, SystemCode):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def execUpdate(self):
    result = self._connect.action('WasteLogUpdate', self._data())
    self._store(result)
  def runUpdate(self, RunDate, TranNo, TranCode, SystemCode, LogSeq, ParentSeq, LinkSeq, ExtRef, Status, Msg, MsgSize, TMStampIn, TMStampOut):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.LogSeq = LogSeq
    self.ParentSeq = ParentSeq
    self.LinkSeq = LinkSeq
    self.ExtRef = ExtRef
    self.Status = Status
    self.Msg = Msg
    self.MsgSize = MsgSize
    self.TMStampIn = TMStampIn
    self.TMStampOut = TMStampOut
    self.execUpdate()
  def querySelectAll(self):
    self._query = self._connect.query('WasteLogSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBWasteLog(self._connect)
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

class DBWasteLogDeleteOne(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranNo', 'TranCode', 'SystemCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranNo = result[1]
    self.TranCode = result[2]
    self.SystemCode = result[3]
  def _data(self):
    return [self.RunDate, self.TranNo, self.TranCode, self.SystemCode]
  def _fields(self):
    return 'RunDate|TranNo|TranCode|SystemCode'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('WasteLogDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, RunDate, TranNo, TranCode, SystemCode):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.execDeleteOne()

class DBWasteLogExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'RunDate', 'TranNo', 'TranCode', 'SystemCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.RunDate = result[1]
    self.TranNo = result[2]
    self.TranCode = result[3]
    self.SystemCode = result[4]
  def _data(self):
    return [self.Count, self.RunDate, self.TranNo, self.TranCode, self.SystemCode]
  def _fields(self):
    return 'Count|RunDate|TranNo|TranCode|SystemCode'.split('|')
  def execExists(self):
    result = self._connect.action('WasteLogExists', self._data())
    self._store(result)
  def readExists(self, RunDate, TranNo, TranCode, SystemCode):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBWasteLogInsertParent(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranNo', 'TranCode', 'SystemCode', 'LogSeq', 'LinkSeq', 'Status', 'ExtRef', 'Msg', 'MsgSize', 'TMStampIn']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
    self.LogSeq = 0
    self.LinkSeq = 0
    self.Status = ''
    self.ExtRef = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranNo = result[1]
    self.TranCode = result[2]
    self.SystemCode = result[3]
    self.LogSeq = result[4]
    self.LinkSeq = result[5]
    self.Status = result[6]
    self.ExtRef = result[7]
    self.Msg = result[8]
    self.MsgSize = result[9]
    self.TMStampIn = result[10]
  def _data(self):
    return [self.RunDate, self.TranNo, self.TranCode, self.SystemCode, self.LogSeq, self.LinkSeq, self.Status, self.ExtRef, self.Msg, self.MsgSize, self.TMStampIn]
  def _fields(self):
    return 'RunDate|TranNo|TranCode|SystemCode|LogSeq|LinkSeq|Status|ExtRef|Msg|MsgSize|TMStampIn'.split('|')
  def execInsertParent(self):
    result = self._connect.action('WasteLogInsertParent', self._data())
    self._store(result)
  def runInsertParent(self, RunDate, TranNo, TranCode, SystemCode, LogSeq, LinkSeq, Status, ExtRef, Msg, MsgSize, TMStampIn):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.LogSeq = LogSeq
    self.LinkSeq = LinkSeq
    self.Status = Status
    self.ExtRef = ExtRef
    self.Msg = Msg
    self.MsgSize = MsgSize
    self.TMStampIn = TMStampIn
    self.execInsertParent()

class DBWasteLogNextLogSeq(object):
  __slots__ = ['_connect', '_query', 'LogSeq']
  def __init__(self, connect=None):
    self._connect = connect
    self.LogSeq = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LogSeq = result[0]
  def _data(self):
    return [self.LogSeq]
  def _fields(self):
    return 'LogSeq'.split('|')
  def execNextLogSeq(self):
    result = self._connect.action('WasteLogNextLogSeq', self._data())
    self._store(result)
  def readNextLogSeq(self):
    try:
      self.execNextLogSeq()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBWasteLogSelectChild(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranCode', 'SystemCode', 'ParentSeq', 'TranNo', 'LogSeq', 'LinkSeq', 'Status', 'ExtRef', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranCode = ''
    self.SystemCode = ''
    self.ParentSeq = 0
    self.TranNo = 0
    self.LogSeq = 0
    self.LinkSeq = 0
    self.Status = ''
    self.ExtRef = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranCode = result[1]
    self.SystemCode = result[2]
    self.ParentSeq = result[3]
    self.TranNo = result[4]
    self.LogSeq = result[5]
    self.LinkSeq = result[6]
    self.Status = result[7]
    self.ExtRef = result[8]
    self.Msg = result[9]
    self.MsgSize = result[10]
    self.TMStampIn = result[11]
    self.TMStampOut = result[12]
  def _data(self):
    return [self.RunDate, self.TranCode, self.SystemCode, self.ParentSeq, self.TranNo, self.LogSeq, self.LinkSeq, self.Status, self.ExtRef, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'RunDate|TranCode|SystemCode|ParentSeq|TranNo|LogSeq|LinkSeq|Status|ExtRef|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def execSelectChild(self):
    result = self._connect.action('WasteLogSelectChild', self._data())
    self._store(result)
  def readSelectChild(self, RunDate, TranCode, SystemCode, ParentSeq):
    self.RunDate = RunDate
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.ParentSeq = ParentSeq
    try:
      self.execSelectChild()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBWasteLogUpdateOutStatus(object):
  __slots__ = ['_connect', '_query', 'LogSeq', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.LogSeq = 0
    self.Status = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LogSeq = result[0]
    self.Status = result[1]
  def _data(self):
    return [self.LogSeq, self.Status]
  def _fields(self):
    return 'LogSeq|Status'.split('|')
  def execUpdateOutStatus(self):
    result = self._connect.action('WasteLogUpdateOutStatus', self._data())
    self._store(result)
  def runUpdateOutStatus(self, LogSeq, Status):
    self.LogSeq = LogSeq
    self.Status = Status
    self.execUpdateOutStatus()

class DBWasteLogSelectByLogSeq(object):
  __slots__ = ['_connect', '_query', 'LogSeq', 'RunDate', 'TranNo', 'TranCode', 'SystemCode', 'ParentSeq', 'LinkSeq', 'Status', 'ExtRef', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.LogSeq = 0
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
    self.ParentSeq = 0
    self.LinkSeq = 0
    self.Status = ''
    self.ExtRef = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LogSeq = result[0]
    self.RunDate = result[1]
    self.TranNo = result[2]
    self.TranCode = result[3]
    self.SystemCode = result[4]
    self.ParentSeq = result[5]
    self.LinkSeq = result[6]
    self.Status = result[7]
    self.ExtRef = result[8]
    self.Msg = result[9]
    self.MsgSize = result[10]
    self.TMStampIn = result[11]
    self.TMStampOut = result[12]
  def _data(self):
    return [self.LogSeq, self.RunDate, self.TranNo, self.TranCode, self.SystemCode, self.ParentSeq, self.LinkSeq, self.Status, self.ExtRef, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'LogSeq|RunDate|TranNo|TranCode|SystemCode|ParentSeq|LinkSeq|Status|ExtRef|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def execSelectByLogSeq(self):
    result = self._connect.action('WasteLogSelectByLogSeq', self._data())
    self._store(result)
  def readSelectByLogSeq(self, LogSeq):
    self.LogSeq = LogSeq
    try:
      self.execSelectByLogSeq()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBWasteLogUpdateNotFinalStatus(object):
  __slots__ = ['_connect', '_query', 'LinkSeq', 'Status']
  def __init__(self, connect=None):
    self._connect = connect
    self.LinkSeq = 0
    self.Status = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LinkSeq = result[0]
    self.Status = result[1]
  def _data(self):
    return [self.LinkSeq, self.Status]
  def _fields(self):
    return 'LinkSeq|Status'.split('|')
  def execUpdateNotFinalStatus(self):
    result = self._connect.action('WasteLogUpdateNotFinalStatus', self._data())
    self._store(result)
  def runUpdateNotFinalStatus(self, LinkSeq, Status):
    self.LinkSeq = LinkSeq
    self.Status = Status
    self.execUpdateNotFinalStatus()

class DBWasteLogSelectByExtRef(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranCode', 'SystemCode', 'ExtRef', 'TranNo', 'LogSeq', 'ParentSeq', 'LinkSeq', 'Status', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranCode = ''
    self.SystemCode = ''
    self.ExtRef = ''
    self.TranNo = 0
    self.LogSeq = 0
    self.ParentSeq = 0
    self.LinkSeq = 0
    self.Status = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranCode = result[1]
    self.SystemCode = result[2]
    self.ExtRef = result[3]
    self.TranNo = result[4]
    self.LogSeq = result[5]
    self.ParentSeq = result[6]
    self.LinkSeq = result[7]
    self.Status = result[8]
    self.Msg = result[9]
    self.MsgSize = result[10]
    self.TMStampIn = result[11]
    self.TMStampOut = result[12]
  def _data(self):
    return [self.RunDate, self.TranCode, self.SystemCode, self.ExtRef, self.TranNo, self.LogSeq, self.ParentSeq, self.LinkSeq, self.Status, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'RunDate|TranCode|SystemCode|ExtRef|TranNo|LogSeq|ParentSeq|LinkSeq|Status|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def execSelectByExtRef(self):
    result = self._connect.action('WasteLogSelectByExtRef', self._data())
    self._store(result)
  def readSelectByExtRef(self, RunDate, TranCode, SystemCode, ExtRef):
    self.RunDate = RunDate
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.ExtRef = ExtRef
    try:
      self.execSelectByExtRef()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBWasteLogInsertWithSeq(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'TranNo', 'TranCode', 'SystemCode', 'LogSeq', 'ParentSeq', 'LinkSeq', 'ExtRef', 'Status', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.TranNo = 0
    self.TranCode = ''
    self.SystemCode = ''
    self.LogSeq = 0
    self.ParentSeq = 0
    self.LinkSeq = 0
    self.ExtRef = ''
    self.Status = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.TranNo = result[1]
    self.TranCode = result[2]
    self.SystemCode = result[3]
    self.LogSeq = result[4]
    self.ParentSeq = result[5]
    self.LinkSeq = result[6]
    self.ExtRef = result[7]
    self.Status = result[8]
    self.Msg = result[9]
    self.MsgSize = result[10]
    self.TMStampIn = result[11]
    self.TMStampOut = result[12]
  def _data(self):
    return [self.RunDate, self.TranNo, self.TranCode, self.SystemCode, self.LogSeq, self.ParentSeq, self.LinkSeq, self.ExtRef, self.Status, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'RunDate|TranNo|TranCode|SystemCode|LogSeq|ParentSeq|LinkSeq|ExtRef|Status|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def execInsertWithSeq(self):
    result = self._connect.action('WasteLogInsertWithSeq', self._data())
    self._store(result)
  def runInsertWithSeq(self, RunDate, TranNo, TranCode, SystemCode, LogSeq, ParentSeq, LinkSeq, ExtRef, Status, Msg, MsgSize, TMStampIn, TMStampOut):
    self.RunDate = RunDate
    self.TranNo = TranNo
    self.TranCode = TranCode
    self.SystemCode = SystemCode
    self.LogSeq = LogSeq
    self.ParentSeq = ParentSeq
    self.LinkSeq = LinkSeq
    self.ExtRef = ExtRef
    self.Status = Status
    self.Msg = Msg
    self.MsgSize = MsgSize
    self.TMStampIn = TMStampIn
    self.TMStampOut = TMStampOut
    self.execInsertWithSeq()

class DBWasteLogDeleteByDays(object):
  __slots__ = ['_connect', '_query', 'NoDays', 'SystemCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.NoDays = 0
    self.SystemCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.NoDays = result[0]
    self.SystemCode = result[1]
  def _data(self):
    return [self.NoDays, self.SystemCode]
  def _fields(self):
    return 'NoDays|SystemCode'.split('|')
  def execDeleteByDays(self):
    result = self._connect.action('WasteLogDeleteByDays', self._data())
    self._store(result)
  def runDeleteByDays(self, NoDays, SystemCode):
    self.NoDays = NoDays
    self.SystemCode = SystemCode
    self.execDeleteByDays()

class DBWasteLogSelectRecovery(object):
  __slots__ = ['_connect', '_query', 'RunDate', 'SystemCode', 'MinutesAgo', 'TranNo', 'TranCode', 'LogSeq', 'ParentSeq', 'LinkSeq', 'Status', 'ExtRef', 'Msg', 'MsgSize', 'TMStampIn', 'TMStampOut']
  def __init__(self, connect=None):
    self._connect = connect
    self.RunDate = ''
    self.SystemCode = ''
    self.MinutesAgo = 0
    self.TranNo = 0
    self.TranCode = ''
    self.LogSeq = 0
    self.ParentSeq = 0
    self.LinkSeq = 0
    self.Status = ''
    self.ExtRef = ''
    self.Msg = ''
    self.MsgSize = 0
    self.TMStampIn = ''
    self.TMStampOut = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.RunDate = result[0]
    self.SystemCode = result[1]
    self.MinutesAgo = result[2]
    self.TranNo = result[3]
    self.TranCode = result[4]
    self.LogSeq = result[5]
    self.ParentSeq = result[6]
    self.LinkSeq = result[7]
    self.Status = result[8]
    self.ExtRef = result[9]
    self.Msg = result[10]
    self.MsgSize = result[11]
    self.TMStampIn = result[12]
    self.TMStampOut = result[13]
  def _data(self):
    return [self.RunDate, self.SystemCode, self.MinutesAgo, self.TranNo, self.TranCode, self.LogSeq, self.ParentSeq, self.LinkSeq, self.Status, self.ExtRef, self.Msg, self.MsgSize, self.TMStampIn, self.TMStampOut]
  def _fields(self):
    return 'RunDate|SystemCode|MinutesAgo|TranNo|TranCode|LogSeq|ParentSeq|LinkSeq|Status|ExtRef|Msg|MsgSize|TMStampIn|TMStampOut'.split('|')
  def querySelectRecovery(self):
    self._query = self._connect.query('WasteLogSelectRecovery', self._data())
  def fetchSelectRecovery(self):
    rc, result = self._connect.fetch(self._query)
    record = DBWasteLogSelectRecovery(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectRecovery(self):
    self._connect.cancel(self._query)
  def loadSelectRecovery(self):
    self.querySelectRecovery()
    result = []
    while 1:
      rc, rec = self.fetchSelectRecovery()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBWasteLogUpdateExtRef(object):
  __slots__ = ['_connect', '_query', 'LinkSeq', 'ExtRef']
  def __init__(self, connect=None):
    self._connect = connect
    self.LinkSeq = 0
    self.ExtRef = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LinkSeq = result[0]
    self.ExtRef = result[1]
  def _data(self):
    return [self.LinkSeq, self.ExtRef]
  def _fields(self):
    return 'LinkSeq|ExtRef'.split('|')
  def execUpdateExtRef(self):
    result = self._connect.action('WasteLogUpdateExtRef', self._data())
    self._store(result)
  def runUpdateExtRef(self, LinkSeq, ExtRef):
    self.LinkSeq = LinkSeq
    self.ExtRef = ExtRef
    self.execUpdateExtRef()

class DBWasteLogUpdateTMStampIn(object):
  __slots__ = ['_connect', '_query', 'LogSeq']
  def __init__(self, connect=None):
    self._connect = connect
    self.LogSeq = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.LogSeq = result[0]
  def _data(self):
    return [self.LogSeq]
  def _fields(self):
    return 'LogSeq'.split('|')
  def execUpdateTMStampIn(self):
    result = self._connect.action('WasteLogUpdateTMStampIn', self._data())
    self._store(result)
  def runUpdateTMStampIn(self, LogSeq):
    self.LogSeq = LogSeq
    self.execUpdateTMStampIn()

