# This code is generated using json_to_class from finreq.yaml
from finreq import *

finreq = Finreq()
finreq.Body.createFinTranRq.createFinTran.accountTransaction.accountTransactionSource.sourceSystemID = 618
finreq.Body.createFinTranRq.createFinTran.accountTransaction.additionalInformation = 'BAL'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.description = 'QA Automation Testing U 02 127'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.entryClassificationType.code = 900
finreq.Body.createFinTranRq.createFinTran.accountTransaction.interBankTransactionFlag = False
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.amount = 5000000.01
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.currency = 'ZAR'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDate = '2025-09-27T12:25:30.0Z'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDateTimeUTC = '2025-09-27T10:25:30.0Z'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionEffect = 'DRO'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionGroupId = '2682fb47-a132-407f-a72f-1b5ca2fe438f'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionId = 'c03c2555-31b0-434c-8143-e143dd31b0e3'
finreq.Body.createFinTranRq.createFinTran.accountTransaction.transactionPaymentDirectionType.code = 'OUT'
finreq.Body.createFinTranRq.createFinTran.clientIdentification.append(ClientIdentification())
finreq.Body.createFinTranRq.createFinTran.clientIdentification[0].clientIdTypeCode = 'PPT'
finreq.Body.createFinTranRq.createFinTran.clientIdentification[0].clientIdentifier = 'PERKS'
finreq.Body.createFinTranRq.createFinTran.clientIdentification.append(ClientIdentification())
finreq.Body.createFinTranRq.createFinTran.clientIdentification[1].clientIdTypeCode = 'CTC1'
finreq.Body.createFinTranRq.createFinTran.clientIdentification[1].clientIdentifier = 'CI1'
finreq.Body.createFinTranRq.createFinTran.externalChannel.code = 483
finreq.Body.createFinTranRq.createFinTran.paymentType.code = 'RTL'
finreq.Body.createFinTranRq.createFinTran.productSystem.productSystemID = 'GPSA'
finreq.Body.createFinTranRq.createFinTran.sourceSystem.systemId = 'GPP'
finreq.Body.createFinTranRq.createFinTran.tranCodeSourceSystem.systemId = 'GPP'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferenceType.code = 'AccumulationPreferenceTypeCode'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences.append(AccumulationPreferences())
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[0].preferenceTypeCode = 'MAX'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[0].preferenceValue = 249
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences.append(AccumulationPreferences())
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[1].preferenceTypeCode = 'PTC0'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[1].preferenceValue = 'PV0'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences.append(AccumulationPreferences())
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[2].preferenceTypeCode = 'PTC1'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences[2].preferenceValue = 'PV1'
finreq.Body.createFinTranRq.createFinTran.transactionAccumulation.sourceSystem.systemId = 'SourceSyst'
finreq.Header.Acccept_Language = 'EN'
finreq.Header.x_ned_tenant_code = 'ZANBL'
finreq.Header.x_ned_transaction_id = '622116fa-c7b4-4620-8ebe-99f544691be4'
finreq.Path.accountnumber = 1001004345
finreq.Path.accounttype = 'NCA'
