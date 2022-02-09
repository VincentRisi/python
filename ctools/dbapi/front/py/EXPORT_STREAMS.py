from SYS_FUNCTIONS import *
from INTRINSICS import *
#### Script name:EXPORT_STREAMS

import DB_STREAMS as streams

def main():
  #find id's per queue put in list idLst
  s = streams.DBStreamsByQueueAll(connect)
  s.InQueue = 'SAFFY-FP'
#  s.InQueue = 'TIBOS-FP'
#  s.InQueue = 'WASTE-FP'
  s.InDateFrom = '20020501'  #excluded
  s.InDateTo = '20020531'    #included
  idLst = s.loadByQueueAll()

  f = open('c:\\Denise\\Archiving\\Prod\\SWIFTstreamsMAY.txt','w')

  for i in idLst:
#    print 'Loading',i.Id,i.MessageId
    rec = streams.DBStreamsGetData(connect)
    rec.readGetData(i.Id)
    rc, messageLen, messageData = zdecompress(rec.MessageData, rec.MessageLen)
#    print 'Stream:',messageData
    f.write(str(i.MessageId)+'|'+messageData+'***')

def sortSwift():
#def main():

  fr = open('c:\\Denise\\Archiving\\SWIFTstreams.txt','r')
  fw = open('c:\\Denise\\Archiving\\QA\\swift.txt','w')

  strData = fr.read()
  lstData = strData.split('***')

  for i in range(len(lstData) - 1):
     msgId, stream = lstData[i].split('|')
     j = stream.find('{2:')
     type = stream[j+4:j+7]
     date = ''
     status = ''
     fw.write(msgId+','+type+','+date+','+status+','+stream+'\n')

  count = '<count>' + str(len(lstData)) + '</count>'
  print(count)
  fw.write(count)


def sortWaste():
#def main():

  fr = open('c:\\Denise\\Archiving\\WASTEstreams.txt','r')
  fw = open('c:\\Denise\\Archiving\\QA\\waste.txt','w')

  strData = fr.read()
  lstData = strData.split('***')

  for i in range(len(lstData) - 1):
     msgId, stream = lstData[i].split('|')
     tranCde = stream[112:116]
     if tranCde[0:2] == '63':
        drcr = 'CR'
     elif tranCde[0:2] == '14':
        drcr = 'DR'
     accNo = stream[87:103]
     amt = stream[139:152]
     narrative = stream[152:248].strip()
     status = ''

     fw.write(msgId+','+tranCde+','+drcr+','+amt+','+accNo+','+narrative+','+status+'\n')

  count = '<count>' + str(len(lstData)) + '</count>'
  print(count)
  fw.write(count)

def sortTibos():
#def main():

  fr = open('c:\\Denise\\Archiving\\TIBOSstreams.txt','r')
  fw = open('c:\\Denise\\Archiving\\QA\\tibos.txt','w')

  strData = fr.read()
  lstData = strData.split('***')

  for i in range(len(lstData) - 1):

    purchCcy = ''
    purchAmt = ''
    purchAccNo = ''
    saleCcy = ''
    saleAmt = ''
    saleAccNo = ''
    rate = ''
    fecNo = ''
    status = ''

    msgId, stream = lstData[i].split('|')
    tranCde = 'FA' + stream[0:2]

    if tranCde == 'FAAJ':
      purchCcy = stream[182:185]
      purchAmt = stream[70:86]
      purchAccNo = stream[58:68]
      saleCcy = stream[185:188]
      saleAmt = stream[42:58]
      saleAccNo =stream[30:40]
      rate = ''
      fecNo = ''
      status = ''
    elif tranCde == 'FADR':
      purchCcy = stream[25:28]
      purchAmt = stream[31:47]
      purchAccNo = stream[108:118]
      saleCcy = stream[28:31]
      saleAmt = stream[47:63]
      saleAccNo =stream[118:128]
      rate = stream[63:73]
      fecNo = stream[98:108]
      status = ''
    elif tranCde == 'FAAS' or tranCde == 'FABJ':
      purchCcy = stream[27:30]
      purchAmt = stream[34:50]
      purchAccNo = ''
      saleCcy = 'ZAR'
      saleAmt = stream[126:142]
      saleAccNo =stream[79:89]
      rate = stream[50:60]
      fecNo = ''
      status = ''

    fw.write(msgId+','+tranCde+','+purchCcy+','+purchAmt+','+purchAccNo+','+saleCcy+','+
          saleAmt+','+saleAccNo+','+rate+','+fecNo+','+status+'\n')

  count = '<count>' + str(len(lstData)) + '</count>'
  print(count)
  fw.write(count)















