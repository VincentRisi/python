from INTRINSICS import *
### generated code from DBPortal ###

class DBFileOutput(object):
  __slots__ = ['_connect', '_query', 'ID', 'Name', 'FileDate', 'FileSize', 'Message', 'Header', 'Trailer', 'Error', 'Status', 'USId', 'TMstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.Name = ''
    self.FileDate = ''
    self.FileSize = 0
    self.Message = ''
    self.Header = ''
    self.Trailer = ''
    self.Error = 0
    self.Status = 0
    self.USId = ''
    self.TMstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.Name = result[1]
    self.FileDate = result[2]
    self.FileSize = result[3]
    self.Message = result[4]
    self.Header = result[5]
    self.Trailer = result[6]
    self.Error = result[7]
    self.Status = result[8]
    self.USId = result[9]
    self.TMstamp = result[10]
  def _data(self):
    return [self.ID, self.Name, self.FileDate, self.FileSize, self.Message, self.Header, self.Trailer, self.Error, self.Status, self.USId, self.TMstamp]
  def _fields(self):
    return 'ID|Name|FileDate|FileSize|Message|Header|Trailer|Error|Status|USId|TMstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FileOutputInsert', self._data())
    self._store(result)
  def runInsert(self, ID, Name, FileDate, FileSize, Message, Header, Trailer, Error, Status, USId, TMstamp):
    self.ID = ID
    self.Name = Name
    self.FileDate = FileDate
    self.FileSize = FileSize
    self.Message = Message
    self.Header = Header
    self.Trailer = Trailer
    self.Error = Error
    self.Status = Status
    self.USId = USId
    self.TMstamp = TMstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('FileOutputUpdate', self._data())
    self._store(result)
  def runUpdate(self, ID, Name, FileDate, FileSize, Message, Header, Trailer, Error, Status, USId, TMstamp):
    self.ID = ID
    self.Name = Name
    self.FileDate = FileDate
    self.FileSize = FileSize
    self.Message = Message
    self.Header = Header
    self.Trailer = Trailer
    self.Error = Error
    self.Status = Status
    self.USId = USId
    self.TMstamp = TMstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('FileOutputSelectOne', self._data())
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
  def execSelectOneUpd(self):
    result = self._connect.action('FileOutputSelectOneUpd', self._data())
    self._store(result)
  def readSelectOneUpd(self, ID):
    self.ID = ID
    try:
      self.execSelectOneUpd()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('FileOutputSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFileOutput(self._connect)
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

class DBFileOutputDeleteOne(object):
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
    result = self._connect.action('FileOutputDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ID):
    self.ID = ID
    self.execDeleteOne()

class DBFileOutputExists(object):
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
    result = self._connect.action('FileOutputExists', self._data())
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

class DBFileOutputProcessed(object):
  __slots__ = ['_connect', '_query', 'File_Name', 'File_Size', 'Status', 'Hash1', 'MyCount']
  def __init__(self, connect=None):
    self._connect = connect
    self.File_Name = ''
    self.File_Size = 0
    self.Status = 0
    self.Hash1 = ''
    self.MyCount = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.File_Name = result[0]
    self.File_Size = result[1]
    self.Status = result[2]
    self.Hash1 = result[3]
    self.MyCount = result[4]
  def _data(self):
    return [self.File_Name, self.File_Size, self.Status, self.Hash1, self.MyCount]
  def _fields(self):
    return 'File_Name|File_Size|Status|Hash1|MyCount'.split('|')
  def execProcessed(self):
    result = self._connect.action('FileOutputProcessed', self._data())
    self._store(result)
  def readProcessed(self, File_Name, File_Size, Status, Hash1):
    self.File_Name = File_Name
    self.File_Size = File_Size
    self.Status = Status
    self.Hash1 = Hash1
    try:
      self.execProcessed()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

