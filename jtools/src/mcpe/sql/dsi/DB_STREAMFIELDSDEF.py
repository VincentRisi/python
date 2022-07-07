from INTRINSICS import *
### generated code from DBPortal ###

StreamFieldsDefMandatoryConst = {
  'No' : 0, 0 : 'No',
  'Optional' : 1, 1 : 'Optional',
  'Yes' : 2, 2 : 'Yes',
  }
class DBStreamFieldsDef(object):
  __slots__ = ['_connect', '_query', 'Id', 'Name', 'Descr', 'Length', 'Format', 'DefaultValue', 'Mandatory', 'USId', 'TmStamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
    self.Name = ''
    self.Descr = ''
    self.Length = 0
    self.Format = ''
    self.DefaultValue = ''
    self.Mandatory = 0
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.Name = result[1]
    self.Descr = result[2]
    self.Length = result[3]
    self.Format = result[4]
    self.DefaultValue = result[5]
    self.Mandatory = result[6]
    self.USId = result[7]
    self.TmStamp = result[8]
  def _data(self):
    return [self.Id, self.Name, self.Descr, self.Length, self.Format, self.DefaultValue, self.Mandatory, self.USId, self.TmStamp]
  def _fields(self):
    return 'Id|Name|Descr|Length|Format|DefaultValue|Mandatory|USId|TmStamp'.split('|')
  def execInsert(self):
    result = self._connect.action('StreamFieldsDefInsert', self._data())
    self._store(result)
  def runInsert(self, Id, Name, Descr, Length, Format, DefaultValue, Mandatory, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Descr = Descr
    self.Length = Length
    self.Format = Format
    self.DefaultValue = DefaultValue
    self.Mandatory = Mandatory
    self.USId = USId
    self.TmStamp = TmStamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('StreamFieldsDefUpdate', self._data())
    self._store(result)
  def runUpdate(self, Id, Name, Descr, Length, Format, DefaultValue, Mandatory, USId, TmStamp):
    self.Id = Id
    self.Name = Name
    self.Descr = Descr
    self.Length = Length
    self.Format = Format
    self.DefaultValue = DefaultValue
    self.Mandatory = Mandatory
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('StreamFieldsDefSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Id):
    self.Id = Id
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBStreamFieldsDefDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
  def _data(self):
    return [self.Id]
  def _fields(self):
    return 'Id'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('StreamFieldsDefDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Id):
    self.Id = Id
    self.execDeleteOne()

