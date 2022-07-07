## Original DBPortal proforma

``` python
#use INTRINSICS
### generated code from DBPortal ###

class DBLookup(Proforma):
  def __init__(self, connect=None):
    Proforma.__init__(self, ['_connect', '_query', 'Name', 'Refs', 'Value', 'USId', 'TmStamp'])
    self._connect = connect
    self.Name = ''
    self.Refs = ''
    self.Value = ''
    self.USId = ''
    self.TmStamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
    self.Value = result[2]
    self.USId = result[3]
    self.TmStamp = result[4]
  def _data(self):
    return [self.Name, self.Refs, self.Value, self.USId, self.TmStamp]
  def _fields(self):
    return 'Name|Refs|Value|USId|TmStamp'.split('|')
  def execUpdate(self):
    result = self._connect.action('LookupUpdate', self._data())
    self._store(result)
  def runUpdate(self, Name, Refs, Value, USId, TmStamp):
    self.Name = Name
    self.Refs = Refs
    self.Value = Value
    self.USId = USId
    self.TmStamp = TmStamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('LookupSelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Name, Refs):
    self.Name = Name
    self.Refs = Refs
    try:
      self.execSelectOne()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
  def runDeleteAll(self):
    self._connect.action('LookupDeleteAll', [])
```

``` python
class DBLookupDeleteOne(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Name', 'Refs'])
    self._connect = connect
    self.Name = ''
    self.Refs = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
  def _data(self):
    return [self.Name, self.Refs]
  def _fields(self):
    return 'Name|Refs'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('LookupDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Name, Refs):
    self.Name = Name
    self.Refs = Refs
    self.execDeleteOne()
```

## si proc

``` sql
PROC SelectList  
INPUT
  Name         Char(255)
OUTPUT (1000)
  Ref(Refs)    Char(255)
  Value        Char(255)
SQLCODE
  select Ref, Value from Lookup where Name = :Name
ENDCODE
```

## dbportal

``` python
class DBLookupSelectList(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Name', 'Refs', 'Value'])
    self._connect = connect
    self.Name = ''
    self.Refs = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Refs = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Name, self.Refs, self.Value]
  def _fields(self):
    return 'Name|Refs|Value'.split('|')
  def querySelectList(self):
    self._query = self._connect.query('LookupSelectList', self._data())
  def fetchSelectList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupSelectList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectList(self):
    self._connect.cancel(self._query)
  def loadSelectList(self):
    self.querySelectList()
    result = []
    while 1:
      rc, rec = self.fetchSelectList()
      if rc == 0:
        break
      result.append(rec)
    return result
```

## LookupDBApi.py I

``` python
class DLookupSelectList():
    Name: Char(256)
    Refs: Char(256)
    Value: Char(256)
    def _make(self): return DLookupSelectList()
    __slots__ = ['Name',
        'Refs',
        'Value']
    def __init__(self):
        self.Name = ''
        self.Refs = ''
        self.Value = ''
    def _fields(self):
        return DLookupSelectList.__slots__

class LookupSelectList(DLookupSelectList):
    def execute(self, connect): # selectList
        def _get_output(_result):
            self.Refs = _result[0]
            self.Value = _result[1]
            return 2
        def _copy_input(record):
            record.Name = self.Name
        _command = f'''\
select Ref, Value from Lookup where Name = ? 
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.Name])
        records = []
        for row in cursor:
            record = LookupSelectList()
            self._copy_input(record)
            record._get_output(row)
            records.append(record)
        return records

```

## New generated DB I

``` python
class DBLookupSelectList(LookupSelectList):
    def __init__(self, connect):
        self.connect = connect
    def _data(self, record):
        result = []
        for field in self._fields():
            result.append(getattr(record, field))
        return result
```

``` python
class DBLookupGet(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Name', 'Ref', 'Value'])
    self._connect = connect
    self.Name = ''
    self.Ref = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
    self.Ref = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Name, self.Ref, self.Value]
  def _fields(self):
    return 'Name|Ref|Value'.split('|')
  def execGet(self):
    result = self._connect.action('LookupGet', self._data())
    self._store(result)
  def readGet(self, Name, Ref):
    self.Name = Name
    self.Ref = Ref
    try:
      self.execGet()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBLookupNameList(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Name'])
    self._connect = connect
    self.Name = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Name = result[0]
  def _data(self):
    return [self.Name]
  def _fields(self):
    return 'Name'.split('|')
  def queryNameList(self):
    self._query = self._connect.query('LookupNameList', self._data())
  def fetchNameList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupNameList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelNameList(self):
    self._connect.cancel(self._query)
  def loadNameList(self):
    self.queryNameList()
    result = []
    while 1:
      rc, rec = self.fetchNameList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBLookupSelectIBAN(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'Ref', 'Name', 'Value'])
    self._connect = connect
    self.Ref = ''
    self.Name = ''
    self.Value = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Ref = result[0]
    self.Name = result[1]
    self.Value = result[2]
  def _data(self):
    return [self.Ref, self.Name, self.Value]
  def _fields(self):
    return 'Ref|Name|Value'.split('|')
  def querySelectIBAN(self):
    self._query = self._connect.query('LookupSelectIBAN', self._data())
  def fetchSelectIBAN(self):
    rc, result = self._connect.fetch(self._query)
    record = DBLookupSelectIBAN(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelSelectIBAN(self):
    self._connect.cancel(self._query)
  def loadSelectIBAN(self):
    self.querySelectIBAN()
    result = []
    while 1:
      rc, rec = self.fetchSelectIBAN()
      if rc == 0:
        break
      result.append(rec)
    return result
```
