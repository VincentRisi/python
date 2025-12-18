from c2j_classes import FinReqClass, AccumulationPreference, ClientIdentification

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
