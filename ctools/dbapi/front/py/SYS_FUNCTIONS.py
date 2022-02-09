##---------------------------------------------
## Replaces SYS_IDE_FUNCTION and SYS_FUNCTIONS
## In python version 3
##---------------------------------------------
from INTRINSICS import *

#
# Get interface data function
#
def GetMessageId():
    return getInterfaceData()[0]

def GetRelatedMessageId():
    return getInterfaceData()[1]

def GetResponseQueue():
    return getInterfaceData()[2]

def GetEventQueue():
    return getInterfaceData()[3]

def GetServiceQueue():
    return getInterfaceData()[4]

def GetToQueue():
    return getInterfaceData()[5]

def GetPriority():
    return getInterfaceData()[6]

def GetReferrance():
    return getInterfaceData()[7]

def result(rc):
    if rc > 0:
        return 'OK'
    else:
        return 'FAILED'

import DB_MESSAGE as message
def getRelatedMessage(messageId):
    printCaller()
    msg = message.DBMessage(connect)
    rc = msg.readSelectOne(messageId)
    if rc != 1:
        if puttyTrace == 1:
            print('related message not found %s' % (messageId))
        return None
    rc, decompLen, msg.MessageData = zdecompress(msg.MessageData,msg.MessageLen)
    return msg

def checkDuplicatMessage(QueueID, Referrance):
    printCaller()
    msg = message.DBMessageDuplicateCnt(connect)
    rc = msg.readDuplicateCnt(Referrance, QueueID)
    if msg.Cnt > 1:
       rc = 1
       if puttyTrace == 1:
          print('checkDuplicatMessage(%s, %s) = %s' % (repr(QueueID), repr(Referrance), result(rc)))
    else:
       rc = 0

    return rc

import DB_STREAMS as streams
import DB_RESPONSE as response
def getStreamResponses():
    rec = streams.DBStreamsByMessageIDData(connect)
    rec.InMessageId = getInterfaceData()[1]
    print(getInterfaceData())
    streamList = rec.loadByMessageIDData()
    dict = {}
    dict['STREAMRESPONSES/COUNT'] = repr(len(streamList))
    strCount = 0;
    for i in streamList:
        rc, decompLen, i.MessageData = zdecompress(i.MessageData,i.MessageLen)
        rec = response.DBResponseByStreamID(connect)
        rec.InStreamID = i.Id
        i.__dict__['RESPONSES'] = rec.loadByStreamID() #Can't just assign a new member, The proforma class would claim it is not an existing member
        key = 'STREAMRESPONSES.STREAM'+repr(strCount)
        dict[key+'/ID'] = repr(i.Id)
        dict[key+'/QUEUEID'] = i.QueueId
        dict[key+'/REF'] = i.StreamRef
        dict[key+'/TYPE'] = i.StreamType
        dict[key+'/DESCR'] = i.StreamDescr
        dict[key+'/STATUS'] = repr(i.Status)
        dict[key+'/DATA'] = i.MessageData
        dict[key+'/DATECREATED'] = i.DateCreated
        dict[key+'/TIMESTAMP'] = i.TmStamp
        dict[key+'/RESPONSECOUNT'] = repr(len(i.Responses))
#     print 'StreamId',i.Id,':',i.MessageData
        rspCount = 0
        for r in i.Responses:
            rc, decompLen, r.MessageData = zdecompress(r.MessageData,r.MessageLen)
            respkey = key+'.RESPONSE'+repr(rspCount)
            dict[respkey+'/ID'] = repr(r.Id)
            dict[respkey+'/QUEUEID'] = r.QueueId
            dict[respkey+'/STATUS'] = repr(r.Status)
            dict[respkey+'/DATA'] = r.MessageData
            dict[key+'/DATECREATED'] = r.DateCreated
            dict[key+'/TIMESTAMP'] = r.TmStamp
            rspCount += 1
        strCount += 1
