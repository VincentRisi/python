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
    sourceSystem: SourceSystem
    accumulationPreferences: [ AccumulationPreferences ] # type: ignore
    def __init__(self):
        self.accumulationPreferenceType = AccumulationPreferenceType()
        self.sourceSystem = SourceSystem()
        self.accumulationPreferences = list()

class ClientIdentification:
    clientIdentifier: str
    clientIdTypeCode: str
    def __init__(self):
        self.clientIdentifier = ''
        self.clientIdTypeCode = ''

class CreateFinTran:
    accountTransaction: AccountTransaction
    externalChannel: ExternalChannel
    paymentType: PaymentType
    productSystem: ProductSystem
    sourceSystem: SourceSystem
    tranCodeSourceSystem: TranCodeSourceSystem
    transactionAccumulation: TransactionAccumulation
    clientIdentification: [ ClientIdentification ] # type: ignore
    def __init__(self):
        self.accountTransaction = AccountTransaction()
        self.externalChannel = ExternalChannel()
        self.paymentType = PaymentType()
        self.productSystem = ProductSystem()
        self.sourceSystem = SourceSystem()
        self.tranCodeSourceSystem = TranCodeSourceSystem()
        self.transactionAccumulation = TransactionAccumulation()
        self.clientIdentification = list()

class CreateFinTranRq:
    createFinTran: CreateFinTran
    def __init__(self):
        self.createFinTran = CreateFinTran()

class HeaderClass:
    Acccept_Language: str
    x_ned_tenant_code: str
    x_ned_transaction_id: uuid
    def __init__(self):
        self.Acccept_Language = ''
        self.x_ned_tenant_code = ''
        self.x_ned_transaction_id = ''

class PathClass:
    accounttype: str
    accountnumber: int
    def __init__(self):
        self.accounttype = ''
        self.accountnumber = 0

class BodyClass:
    createFinTranRq: CreateFinTranRq
    def __init__(self):
        self.createFinTranRq = CreateFinTranRq()

class Finreq:
    Header: HeaderClass
    Path: PathClass
    Body: BodyClass
    def __init__(self):
        self.Header = HeaderClass()
        self.Path = PathClass()
        self.Body = BodyClass()

