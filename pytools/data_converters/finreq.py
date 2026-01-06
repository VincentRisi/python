# This code is generated using json_to_class from finreq.yaml
from datetime import datetime
import uuid

class AccountTransactionSource:
    sourceSystemID: int
    def __init__(self):
        self.sourceSystemID = 0

class EntryClassificationType:
    code: str
    def __init__(self):
        self.code = ''

class TransactionAmount:
    amount: float
    currency: str
    def __init__(self):
        self.amount = 0.0
        self.currency = ''

class TransactionPaymentDirectionType:
    code: str
    def __init__(self):
        self.code = ''

class AccumulationPreferenceType:
    code: str
    def __init__(self):
        self.code = ''

class AccumulationPreferences:
    preferenceTypeCode: str
    preferenceValue: int
    def __init__(self):
        self.preferenceTypeCode = ''
        self.preferenceValue = 0

class AccountTransaction:
    accountTransactionSource: AccountTransactionSource
    additionalInformation: str
    description: str
    entryClassificationType: EntryClassificationType
    interBankTransactionFlag: bool
    transactionAmount: TransactionAmount
    transactionDate: datetime
    transactionDateTimeUTC: datetime
    transactionEffect: str
    transactionGroupId: uuid
    transactionId: uuid
    transactionPaymentDirectionType: TransactionPaymentDirectionType
    def __init__(self):
        self.accountTransactionSource = AccountTransactionSource()
        self.additionalInformation = ''
        self.description = ''
        self.entryClassificationType = EntryClassificationType()
        self.interBankTransactionFlag = False
        self.transactionAmount = TransactionAmount()
        self.transactionDate = datetime.now()
        self.transactionDateTimeUTC = datetime.now()
        self.transactionEffect = ''
        self.transactionGroupId = ''
        self.transactionId = ''
        self.transactionPaymentDirectionType = TransactionPaymentDirectionType()

class ClientIdentification:
    clientIdTypeCode: str
    clientIdentifier: str
    def __init__(self):
        self.clientIdTypeCode = ''
        self.clientIdentifier = ''

class ExternalChannel:
    code: str
    def __init__(self):
        self.code = ''

class PaymentType:
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

class TransactionAccumulation:
    accumulationPreferenceType: AccumulationPreferenceType
    accumulationPreferences: list[AccumulationPreferences]
    sourceSystem: SourceSystem
    def __init__(self):
        self.accumulationPreferenceType = AccumulationPreferenceType()
        self.accumulationPreferences = list[AccumulationPreferences]()
        self.sourceSystem = SourceSystem()

class CreateFinTran:
    accountTransaction: AccountTransaction
    clientIdentification: list[ClientIdentification]
    externalChannel: ExternalChannel
    paymentType: PaymentType
    productSystem: ProductSystem
    sourceSystem: SourceSystem
    tranCodeSourceSystem: TranCodeSourceSystem
    transactionAccumulation: TransactionAccumulation
    def __init__(self):
        self.accountTransaction = AccountTransaction()
        self.clientIdentification = list[ClientIdentification]()
        self.externalChannel = ExternalChannel()
        self.paymentType = PaymentType()
        self.productSystem = ProductSystem()
        self.sourceSystem = SourceSystem()
        self.tranCodeSourceSystem = TranCodeSourceSystem()
        self.transactionAccumulation = TransactionAccumulation()

class CreateFinTranRq:
    createFinTran: CreateFinTran
    def __init__(self):
        self.createFinTran = CreateFinTran()

class BodyClass:
    createFinTranRq: CreateFinTranRq
    def __init__(self):
        self.createFinTranRq = CreateFinTranRq()

class HeaderClass:
    Acccept_Language: str
    x_ned_tenant_code: str
    x_ned_transaction_id: uuid
    def __init__(self):
        self.Acccept_Language = ''
        self.x_ned_tenant_code = ''
        self.x_ned_transaction_id = ''
        self._renames = {'Acccept_Language': 'Acccept-Language', 'x_ned_tenant_code': 'x-ned-tenant-code', 'x_ned_transaction_id': 'x-ned-transaction-id'}

class PathClass:
    accountnumber: int
    accounttype: str
    def __init__(self):
        self.accountnumber = 0
        self.accounttype = ''

class Finreq:
    Body: BodyClass
    Header: HeaderClass
    Path: PathClass
    def __init__(self):
        self.Body = BodyClass()
        self.Header = HeaderClass()
        self.Path = PathClass()

