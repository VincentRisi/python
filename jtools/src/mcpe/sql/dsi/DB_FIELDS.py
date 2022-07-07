from INTRINSICS import *
### generated code from DBPortal ###

class DBFields(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'Tag', 'Content', 'Fieldsearchid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.Tag = ''
    self.Content = ''
    self.Fieldsearchid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.Tag = result[1]
    self.Content = result[2]
    self.Fieldsearchid = result[3]
    self.USId = result[4]
    self.Tmstamp = result[5]
  def _data(self):
    return [self.MessageID, self.Tag, self.Content, self.Fieldsearchid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'MessageID|Tag|Content|Fieldsearchid|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('FieldsInsert', self._data())
    self._store(result)
  def runInsert(self, MessageID, Tag, Content, Fieldsearchid, USId, Tmstamp):
    self.MessageID = MessageID
    self.Tag = Tag
    self.Content = Content
    self.Fieldsearchid = Fieldsearchid
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execSelectOne(self):
    result = self._connect.action('FieldsSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, MessageID, Tag):
    self.MessageID = MessageID
    self.Tag = Tag
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def querySelectAll(self):
    self._query = self._connect.query('FieldsSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFields(self._connect)
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

class DBFieldsExists(object):
  __slots__ = ['_connect', '_query', 'Count', 'MessageID', 'Tag']
  def __init__(self, connect=None):
    self._connect = connect
    self.Count = 0
    self.MessageID = 0
    self.Tag = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Count = result[0]
    self.MessageID = result[1]
    self.Tag = result[2]
  def _data(self):
    return [self.Count, self.MessageID, self.Tag]
  def _fields(self):
    return 'Count|MessageID|Tag'.split('|')
  def execExists(self):
    result = self._connect.action('FieldsExists', self._data())
    self._store(result)
  def readExists(self, MessageID, Tag):
    self.MessageID = MessageID
    self.Tag = Tag
    try:
      self.execExists()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBFieldsCount(object):
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
    result = self._connect.action('FieldsCount', self._data())
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

class DBFieldsByTag(object):
  __slots__ = ['_connect', '_query', 'InTag', 'InDateFrom', 'InDateTo', 'MessageID', 'Tag', 'Content', 'Fieldsearchid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InTag = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.MessageID = 0
    self.Tag = ''
    self.Content = ''
    self.Fieldsearchid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InTag = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.MessageID = result[3]
    self.Tag = result[4]
    self.Content = result[5]
    self.Fieldsearchid = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.InTag, self.InDateFrom, self.InDateTo, self.MessageID, self.Tag, self.Content, self.Fieldsearchid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InTag|InDateFrom|InDateTo|MessageID|Tag|Content|Fieldsearchid|USId|Tmstamp'.split('|')
  def queryByTag(self):
    self._query = self._connect.query('FieldsByTag', self._data())
  def fetchByTag(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFieldsByTag(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByTag(self):
    self._connect.cancel(self._query)
  def loadByTag(self):
    self.queryByTag()
    result = []
    while 1:
      rc, rec = self.fetchByTag()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBFieldsByContent(object):
  __slots__ = ['_connect', '_query', 'InContent', 'InDateFrom', 'InDateTo', 'MessageID', 'Tag', 'Content', 'Fieldsearchid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InContent = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.MessageID = 0
    self.Tag = ''
    self.Content = ''
    self.Fieldsearchid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InContent = result[0]
    self.InDateFrom = result[1]
    self.InDateTo = result[2]
    self.MessageID = result[3]
    self.Tag = result[4]
    self.Content = result[5]
    self.Fieldsearchid = result[6]
    self.USId = result[7]
    self.Tmstamp = result[8]
  def _data(self):
    return [self.InContent, self.InDateFrom, self.InDateTo, self.MessageID, self.Tag, self.Content, self.Fieldsearchid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InContent|InDateFrom|InDateTo|MessageID|Tag|Content|Fieldsearchid|USId|Tmstamp'.split('|')
  def queryByContent(self):
    self._query = self._connect.query('FieldsByContent', self._data())
  def fetchByContent(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFieldsByContent(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByContent(self):
    self._connect.cancel(self._query)
  def loadByContent(self):
    self.queryByContent()
    result = []
    while 1:
      rc, rec = self.fetchByContent()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBFieldsByTagContent(object):
  __slots__ = ['_connect', '_query', 'InTag', 'InContent', 'InDateFrom', 'InDateTo', 'MessageID', 'Tag', 'Content', 'Fieldsearchid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.InTag = ''
    self.InContent = ''
    self.InDateFrom = ''
    self.InDateTo = ''
    self.MessageID = 0
    self.Tag = ''
    self.Content = ''
    self.Fieldsearchid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.InTag = result[0]
    self.InContent = result[1]
    self.InDateFrom = result[2]
    self.InDateTo = result[3]
    self.MessageID = result[4]
    self.Tag = result[5]
    self.Content = result[6]
    self.Fieldsearchid = result[7]
    self.USId = result[8]
    self.Tmstamp = result[9]
  def _data(self):
    return [self.InTag, self.InContent, self.InDateFrom, self.InDateTo, self.MessageID, self.Tag, self.Content, self.Fieldsearchid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'InTag|InContent|InDateFrom|InDateTo|MessageID|Tag|Content|Fieldsearchid|USId|Tmstamp'.split('|')
  def queryByTagContent(self):
    self._query = self._connect.query('FieldsByTagContent', self._data())
  def fetchByTagContent(self):
    rc, result = self._connect.fetch(self._query)
    record = DBFieldsByTagContent(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelByTagContent(self):
    self._connect.cancel(self._query)
  def loadByTagContent(self):
    self.queryByTagContent()
    result = []
    while 1:
      rc, rec = self.fetchByTagContent()
      if rc == 0:
        break
      result.append(rec)
    return result