#       print '  Response',r.Id,':',r.MessageData

    rc = len(streamList)
    if puttyTrace == 1:
        print('getStreamResponses() = %s %s' % (repr(len(streamList))+' Stream(s)', result(rc)))
    return rc,xmlbuild(dict),streamList

def updateStreamRef(newRef):
    rec = streams.DBStreamsUpdateStreamRef(connect)
    id = getInterfaceData()[0]
    rec.runUpdateStreamRef(id,newRef,'SYSFUNC')
    rc = 1
    if puttyTrace == 1:
        print('updateStreamRef(%s) = Updated streamref id %d %s' % (repr(newRef), id, result(rc)))
    return rc


import DB_SUMMARY as summary
def summaryByDateAndQueueId(date,queueId):
    rec = summary.DBSummaryByDayAndQueueId(connect)
    rec.InDate = date
    rec.QueueId = queueId
    list = rec.loadByDayAndQueueId()
    rc, value = len(list)>0, list
    if puttyTrace == 1:
        print('summaryByDateAndQueueId(%s, %s) = %s' % (repr(date), repr(queueId), result(rc)))
    return rc, value


CardBinFileDictionary = {}
def loadCardBinFile():
    f = open(lookup('CARD','BINFILEPATH')[1])
    CardBinFileDictionary.clear()
    for i in f.readlines():
        CardBinFileDictionary[i[:6]] = i[9:12]

#Returns a three letter string, or empty string if not found
#s[0] - Y means its in CAMS
#s[1:2] - 'AV' or 'NV'
def cardBinFile(cardNo):
    if len(CardBinFileDictionary) == 0:
        loadCardBinFile()
    try:
        return CardBinFileDictionary[cardNo]
    except KeyError:
        return ''


import DB_PERSISTENT as persistent
def getPersistent(name, reference):
    rec = persistent.DBPersistentGetForUpdate(connect)
    rc = rec.readGetForUpdate(name, reference)
    if (rc == 0):
        value = ""
    else:
        value = rec.Value
    if puttyTrace == 1:
        print("getPersistent(%s, %s) = %s %s" % (repr(name),repr(reference),repr(value),result(rc)))
    if rec.Type == persistent.PersistentTypeConst['StoreInteger']:
        return rc,int(value)
    elif rec.Type == persistent.PersistentTypeConst['StoreDouble']:
        return rc,float(value)
    else:
        return rc,value

import types
def setPersistent(name, reference, value):
    rec = persistent.DBPersistent(connect)
    if type(value) is int: # or type(value) is int:
        tpe = persistent.PersistentTypeConst['StoreInteger']
    elif type(value) is float:
        tpe = persistent.PersistentTypeConst['StoreDouble']
    else:
        tpe = persistent.PersistentTypeConst['StoreString']
    try:
        rec.runInsert(name,reference,tpe,str(value),'SYS_FUNCTIONS',sysdate())
        if puttyTrace == 1:
            print("setPersistent(%s, %s, %s) Inserted as %s" % (repr(name),repr(reference),repr(value),persistent.PersistentTypeConst[tpe]))
    except DBError as x:
        rec.runUpdate(name,reference,tpe,str(value),'SYS_FUNCTIONS',sysdate())
        if puttyTrace == 1:
            print("setPersistent(%s, %s, %s) Updated as %s" % (repr(name),repr(reference),repr(value),persistent.PersistentTypeConst[tpe]))

import DB_LOOKUP as dblookup
def lookup(name, reference):
    rec = dblookup.DBLookupGet(connect)
    rc = rec.readGet(name.upper(), reference.upper())
    if (rc == 0):
        value = ""
    else:
        value = rec.Value
    if puttyTrace == 1:
        print("lookup(%s, %s) = %s %s" % (repr(name),repr(reference),repr(value),result(rc)))
    return rc, value

