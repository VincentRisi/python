from INTRINSICS import *
### generated code from DBPortal ###

ScriptGroupAccessTypeConst = {
  'ReadWrite' : 0, 0 : 'ReadWrite',
  'ReadOnly' : 1, 1 : 'ReadOnly',
  'None' : 2, 2 : 'None',
  }
class DBScriptGroup(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'GroupId', 'AccessType', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.GroupId = ''
    self.AccessType = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.GroupId = result[1]
    self.AccessType = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.ScriptName, self.GroupId, self.AccessType, self.USId, self.TmStamp]
  def _fields(self):
    return 'ScriptName|GroupId|AccessType|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('ScriptGroupInsert', self._data())
    self._store(result)
  def runInsert(self, ScriptName, GroupId, AccessType, USId, TmStamp):
    self.ScriptName = ScriptName
    self.GroupId = GroupId
    self.AccessType = AccessType
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('ScriptGroupUpdate', self._data())
    self._store(result)
  def runUpdate(self, ScriptName, GroupId, AccessType, USId, TmStamp):
    self.ScriptName = ScriptName
    self.GroupId = GroupId
    self.AccessType = AccessType
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def querySelectAll(self):
    self._query = self._connect.query('ScriptGroupSelectAll', self._data())
  def fetchSelectAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptGroup(self._connect)
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
  def execSelectOne(self):
    result = self._connect.action('ScriptGroupSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, ScriptName, GroupId):
    self.ScriptName = ScriptName
    self.GroupId = GroupId
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBScriptGroupDeleteOne(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'GroupId']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.GroupId = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.GroupId = result[1]
  def _data(self):
    return [self.ScriptName, self.GroupId]
  def _fields(self):
    return 'ScriptName|GroupId'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('ScriptGroupDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, ScriptName, GroupId):
    self.ScriptName = ScriptName
    self.GroupId = GroupId
    self.execDeleteOne()

class DBScriptGroupListAll(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'GroupId', 'AccessType']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.GroupId = ''
    self.AccessType = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.GroupId = result[1]
    self.AccessType = result[2]
  def _data(self):
    return [self.ScriptName, self.GroupId, self.AccessType]
  def _fields(self):
    return 'ScriptName|GroupId|AccessType'.split('|')
  def queryListAll(self):
    self._query = self._connect.query('ScriptGroupListAll', self._data())
  def fetchListAll(self):
    rc, result = self._connect.fetch(self._query)
    record = DBScriptGroupListAll(self._connect)
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

class DBScriptGroupInsertScripts(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'AccessType', 'USId', 'ScriptList']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.AccessType = 0
    self.USId = ''
    self.ScriptList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.AccessType = result[1]
    self.USId = result[2]
    self.ScriptList = result[3]
  def _data(self):
    return [self.GroupId, self.AccessType, self.USId, self.ScriptList]
  def _fields(self):
    return 'GroupId|AccessType|USId|ScriptList'.split('|')
  def execInsertScripts(self):
    result = self._connect.action('ScriptGroupInsertScripts', self._data())
    self._store(result)
  def runInsertScripts(self, GroupId, AccessType, USId, ScriptList):
    self.GroupId = GroupId
    self.AccessType = AccessType
    self.USId = USId
    self.ScriptList = ScriptList
    self.execInsertScripts()

class DBScriptGroupDeleteScripts(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'ScriptList']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.ScriptList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.ScriptList = result[1]
  def _data(self):
    return [self.GroupId, self.ScriptList]
  def _fields(self):
    return 'GroupId|ScriptList'.split('|')
  def execDeleteScripts(self):
    result = self._connect.action('ScriptGroupDeleteScripts', self._data())
    self._store(result)
  def runDeleteScripts(self, GroupId, ScriptList):
    self.GroupId = GroupId
    self.ScriptList = ScriptList
    self.execDeleteScripts()

class DBScriptGroupUpdateScriptsAccess(object):
  __slots__ = ['_connect', '_query', 'GroupId', 'AccessType', 'USId', 'ScriptList']
  def __init__(self, connect=None):
    self._connect = connect
    self.GroupId = ''
    self.AccessType = 0
    self.USId = ''
    self.ScriptList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.GroupId = result[0]
    self.AccessType = result[1]
    self.USId = result[2]
    self.ScriptList = result[3]
  def _data(self):
    return [self.GroupId, self.AccessType, self.USId, self.ScriptList]
  def _fields(self):
    return 'GroupId|AccessType|USId|ScriptList'.split('|')
  def execUpdateScriptsAccess(self):
    result = self._connect.action('ScriptGroupUpdateScriptsAccess', self._data())
    self._store(result)
  def runUpdateScriptsAccess(self, GroupId, AccessType, USId, ScriptList):
    self.GroupId = GroupId
    self.AccessType = AccessType
    self.USId = USId
    self.ScriptList = ScriptList
    self.execUpdateScriptsAccess()

class DBScriptGroupInsertGroups(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'AccessType', 'USId', 'GroupList']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.AccessType = 0
    self.USId = ''
    self.GroupList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.AccessType = result[1]
    self.USId = result[2]
    self.GroupList = result[3]
  def _data(self):
    return [self.ScriptName, self.AccessType, self.USId, self.GroupList]
  def _fields(self):
    return 'ScriptName|AccessType|USId|GroupList'.split('|')
  def execInsertGroups(self):
    result = self._connect.action('ScriptGroupInsertGroups', self._data())
    self._store(result)
  def runInsertGroups(self, ScriptName, AccessType, USId, GroupList):
    self.ScriptName = ScriptName
    self.AccessType = AccessType
    self.USId = USId
    self.GroupList = GroupList
    self.execInsertGroups()

class DBScriptGroupDeleteGroups(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'GroupList']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.GroupList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.GroupList = result[1]
  def _data(self):
    return [self.ScriptName, self.GroupList]
  def _fields(self):
    return 'ScriptName|GroupList'.split('|')
  def execDeleteGroups(self):
    result = self._connect.action('ScriptGroupDeleteGroups', self._data())
    self._store(result)
  def runDeleteGroups(self, ScriptName, GroupList):
    self.ScriptName = ScriptName
    self.GroupList = GroupList
    self.execDeleteGroups()

class DBScriptGroupUpdateGroupsAccess(object):
  __slots__ = ['_connect', '_query', 'ScriptName', 'AccessType', 'USId', 'GroupList']
  def __init__(self, connect=None):
    self._connect = connect
    self.ScriptName = ''
    self.AccessType = 0
    self.USId = ''
    self.GroupList = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ScriptName = result[0]
    self.AccessType = result[1]
    self.USId = result[2]
    self.GroupList = result[3]
  def _data(self):
    return [self.ScriptName, self.AccessType, self.USId, self.GroupList]
  def _fields(self):
    return 'ScriptName|AccessType|USId|GroupList'.split('|')
  def execUpdateGroupsAccess(self):
    result = self._connect.action('ScriptGroupUpdateGroupsAccess', self._data())
    self._store(result)
  def runUpdateGroupsAccess(self, ScriptName, AccessType, USId, GroupList):
    self.ScriptName = ScriptName
    self.AccessType = AccessType
    self.USId = USId
    self.GroupList = GroupList
    self.execUpdateGroupsAccess()

