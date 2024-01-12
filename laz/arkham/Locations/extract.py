import glob, os

codename = {}
codename['Administration']     = 'ABUILDING'
codename['ArkhamAsylum']       = 'ARKASYLUM'
codename['BankOfArkham']       = 'BOARKHAM'
codename['BlackCave']          = 'BCAVE'
codename['CuriositieShoppe']   = 'CSHOPPE'
codename['GeneralStore']       = 'GENSTORE'
codename['Graveyard']          = 'GRAVEYARD'
codename['HibbsRoadhouse']     = 'HROADHOUSE'
codename['HistoricalSociety']  = 'HSOCIETY'
codename['IndependenceSquare'] = 'INDSQUARE'
codename['InnerSanctum']       = 'ISANCTUM'
codename['Library']            = 'LIBRARY'
codename['MasBoardingHouse']   = 'MBHOUSE'
codename['PoliceStation']      = 'PSTATION'
codename['RiverDocks']         = 'RDOCKS'
codename['ScienceBuilding']     = 'SBUILDING'
codename['SilverTwilightLodge'] = 'STLODGE'
codename['SouthChurch']         = 'SCHURCH'
codename['StMarysHospital']     = 'STMHOSPITAL'
codename['TheUnnamable']        = 'TUNNAMABLE'
codename['TheWitchHouse']       = 'TWHOUSE'
codename['TrainStation']        = 'TSTATION'
codename['UnvisitedIsle']       = 'UISLE'
codename['VelmasDiner']         = 'VDINER'
codename['Woods']               = 'WOODS'
codename['YeOldeMagickShoppe']  = 'YOMSHOPPE'

groups = '''
Dunwich Horror
Curse of the Dark PharaohCurse of the Dark Pharaoh (Revised Edition)
Curse of the Dark Pharaoh (Revised Edition)
Curse of the Dark Pharaoh
The Black Goat of the Woods
The King in Yellow
Kingsport Horror
The Lurker at the Threshold
Innsmouth Horror
'''.splitlines()

def pull(filename, group, ofilename, no):
  ofile = open(ofilename, 'at')
  infile = open(filename, 'rt')
  lines = infile.readlines()
  infile.close()
  for line in lines:
    parts = line[:-1].split('\t')
    if parts[-1] == group:
      ofile.write("  Add('%s', %d, '%s');\n" % (codename[filename.replace('.txt','')], no, parts[0].replace("'","''")))
      no += 1
  ofile.close()

def main():
  if os.access('thelurker.enc', 0):
    os.remove('thelurker.enc')
  files = glob.glob('*.txt')
  for file in files:
    pull(file, 'The Lurker at the Threshold', 'thelurker.enc', 21)

main()
