from INTRINSICS import *
### generated code from DBPortal ###

class DBCountryCurrency(object):
  __slots__ = ['_connect', '_query', 'Countryid', 'Currencyid', 'USId', 'Tmstamp']
  def __init__(self, connect=None):
    self._connect = connect
    self.Countryid = ''
    self.Currencyid = ''
    self.USId = ''
    self.Tmstamp = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Countryid = result[0]
    self.Currencyid = result[1]
    self.USId = result[2]
    self.Tmstamp = result[3]
  def _data(self):
    return [self.Countryid, self.Currencyid, self.USId, self.Tmstamp]
  def _fields(self):
    return 'Countryid|Currencyid|USId|Tmstamp'.split('|')
  def execInsert(self):
    result = self._connect.action('CountryCurrencyInsert', self._data())
    self._store(result)
  def runInsert(self, Countryid, Currencyid, USId, Tmstamp):
    self.Countryid = Countryid
    self.Currencyid = Currencyid
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execInsert()
  def execUpdate(self):
    result = self._connect.action('CountryCurrencyUpdate', self._data())
    self._store(result)
  def runUpdate(self, Countryid, Currencyid, USId, Tmstamp):
    self.Countryid = Countryid
    self.Currencyid = Currencyid
    self.USId = USId
    self.Tmstamp = Tmstamp
    self.execUpdate()
  def execSelectOne(self):
    result = self._connect.action('CountryCurrencySelectOne', self._data())
    self._store(result)
  def readSelectOne(self, Countryid, Currencyid):
    self.Countryid = Countryid
    self.Currencyid = Currencyid
    try:
      self.execSelectOne()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBCountryCurrencyDeleteOne(object):
  __slots__ = ['_connect', '_query', 'Countryid', 'Currencyid']
  def __init__(self, connect=None):
    self._connect = connect
    self.Countryid = ''
    self.Currencyid = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Countryid = result[0]
    self.Currencyid = result[1]
  def _data(self):
    return [self.Countryid, self.Currencyid]
  def _fields(self):
    return 'Countryid|Currencyid'.split('|')
  def execDeleteOne(self):
    result = self._connect.action('CountryCurrencyDeleteOne', self._data())
    self._store(result)
  def runDeleteOne(self, Countryid, Currencyid):
    self.Countryid = Countryid
    self.Currencyid = Currencyid
    self.execDeleteOne()

