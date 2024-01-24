import glob, os.path

UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_district(data):
  s = 0
  district = ''
  code = ''
  name = ''
  work = ''
  for ch in data:
    if s == 0:
      if not ch in UPPERS:
        break
      code = ch
      s = 1
      continue
    elif s == 1:
      if ch in UPPERS:
        name = ch
        district = ch
        s = 2
        continue
      code += ch.upper()
      continue
    elif s == 2:
      if ch in UPPERS:
        name += ' '+ch
        district += ch
        work = ''
        continue
      name += ch
      work += ch.upper()
  return district+work, code, name

def make_name(name):
  filename = name[:-3]
  n = filename.find('\\')
  if n == -1:
    return filename
  n += 1
  result = filename[n]
  n += 1
  while n < len(filename):
    result += filename[n]
    n += 1
    if n < len(filename) and filename[n] in UPPERS:
      result += ' '
  return result

def get_places(d, district):
  txts = glob.glob('%s\\*.txt' % (d))
  for txt in txts:
    infile = open(txt, 'rt')
    place = ''
    no = 1
    while True:
      line = infile.readline()
      if line == '':
        break;
      line = line.strip()
      if len(place) == 0:
        for ch in line:
          if ch in UPPERS: place = place + ch
        print "insert into places values ('%s', '%s', '%s');" % (place, district, make_name(txt))
        description = ''
        continue
      if line == place:
        #print "insert into encounters values ('%s', %d, '%s');" % (place, no, description.strip())
        no += 1
        description = ''
        continue
      description += line + ' '
    #print "insert into encounters values ('%s', %d, '%s');" % (place, no, description.strip())
    infile.close()

def spells():
  xxx = '''\
DREADCURSEAZAROTH 4
MISTSOFRELEH  4
WITHERSPELL 4
FINDGATE 4
SHRIVELLING 5
VOICEOFRA 3
HEAL 3
ENCHANTWEAPON 3
BINDMONSTER 2
FLESHWARD 4
REDSIGNSHUDDEMELL 2
'''
  for line in xxx.splitlines():
    a, b = line.split()
    print "insert into Items values ('%s', 'spells', %s, 0);" % (a, b)

def skills():
  xxx = '''\
FIGHT 2
SNEAK 2
EXPERTOCCULTIST 2
BRAVERY 2
MARKSMAN 2
SPEED 2
STEALTH 2
WILL 2
LUCK 2
LORE 2
'''
  for line in xxx.splitlines():
    a, b = line.split()
    print "insert into Items values ('%s', 'skills', %s, 0);" % (a, b)

def allies():
  xxx = '''\
ERICCOLT
TOMMURPHY
SIRBRINTON
RYANDEAN
RICHARDPICKMAN
ANNAKASLOW
DUKE
PROFARMITAGE
RUBYSTANDISH
JOHLEGRASSE
'''
  for line in xxx.splitlines():
    print "insert into Items values ('%s', 'allies', 0, 0);" % (line)

def patrols():
  for x in ['PATROLWAGON','DEPUTYREVOLVER','DEPUTYOFARKHAM']:
    print "insert into Items values ('%s', 'patrol', 0, 0);" % (x)

def encounters():
  dirs = glob.glob('*')
  for d in dirs:
    if not os.path.isdir(d): continue
    district, code, name = get_district(d)
    #print "insert into district values('%s', '%s', '%s');" % (district, code, name)
    get_places(d, district)

def investigators():
  format = '''\
  insert into Investigators values ('%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''
#name         profession    home              status  sanity stamina clues cash focus speed sneak fight will lore luck
  data = '''\
