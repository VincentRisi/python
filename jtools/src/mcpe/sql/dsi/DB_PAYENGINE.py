from INTRINSICS import *
### generated code from DBPortal ###

class DBPayEngineReqBankByName(object):
  __slots__ = ['_connect', '_query', 'Country', 'BankName', 'FinId', 'BranchId', 'Town', 'AddressLine1', 'SwiftAddress', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.BankName = ''
    self.FinId = 0
    self.BranchId = 0
    self.Town = ''
    self.AddressLine1 = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.BankName = result[1]
    self.FinId = result[2]
    self.BranchId = result[3]
    self.Town = result[4]
    self.AddressLine1 = result[5]
    self.SwiftAddress = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.Country, self.BankName, self.FinId, self.BranchId, self.Town, self.AddressLine1, self.SwiftAddress, self.NationalBankCode]
  def _fields(self):
    return 'Country|BankName|FinId|BranchId|Town|AddressLine1|SwiftAddress|NationalBankCode'.split('|')
  def queryReqBankByName(self):
    self._query = self._connect.query('PayEngineReqBankByName', self._data())
  def fetchReqBankByName(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankByName(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankByName(self):
    self._connect.cancel(self._query)
  def loadReqBankByName(self):
    self.queryReqBankByName()
    result = []
    while 1:
      rc, rec = self.fetchReqBankByName()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqBankByNameANDTown(object):
  __slots__ = ['_connect', '_query', 'Country', 'BankName', 'Town', 'FinId', 'BranchId', 'AddressLine1', 'SwiftAddress', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.BankName = ''
    self.Town = ''
    self.FinId = 0
    self.BranchId = 0
    self.AddressLine1 = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.BankName = result[1]
    self.Town = result[2]
    self.FinId = result[3]
    self.BranchId = result[4]
    self.AddressLine1 = result[5]
    self.SwiftAddress = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.Country, self.BankName, self.Town, self.FinId, self.BranchId, self.AddressLine1, self.SwiftAddress, self.NationalBankCode]
  def _fields(self):
    return 'Country|BankName|Town|FinId|BranchId|AddressLine1|SwiftAddress|NationalBankCode'.split('|')
  def queryReqBankByNameANDTown(self):
    self._query = self._connect.query('PayEngineReqBankByNameANDTown', self._data())
  def fetchReqBankByNameANDTown(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankByNameANDTown(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankByNameANDTown(self):
    self._connect.cancel(self._query)
  def loadReqBankByNameANDTown(self):
    self.queryReqBankByNameANDTown()
    result = []
    while 1:
      rc, rec = self.fetchReqBankByNameANDTown()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqBankByNameOnly(object):
  __slots__ = ['_connect', '_query', 'BankName', 'FinId', 'BranchId', 'Town', 'Country', 'AddressLine1', 'SwiftAddress', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.BankName = ''
    self.FinId = 0
    self.BranchId = 0
    self.Town = ''
    self.Country = ''
    self.AddressLine1 = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.BankName = result[0]
    self.FinId = result[1]
    self.BranchId = result[2]
    self.Town = result[3]
    self.Country = result[4]
    self.AddressLine1 = result[5]
    self.SwiftAddress = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.BankName, self.FinId, self.BranchId, self.Town, self.Country, self.AddressLine1, self.SwiftAddress, self.NationalBankCode]
  def _fields(self):
    return 'BankName|FinId|BranchId|Town|Country|AddressLine1|SwiftAddress|NationalBankCode'.split('|')
  def queryReqBankByNameOnly(self):
    self._query = self._connect.query('PayEngineReqBankByNameOnly', self._data())
  def fetchReqBankByNameOnly(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankByNameOnly(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankByNameOnly(self):
    self._connect.cancel(self._query)
  def loadReqBankByNameOnly(self):
    self.queryReqBankByNameOnly()
    result = []
    while 1:
      rc, rec = self.fetchReqBankByNameOnly()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqBankByNameOnlyANDTown(object):
  __slots__ = ['_connect', '_query', 'BankName', 'Town', 'FinId', 'BranchId', 'Country', 'AddressLine1', 'SwiftAddress', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.BankName = ''
    self.Town = ''
    self.FinId = 0
    self.BranchId = 0
    self.Country = ''
    self.AddressLine1 = ''
    self.SwiftAddress = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.BankName = result[0]
    self.Town = result[1]
    self.FinId = result[2]
    self.BranchId = result[3]
    self.Country = result[4]
    self.AddressLine1 = result[5]
    self.SwiftAddress = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.BankName, self.Town, self.FinId, self.BranchId, self.Country, self.AddressLine1, self.SwiftAddress, self.NationalBankCode]
  def _fields(self):
    return 'BankName|Town|FinId|BranchId|Country|AddressLine1|SwiftAddress|NationalBankCode'.split('|')
  def queryReqBankByNameOnlyANDTown(self):
    self._query = self._connect.query('PayEngineReqBankByNameOnlyANDTown', self._data())
  def fetchReqBankByNameOnlyANDTown(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankByNameOnlyANDTown(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankByNameOnlyANDTown(self):
    self._connect.cancel(self._query)
  def loadReqBankByNameOnlyANDTown(self):
    self.queryReqBankByNameOnlyANDTown()
    result = []
    while 1:
      rc, rec = self.fetchReqBankByNameOnlyANDTown()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqBankBySWIFTANDTown(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'Town', 'FinId', 'BranchId', 'BankName', 'Country', 'AddressLine1', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.Town = ''
    self.FinId = 0
    self.BranchId = 0
    self.BankName = ''
    self.Country = ''
    self.AddressLine1 = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.Town = result[1]
    self.FinId = result[2]
    self.BranchId = result[3]
    self.BankName = result[4]
    self.Country = result[5]
    self.AddressLine1 = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.SwiftAddress, self.Town, self.FinId, self.BranchId, self.BankName, self.Country, self.AddressLine1, self.NationalBankCode]
  def _fields(self):
    return 'SwiftAddress|Town|FinId|BranchId|BankName|Country|AddressLine1|NationalBankCode'.split('|')
  def queryReqBankBySWIFTANDTown(self):
    self._query = self._connect.query('PayEngineReqBankBySWIFTANDTown', self._data())
  def fetchReqBankBySWIFTANDTown(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankBySWIFTANDTown(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankBySWIFTANDTown(self):
    self._connect.cancel(self._query)
  def loadReqBankBySWIFTANDTown(self):
    self.queryReqBankBySWIFTANDTown()
    result = []
    while 1:
      rc, rec = self.fetchReqBankBySWIFTANDTown()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqBankBySWIFT(object):
  __slots__ = ['_connect', '_query', 'SwiftAddress', 'FinId', 'BranchId', 'BankName', 'Town', 'Country', 'AddressLine1', 'NationalBankCode']
  def __init__(self, connect=None):
    self._connect = connect
    self.SwiftAddress = ''
    self.FinId = 0
    self.BranchId = 0
    self.BankName = ''
    self.Town = ''
    self.Country = ''
    self.AddressLine1 = ''
    self.NationalBankCode = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SwiftAddress = result[0]
    self.FinId = result[1]
    self.BranchId = result[2]
    self.BankName = result[3]
    self.Town = result[4]
    self.Country = result[5]
    self.AddressLine1 = result[6]
    self.NationalBankCode = result[7]
  def _data(self):
    return [self.SwiftAddress, self.FinId, self.BranchId, self.BankName, self.Town, self.Country, self.AddressLine1, self.NationalBankCode]
  def _fields(self):
    return 'SwiftAddress|FinId|BranchId|BankName|Town|Country|AddressLine1|NationalBankCode'.split('|')
  def queryReqBankBySWIFT(self):
    self._query = self._connect.query('PayEngineReqBankBySWIFT', self._data())
  def fetchReqBankBySWIFT(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqBankBySWIFT(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqBankBySWIFT(self):
    self._connect.cancel(self._query)
  def loadReqBankBySWIFT(self):
    self.queryReqBankBySWIFT()
    result = []
    while 1:
      rc, rec = self.fetchReqBankBySWIFT()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqDraftBanks(object):
  __slots__ = ['_connect', '_query', 'CurrId', 'Country', 'FinId', 'BranchId', 'BankName', 'Town', 'SwiftAddress']
  def __init__(self, connect=None):
    self._connect = connect
    self.CurrId = ''
    self.Country = ''
    self.FinId = 0
    self.BranchId = 0
    self.BankName = ''
    self.Town = ''
    self.SwiftAddress = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CurrId = result[0]
    self.Country = result[1]
    self.FinId = result[2]
    self.BranchId = result[3]
    self.BankName = result[4]
    self.Town = result[5]
    self.SwiftAddress = result[6]
  def _data(self):
    return [self.CurrId, self.Country, self.FinId, self.BranchId, self.BankName, self.Town, self.SwiftAddress]
  def _fields(self):
    return 'CurrId|Country|FinId|BranchId|BankName|Town|SwiftAddress'.split('|')
  def queryReqDraftBanks(self):
    self._query = self._connect.query('PayEngineReqDraftBanks', self._data())
  def fetchReqDraftBanks(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqDraftBanks(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqDraftBanks(self):
    self._connect.cancel(self._query)
  def loadReqDraftBanks(self):
    self.queryReqDraftBanks()
    result = []
    while 1:
      rc, rec = self.fetchReqDraftBanks()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqCountries(object):
  __slots__ = ['_connect', '_query', 'Country']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
  def _data(self):
    return [self.Country]
  def _fields(self):
    return 'Country'.split('|')
  def queryReqCountries(self):
    self._query = self._connect.query('PayEngineReqCountries', self._data())
  def fetchReqCountries(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqCountries(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqCountries(self):
    self._connect.cancel(self._query)
  def loadReqCountries(self):
    self.queryReqCountries()
    result = []
    while 1:
      rc, rec = self.fetchReqCountries()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqPresentationCountries(object):
  __slots__ = ['_connect', '_query', 'CurrId', 'Country']
  def __init__(self, connect=None):
    self._connect = connect
    self.CurrId = ''
    self.Country = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.CurrId = result[0]
    self.Country = result[1]
  def _data(self):
    return [self.CurrId, self.Country]
  def _fields(self):
    return 'CurrId|Country'.split('|')
  def queryReqPresentationCountries(self):
    self._query = self._connect.query('PayEngineReqPresentationCountries', self._data())
  def fetchReqPresentationCountries(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqPresentationCountries(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqPresentationCountries(self):
    self._connect.cancel(self._query)
  def loadReqPresentationCountries(self):
    self.queryReqPresentationCountries()
    result = []
    while 1:
      rc, rec = self.fetchReqPresentationCountries()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqSWIFTSentDet(object):
  __slots__ = ['_connect', '_query', 'MessageID', 'StreamDescr', 'DateCreated']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageID = 0
    self.StreamDescr = ''
    self.DateCreated = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageID = result[0]
    self.StreamDescr = result[1]
    self.DateCreated = result[2]
  def _data(self):
    return [self.MessageID, self.StreamDescr, self.DateCreated]
  def _fields(self):
    return 'MessageID|StreamDescr|DateCreated'.split('|')
  def queryReqSWIFTSentDet(self):
    self._query = self._connect.query('PayEngineReqSWIFTSentDet', self._data())
  def fetchReqSWIFTSentDet(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqSWIFTSentDet(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqSWIFTSentDet(self):
    self._connect.cancel(self._query)
  def loadReqSWIFTSentDet(self):
    self.queryReqSWIFTSentDet()
    result = []
    while 1:
      rc, rec = self.fetchReqSWIFTSentDet()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqSWIFTSentDetail(object):
  __slots__ = ['_connect', '_query', 'MessageRef', 'StreamDescr', 'DateCreated', 'Id']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageRef = ''
    self.StreamDescr = ''
    self.DateCreated = ''
    self.Id = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageRef = result[0]
    self.StreamDescr = result[1]
    self.DateCreated = result[2]
    self.Id = result[3]
  def _data(self):
    return [self.MessageRef, self.StreamDescr, self.DateCreated, self.Id]
  def _fields(self):
    return 'MessageRef|StreamDescr|DateCreated|Id'.split('|')
  def queryReqSWIFTSentDetail(self):
    self._query = self._connect.query('PayEngineReqSWIFTSentDetail', self._data())
  def fetchReqSWIFTSentDetail(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqSWIFTSentDetail(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqSWIFTSentDetail(self):
    self._connect.cancel(self._query)
  def loadReqSWIFTSentDetail(self):
    self.queryReqSWIFTSentDetail()
    result = []
    while 1:
      rc, rec = self.fetchReqSWIFTSentDetail()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqSWIFTMsgData(object):
  __slots__ = ['_connect', '_query', 'Id', 'StreamDescr', 'DateCreated', 'MessageData']
  def __init__(self, connect=None):
    self._connect = connect
    self.Id = 0
    self.StreamDescr = ''
    self.DateCreated = ''
    self.MessageData = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Id = result[0]
    self.StreamDescr = result[1]
    self.DateCreated = result[2]
    self.MessageData = result[3]
  def _data(self):
    return [self.Id, self.StreamDescr, self.DateCreated, self.MessageData]
  def _fields(self):
    return 'Id|StreamDescr|DateCreated|MessageData'.split('|')
  def execReqSWIFTMsgData(self):
    result = self._connect.action('PayEngineReqSWIFTMsgData', self._data())
    self._store(result)
  def readReqSWIFTMsgData(self, Id):
    self.Id = Id
    try:
      self.execReqSWIFTMsgData()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBPayEngineReqTIBOSSettleList(object):
  __slots__ = ['_connect', '_query', 'MessageRef', 'StreamDescr', 'DateCreated', 'ID']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageRef = ''
    self.StreamDescr = ''
    self.DateCreated = ''
    self.ID = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageRef = result[0]
    self.StreamDescr = result[1]
    self.DateCreated = result[2]
    self.ID = result[3]
  def _data(self):
    return [self.MessageRef, self.StreamDescr, self.DateCreated, self.ID]
  def _fields(self):
    return 'MessageRef|StreamDescr|DateCreated|ID'.split('|')
  def queryReqTIBOSSettleList(self):
    self._query = self._connect.query('PayEngineReqTIBOSSettleList', self._data())
  def fetchReqTIBOSSettleList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqTIBOSSettleList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqTIBOSSettleList(self):
    self._connect.cancel(self._query)
  def loadReqTIBOSSettleList(self):
    self.queryReqTIBOSSettleList()
    result = []
    while 1:
      rc, rec = self.fetchReqTIBOSSettleList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetchSettleDetail(object):
  __slots__ = ['_connect', '_query', 'ID', 'SummaryData']
  def __init__(self, connect=None):
    self._connect = connect
    self.ID = 0
    self.SummaryData = 0
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.ID = result[0]
    self.SummaryData = result[1]
  def _data(self):
    return [self.ID, self.SummaryData]
  def _fields(self):
    return 'ID|SummaryData'.split('|')
  def execFetchSettleDetail(self):
    result = self._connect.action('PayEngineFetchSettleDetail', self._data())
    self._store(result)
  def readFetchSettleDetail(self, ID):
    self.ID = ID
    try:
      self.execFetchSettleDetail()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

class DBPayEngineFetch05aDetail(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'StreamId', 'MessageId', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.StreamId = 0
    self.MessageId = 0
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.StreamId = result[1]
    self.MessageId = result[2]
    self.Reference = result[3]
  def _data(self):
    return [self.DateCreated, self.StreamId, self.MessageId, self.Reference]
  def _fields(self):
    return 'DateCreated|StreamId|MessageId|Reference'.split('|')
  def queryFetch05aDetail(self):
    self._query = self._connect.query('PayEngineFetch05aDetail', self._data())
  def fetchFetch05aDetail(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetch05aDetail(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetch05aDetail(self):
    self._connect.cancel(self._query)
  def loadFetch05aDetail(self):
    self.queryFetch05aDetail()
    result = []
    while 1:
      rc, rec = self.fetchFetch05aDetail()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetch003Detail(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'StreamId', 'MessageId', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.StreamId = 0
    self.MessageId = 0
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.StreamId = result[1]
    self.MessageId = result[2]
    self.Reference = result[3]
  def _data(self):
    return [self.DateCreated, self.StreamId, self.MessageId, self.Reference]
  def _fields(self):
    return 'DateCreated|StreamId|MessageId|Reference'.split('|')
  def queryFetch003Detail(self):
    self._query = self._connect.query('PayEngineFetch003Detail', self._data())
  def fetchFetch003Detail(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetch003Detail(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetch003Detail(self):
    self._connect.cancel(self._query)
  def loadFetch003Detail(self):
    self.queryFetch003Detail()
    result = []
    while 1:
      rc, rec = self.fetchFetch003Detail()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetch08aDetail(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'StreamId', 'MessageId', 'Reference', 'QueueId', 'StreamDescr']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.StreamId = 0
    self.MessageId = 0
    self.Reference = ''
    self.QueueId = ''
    self.StreamDescr = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.StreamId = result[1]
    self.MessageId = result[2]
    self.Reference = result[3]
    self.QueueId = result[4]
    self.StreamDescr = result[5]
  def _data(self):
    return [self.DateCreated, self.StreamId, self.MessageId, self.Reference, self.QueueId, self.StreamDescr]
  def _fields(self):
    return 'DateCreated|StreamId|MessageId|Reference|QueueId|StreamDescr'.split('|')
  def queryFetch08aDetail(self):
    self._query = self._connect.query('PayEngineFetch08aDetail', self._data())
  def fetchFetch08aDetail(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetch08aDetail(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetch08aDetail(self):
    self._connect.cancel(self._query)
  def loadFetch08aDetail(self):
    self.queryFetch08aDetail()
    result = []
    while 1:
      rc, rec = self.fetchFetch08aDetail()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetch008Detail(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'StreamId', 'MessageId', 'Reference', 'QueueId', 'StreamDescr']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.StreamId = 0
    self.MessageId = 0
    self.Reference = ''
    self.QueueId = ''
    self.StreamDescr = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.StreamId = result[1]
    self.MessageId = result[2]
    self.Reference = result[3]
    self.QueueId = result[4]
    self.StreamDescr = result[5]
  def _data(self):
    return [self.DateCreated, self.StreamId, self.MessageId, self.Reference, self.QueueId, self.StreamDescr]
  def _fields(self):
    return 'DateCreated|StreamId|MessageId|Reference|QueueId|StreamDescr'.split('|')
  def queryFetch008Detail(self):
    self._query = self._connect.query('PayEngineFetch008Detail', self._data())
  def fetchFetch008Detail(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetch008Detail(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetch008Detail(self):
    self._connect.cancel(self._query)
  def loadFetch008Detail(self):
    self.queryFetch008Detail()
    result = []
    while 1:
      rc, rec = self.fetchFetch008Detail()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineReqCountryList(object):
  __slots__ = ['_connect', '_query', 'Country', 'CountryCde']
  def __init__(self, connect=None):
    self._connect = connect
    self.Country = ''
    self.CountryCde = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.Country = result[0]
    self.CountryCde = result[1]
  def _data(self):
    return [self.Country, self.CountryCde]
  def _fields(self):
    return 'Country|CountryCde'.split('|')
  def queryReqCountryList(self):
    self._query = self._connect.query('PayEngineReqCountryList', self._data())
  def fetchReqCountryList(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineReqCountryList(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelReqCountryList(self):
    self._connect.cancel(self._query)
  def loadReqCountryList(self):
    self.queryReqCountryList()
    result = []
    while 1:
      rc, rec = self.fetchReqCountryList()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetchCashManDet(object):
  __slots__ = ['_connect', '_query', 'DateCreated', 'StreamDescr', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.DateCreated = ''
    self.StreamDescr = ''
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.DateCreated = result[0]
    self.StreamDescr = result[1]
    self.Reference = result[2]
  def _data(self):
    return [self.DateCreated, self.StreamDescr, self.Reference]
  def _fields(self):
    return 'DateCreated|StreamDescr|Reference'.split('|')
  def queryFetchCashManDet(self):
    self._query = self._connect.query('PayEngineFetchCashManDet', self._data())
  def fetchFetchCashManDet(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetchCashManDet(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetchCashManDet(self):
    self._connect.cancel(self._query)
  def loadFetchCashManDet(self):
    self.queryFetchCashManDet()
    result = []
    while 1:
      rc, rec = self.fetchFetchCashManDet()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetchValueCashMan(object):
  __slots__ = ['_connect', '_query', 'MessageRef1', 'MessageRef2', 'MessageRef3', 'MessageRef4', 'MessageRef5', 'MessageRef6', 'MessageRef7', 'MessageRef8', 'MessageRef9', 'MessageRef10', 'MessageRef11', 'MessageRef12', 'MessageRef13', 'MessageRef14', 'MessageRef15', 'MessageRef16', 'MessageRef17', 'MessageRef18', 'MessageRef19', 'MessageRef20', 'MessageRef21', 'MessageRef22', 'MessageRef23', 'MessageRef24', 'MessageRef25', 'MessageRef26', 'MessageRef27', 'MessageRef28', 'MessageRef29', 'MessageRef30', 'MessageRef31', 'MessageRef32', 'MessageRef33', 'MessageRef34', 'MessageRef35', 'MessageRef36', 'MessageRef37', 'MessageRef38', 'MessageRef39', 'MessageRef40', 'StreamDescr', 'Reference']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageRef1 = ''
    self.MessageRef2 = ''
    self.MessageRef3 = ''
    self.MessageRef4 = ''
    self.MessageRef5 = ''
    self.MessageRef6 = ''
    self.MessageRef7 = ''
    self.MessageRef8 = ''
    self.MessageRef9 = ''
    self.MessageRef10 = ''
    self.MessageRef11 = ''
    self.MessageRef12 = ''
    self.MessageRef13 = ''
    self.MessageRef14 = ''
    self.MessageRef15 = ''
    self.MessageRef16 = ''
    self.MessageRef17 = ''
    self.MessageRef18 = ''
    self.MessageRef19 = ''
    self.MessageRef20 = ''
    self.MessageRef21 = ''
    self.MessageRef22 = ''
    self.MessageRef23 = ''
    self.MessageRef24 = ''
    self.MessageRef25 = ''
    self.MessageRef26 = ''
    self.MessageRef27 = ''
    self.MessageRef28 = ''
    self.MessageRef29 = ''
    self.MessageRef30 = ''
    self.MessageRef31 = ''
    self.MessageRef32 = ''
    self.MessageRef33 = ''
    self.MessageRef34 = ''
    self.MessageRef35 = ''
    self.MessageRef36 = ''
    self.MessageRef37 = ''
    self.MessageRef38 = ''
    self.MessageRef39 = ''
    self.MessageRef40 = ''
    self.StreamDescr = ''
    self.Reference = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageRef1 = result[0]
    self.MessageRef2 = result[1]
    self.MessageRef3 = result[2]
    self.MessageRef4 = result[3]
    self.MessageRef5 = result[4]
    self.MessageRef6 = result[5]
    self.MessageRef7 = result[6]
    self.MessageRef8 = result[7]
    self.MessageRef9 = result[8]
    self.MessageRef10 = result[9]
    self.MessageRef11 = result[10]
    self.MessageRef12 = result[11]
    self.MessageRef13 = result[12]
    self.MessageRef14 = result[13]
    self.MessageRef15 = result[14]
    self.MessageRef16 = result[15]
    self.MessageRef17 = result[16]
    self.MessageRef18 = result[17]
    self.MessageRef19 = result[18]
    self.MessageRef20 = result[19]
    self.MessageRef21 = result[20]
    self.MessageRef22 = result[21]
    self.MessageRef23 = result[22]
    self.MessageRef24 = result[23]
    self.MessageRef25 = result[24]
    self.MessageRef26 = result[25]
    self.MessageRef27 = result[26]
    self.MessageRef28 = result[27]
    self.MessageRef29 = result[28]
    self.MessageRef30 = result[29]
    self.MessageRef31 = result[30]
    self.MessageRef32 = result[31]
    self.MessageRef33 = result[32]
    self.MessageRef34 = result[33]
    self.MessageRef35 = result[34]
    self.MessageRef36 = result[35]
    self.MessageRef37 = result[36]
    self.MessageRef38 = result[37]
    self.MessageRef39 = result[38]
    self.MessageRef40 = result[39]
    self.StreamDescr = result[40]
    self.Reference = result[41]
  def _data(self):
    return [self.MessageRef1, self.MessageRef2, self.MessageRef3, self.MessageRef4, self.MessageRef5, self.MessageRef6, self.MessageRef7, self.MessageRef8, self.MessageRef9, self.MessageRef10, self.MessageRef11, self.MessageRef12, self.MessageRef13, self.MessageRef14, self.MessageRef15, self.MessageRef16, self.MessageRef17, self.MessageRef18, self.MessageRef19, self.MessageRef20, self.MessageRef21, self.MessageRef22, self.MessageRef23, self.MessageRef24, self.MessageRef25, self.MessageRef26, self.MessageRef27, self.MessageRef28, self.MessageRef29, self.MessageRef30, self.MessageRef31, self.MessageRef32, self.MessageRef33, self.MessageRef34, self.MessageRef35, self.MessageRef36, self.MessageRef37, self.MessageRef38, self.MessageRef39, self.MessageRef40, self.StreamDescr, self.Reference]
  def _fields(self):
    return 'MessageRef1|MessageRef2|MessageRef3|MessageRef4|MessageRef5|MessageRef6|MessageRef7|MessageRef8|MessageRef9|MessageRef10|MessageRef11|MessageRef12|MessageRef13|MessageRef14|MessageRef15|MessageRef16|MessageRef17|MessageRef18|MessageRef19|MessageRef20|MessageRef21|MessageRef22|MessageRef23|MessageRef24|MessageRef25|MessageRef26|MessageRef27|MessageRef28|MessageRef29|MessageRef30|MessageRef31|MessageRef32|MessageRef33|MessageRef34|MessageRef35|MessageRef36|MessageRef37|MessageRef38|MessageRef39|MessageRef40|StreamDescr|Reference'.split('|')
  def queryFetchValueCashMan(self):
    self._query = self._connect.query('PayEngineFetchValueCashMan', self._data())
  def fetchFetchValueCashMan(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetchValueCashMan(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetchValueCashMan(self):
    self._connect.cancel(self._query)
  def loadFetchValueCashMan(self):
    self.queryFetchValueCashMan()
    result = []
    while 1:
      rc, rec = self.fetchFetchValueCashMan()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetchNOSTROSWIFTAddr(object):
  __slots__ = ['_connect', '_query', 'SWIFTAddr']
  def __init__(self, connect=None):
    self._connect = connect
    self.SWIFTAddr = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.SWIFTAddr = result[0]
  def _data(self):
    return [self.SWIFTAddr]
  def _fields(self):
    return 'SWIFTAddr'.split('|')
  def queryFetchNOSTROSWIFTAddr(self):
    self._query = self._connect.query('PayEngineFetchNOSTROSWIFTAddr', self._data())
  def fetchFetchNOSTROSWIFTAddr(self):
    rc, result = self._connect.fetch(self._query)
    record = DBPayEngineFetchNOSTROSWIFTAddr(self._connect)
    if rc == 1:
      record._store(result)
    return rc, record
  def cancelFetchNOSTROSWIFTAddr(self):
    self._connect.cancel(self._query)
  def loadFetchNOSTROSWIFTAddr(self):
    self.queryFetchNOSTROSWIFTAddr()
    result = []
    while 1:
      rc, rec = self.fetchFetchNOSTROSWIFTAddr()
      if rc == 0:
        break
      result.append(rec)
    return result

class DBPayEngineFetchFORCashUpdate(object):
  __slots__ = ['_connect', '_query', 'MessageRef', 'StreamDescr']
  def __init__(self, connect=None):
    self._connect = connect
    self.MessageRef = ''
    self.StreamDescr = ''
  def set_connect(self, connect):
    self._connect = connect
  def _store(self, result):
    self.MessageRef = result[0]
    self.StreamDescr = result[1]
  def _data(self):
    return [self.MessageRef, self.StreamDescr]
  def _fields(self):
    return 'MessageRef|StreamDescr'.split('|')
  def execFetchFORCashUpdate(self):
    result = self._connect.action('PayEngineFetchFORCashUpdate', self._data())
    self._store(result)
  def readFetchFORCashUpdate(self, MessageRef):
    self.MessageRef = MessageRef
    try:
      self.execFetchFORCashUpdate()
      result = 1
    except DBError as x:
      if x.ociErr == 1403:
        result = 0
      else:
        raise
    return result

