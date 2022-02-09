from SYS_FUNCTIONS import *
from INTRINSICS import *

#### Script name:SYS_CLEANUP
## Author: Vincent Risi
## --------------------
## In order to produce archive ready data (if archiving is decided upon) and
## removal of stale messages and related paraphenalia
## This module will be run as a batch operation periodically
####

import sys
import os
import DB_MESSAGE as message
import DB_FIELDS as fields
import DB_DATES as dates
import GENERAL_ROUTINES as gen

minimumNoDays = 30
defaultNoDays = 60

def remover(table, inList):
  rec = message.DBMessageRemoveFromTable(connect)
  print('Removing from table %s list (%s)' % (table, inList))
  rec. runRemoveFromTable(table, inList)
  connect.commit() # change to commit later

def doFiles(table, fileList):
  for id in fileList:
    rec = message.DBMessageGetFileName(connect)
    if rec.readGetFileName(id, table) == 1:
      rc, messageLen, messageData = zdecompress(rec.MessageData, rec.MessageLen)
      dict = xmlparse(messageData)
      msg = gen.msgname(dict)
      fileName = dict[msg+'.FILE.NAME']
      print('rm -f %s' % (fileName))
      os.system('rm -f '+fileName)

def doTable(table, inList):
  rec = message.DBMessageReadFromTable(connect)
  rec.MessageList = inList
  rec.Table = table
  list = rec.loadReadFromTable()
  print('Removing %d records from table %s' % (len(list), table))
  idList = ''
  comma = ''
  for x in list:
    idList = idList + comma + repr(x.Id)
    comma = ','
    if len(idList) > 512:
      remover(table, idList)
      idList = ''
      comma = ''
  if len(idList) > 0:
    remover(table, idList)
  return len(list)

def doTableType(table, inList):
  rec = message.DBMessageReadFromTableType(connect)
  rec.MessageList = inList
  rec.Table = table
  list = rec.loadReadFromTableType()
  print('Removing %d records from table %s' % (len(list), table))
  idList = ''
  fileList = []
  comma = ''
  for x in list:
    idList = idList + comma + repr(x.Id)
    if x.MessageType == message.MessageMessageTypeConst['File']:
      fileList.append(x.Id)
    comma = ','
    if len(idList) > 512:
      remover(table, idList)
      doFiles(table, fileList)
      idList = ''
      fileList = []
      comma = ''
  if len(idList) > 0:
    remover(table, idList)
    doFiles(table, fileList)
  return len(list)

def doFields(inList):
  rec = fields.DBFieldsRemoveFromTable(connect)
  print('Removing from table Fields list (%s)' % (inList))
  rec.runRemoveFromTable(inList)
  connect.commit()

def process(lookupList, fileList):
  count = 0
  count += doTableType('Reply', lookupList)
  count += doTableType('Response', lookupList)
  count += doTableType('Streams', lookupList)
  count += doTable('Summary', lookupList)
  count += doTable('Routing', lookupList)
  count += doTable('Comments', lookupList)
  doFields(lookupList)
  doFiles('Message', fileList)
  remover('Message', lookupList)
  return count

def getDays():
  if len(sys.argv) >= 3:
    result = int(sys.argv[2])
  else:
    result = defaultNoDays
  if result < minimumNoDays:
    result = minimumNoDays
  return result

def main():
  rec = message.DBMessageCleanup(connect)
  rec.DateType = dates.DatesDateTypeConst['RunDate']
  rec.AgeInDays = getDays()
  list = rec.loadCleanup()
  print('Removing %d messages older than %d days' % (len(list), rec.AgeInDays))
  idList = ''
  fileList = []
  comma = ''
  count = 0
  for x in list:
    idList = idList + comma + repr(x.Id)
    if x.MessageType == message.MessageMessageTypeConst['File']:
      fileList.append(x.Id)
    comma = ','
    if len(idList) > 512:
      count += process(idList, fileList)
      idList = ''
      fileList = []
      comma = ''
  if len(idList) > 0:
    count += process(idList, fileList)
  count += len(list)
  print(count)


