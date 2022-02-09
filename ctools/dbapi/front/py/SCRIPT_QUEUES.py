''' SCRIPT QUEUES - This is used as an addendum to config loading.
It has common routines used for running from router script and
idl2 and idl2 http usage.
The script_cntl dictionary hold information like route_plan_name, queue_name and usage
model
'''
import sys, os, os.path

class Script(object):
    __slots__ = ['name', 'route_plan_name', 'queue_name', 'depends']
    def __init__(self, name, route_plan_name, queue_name, depends):
        self.name = name 
        self.route_plan_name = route_plan_name
        self.queue_name = queue_name
        self.depends = depends
  
script_cntl = dict()
script_cntl['npup0060s'] = Script('npup0060s', '', 'DT-TOPUTTY', ['intrsys'])
script_cntl['npup0090s'] = Script('npup0090s', 'WASTE_SETTLEMENTDIARY', 'WASTESETTLEMENTDIARY', ['intrsys', 'waste'])
script_cntl['npup0100s'] = Script('npup0100s', 'TIBOS_SETTLEMENTDIARY', 'TIBOS-SETTLEMENTDIARY', ['intrsys', 'tibos'])
script_cntl['npup0121s'] = Script('npup0121s', 'WASTE_TIBOSFXFTAMVSDIARY_MAIN', 'FACTS-MVS-WASTE-DIARY', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup0240s'] = Script('npup0240s', 'ZAR_MAIN', 'ZAR-ONLINE-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0250s'] = Script('npup0250s', 'ZAR_ACB_SSV_ROUTER', 'ZAR-ACB-SSV-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0260s'] = Script('npup0260s', 'ZAR_WASTE_BATCH', 'ZAR-WASTE-BATCH-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0280s'] = Script('npup0280s', 'ZAR_ACB_UNPAIDS', 'ZAR-ACB-UNPAIDS-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0340s'] = Script('npup0340s', 'ZAR_ACB_FTP_OUT', 'ZAR-ACB-SFP', ['intrsys', 'zarpaym'])
script_cntl['npup0370s'] = Script('npup0370s', 'ZAR_ACB_1DAY_ROUTER', 'ZAR-ACB-1DAY-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0380s'] = Script('npup0380s', 'ZAR_ACB_2DAY_ROUTER', 'ZAR-ACB-2DAY-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0390s'] = Script('npup0390s', 'ZAR_ACB_5DAY_ROUTER', 'ZAR-ACB-5DAY-MTP', ['intrsys', 'zarpaym'])
script_cntl['npup0400s'] = Script('npup0400s', 'ZAR_WASTE_DIARY', 'ZAR-WASTE-ONLINE-DIARY-SFP', ['intrsys', 'zarpaym'])
script_cntl['npup0520s'] = Script('npup0520s', 'DERIV_MAIN', 'DERIV-MTP', ['intrsys'])
script_cntl['npup0530s'] = Script('npup0530s', 'DERIV_RESPONSES', 'DERIV-RFP', ['intrsys'])
script_cntl['npup0560s'] = Script('npup0560s', 'NOSTRO_CNL', 'NOSTRO-CNL-MTP', ['intrsys', 'nostro', 'swift'])
script_cntl['npup0620s'] = Script('npup0620s', 'NOSTRO_CNL_XML_RESPONSE', 'NOSTRO-CNL-RFP', ['intrsys', 'nostro'])
script_cntl['npup0704s'] = Script('npup0704s', 'TIBOSDF_MAIN', 'TIBOSDF-MTP', ['intrsys', 'tibosdf'])
script_cntl['npup0803s'] = Script('npup0803s', 'DTLITE_REPLY', 'DTLITE-RFP', ['intrsys', 'dtlite'])
script_cntl['npup0804s'] = Script('npup0804s', 'DTLITE_MAIN', 'DTLITE-MTP', ['intrsys', 'dtlite', 'wallstreet'])
script_cntl['npup0903s_NedExchangeMain'] = Script('npup0903s_NedExchangeMain', 'NEDEXCHANGE_MAIN', 'NEDEXCHANGE-MTP', ['intrsys', 'nedexchange', 'wallstreet'])
script_cntl['npup0904s_NedExchange_Reply'] = Script('npup0904s_NedExchange_Reply', 'NEDEXCHANGE_REPLY', 'NEDEXCHANGE-RFP', ['intrsys', 'nedexchange', 'wallstreet'])
script_cntl['npup1006s'] = Script('npup1006s', 'VOSTRO_NORMAL_MESSAGE', 'VOSTRO-MTP', ['intrsys', 'vostro', 'komon'])
script_cntl['npup1007s'] = Script('npup1007s', 'VOSTRO_CLS_MESSAGE', 'VOSTROCLS-MTP', ['intrsys', 'vostro', 'komon'])
script_cntl['npup1008s'] = Script('npup1008s', 'VOSTRO_REPLY', 'VOSTRO-REPLY', ['intrsys', 'vostro', 'komon'])
script_cntl['npup1011s'] = Script('npup1011s', 'VOSTROCLS_REPLY', 'VOSTROCLS-REPLY', ['intrsys', 'vostro', 'komon'])
script_cntl['npup1212s'] = Script('npup1212s', 'EXCON_MAIN', 'EXCON-MTP', ['intrsys', 'exconcharges'])
script_cntl['npup1300s'] = Script('npup1300s', 'WASTE_MVS_TIBOS_SPLIT', 'WASTE-FP', ['intrsys'])
script_cntl['npup1400s'] = Script('npup1400s', 'TIBOSFXFTA_MAIN', 'TIBOSFXFTA-MTP', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup1404s'] = Script('npup1404s', 'TIBOSFXFTA_REPLY', 'TIBOSFXFTA-RFP', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup1500s'] = Script('npup1500s', 'WACHOVIA_MAIN', 'WACHOVIA-MTP', ['intrsys', 'wachovia', 'swift', 'wallstreet'])
script_cntl['npup1551s'] = Script('npup1551s', 'EXIMBILLS_MAIN', 'EXIMBILLS-MTP', ['intrsys', 'eximbills', 'wallstreet', 'wachovia'])
script_cntl['npup1552s'] = Script('npup1552s', 'EXIMBILLS_REPLY', 'EXIMBILLS-RFP', ['intrsys', 'eximbills', 'wallstreet'])
script_cntl['npup1711s'] = Script('npup1711s', 'WSS_TIBOSFXFTA_WASTE_DIARY_MAIN', 'WSS-FACTS-WASTE-DIARY', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup1712s'] = Script('npup1712s', 'WSS_NEDPAY_WASTE_DIARY_MAIN', 'WSS-NEDPAY-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1713s'] = Script('npup1713s', 'WSS_NEDXCG_WASTE_DIARY_MAIN', 'WSS-NEDXCG-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1714s'] = Script('npup1714s', 'WSS_WACHOVIA_WASTE_DIARY_MAIN', 'WSS-WACHOVIA-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1715s'] = Script('npup1715s', 'WSS_MT103_WASTE_DIARY_MAIN', 'WSS-MT103-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1716s'] = Script('npup1716s', 'WSS_MT204_WASTE_DIARY_MAIN', 'WSS-MT204-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1717s'] = Script('npup1717s', 'WSS_GPSOTT_WASTE_DIARY_MAIN', 'GPSOTT-WASTE-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1721s'] = Script('npup1721s', 'WSS_TIBOSFXFTA_MCA_DIARY_MAIN', 'WSS-FACTS-MCA-DIARY', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup1722s'] = Script('npup1722s', 'WSS_NEDPAY_MCA_DIARY_MAIN', 'WSS-NEDPAY-MCA-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1723s'] = Script('npup1723s', 'WSS_NEDXCG_MCA_DIARY_MAIN', 'WSS-NEDXCG-MCA-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1724s'] = Script('npup1724s', 'WSS_WACHOVIA_MCA_DIARY_MAIN', 'WSS-WACHOVIA-MCA-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1727s'] = Script('npup1727s', 'WSS_GPSOTT_MCA_DIARY_MAIN', 'GPSOTT-MCA-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1731s'] = Script('npup1731s', 'WSS_TIBOSFXFTA_WALLSTREET_DIARY_MAIN', 'WSS-FACTS-WALLSTREET-DIARY', ['intrsys', 'tibosfxfta', 'wallstreet'])
script_cntl['npup1732s'] = Script('npup1732s', 'WSS_NEDPAY_WALLSTREET_DIARY_MAIN', 'WSS-NEDPAY-WALLSTREET-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1734s'] = Script('npup1734s', 'WSS_WACHOVIA_WALLSTREET_DIARY_MAIN', 'WSS-WACHOVIA-WALLSTREET-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1737s'] = Script('npup1737s', 'WSS_GPSOTT_WALLSTREET_DIARY_MAIN', 'GPSOTT-WSS-DIARY', ['intrsys', 'wallstreet'])
script_cntl['npup1751s'] = Script('npup1751s', 'WSS_MT103_MAIN', 'WSS-MT103-MTP', ['intrsys', 'wallstreet'])
script_cntl['npup1753s'] = Script('npup1753s', 'WSS_MT204_MAIN', 'WSS-MT204-MTP', ['intrsys', 'wallstreet'])
script_cntl['npup1761s'] = Script('npup1761s', 'WSS_MCAINTEREST_MAIN', 'WSS-MCAINTEREST-MTP', ['intrsys', 'wallstreet'])
script_cntl['npup1801s'] = Script('npup1801s', 'GPS_MAIN', 'GPS-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1802s'] = Script('npup1802s', 'GPS_REPLY', 'GPS-RFP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1808s'] = Script('npup1808s', 'GPS_MAIN', 'GPS-VOSTRO-PAYON-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1810s'] = Script('npup1810s', 'GPS_MAIN', 'GPS-VOSTRO-ONUS-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1812s'] = Script('npup1812s', 'GPS_MAIN', 'GPS-CLS-PAYIN-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1814s'] = Script('npup1814s', 'GPS_MAIN', 'GPS-CLS-PAYOUT-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1816s'] = Script('npup1816s', 'GPS_MAIN', 'GPS-FOREIGN-MTP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1817s'] = Script('npup1817s', 'GPS_REPLY', 'GPS-RFP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['npup1851s'] = Script('npup1851s', 'BANCS_MAIN', 'BANCS-MTP', ['intrsys', 'bancs'])
script_cntl['npup1881s'] = Script('npup1881s', 'NPS_MTWASTE_MAIN', 'NPS-MTWASTE-MTP', ['intrsys', 'nps', 'wallstreet'])
script_cntl['npup1884s'] = Script('npup1884s', 'CPL_MAIN', 'CPL-MTWASTE-MTP', ['intrsys', 'cpl', 'swift', 'waste'])
script_cntl['npup1901s'] = Script('npup1901s', 'GPSOTT_MAIN_ONE', 'GPSOTT-MTP', ['intrsys', 'gpsott', 'wallstreet'])
script_cntl['npup1920s'] = Script('npup1920s', 'SIRESS_NEDPAY_MSG_DIARY_MAIN', 'SIRESS-NEDPAY-MSG-DIARY', ['intrsys', 'siress', 'wallstreet'])
script_cntl['npup1921s'] = Script('npup1921s', 'SIRESS_GPS_MSG_DIARY_MAIN', 'SIRESS-GPS-MSG-DIARY', ['intrsys'])
script_cntl['npup1922s'] = Script('npup1922s', 'SIRESS_TIBOSDF_MSG_DIARY_MAIN', 'SIRESS-TIBOSDF-MSG-DIARY', ['intrsys', 'siress', 'wallstreet'])
script_cntl['npup1923s'] = Script('npup1923s', 'SIRESS_WACHOVIA_MSG_DIARY_MAIN', 'SIRESS-WACH-MSG-DIARY', ['intrsys', 'siress', 'wallstreet'])
script_cntl['npup2101s'] = Script('npup2101s', 'MERCURY_MAIN', 'MERCURY-MTP', ['intrsys', 'mercury', 'wallstreet'])
script_cntl['npup2102s'] = Script('npup2102s', 'MERCURY_REPLY', 'MERCURY-RFP', ['intrsys', 'mercury', 'wallstreet'])
script_cntl['npup2104s'] = Script('npup2104s', 'GPS_ECO_RESPONSE', 'SAFFY-ECO-TP', ['intrsys', 'gps', 'wallstreet'])
script_cntl['pydtester'] = Script('pydtester', 'PYD_TESTER', 'DT-TOPUTTY', ['intrsys', 'swift'])
script_cntl['mmtitest']  = Script('mmtitest',  'MMTI_MAIN', 'MMTI-TP', ['intrsys', 'mmti', 'swift'])
script_cntl['ingress3']  = Script('ingress3',  'INGRESS3_TESTS', 'DT_TOPUTTY', ['intrsys', 'ingress3'])
script_cntl['eximbills'] = Script('eximbills',  'EXIMBILLS_MAIN', 'EXIMBILLS-MTP', ['intrsys', 'eximbills', 'wallstreet', 'wachovia'])
script_cntl['npup4001s-3'] = Script('npup4001s-3',  'MCA_RESPONDER_MAIN', 'WSS-FACTS-MCA-RESP', ['intrsys', 'mca', 'wallstreet'])
script_cntl['npup4002s-3'] = Script('npup4002s-3',  'MCA_RESPONDER_MAIN', 'WSS-NEDXCG-MCA-RESP', ['intrsys', 'mca', 'wallstreet'])
script_cntl['npup4003s-3'] = Script('npup4003s-3',  'MCA_RESPONDER_MAIN', 'WSS-MT103-MCA-RESP', ['intrsys', 'mca', 'wallstreet'])
script_cntl['npup4004s-3'] = Script('npup4004s-3',  'MCA_RESPONDER_MAIN', 'WSS-MT204-MCA-RESP', ['intrsys', 'mca', 'wallstreet'])
script_cntl['npup4005s-3'] = Script('npup4005s-3',  'MCA_RESPONDER_MAIN', 'GPSOTT-MCA-RESP', ['intrsys', 'mca', 'wallstreet'])
script_cntl['npup4006s-3'] = Script('npup4006s-3',  'MCA_RESPONDER_DRIVER', 'MCA-RS-TP', ['intrsys', 'mca'])
script_cntl['mmti_frontarena']  = Script('mmti_frontarena',  'MMTI_FRONTARENA_MAIN', 'FRONTARENA-MTP', ['mmti_frontarena', 'intrsys', 'wallstreet'])
script_cntl['mmti_frontarena_reply']  = Script('mmti_frontarena_reply',  'MMTI_FRONTARENA_REPLY', 'FRONTARENA-RFP', ['mmti_frontarena', 'intrsys'])

def expand(value: str) -> str:
    while True:
        p = value.find('$(')
        if p < 0: break
        e = value.find(')', p)
        if e < 0: break
        var = value[p+2:e]
        env=os.getenv(var,'')
        value = '%s%s%s' % (value[:p], env, value[e+1:])
    if value.find('..') == 0:
        value = os.path.abspath(value)
    return value;

config_args ='''\
Sqlapi Bin File
Sql Logon String
Log File
Log Hist Ext
Log Max Size
Log Level
Log Display
No Days Back
Route Plan Name
Route Plan Type
Queue Name
Queue File Path
lock File Path
Python Temp Path
Trace
Trace File
Trace Max Size
Trace Display'''.splitlines()

def load_config(config_file):
    if os.path.exists(config_file) == False:
        return False, None
    infile = open(config_file, 'rt')
    lines = infile.readlines()
    infile.close()
    config = dict()
    START, IN_CONTROL = 0, 1
    state = START
    for line in lines:
        if line.find('[Control]') == 0:
            state = IN_CONTROL
            continue
        if state == START or line[0] != '{':
            continue
        e = line.find('}')
        key = line[1:e]
        if key in config_args:
            value = line[e+1:].replace('\n','').replace('\r','')
            config[key.replace(' ','')] = expand(value)
    return True, config

def get_script_cntl(args):
    if len(args.start_key) > 0: 
        if args.start_key in script_cntl:
            return script_cntl[args.start_key]
        print ('Script details start_key {0} not present in SCRIPT_QUEUES.script_cntl'.format(args.start_key))
    elif len(args.queue_name) > 0:
        for key in script_cntl:
            cntl = script_cntl[key]
            if cntl.queue_name == args.queue_name:
                return cntl
        print ('Script details for queue_name {0} not present in SCRIPT_QUEUES.script_cntl'.format(args.queue_name))
    return None

def get_zipped_mask():
    for path in sys.path:
       n = path.replace('\\','/').find('/pyd/')
       if n <= 0:
           continue
       print (path[:n+5], 'mask found')
       return path[:n+5]
    print ('ERROR: no pyd mask found')
    return '.'

def set_path_depends(depends, mask, addend):
    for depend in depends:
        if depend == 'intrsys':
            continue
        appender = '{0}/{1}{2}'.format(mask, depend, addend)
        sys.path.append(os.path.abspath(appender))

