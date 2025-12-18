class HeaderClass:
  accept_language: str
  tenant_code: str
  transaction_id: str
  def __init__(self):
    self.accept_language = ''
    self.tenant_code = ''
    self.transaction_id = ''

class PathClass:
  accounttype: str
  accountnumber: str
  def __init__(self):
    self.accounttype = ''
    self.accountnumber = ''

class AccountTransactionSource:
  sourceSystemID: str
  def __init__(self):
    sourceSystemID = ''

class EntryClassificationType:
  code: str
  def __init__(self):
    self.code = ''

class TransactionAmount:
  amount : str
  currency : str
  def __init__(self):
    amount = ''
    currency = ''

class TransactionPaymentDirectionType:
  code: str
  def __init__(self):
    self.code = '' 

class AccountTransaction:
  accountTransactionSource: AccountTransactionSource
  additionalInformation: str
  description: str 
  entryClassificationType: EntryClassificationType
  interBankTransactionFlag: str
  transactionAmount: TransactionAmount
  transactionDate: str
  transactionDateTimeUTC: str
  transactionEffect: str
  transactionGroupId: str
  transactionId: str
  transactionPaymentDirectionType: TransactionPaymentDirectionType
  def __init__(self):
    self.accountTransactionSource = AccountTransactionSource()
    self.additionalInformation = ''
    self.description = '' 
    self.entryClassificationType = EntryClassificationType()
    self.interBankTransactionFlag = ''
    self.transactionAmount = TransactionAmount()
    self.transactionDate = ''
    self.transactionDateTimeUTC = ''
    self.transactionEffect = ''
    self.transactionGroupId = ''
    self.transactionId = ''
    self.transactionPaymentDirectionType = TransactionPaymentDirectionType()

class ExternalChannel:
  code: str
  def __init__(self):
    self.code = ''    

class ProductSystem:
  productSystemID: str
  def __init__(self):
    self.productSystemID = ''

class SourceSystem:
  systemId: str
  def __init__(self):
    self.systemId = ''

class TranCodeSourceSystem:
  systemId: str
  def __init__(self):
    self.systemId = ''

class AccumulationPreferenceType:
  code : str
  def __init__(self):
    self.code = ''

class SourceSystem:
  systemId: str
  def __init__(self):
    self.systemId = ''    

class AccumulationPreference:
  PreferenceTypeCode: str
  PreferenceValue: str
  def __init__(self, code, value):
    self.PreferenceTypeCode = code
    self.PreferenceValue = value

class TransactionAccumulation:
  accumulationPreference: [AccumulationPreference] # type: ignore
  sourceSystem: SourceSystem
  accumulationPreferenceType: AccumulationPreferenceType
  def __init__(self):
    self.accumulationPreference = []
    self.sourceSystem = SourceSystem()
    self.accumulationPreferenceType = AccumulationPreferenceType()

class PaymentType:
  code: str
  def __init__(self):
    self.code = '' 

class ClientIdentification:
  ClientIdentifier: str
  ClientIdTypeCode: str
  def __init__(self):#, id, code):
    self.ClientIdentifier = ''
    self.ClientIdTypeCode = ''

class CreateFinTran:
  accountTransaction: AccountTransaction 
  externalChannel: ExternalChannel
  productSystem: ProductSystem
  sourceSystem: SourceSystem  
  tranCodeSourceSystem: TranCodeSourceSystem
  transactionAccumulation: TransactionAccumulation
  paymentType: PaymentType
  clientIdentification: [ClientIdentification] # type: ignore
  def __init__(self):
    self.accountTransaction = AccountTransaction()
    self.externalChannel = ExternalChannel()
    self.productSystem = ProductSystem()
    self.sourceSystem = SourceSystem()
    self.tranCodeSourceSystem = TranCodeSourceSystem()
    self.transactionAccumulation = TransactionAccumulation()
    self.paymentType = PaymentType()
    self.clientIdentification = []

class CreateFinTranRq:
  createFinTran: CreateFinTran
  def __init__(self):
    self.createFinTran = CreateFinTran()
    
class BodyClass:
  createFinTranRq: CreateFinTranRq
  def __init__(self):
    self.createFinTranRq = CreateFinTranRq()

class FinReqClass:
  Header: HeaderClass
  Path: PathClass
  Body: BodyClass    
  def __init__(self):
    self.Header = HeaderClass()
    self.Path = PathClass()
    self.Body = BodyClass()