import DB_DATES as dbdates
def rundate(delim=''):
    rec = dbdates.DBDatesGet(connect)
    rc = rec.readGet(dbdates.DatesDateTypeConst['RunDate'])
    if (rc == 0):
        value = ""
    elif len(delim) == 0:
        value = rec.Value
    elif len(delim) > 1:
        value = rec.Value[0:4]+delim[0]+rec.Value[4:6]+delim[0]+rec.Value[6:8]+' '+rec.Value[8:10]+delim[1]+rec.Value[10:12]+delim[1]+rec.Value[12:14]
    elif delim[0] == ':':
        value = rec.Value[8:10]+':'+rec.Value[10:12]+':'+rec.Value[12:14]
    else:
        value = rec.Value[0:4]+delim[0]+rec.Value[4:6]+delim[0]+rec.Value[6:8]
    if puttyTrace == 1:
        print("rundate(%s) = %s" % (repr(delim), repr(value)))
    return value

import DB_BANKACCPROC as dbbankacc
def fromLT(LT, currency, accType):
    rec = dbbankacc.DBBankAccountFromLT(connect)
    rc = rec.readFromLT(LT, currency, accType)
    if (rc == 0):
        value = ""
    else:
        value = rec.AccountNo
    if puttyTrace == 1:
        print("fromLT(%s, %s, %s) = %s %s" % (repr(LT),repr(currency),repr(accType),repr(value),result(rc)))
    return rc, value

import DB_ALMANACBANK as dbAlmanacBank
class AlmanacBank:
    def __init__(self, finId, branchId):
        self.finId = finId
        self.branchId = branchId
        rec = dbAlmanacBank.DBAlmanacBankGet(connect)
        self.rc = rec.readGet(finId, branchId)
        if (self.rc == 0):
            self.bankName = ''
            self.town = ''
            self.country = ''
            self.swiftAddress = ''
            self.nationalBankCode = ''
            self.status = 0
        else:
            self.bankName = rec.BankName
            self.town = rec.Town
            self.country = rec.Country
            self.swiftAddress = rec.SwiftAddress
            self.nationalBankCode = rec.NationalBankCode
            self.status = rec.Status
        if puttyTrace == 1:
            print('AlmanacBank(%d,%d) = %s %s' % (finId, branchId, repr(self.__dict__), result(self.rc)))

def finIdBankCodeCheck(finId,bankCode):
    rec = dbAlmanacBank.DBAlmanacBankFinIdBankCodeCheck(connect)
    rc = rec.readFinIdBankCodeCheck(finId, bankCode)
    if (rc == 0):
        value = 0
    else:
        value = rec.MatchCount
    if puttyTrace == 1:
        print('finIdBankCodeCheck(%d, %s) = %s %s' % (finId, repr(bankCode), value, result(rc)))
    return rc, value

def almanacSwiftLookup(swift, currency):
    rec = dbAlmanacBank.DBAlmanacBankSwiftLookup(connect)
    rec.SwiftAddress = swift
    rec.Currency = currency
    list = rec.loadSwiftLookup()
    rc, value = len(list)>0, [x.SwiftAddressOut for x in list]
    if puttyTrace == 1:
        print('almanacSwiftLookup(%s, %s) = %s %s' % (repr(swift), repr(currency), repr(value), result(rc)))
    return rc, value

def almanacSwiftByCountry(swift, country):
    rec = dbAlmanacBank.DBAlmanacBankSwiftCountryLookup(connect)
    rec.SwiftAddress = swift
    rec.Country = country
    list = rec.loadSwiftCountryLookup()
    rc, value = len(list)>0, [x.SwiftAddressOut for x in list]
    if puttyTrace == 1:
        print('almanacSwiftByCountry(%s, %s) = %s %s' % (repr(swift), repr(country), repr(value), result(rc)))
    return rc, value

def almanacFinIdLookup(swift):
    rec = dbAlmanacBank.DBAlmanacBankFinIdLookup(connect)
    rec.SwiftAddress = swift
    list = rec.loadFinIdLookup()
    rc, value = len(list)>0, [(x.FinId, x.BranchId) for x in list]
    if puttyTrace == 1:
        print('almanacFinIdLookup(%s) = %s %s' % (repr(swift), repr(value), result(rc)))
    return rc, value

