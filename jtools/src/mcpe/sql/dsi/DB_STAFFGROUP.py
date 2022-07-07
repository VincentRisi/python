from INTRINSICS import *
### generated code from DBPortal ###

class DBStaffGroup(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
    self.USId = result[2]
    self.TmStamp = result[3]
  def _data(self):
    return [self.StaffId, self.GroupId, self.USId, self.TmStamp]
  def _fields(self):
    return 'StaffId|GroupId|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StaffGroupInsert', self._data())
    self._store(result)
  def runInsert(self, StaffId, GroupId, USId, TmStamp):
    self.StaffId = StaffId
    self.GroupId = GroupId
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()

class DBStaffGroupDeleteOne(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
  def _data(self):
    return [self.StaffId, self.GroupId]
  def _fields(self):
    return 'StaffId|GroupId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StaffGroupDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, StaffId, GroupId):
    self.StaffId = StaffId
    self.GroupId = GroupId
    self.execDeleteOne()

class DBStaffGroupInsertStaff(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'USId', 'StaffList']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.USId = ''
    self.StaffList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.USId = result[1]
    self.StaffList = result[2]
  def _data(self):
    return [self.GroupId, self.USId, self.StaffList]
  def _fields(self):
    return 'GroupId|USId|StaffList'.split('|')
  def execInsertStaff(self):
    result = self._connect.action('StaffGroupInsertStaff', self._data())
    self._store(result)
  def runInsertStaff(self, GroupId, USId, StaffList):
    self.GroupId = GroupId
    self.USId = USId
    self.StaffList = StaffList
    self.execInsertStaff()

class DBStaffGroupDeleteStaff(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'StaffList']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.StaffList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.StaffList = result[1]
  def _data(self):
    return [self.GroupId, self.StaffList]
  def _fields(self):
    return 'GroupId|StaffList'.split('|')
  def execDeleteStaff(self):
    result = self._connect.action('StaffGroupDeleteStaff', self._data())
    self._store(result)
  def runDeleteStaff(self, GroupId, StaffList):
    self.GroupId = GroupId
    self.StaffList = StaffList
    self.execDeleteStaff()

class DBStaffGroupInsertGroups(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'USId', 'GroupList']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.USId = ''
    self.GroupList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.USId = result[1]
    self.GroupList = result[2]
  def _data(self):
    return [self.StaffId, self.USId, self.GroupList]
  def _fields(self):
    return 'StaffId|USId|GroupList'.split('|')
  def execInsertGroups(self):
    result = self._connect.action('StaffGroupInsertGroups', self._data())
    self._store(result)
  def runInsertGroups(self, StaffId, USId, GroupList):
    self.StaffId = StaffId
    self.USId = USId
    self.GroupList = GroupList
    self.execInsertGroups()

class DBStaffGroupDeleteGroups(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupList']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupList = result[1]
  def _data(self):
    return [self.StaffId, self.GroupList]
  def _fields(self):
    return 'StaffId|GroupList'.split('|')
  def execDeleteGroups(self):
    result = self._connect.action('StaffGroupDeleteGroups', self._data())
    self._store(result)
  def runDeleteGroups(self, StaffId, GroupList):
    self.StaffId = StaffId
    self.GroupList = GroupList
    self.execDeleteGroups()

class DBStaffGroupList(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
  def _data(self):
    return [self.StaffId, self.GroupId]
  def _fields(self):
    return 'StaffId|GroupId'.split('|')
  def queryList(self):
    self._query = self._connect.query('StaffGroupList', self._data())
  def fetchList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffGroupList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelList(self):
    self._connect.cancel(self._query)
  def loadList(self):
    self.queryList()
    result = []
    while 1:
      rc, rec = self.fetchList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBStaffGroupListAll(object):
  __slots__ = ['_connect', '_query', 'StaffId', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.StaffId = ''
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.StaffId = result[0]
    self.GroupId = result[1]
  def _data(self):
    return [self.StaffId, self.GroupId]
  def _fields(self):
    return 'StaffId|GroupId'.split('|')
  def queryListAll(self):
    self._query = self._connect.query('StaffGroupListAll', self._data())
  def fetchListAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBStaffGroupListAll(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelListAll(self):
    self._connect.cancel(self._query)
  def loadListAll(self):
    self.queryListAll()
    result = []
    while 1:
      rc, rec = self.fetchListAll()
      if rc == 0:
        break
      result.append(rec)
    return result

