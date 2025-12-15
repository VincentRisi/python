def _build_json_attrib(attribs_dict, group_name):
    attrib = {}
    for field, value in attribs_dict[group_name]:
        attrib[field]=value
    return attrib

def _build_json(classes_dict, attribs_dict, group_name, done):
    group = {}
    if group_name in attribs_dict:
        attribs = _build_json_attrib(attribs_dict, group_name)
        group['Attributes'] = attribs
    for field_name, field_value in classes_dict[group_name]:
        sub_group_name = group_name + '.' + field_name
        if sub_group_name in classes_dict: 
            if not sub_group_name in done:
                sub_group = _build_json(classes_dict, attribs_dict, sub_group_name, done)
                group[field_name.replace('%', '_')] = sub_group
                done.append(sub_group_name)
        else:
            group[field_name.replace('%', '_')] = field_value
    return group

def _build_yaml_attrib(attribs_dict, key_name, pad):
    attrib = []
    attrib.append('%sAttributes:' % (pad))
    for key, value in attribs_dict[key_name]:
        attrib.append("%s%s: '%s'" % (pad+'  ', key, value))
    return attrib

def _build_yaml(classes_dict, attribs_dict, key_name, done, pad=''):
    entry = []
    if key_name in attribs_dict:
        attribs = _build_yaml_attrib(attribs_dict, key_name, pad)
        entry.extend(attribs)
    for field_name, field_value in classes_dict[key_name]:
        sub_key_name = key_name + '.' + field_name
        if sub_key_name in classes_dict: 
            if not sub_key_name in done:
                sub_entry = _build_yaml(classes_dict, attribs_dict, sub_key_name, done, pad+'    ')
                entry.append('%s%s:' % (pad, field_name.replace('%', '_')))
                entry.extend(sub_entry)
                done.append(sub_key_name)
        else:
            entry.append('%s%s: %s' % (pad, field_name.replace('%', '_'), field_value))
    return entry

def _check_attribs(key, name, value, attribs_dict):
    if len(name) > 0:
        if not key in attribs_dict:
            attribs_dict[key] = []
        attribs_dict[key].append((name, value))

def load_in_dicts(input):
    classes_dict = {}
    start_module = ''
    done = []
    attribs_dict = {}
    for input_key in input:
        input_value = input[input_key]
        attrib_name = ''
        n = input_key.find('/')
        if n != -1:
            attrib_name = input_key[n + 1:]
            input_key = input_key[:n]
        parts = input_key.split('.')
        if len(parts) == 1:
            _check_attribs(input_key, attrib_name, input_value, attribs_dict)
            continue
        if parts[0] != start_module:
            start_module = parts[0]
        class_key = ''
        attrib_key = ''
        for i in range(len(parts) - 1):
            class_key += parts[i]
            class_field = parts[i + 1]
            attrib_key = class_key + '.' + class_field
            if class_key not in classes_dict:
                classes_dict[class_key] = []
            if class_field not in classes_dict[class_key]:
                classes_dict[class_key].append((class_field, input_value))
            class_key += '.'
        _check_attribs(attrib_key, attrib_name, input_value, attribs_dict)
    return start_module, classes_dict, attribs_dict
 
import json
 
def dict_to_json(input_dict):
     '''
     Returns a string in json format translates %[0-9] to _[0-9]
     for duplicate tags.
     '''
     done = []
     start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
     build = _build_json(classes_dict, attribs_dict, start_name, done)
     return json.dumps(build, indent=4)

def dict_to_yaml(input_dict):
    '''
    Returns a string in json format translates %[0-9] to _[0-9]
    for duplicate tags.
    '''
    done = []
    start_name, classes_dict, attribs_dict = load_in_dicts(input_dict)
    lines = _build_yaml(classes_dict, attribs_dict, start_name, done)
    result = '%YAML 1.2\n---\n'
    for line in lines:
        result += line + '\n'
    return result

