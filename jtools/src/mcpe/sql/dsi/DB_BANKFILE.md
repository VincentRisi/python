## DBPortal proforma style

``` python
#use INTRINSICS
### generated code from DBPortal ###

BankFileStatusConst = {
  'Active' : 0, 0 : 'Active',
  'Inactive' : 1, 1 : 'Inactive',
  'MarkForDelete' : 2, 2 : 'MarkForDelete',
  'ConfirmDelete' : 3, 3 : 'ConfirmDelete',
  }

class DBBankFileGetAuthKeys(Proforma):
  def __init__(self, connect):
    Proforma.__init__(self, ['_connect', '_query', 'SwiftAddress', 'AuthKeysExchd'])
    self._connect = connect
    self.SwiftAddress = ''
    self.AuthKeysExchd = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.AuthKeysExchd = result[1]
  def _data(self):
    return [self.SwiftAddress, self.AuthKeysExchd]
  def _fields(self):
    return 'SwiftAddress|AuthKeysExchd'.split('|')
  def execGetAuthKeys(self):
    result = self._connect.action('BankFileGetAuthKeys', self._data())
    self._store(result)
  def readGetAuthKeys(self, SwiftAddress):
    self.SwiftAddress = SwiftAddress
    try:
      self.execGetAuthKeys()
      result = 1
    except DBError, x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result
```

## --- BankFileDBApi.py

``` python
class DBankFileGetAuthKeys():
    SwiftAddress: Char(12)
    AuthKeysExchd: Char(2)
    def _make(self): return DBankFileGetAuthKeys()
    __slots__ = ['SwiftAddress',
        'AuthKeysExchd']
    def __init__(self):
        self.SwiftAddress = ''
        self.AuthKeysExchd = ''
    def _fields(self):
        return DBankFileGetAuthKeys.__slots__

class BankFileGetAuthKeys(DBankFileGetAuthKeys):
    def execute(self, connect): # getAuthKeys
        def _get_output(_result):
            self.AuthKeysExchd = _result[0]
            return 1
        def _copy_input(record):
            record.SwiftAddress = self.SwiftAddress
        _command = f'''\
Select 
AuthKeysExchd 
FROM 
Bankfile 
WHERE 
SwiftAddress = ? 
'''
        cursor = connect.cursor()
        cursor.execute(_command, [
            self.SwiftAddress])
        record = BankFileGetAuthKeys()
        self._copy_input(record)
        result = cursor.fetchone()
        if result == None:
            return None
        record._get_output(result)
        return record

```

## proc

``` sql
PROC GetAuthKeys 
INPUT
   SwiftAddress      char(11)
OUTPUT (single)
  AuthKeysExchd    Char(1)
sqlcode
   Select
   AuthKeysExchd
   FROM
      Bankfile
   WHERE
      SwiftAddress = :SwiftAddress
ENDCODE
```

## replacement DBBnbakFile.py

``` python

class DBBankFileGetAuthKeys(BankFileGetAuthKeys):
    def __init__(self, connect):
        self.connect = connect
    def _data(self):
        result = []
        for field in self._fields():
            result.append(getattr(self, field))
        return result
```