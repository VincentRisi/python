from SYS_FUNCTIONS import *
from INTRINSICS import *
#FIG
#__________________________________________________________________________
#Fig correspondent python functions
from GENERAL_ROUTINES import *
import random

def _getBestFigRank(list):
  '''Sums all the rankings in this list and use ranking/sum to decide the probabilities
  'for selecting that swift address
  '
  'list - [[swift1,x,x,x,ranking,...]
  '        [swift,country,ccy,rankType,ranking,frequency,counter]
  '        ...]
  'Private function, not imported by #use /from fig import *
  '''

  # if any p exists then just use p's. If not use the rest ie. all the s's
  pList = [x for x in list if x[3] == 'P']
  if len(pList) > 0:
   list = pList

  tot = 0
  for i in list:
   tot += float(i[4])
  if tot == 0:
   return ('',-1)
  board = []
  counter = 0
  for i in list:
   counter += i[4]
   board.append(counter /tot)

  rnd = random.random()
  for j in range(len(board)):
   if rnd < board[j]:
    return (list[j][0],j)


def getBestFigBySwift(swiftList):
  'returns rc,swiftaddress for the best matched fig correspondent bank in the list of swift addresses'
  print('getBestFigBySwift(',swiftList,')')
  rc,list = selectFigRankingsBySwift(swiftList)
  if not rc:
   return (0,'')
  bestSwift,idx = _getBestFigRank(list)
  return 1,bestSwift

def getBestFigByCountry(country):
  'returns rc,swiftaddress for the best matched fig correspondent bank in country'
  print('getBestFigByCountry(',country,')')
  rc,list = selectFigRankingsByCountry(country)
  if not rc:
   return (0,'')
  bestSwift,idx = _getBestFigRank(list)
  return 1,bestSwift

def testFunc(a):
  try:
    raise "Harry"
  except:
    (xType, xValue, xTraceback) = sys.exc_info ()
    Catch(__name__, xType, xValue, xTraceback)
  return a+5

#Testing code
#_______________________________________________
#print getBestFigByCountry('AFGHANISTAN')

#import time

#a = [0,0,0]
#s = ['AAACKWKW','AAALSARIALK','AAALSARIJED']
#for i in range(1000):
# rc,val = getBestFigByCountry('AFGHANISTAN') #getBestFigBySwift(s)
# time.sleep(1)
# idx = s.index(val)
# a[idx] += 1

#print s
#print a


#_______________________________________________
#list = [
#['SWIFT1', 'AFGHANISTAN', 'BWP', 'P', 50, 2, 0],
#['SWIFT2', 'Seaworld',    'SWD', 'P', 20, 0, 0],
#['SWIFT3', 'AboeDabi',    'ABD', 'P', 12, 0, 0],
#['SWIFT4', 'AFGHANISTAN', 'ATS', 'P', 18, 5, 0]
#]
#
#sample = 1000.0
#
#for i in range(sample):
# swift,idx = _getBestFigRank(list)
# list[idx][6] += 1
#
#
#print 'Samples=',sample
#actlE = [[i[0],round(i[6]/sample*100,2)] for i in list]
#
#print 'actlE=',actlE

def main():
  print('FigInit')