def main():
    finreq = {}
    finreq['FinReq.Header.Acccept-Language'] = 'EN'
    finreq['FinReq.Header.x-ned-tenant-code'] = 'ZANBL'
    finreq['FinReq.Header.x-ned-transaction-id'] = '622116fa-c7b4-4620-8ebe-99f544691be4'
    finreq['FinReq.Path.accounttype'] = 'NCA'
    finreq['FinReq.Path.accountnumber'] = '1001004345'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.accountTransactionSource.sourceSystemID'] = '618'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.additionalInformation'] = 'BAL'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.description'] = 'QA Automation Testing U 02 127'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.entryClassificationType.code'] = '900'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.interBankTransactionFlag'] = 'false'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.amount'] = '5000000.01'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionAmount.currency'] = 'ZAR'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDate'] = '2025-09-27T12:25:30.0Z'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionDateTimeUTC'] = '2025-09-27T10:25:30.0Z'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionEffect'] = 'DRO'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionGroupId'] = '2682fb47-a132-407f-a72f-1b5ca2fe438f'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionId'] = 'c03c2555-31b0-434c-8143-e143dd31b0e3'
    finreq['FinReq.Body.createFinTranRq.createFinTran.accountTransaction.transactionPaymentDirectionType.code'] = 'OUT'
    finreq['FinReq.Body.createFinTranRq.createFinTran.externalChannel.code'] = '483'
    finreq['FinReq.Body.createFinTranRq.createFinTran.paymentType.code'] = 'RTL'
    finreq['FinReq.Body.createFinTranRq.createFinTran.productSystem.productSystemID'] = 'GPSA'
    finreq['FinReq.Body.createFinTranRq.createFinTran.sourceSystem.systemId'] = 'GPP'
    finreq['FinReq.Body.createFinTranRq.createFinTran.tranCodeSourceSystem.systemId'] = 'GPP'
    finreq['FinReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferenceType.code'] = 'AccumulationPreferenceTypeCode'
    finreq['FinReq.Body.createFinTranRq.createFinTran.transactionAccumulation.sourceSystem.systemId'] = 'SourceSyst'

    def pref_dict(type, value):
        return {'PreferenceTypeCode': type, 'PreferenceValue': value}

    finreq['FinReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences'] = [pref_dict('MAX','249'), pref_dict('PTC0', 'PV0'), pref_dict("PTC1", 'PV1')]

    def client_dict(id, code):
        return {'ClientIdentifier': id, "ClientIdTypeCode": code}  

    finreq['FinReq.Body.createFinTranRq.createFinTran.clientIdentification'] = [client_dict('PERKS', 'PPT'), client_dict('CI1', 'CTC1')]
    finreq_json = dict_to_json(finreq)
    print('\n## json string')
    print(finreq_json)

#using the json built above
    import yaml
    finreq_dict = json.loads(finreq_json)

    finreq_yaml = yaml.dump(finreq_dict)
    print('\n## json string converted to yaml string')
    print(finreq_yaml)

# using dict_to_yaml
# finreq was loaded above

    def pref_yaml_string(type, value):
        return '{PreferenceTypeCode: %s, PreferenceValue: %s}' % (type, value)

    finreq['FinReq.Body.createFinTranRq.createFinTran.transactionAccumulation.accumulationPreferences'] = [pref_yaml_string('MAX','249'), pref_yaml_string('PTC0', 'PV0'), pref_yaml_string("PTC1", 'PV1')]

    def client_yaml_string(id, code):
        return '{ClientIdentifier: %s ,ClientIdTypeCode: %s}' % (id, code)  

    finreq['FinReq.Body.createFinTranRq.createFinTran.clientIdentification'] = [client_yaml_string('PERKS', 'PPT'), client_yaml_string('CI1', 'CTC1')]
    yaml_load_string = dict_to_yaml(finreq)
    print('\n## dict to yaml string')
    print(yaml_load_string)

if __name__ == '__main__':
    main()