MontereyJack  ARCHAEOLOGIST CSHOPPE           normal     3     7       1     7    2     1     3     2     3    1    5
VincentLee    PHYSICIAN     STMHOSPITAL       normal     5     5       1     9    2     0     5     0     4    2    4
AshcanPete    SCROUNGE      RDOCKS            normal     4     6       3     1    1     0     6     2     5    0    3
JoeDiamond    HUNCHES       PSTATION          normal     4     6       3     8    3     3     4     2     3    0    3
JennyBarnes   TRUSTFUND     TSTATION          normal     6     4       0    10    1     0     4     1     5    1    5
GloriaGoldberg PSYCHIC      VDINER            normal     6     4       2     7    2     1     3     0     5    1    5
BobJenkins     DEALER       GENSTORE          normal     4     6       0     9    1     2     3     1     6    0    4
AmandaSharpe   STUDIOUS     BOARKHAM          normal     5     5       1     1    3     1     4     1     4    1    4
SisterMary     GUARDANGEL   SCHURCH           blessed    7     3       0     0    1     1     4     0     4    1    6
DarrellSimmons HOMETOWN     NEWSPAPER         normal     4     6       1     4    2     2     3     2     4    0    4
CarolynFern   PHYCHOLOGY    ARKASYLUM         normal     6     4       1     7    2     0     3     1     4    2    5
MichaelMcGlen STRONGBODY    MBHOUSE           normal     3     7       0     8    1     2     4     3     4    0    3
MandyThompson RESEARCH      LIBRARY           normal     5     5       4     6    2     1     5     0     5    1    3
KateWinthrop  SCIENCE       SBUILDING         normal     6     4       2     7    1     1     5     1     3    2    4
HarveyWalters STRONGMIND    ABUILDING         normal     7     3       1     5    2     0     5     0     3    3    4
DexterDrake   MAGICAL       YOMSHOPPE         normal     5     5       0     5    2     2     4     1     3    2    3
'''
  for line in data.splitlines():
    x = tuple(line.split())
    print format % x

def possessions():
  format = "  insert into Possessions values ( '%s', '%s', %s);"
  data = '''\
MontereyJack BULLWHIP      1
MontereyJack .38REVOLVER   1
MontereyJack uniques       2
MontereyJack skills        1
VincentLee   commons       2
VincentLee   spells        2
VincentLee   skills        1
AshcanPete   DUKE          1
AshcanPete   commons       1
AshcanPete   uniques       1
AshcanPete   skills        1
JoeDiamond   .45AUTOMATIC  1
JoeDiamond   commons       2
JoeDiamond   skills        1
JennyBarnes  commons       2
JennyBarnes  uniques       1
JennyBarnes  spells        1
JennyBarnes  skills        1
GloriaGoldberg commons     2
GloriaGoldberg spells      2
GloriaGoldberg skills      1
BobJenkins   commons       2
BobJenkins   uniques       2
BobJenkins   skills        1
AmandaSharpe commons       1
AmandaSharpe uniques       1
AmandaSharpe spells        1
AmandaSharpe skills        1
SisterMary   BLESSING      1
SisterMary   CROSS         1
SisterMary   HOLYWATER     1
SisterMary   spells        2
SisterMary   skills        1
DarrellSimmons RETAINER    1
DarrellSimmons commons     1
DarrellSimmons uniques     2
DarrellSimmons skills      1
CarolynFern    commons     2
CarolynFern    uniques     2
CarolynFern    skills      1
MichaelMcGlen  DYNAMITE    1
MichaelMcGlen  TOMMYGUN    1
MichaelMcGlen  uniques     1
MichaelMcGlen  skills      1
MandyThompson  commons     2
MandyThompson  uniques     1
MandyThompson  skills      1
KateWinthrop   commons     1
KateWinthrop   uniques     1
KateWinthrop   spells      2
KateWinthrop   skills      1
HarveyWalters  uniques     2
HarveyWalters  spells      2
HarveyWalters  skills      1
DexterDrake    SHRIVELLING 1
DexterDrake    commons     1
DexterDrake    uniques     1
DexterDrake    spells      2
DexterDrake    skills      1
'''
  for line in data.splitlines():
    x = tuple(line.split())
    print format % x

def mythos():
  format = "  insert into Mythos values ('%s', '%s', '%s', '%s', '%s', '%s');"
  data = '''\
