from io import StringIO

def make_class_name(name):
    if name[0] in 'abcdefghijklmnopqrstuvwxyz':
        return name[0].upper()+name[1:]
    return f'{name}Class'

def get_annotation(annotations, field):
    if field in annotations:
        return annotations[field]
    return make_class_name(field)

inits = {}
inits['str'] = "''"
inits['int'] = 0
inits['uuid'] = "''"
inits['bool'] = 'False'
inits['float'] = 0.0

def load_in_list(classes, annotations, class_name, class_field, annotation):
    if class_field not in classes:
       classes[class_field] = []
    if type(annotation) is dict:
        for field in annotation:
            value = annotation[field]
            classes[class_field].append(field)
            annotations[field] = value
        annotations[class_field] = f'[ {make_class_name(class_field)} ] # type: ignore'
    else:
        annotations[class_field] = f'[ {annotation} ]'

def load_in_dict(input):
    classes = {}
    annotations = {}
    for input_key in input:
        annotation = input[input_key]
        parts = input_key.split('.')
        no = len(parts)
        for i in range(len(parts) - 1):
            class_name = parts[i]
            class_field = parts[i + 1].replace('-','_')
            if class_name not in classes:
                classes[class_name] = []
            if class_field not in classes[class_name]:
                classes[class_name].append(class_field)
        if type(annotation) is list:
            load_in_list(classes, annotations, class_name, class_field, annotation[0])
        else:
            annotations[class_field] = annotation
    return classes, annotations

def build_code(code, name, classes, annotations):
    code.write(f'class {make_class_name(name)}:\n')
    fields = classes[name]
    for field in fields:
        annotation = get_annotation(annotations, field)
        code.write(f'    {field}: {annotation}\n')
    code.write('    def __init__(self):\n')
    for field in fields:
        annotation = get_annotation(annotations, field)
        if annotation in inits:
            code.write(f'        self.{field} = {inits[annotation]}\n')
        elif annotation[0] == '[':
            code.write(f'        self.{field} = []\n')
        else:
            code.write(f'        self.{field} = {annotation}()\n')
    code.write('\n')

def main():
    finreq = {}
    finreq['finReq.header.acceptLanguage'] = 'str'
    finreq['finReq.header.xNedTenantCode'] = 'str'
    finreq['finReq.header.xNedTransactionId'] = 'uuid'
    finreq['finReq.path.accountType'] = 'str'
    finreq['finReq.path.accountNumber'] = 'int'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.accountTransactionSource.sourceSystemID'] = 'int'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.additionalInformation'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.description'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.entryClassificationType.code'] = 'int'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.interBankTransactionFlag'] = 'bool'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.amount'] = 'float'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.currency'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionDate'] = 'datetime'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionDateTimeUTC'] = 'datetime'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionEffect'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionGroupId'] = 'uuid'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionId'] = 'uuid'
    finreq['finReq.body.createFinTranRq.createFinTran.accountTransaction.transactionPaymentDirectionType.code'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.externalChannel.codes'] = ['int']
    finreq['finReq.body.createFinTranRq.createFinTran.paymentType.code'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.productSystem.productSystemID'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.tranCodeSourceSystem.systemId'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferenceType.code'] ='str'
    finreq['finReq.body.createFinTranRq.createFinTran.transactionAccumulation.sourceSystem.systemId'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.sourceSystem.systemId'] = 'str'
    finreq['finReq.body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences'] = [{'preferencetypeCode': 'str','preferenceValue': 'str'}]
    finreq['finReq.body.createFinTranRq.createFinTran.clientIdentification'] = [{'clientIdentifier': 'str', 'clientTypeCode': 'str'}]

    classes, annotations = load_in_dict(finreq)
    names = []
    for key in classes:
        names.append(key)
    i = len(names)
    code = StringIO()
    code.write('from datetime import datetime\n')
    code.write('import uuid\n\n')
    while i > 0:
        i -= 1
        build_code (code, names[i], classes, annotations)
    code.seek(0)
    print(code.read())
    return 0
        

main()