'''
## json string
{
    "Header": {
        "Acccept-Language": "EN",
        "x-ned-tenant-code": "ZANBL",
        "x-ned-transaction-id": "622116fa-c7b4-4620-8ebe-99f544691be4"
    },
    "Path": {
        "accounttype": "NCA",
        "accountnumber": "1001004345"
    },
    "Body": {
        "createFinTranRq": {
            "createFinTran": {
                "accountTransaction": {
                    "accountTransactionSource": {
                        "sourceSystemID": "618"
                    },
                    "additionalInformation": "BAL",
                    "description": "QA Automation Testing U 02 127",
                    "entryClassificationType": {
                        "code": "900"
                    },
                    "interBankTransactionFlag": "false",
                    "transactionAmount": {
                        "amount": "5000000.01",
                        "currency": "ZAR"
                    },
                    "transactionDate": "2025-09-27T12:25:30.0Z",
                    "transactionDateTimeUTC": "2025-09-27T10:25:30.0Z",
                    "transactionEffect": "DRO",
                    "transactionGroupId": "2682fb47-a132-407f-a72f-1b5ca2fe438f",
                    "transactionId": "c03c2555-31b0-434c-8143-e143dd31b0e3",
                    "transactionPaymentDirectionType": {
                        "code": "OUT"
                    }
                },
                "externalChannel": {
                    "code": "483"
                },
                "paymentType": {
                    "code": "RTL"
                },
                "productSystem": {
                    "productSystemID": "GPSA"
                },
                "sourceSystem": {
                    "systemId": "GPP"
                },
                "tranCodeSourceSystem": {
                    "systemId": "GPP"
                },
                "transactionAccumulation": {
                    "accumulationPreferenceType": {
                        "code": "AccumulationPreferenceTypeCode"
                    },
                    "sourceSystem": {
                        "systemId": "SourceSyst"
                    },
                    "accumulationPreferences": [
                        {
                            "PreferenceTypeCode": "MAX",
                            "PreferenceValue": "249"
                        },
                        {
                            "PreferenceTypeCode": "PTC0",
                            "PreferenceValue": "PV0"
                        },
                        {
                            "PreferenceTypeCode": "PTC1",
                            "PreferenceValue": "PV1"
                        }
                    ]
                },
                "clientIdentification": [
                    {
                        "ClientIdentifier": "PERKS",
                        "ClientIdTypeCode": "PPT"
                    },
                    {
                        "ClientIdentifier": "CI1",
                        "ClientIdTypeCode": "CTC1"
                    }
                ]
            }
        }
    }
}

## json string converted to yaml string
Body:
  createFinTranRq:
    createFinTran:
      accountTransaction:
        accountTransactionSource:
          sourceSystemID: '618'
        additionalInformation: BAL
        description: QA Automation Testing U 02 127
        entryClassificationType:
          code: '900'
        interBankTransactionFlag: 'false'
        transactionAmount:
          amount: '5000000.01'
          currency: ZAR
        transactionDate: '2025-09-27T12:25:30.0Z'
        transactionDateTimeUTC: '2025-09-27T10:25:30.0Z'
        transactionEffect: DRO
        transactionGroupId: 2682fb47-a132-407f-a72f-1b5ca2fe438f
        transactionId: c03c2555-31b0-434c-8143-e143dd31b0e3
        transactionPaymentDirectionType:
          code: OUT
      clientIdentification:
      - ClientIdTypeCode: PPT
        ClientIdentifier: PERKS
      - ClientIdTypeCode: CTC1
        ClientIdentifier: CI1
      externalChannel:
        code: '483'
      paymentType:
        code: RTL
      productSystem:
        productSystemID: GPSA
      sourceSystem:
        systemId: GPP
      tranCodeSourceSystem:
        systemId: GPP
      transactionAccumulation:
        accumulationPreferenceType:
          code: AccumulationPreferenceTypeCode
        accumulationPreferences:
        - PreferenceTypeCode: MAX
          PreferenceValue: '249'
        - PreferenceTypeCode: PTC0
          PreferenceValue: PV0
        - PreferenceTypeCode: PTC1
          PreferenceValue: PV1
        sourceSystem:
          systemId: SourceSyst
Header:
  Acccept-Language: EN
  x-ned-tenant-code: ZANBL
  x-ned-transaction-id: 622116fa-c7b4-4620-8ebe-99f544691be4
Path:
  accountnumber: '1001004345'
  accounttype: NCA


'''