ChurchGroupReclaimsSouthside      headline      HROADHOUSE BCAVE       HEX                 SLASH,TRIANGLE,STAR
DreamOfASunkenCity                environment   TUNNAMABLE INDSQUARE   CROSS               MOON
StrangeTremorsCease               headline      TUNNAMABLE INDSQUARE   HEX                 SLASH,TRIANGLE,STAR
FourthOfJulyParade                headline      BCAVE      TWHOUSE     MOON                CROSS
EgyptianExhibitVisitsMiskatonicU  environment   BCAVE      TWHOUSE     CROSS               MOON
GangsCleanUpEasttown              headline      BCAVE      TWHOUSE     ROUND               SQUARE,DIAMOND
NodensFavor                       environment   BCAVE      TWHOUSE     SLASH,TRIANGLE,STAR HEX
SlumMurdersContinue               headline      HSOCIETY   WOODS       MOON                CROSS
FamilyFoundButchered              headline      UISLE      GRAVEYARD   MOON                CROSS
NoOneCanHelpYou                   environment   WOODS      UISLE       CROSS               MOON
DisturbingTheDead                 rumor         none       BCAVE       SLASH,TRIANGLE,STAR HEX
IllWindGripsArkham                headline      UISLE      GRAVEYARD   HEX                 SLASH,TRIANGLE,STAR
HorrorAtGroundbreaking            headline      STLODGE    HSOCIETY    MOON                CROSS
AStrangePlague                    environment   TUNNAMABLE INDSQUARE   SQUARE,DIAMOND      ROUND
WitchBurningAnniversary           headline      SBUILDING  UISLE       MOON                CROSS
HeatWave                          environment   INDSQUARE  WOODS       SQUARE,DIAMOND      ROUND
MissingPeopleReturn               headline      WOODS      TUNNAMABLE  SLASH,TRIANGLE,STAR HEX
PoliceStepUpPatrolsInNorthside    headline      GRAVEYARD  STLODGE     ROUND               SQUARE,DIAMOND
AlienTechnology                   environment   SBUILDING  UISLE       SQUARE,DIAMOND      ROUND
'''
  for line in data.splitlines():
    x = tuple(line.split())
    print format % x

'''name
   colour
   symbol
   attributes
   awareness
   sanity
   stamina
   noof
'''
def monsters():
  format = "  insert into Monsters values ('%s', '%s', '%s', '%s', %s, %s, %s, %s, %s, %s, %s);"
  data = '''\
TheBlackMan      black   moon      MASK,ENDLESS       -3  0  0  1  0  0  1
THeBloatedWoman  black   hex       MASK,ENDLESS       -1 -1  2  2 -2  2  1
TheDarkPharoah   black   slash     MASK,ENDLESS       -1 -1  1  2 -3  3  1
GodOfTheBloodyTongue black diamond MASK,ENDLESS,O=1,N=1 1 -3 3  4 -4  4  1
Gug              black   slash     O=1                -2 -1  2  3 -2  4  2
ElderThing       black   diamond   NORMAL             -2 -3  2  2  0  1  2
Ghoul            black   hex       AMBUSH             -3  0  1  1 -1  1  3
Cultist          black   moon      NORMAL             -3  0  0  1  1  1  6
Maniac           black   moon      NORMAL             -1  0  0  1  1  1  3
Vampire          black   moon      UNDEAD,PHYSR       -3  0  2  2 -3  3  1
FormlessSpawn    black   hex       PHYSI               0 -1  2  2 -2  2  2
HighPriest       black   cross     MAGICI             -2  1  1  2 -2  2  1
Dhole            black   round   PHYSR,MAGICR,N=1,O=1 -1 -1  4  3 -3  4  1
Zombie           black   moon      UNDEAD              1 -1  1  1 -1  2  3
StarSpawn        black   cross     NORMAL             -1 -3  2  3 -3  3  2
Witch            black   round     MAGICR             -1  0  0  1 -3  2  2
Byakhee          blue    round     NORMAL             -2 -1  1  1  0  2  3
Nightgaunt       blue    slash     NORMAL             -2 -1  1  2 -2  0  2
MiGo             blue    round     NORMAL             -2 -1  2  1  0  1  3
HaunterOfTheDark blue    square    MASK,ENDLESS       -3 -2  2  2 -2  2  1
FlyingPolyp      blue    hex       PHYSR,N=1,O=1       0 -2  4  3 -3  3  1
FireVampire      blue    star      AMBUSH,PHYSI        0  0  0  1 -2  2  2
Shoggoth         red     diamond   PHYSR,N=1          -1 -1  3  3 -1  3  2
DimensionalShambler red  square    NORMAL             -3 -2  1  1 -2  0  2
Ghost            yellow  moon      PHYSI,UNDEAD       -3 -2  2  1 -3  2  3
DarkYoung        yellow  hex       PHYSR,N=1          -2  0  3  3 -1  3  3
Warlock          yellow  round     MAGICI             -2 -1  1  2 -3  1  2
HoundOfTindalos  green   square    PHYSI              -1 -2  4  2 -1  3  1
Chthonian        green   triangle  NORMAL              1 -2  2  3 -3  3  2
'''
  for line in data.splitlines():
    x = tuple(line.split())
    print format % x

if __name__ == '__main__':
  pass
  #encounters()
  #skills()
  #allies()
  #patrols()
  #spells()
  #investigators()
  #possessions()
  #mythos()
  monsters()