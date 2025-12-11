from datetime import datetime
import uuid

class ClientIdentification:
    clientIdentifier: str
    clientTypeCode: str
    def __init__(self):
        self.clientIdentifier = ''
        self.clientTypeCode = ''

class AccumulationPreferences:
    preferencetypeCode: str
    preferenceValue: str
    def __init__(self):
        self.preferencetypeCode = ''
        self.preferenceValue = ''

class SourceSystem:
    systemId: str
    def __init__(self):
        self.systemId = ''

class AccumulationPreferenceType:
    code: str
    def __init__(self):
        self.code = ''

class TransactionAccumulation:
    accumulationPreferenceType: AccumulationPreferenceType
    sourceSystem: SourceSystem
    accumulationPreferences: [ AccumulationPreferences ] # type: ignore
    def __init__(self):
        self.accumulationPreferenceType = AccumulationPreferenceType()
        self.sourceSystem = SourceSystem()
        self.accumulationPreferences = []

class TranCodeSourceSystem:
    systemId: str
    def __init__(self):
        self.systemId = ''

class ProductSystem:
    productSystemID: str
    def __init__(self):
        self.productSystemID = ''

class PaymentType:
    code: str
    def __init__(self):
        self.code = ''

class Codes:
    def __init__(self):

class ExternalChannel:
    codes: [ int ] # type: ignore
    def __init__(self):
        self.codes = []

class TransactionPaymentDirectionType:
    code: str
    def __init__(self):
        self.code = ''

class TransactionAmount:
    amount: float
    currency: str
    def __init__(self):
        self.amount = 0.0
        self.currency = ''

class EntryClassificationType:
    code: str
    def __init__(self):
        self.code = ''

class AccountTransactionSource:
    sourceSystemID: int
    def __init__(self):
        self.sourceSystemID = 0

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
        self.transactionDate = datetime()
        self.transactionDateTimeUTC = datetime()
        self.transactionEffect = ''
        self.transactionGroupId = ''
        self.transactionId = ''
        self.transactionPaymentDirectionType = TransactionPaymentDirectionType()

class CreateFinTran:
    accountTransaction: AccountTransaction
    externalChannel: ExternalChannel
    paymentType: PaymentType
    productSystem: ProductSystem
    tranCodeSourceSystem: TranCodeSourceSystem
    transactionAccumulation: TransactionAccumulation
    sourceSystem: SourceSystem
    clientIdentification: [ ClientIdentification ] # type: ignore
    def __init__(self):
        self.accountTransaction = AccountTransaction()
        self.externalChannel = ExternalChannel()
        self.paymentType = PaymentType()
        self.productSystem = ProductSystem()
        self.tranCodeSourceSystem = TranCodeSourceSystem()
        self.transactionAccumulation = TransactionAccumulation()
        self.sourceSystem = SourceSystem()
        self.clientIdentification = []

class CreateFinTranRq:
    createFinTran: CreateFinTran
    def __init__(self):
        self.createFinTran = CreateFinTran()

class Body:
    createFinTranRq: CreateFinTranRq
    def __init__(self):
        self.createFinTranRq = CreateFinTranRq()

class Path:
    accountType: str
    accountNumber: int
    def __init__(self):
        self.accountType = ''
        self.accountNumber = 0

class Header:
    acceptLanguage: str
    xNedTenantCode: str
    xNedTransactionId: uuid
    def __init__(self):
        self.acceptLanguage = ''
        self.xNedTenantCode = ''
        self.xNedTransactionId = ''

class FinReq:
    header: Header
    path: Path
    body: Body
    def __init__(self):
        self.header = Header()
        self.path = Path()
        self.body = Body()