import DB_ALMANACCORRESPONDENT as dbAlmanacCorrespondent
class AlmanacCorrespondent:
    def __init__(self, finId, ccy):
        self.finId = finId
        self.corrCurrency = ccy
        rec = dbAlmanacCorrespondent.DBAlmanacCorrespondentGet(connect)
        self.rc = rec.readGet(finId, ccy)
        if (self.rc == 0):
            self.corrFinId = 0
            self.corrBankName = ''
            self.corrTown = ''
            self.corrCountry = ''
            self.corrAccountNo = 0
            self.corrSwiftAddress = ''
            self.preferredInd = 0
            self.status = 0
        else:
            self.corrFinId = rec.CorrFinId
            self.corrBankName = rec.CorrBankName
            self.corrTown = rec.CorrTown
            self.corrCountry = rec.CorrCountry
            self.corrAccountNo = rec.CorrAccountNo
            self.corrSwiftAddress = rec.CorrSwiftAddress
            self.preferredInd = rec.PreferredInd
            self.status = rec.Status
        if puttyTrace == 1:
            print('AlmanacCorrespondent(%d, %s) = %s %s' % (finId, repr(ccy), repr(self.__dict__), result(self.rc)))

def almanacCorr(finId, ccy):
    rec = AlmanacCorrespondent(finId, ccy)
    rc, value = rec.rc, rec.corrSwiftAddress
    if puttyTrace == 1:
        print('almanacCorr(%d, %s) = %s %s' % (finId, repr(ccy), repr(value), result(rc)))
    return rc, value

def almanacCorrList(finId, ccy):
    rec = dbAlmanacCorrespondent.DBAlmanacCorrespondentGetSwiftList(connect)
    rec.FinId = finId
    rec.CorrCurrency = ccy
    list = rec.loadGetSwiftList()
    rc, value = len(list)>0, [x.CorrSwiftAddress for x in list]
    if puttyTrace == 1:
        print('almanacCorrList(%d, %s) = %s %s' % (finId, repr(ccy), repr(value), result(rc)))
    return rc, value

import DB_BANKFILE as dbBankFile
def bankFileAuthKeys(swift):
    if len(swift) == 0:
        return 0, ""
    rec = dbBankFile.DBBankFileGetAuthKeys(connect)
    rc = rec.readGetAuthKeys(swift)
    if (rc == 0):
        value = ""
    else:
        value = rec.AuthKeysExchd
    if puttyTrace == 1:
        print('bankFileAuthKeys(%s) = %s %s' % (repr(swift), repr(value), result(rc)))
    return rc, value

import DB_BANKCORRESPONDENTS as dbBankCorrespondent
def bankCorrespondent(swift, currency):
    rec = dbBankCorrespondent.DBBankCorrespondentsGet(connect)
    rec.SwiftAddress = swift
    rec.CurrId = currency
    list = rec.loadGet()
    rc, value = len(list)>0, [x.Correspondent for x in list]
    if puttyTrace == 1:
        print('bankCorrespondent(%s, %s) = %s %s' % (repr(swift), repr(currency), repr(value), result(rc)))
    return rc, value

import DB_FINIDCORRESPONDENTROUTING as dbFinidCorrespondentRouting
def finIdRoute(finId):
    rec = dbFinidCorrespondentRouting.DBFinidCorrespondentRoutingGet(connect)
    rc = rec.readGet(finId)
    if (rc == 0):
        value = ""
    else:
        value = rec.RouteFinId
    if puttyTrace == 1:
        print('finIdRoute(%d) = %s %s' % (finId, repr(value), result(rc)))
    return rc, value

