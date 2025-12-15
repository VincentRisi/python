from io import StringIO

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

finReq = FinReqClass()
finReq.Header.accept_language = 'EN'
finReq.Header.tenant_code = 'ZANBL'
finReq.Header.transaction_id = '622116fa-c7b4-4620-8ebe-99f544691be4'
finReq.Path.accounttype = 'NCA'
finReq.Path.accountnumber = '1001004345'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.accountTransactionSource.sourceSystemID = '618'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.additionalInformation = 'BAL'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.description = 'QA Automation Testing U 02 127'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.entryClassificationType.code = '900'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.interBankTransactionFlag = 'false'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.amount = '5000000.01'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.currency = 'ZAR'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDate = '2025-09-27T12:25:30.0Z'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDateTimeUTC = '2025-09-27T10:25:30.0Z'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionEffect = 'DRO'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionGroupId = '2682fb47-a132-407f-a72f-1b5ca2fe438f'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionId = 'c03c2555-31b0-434c-8143-e143dd31b0e3'
finReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionPaymentDirectionType.code = 'OUT'
finReq.Body.createFinTranRq.createFinTran.externalChannel.code = '483'
finReq.Body.createFinTranRq.createFinTran.paymentType.code = 'RTL'
finReq.Body.createFinTranRq.createFinTran.productSystem.productSystemID = 'GPSA'
finReq.Body.createFinTranRq.createFinTran.sourceSystem.systemId = 'GPP'
finReq.Body.createFinTranRq.createFinTran.tranCodeSourceSystem.systemId = 'GPP'
finReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferenceType.code = 'AccumulationPreferenceTypeCode'
finReq.Body.createFinTranRq.createFinTran.transactionAccumulation.sourceSystem.systemId = 'SourceSyst'
finReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreference.append(AccumulationPreference('MAX', '249'))
finReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreference.append(AccumulationPreference('MIN', '200'))
finReq.Body.createFinTranRq.createFinTran.clientIdentification.append(ClientIdentification())
finReq.Body.createFinTranRq.createFinTran.clientIdentification[-1].ClientIdentifier = 'PERKS'
finReq.Body.createFinTranRq.createFinTran.clientIdentification[-1].ClientIdTypeCode = 'PPT'
finReq.Body.createFinTranRq.createFinTran.clientIdentification.append(ClientIdentification())
finReq.Body.createFinTranRq.createFinTran.clientIdentification[-1].ClientIdentifier = 'PORKS'
finReq.Body.createFinTranRq.createFinTran.clientIdentification[-1].ClientIdTypeCode = 'PIE'

def expand_vars(class_var_dict, class_annotations):
    for name in class_var_dict:
        if type(class_var_dict[name]) is list:
            no = len(class_var_dict[name])
            for i in range(no):
                class_annotations = class_var_dict[name][i].__annotations__
                class_var_dict[name][i] = vars(class_var_dict[name][i])
                expand_vars(class_var_dict[name][i], class_annotations)
        x = repr(type(class_var_dict[name]))
        if '__main__.' in x:
            class_annotations = class_var_dict[name].__annotations__
            class_var_dict[name] = vars(class_var_dict[name])
            expand_vars(class_var_dict[name], class_annotations)

def class_as_dict(cls):
    class_annotations = cls.__annotations__
    cls_var_dict = vars(cls)
    expand_vars(cls_var_dict, class_annotations )
    return cls_var_dict

import yaml, json

def do_dict():
    cls_dict = class_as_dict(finReq)
    json_string = json.dumps(cls_dict, indent=2)
    yaml_string = yaml.dump(cls_dict, sort_keys=False)
    print (json_string)
    print ('----------------- yaml ---------- ')
    print (yaml_string)
 
def main():
    do_dict()

if __name__ == '__main__':
    main()



