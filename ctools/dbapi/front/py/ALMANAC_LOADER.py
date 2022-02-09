from SYS_FUNCTIONS import *
from INTRINSICS import *
import TRANSLATIONS as tran
import DB_ALMANACBANK as dbab
import DB_ALMANACCORRESPONDENT as dbac
import GENERAL_ROUTINES as gr

import DEPRECATED_STRING

def uptopipe(field):
  n = DEPRECATED_STRING.find(field, '|')
  if n != -1:
    field = field[:n]
  field = DEPRECATED_STRING.replace(field, ' ', '')
  return field

def takeon(fileName, commitEvery):
  print("Setting up database recs")
  abone = dbab.DBAlmanacBank(connect)
  abrec = dbab.DBAlmanacBank(connect)
  abrec.USId = 'ALMANACLOAD'
  abrec.TmStamp = sysdate()
  acone = dbac.DBAlmanacCorrespondent(connect)
  acrec = dbac.DBAlmanacCorrespondent(connect)
  acrec.USId = 'ALMANACLOAD'
  acrec.TmStamp = sysdate()
  print("Opening input file")
  fi = open(fileName, 'r', 262144)
  count = 0
  count2 = 0
  print("Making data translation lists")
  trantab = DEPRECATED_STRING.maketrans(tran.fromlist, tran.tolist)
  print("Taking on Almanac Bank and Correspondent", fileName)
  while 1:
    line = DEPRECATED_STRING.upper(fi.readline()[:-1])
    if len(line) == 0:
      connect.commit()
      break;
    line = DEPRECATED_STRING.replace(line, '","', '\t')
    line = DEPRECATED_STRING.translate(line, trantab, '()')
    line = DEPRECATED_STRING.replace(line, '"', '')
    fields = DEPRECATED_STRING.split(line, '\t')
    if fields[0] == '0':
      continue
    if fields[0] == '2':
      del fields[4]
    if fields[0] == '1' or fields[0] == '2':
      abrec.FinId = fields[1]
      abrec.BranchId = fields[2]
      abrec.BankName = fields[3]
      abrec.AddressLine1 = fields[4]
      abrec.AddressLine2 = fields[5]
      abrec.AddressLine3 = fields[6]
      abrec.AddressLine4 = fields[7]
      abrec.AddressLine5 = fields[8]
      abrec.Town = fields[12]
      abrec.Country = fields[13]
      abrec.Telephone = fields[14]
      abrec.Fax = fields[15]
      abrec.Telex = fields[16]
      abrec.SwiftAddress = uptopipe(fields[17])
      abrec.NationalBankCode = uptopipe(fields[18])
      abrec.RBIChangeDate = fields[19]+'000000'
      abrec.RBIInsertDate = fields[20]+'000000'
      try:
        if abone.readSelectOne(abrec.FinId, abrec.BranchId) == 1:
          if abrec.BankName != abone.BankName \
          or abrec.Town != abone.Town \
          or abrec.AddressLine1 != abrec.AddressLine1 \
          or abrec.AddressLine2 != abone.AddressLine2 \
          or abrec.AddressLine3 != abone.AddressLine3 \
          or abrec.AddressLine4 != abone.AddressLine4 \
          or abrec.AddressLine5 != abone.AddressLine5 \
          or abrec.Country != abone.Country \
          or abrec.Telephone != abone.Telephone \
          or abrec.Fax != abone.Fax \
          or abrec.Telex != abone.Telex \
          or abrec.SwiftAddress != abone.SwiftAddress \
          or abrec.NationalBankCode != abone.NationalBankCode \
          or abrec.RBIInsertDate != abone.RBIInsertDate \
          or abrec.RBIChangeDate != abone.RBIChangeDate \
          or abrec.Status != abone.Status:
            abrec.execUpdate()
            count += 1
        else:
          abrec.execInsert()
          count += 1
        if count == commitEvery:
          count2 += count
          count = 0
          print(count2, sysdate())
          connect.commit()
      except DBError as x:
        if x.ociErr == 2291:
          print("Missing SWIFTADDR", abrec.SwiftAddress)
          continue
        gr.printClass(abrec)
        gr.printClass(x)
        connect.rollback()
        return
    elif fields[0] == '3':
      acrec.FinId = fields[1]
      acrec.CorrCurrency = fields[4]
      acrec.CorrFinId = fields[5]
      acrec.CorrBranchId = fields[6]
      acrec.CorrBankName = fields[7]
      acrec.CorrTown = fields[8]
      acrec.CorrCountry = fields[9]
      acrec.CorrSwiftAddress = uptopipe(fields[10])
      acrec.CorrAccountNo = fields[11]
      acrec.PreferredInd = fields[13]
      acrec.RBIChangeDate = fields[14]+'000000'
      acrec.RBIInsertDate = fields[15]+'000000'
      try:
        if acone.readSelectOne(acrec.FinId, acrec.CorrCurrency, acrec.CorrFinId, acrec.CorrBranchId) == 1:
          if acrec.CorrBankName != acone.CorrBankName \
          or acrec.CorrTown != acone.CorrTown \
          or acrec.CorrCountry != acone.CorrCountry \
          or acrec.CorrSwiftAddress != acone.CorrSwiftAddress \
          or acrec.CorrAccountNo != acone.CorrAccountNo \
          or acrec.PreferredInd != acone.PreferredInd \
          or acrec.RBIChangeDate != acone.RBIChangeDate \
          or acrec.RBIInsertDate != acone.RBIInsertDate:
            acrec.execUpdate()
            count += 1
        else:
          acrec.execInsert()
          count += 1
        if count == commitEvery:
          count2 += count
          count = 0
          print(count2, sysdate())
          connect.commit()
      except DBError as x:
        if x.ociErr == 2291:
          continue
        gr.printClass(acrec)
        gr.printClass(x)
        connect.rollback()
        return

def main():
  takeon(r'/main/nedcor/qa/putty/packs/in/nedcor.txt', 250)