import DB_COUNTRY as dbCountry
def currencyForCountry(what):
    rec = dbCountry.DBCountryGet(connect)
    rc = rec.readGet(what)
    if (rc == 0):
        value = ""
    else:
        value = rec.CurrId
    if puttyTrace == 1:
        print('currencyForCountry(%s) = %s' % (repr(what), repr(value)))
    return value

def countryForCurrency(what):
    rec = dbCountry.DBCountryGetByCurrency(connect)
    rc = rec.readGetByCurrency(what)
    if (rc == 0):
        value = ""
    else:
        value = rec.Id
    if puttyTrace == 1:
        print('countryForCurrency(%s) = %s' % (repr(what), repr(value)))
    return value

def countryForCodeId(what):
    rec = dbCountry.DBCountryGetByCurrency(connect)
    rc = rec.readGetByCurrency(what)
    if (rc == 0):
        value = ""
    else:
        value = rec.Id
    if puttyTrace == 1:
        print('countryForCurrency(%s) = %s' % (repr(what), repr(value)))
    return value

import DB_FIGCORRBANKPROC as dbFigCorrBank
def selectFigRankingsBySwift(swiftList):
    rec = dbFigCorrBank.DBFigCorrespondentBankGetBySwiftList(connect)
    rec.SwiftList = '('+repr(swiftList)[1:-1]+')'  #`.` stringize the list drop front and end char and put in parens
    list = rec.loadGetBySwiftList()
    rc, value = len(list)>0, [(x.SwiftAddress,
                               x.Country,
                               x.CurrId,
                               x.RankType,
                               x.Rank,
                               x.Frequency,
                               x.Counter) for x in list]
    if puttyTrace == 1:
        print('selectFigRankingsBySwift(%s) = %s %s' % (repr(swiftList), repr(value), result(rc)))
    return rc, value

def selectFigRankingsByCountry(country):
    rec = dbFigCorrBank.DBFigCorrespondentBankGetByCountry(connect)
    rec.Country = country
    list = rec.loadGetByCountry()
    rc, value = len(list)>0, [(x.SwiftAddress,
                               country,
                               x.CurrId,
                               x.RankType,
                               x.Rank,
                               x.Frequency,
                               x.Counter) for x in list]
    if puttyTrace == 1:
        print('selectFigRankingsByCountry(%s) = %s %s' % (repr(country), repr(value), result(rc)))
    return rc, value

#Fix to remove data value from FACTS transactions because the replies were too big
import DB_STREAMS as streams
import DB_RESPONSE as response
def getPartialStreamResponses():
    rec = streams.DBStreamsByMessageIDData(connect)
    rec.InMessageId = getInterfaceData()[1]
    print(getInterfaceData())
    streamList = rec.loadByMessageIDData()
    dict = {}
    dict['STREAMRESPONSES/COUNT'] = repr(len(streamList))
    strCount = 0;
    for i in streamList:
        rc, decompLen, i.MessageData = zdecompress(i.MessageData,i.MessageLen)
        rec = response.DBResponseByStreamID(connect)
        rec.InStreamID = i.Id
        responses = rec.loadByStreamID() #Can't just assign a new member, The proforma class would claim it is not an existing member
        key = 'STREAMRESPONSES.STREAM'+repr(strCount)
        dict[key+'/ID'] = repr(i.Id)
        dict[key+'/TYPE'] = i.StreamType
        dict[key+'/STATUS'] = repr(i.Status)
        rspCount = 0
        for r in responses:
            rc, decompLen, r.MessageData = zdecompress(r.MessageData,r.MessageLen)
            respkey = key+'.RESPONSE'+repr(rspCount)
            dict[respkey+'/ID'] = repr(r.Id)
            dict[respkey+'/STATUS'] = repr(r.Status)
            rspCount += 1
        strCount += 1
    rc = len(streamList)
    if puttyTrace == 1:
        print('getStreamResponses() = %s %s' % (repr(len(streamList))+' Stream(s)', result(rc)))
    return rc,xmlbuild(dict)
