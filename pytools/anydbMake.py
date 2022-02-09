#!/usr/local/bin/python

import sys
import os.path
import tempfile
import stat
import glob
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--build",      dest="build",      default=False, action="store_true", help='build all anyway')
parser.add_option("-c", "--crackle",    dest="crackle",    default='crackle.jar')
parser.add_option("-f", "--fromdir",    dest="fromdir",    default='/main')
parser.add_option("-j", "--jportal",    dest="jportal",    default='jportal.jar')
parser.add_option("-n", "--nobuild",    dest="nobuild",    default=False, action="store_true", help="do not do the build")
parser.add_option("-o", "--outfile",    dest="outfile",    default='')
parser.add_option("-p", "--pickle",     dest="pickle",     default='pickle.jar')
parser.add_option("-t", "--todir",      dest="todir",      default='/main')
parser.add_option("-v", "--verbose",    dest="verbose",    default=False, action="store_true", help="verbose")
parser.add_option("-I", "--sourcedir",  dest="sourcedir",  default='')
parser.add_option("-O", "--binarydir",  dest="binarydir",  default='')
parser.add_option("-S", "--sources",    dest="sources",    default=False, action="store_true", help="writes sources to outfile if set")
parser.add_option("-T", "--targets",    dest="targets",    default=False, action="store_true", help="writes targets to outfile if set")

(options, args) = parser.parse_args()

def log(*line):
  if (options.verbose == True):
    print('%s ' * len(line) % line)

def fixname(name):
  result = name
  if len(result) > 2 and result[1] == ':':
    result = result[2:]
  result = result.replace('\\','/')
  if options.fromdir != options.todir and result.find(options.fromdir) == 0:
    result = '%s%s' % (options.todir, result[len(options.fromdir):])
  log(result)
  return result

def makedirs(path):
  if os.path.exists(path) == False:
    os.makedirs(path)
  return path  

jportalJar = fixname(options.jportal);log('jportal jar:', jportalJar) 
crackleJar = fixname(options.crackle);log('crackle jar:', crackleJar)
pickleJar  = fixname(options.pickle); log('pickle jar:',  pickleJar)

if len(args) < 1:
  print("usage :-\> anydbMake.py [options] sourcefile")
  parser.print_help()
  exit()

sourceFile = fixname(args[0])
print('Project file:', sourceFile)

class Class(object): pass

def lastmod(name,try_lower=True):
  if os.path.exists(name) == True:
    return os.stat(name)[stat.ST_MTIME]
  elif try_lower == True and os.path.exists(name.lower()) == True:
    return os.stat(name)[stat.ST_MTIME]
  else:
    return 0

def jportal(name, switches, iiFiles, piFiles):
  fd, fname = tempfile.mkstemp('.~tmp')
  os.close(fd)
  command = r'java -jar %s -l %s %s %s' %(jportalJar, fname, name, switches)
  print(command)
  os.system(command)
  for line in open(fname):
    line = line[:-1]
    print(line) 
    if line[:6] == 'Code: ':
      _, tail = os.path.split(line[6:])
      _, ext = os.path.splitext(tail)
      if ext == '.ii':
        iiFile = Class()
        iiFile.name = fixname(line[6:])
        iiFile.lastmod = lastmod(iiFile.name)
        iiFiles.append(iiFile)
      elif ext == '.pi':
        piFile = Class()
        piFile.name = fixname(line[6:])
        piFile.lastmod = lastmod(piFile.name)
        piFiles.append(piFile)
  os.remove(fname)
  return

def crackle(name, switches):
  fd, fname = tempfile.mkstemp('.~tmp')
  os.close(fd)
  command = r'java -jar %s -l %s %s %s' %(crackleJar, fname, name, switches)
  print(command)
  os.system(command)
  for line in open(fname):
    line = line[:-1] 
    print(line)
  os.remove(fname)

def pickle(name, switches):
  fd, fname = tempfile.mkstemp('.~tmp')
  os.close(fd)
  command = r'java -jar %s -l %s %s %s' %(pickleJar, fname, name, switches)
  print(command)
  os.system(command)
  for line in open(fname):
    line = line[:-1] 
    print(line)
  os.remove(fname)

switches = {}
args = {}
args['source_dir'] = options.sourcedir 
args['binary_dir'] = options.binarydir 

def clean(project):
  global dirsep
  dirLists = {}
  dirExts = {}
  for source in project.sources:
    for target in source.targets:
      head, tail = os.path.split(target.name)
      _, ext = os.path.splitext(tail)
      if (head in dirLists) == False:
        dirLists[head] = []
        dirExts[head] = []
      if not tail in dirLists[head]:
        dirLists[head].append(tail)
      if not ext in dirExts[head]:
        dirExts[head].append(ext)
  for head in list(dirLists.keys()):
    for ext in dirExts[head]:
      for fileName in glob.glob('%s%s*%s' % (fixname(head), dirsep, ext)):
        _, ft = os.path.split(fileName)
        if not ft in dirLists[head]:
          print('removing %s' % (fileName))
          os.remove(fileName)

def make_ib_files(pathlist):
  ibFiles = []
  parts = pathlist.split(';')
  for part in parts:
    if len(part) > 3 and part[-3:] in ['.ib', '.ic']:
      ibFiles.append(part)
      continue
    files = glob.glob('%s%s*.ib' % (fixname(part), dirsep))
    for file in files:
      ibFiles.append(file)  
  return ibFiles

def remove_comment(line):
  p = line.find('#')
  if p >= 0:
    line = line[:p]
  return line

def expand(line):
  result = ''
  while True:
    s = line.find('${')
    if s < 0:
      result += line
      break
    result += line[:s]
    line = line[s+2:]
    e = line.find('}')
    if e < 0:
      result += line
      break
    arg = line[:e]
    line = line[e+1:]
    if arg in args:
      result += args[arg]
  return result

state=0;JPORTAL=1;CRACKLE=2;PICKLE=3;SOURCE=4;IDL=5;OCIAPI=6;OCISI=7;APP=8

def parse_anydb(sourceFile):
  ifile = open(sourceFile, 'r')
  lines = ifile.readlines()
  ifile.close()
  project = None
  switches[CRACKLE] = ''
  switches[JPORTAL] = ''
  switches[PICKLE] = ''
  switches[OCIAPI] = ''
  lineNo = 0
  for line in lines:
    lineNo += 1
    line=expand(remove_comment(line.strip()))
    if len(line) == 0:
      continue
    fields=line.split('=')
    if len(fields) == 2:
      args[fields[0]] = fields[1]
      continue
    fields=line.split()
    if fields[0] == 'include':
      if len(fields) == 2:
        ifile = open(fields[1], 'r')
        includeLines = ifile.readlines()
        ifile.close()
        lines[lineNo:lineNo] = includeLines
      continue
    if fields[0] == 'project' and len(fields) > 1:
      project = Class()
      project.name = fixname(fields[1])
      project.switches = []
      project.sources = []
      project.ocisis = []
      project.ptables = []
      project.masks = {}
      project.masks[JPORTAL] = {}
      project.masks[CRACKLE] = {}
      project.masks[PICKLE] = {}
      project.masks[OCIAPI] = {}
      project.idlname = None
      project.idls = {}
      project.apps = {}
      project.idls['iifile'] = iiFiles = []
      project.apps['pifile'] = piFiles = []
      continue
    if project == None:
      print('expecting project name')
      return None
    if fields[0] == 'jportal':
      state = JPORTAL
      continue
    if fields[0] == 'crackle':
      state = CRACKLE
      continue
    if fields[0] == 'pickle':
      state = PICKLE
      continue
    if fields[0] == 'ociapi':
      state = OCIAPI
      continue
    if fields[0] == 'source':
      state = SOURCE
      continue
    if fields[0] == 'idl':
      state = IDL
      continue
    if fields[0] == 'app':
      state = APP
      continue
    if fields[0] == 'ocisi':
      state = OCISI
      continue
    if state in [JPORTAL, CRACKLE, PICKLE]:
      if len(fields) > 1:
        dir = fixname(fields[1])
        makedirs(dir)
        switches[state] += '-o %s %s ' % (dir, fields[0])
      else:
        dir = ''  
        switches[state] += '%s ' % (fields[0])
      if len(fields) > 2:
        if dir not in project.masks:
          project.masks[state][dir] = []
        for mask in fields[2:]:
          project.masks[state][dir].append(mask)
      continue
    if state in [OCIAPI]:
      if len(fields) > 1:
        dir = fixname(fields[1])
        makedirs(dir)
        switches[state] += '%s|%s ' % (dir, fields[0])
      else:
        dir = ''  
        switches[state] += '%s ' % (fields[0])
      if len(fields) > 2:
        if dir not in project.masks:
          project.masks[state][dir] = []
        for mask in fields[2:]:
          project.masks[state][dir].append(mask)
      continue
    if state == SOURCE:
      source = Class()
      source.targets = []
      source.name = fixname(fields[0])
      source.noTargets = 0
      source.lastmod = lastmod(source.name)
      project.sources.append(source)
      continue
    if state == OCISI:
      ocisi = Class()
      ocisi.targets = []
      ocisi.name = fixname(fields[0])
      ocisi.noTargets = 0
      ocisi.lastmod = lastmod(ocisi.name)
      project.ocisis.append(ocisi)
      continue
    if state == APP:
      source = Class()
      app_list = ('appfile', 'pmfile', 'prfile', 'pifile')
      app_type = fields[0]
      if (not app_type in app_list):
        print('%s - not a valid - not in %s' % (app_type, repr(app_list)))
        continue
      source.name = fixname(fields[1])
      source.lastmod = lastmod(source.name)
      if app_type == 'appfile':
        switches['appTarget'] = source.name
        continue
      if app_type == 'pmfile':
        switches['appModule'] = source.name
        continue
      if app_type not in project.apps:
        project.apps[app_type] = []
      project.apps[app_type].append(source)
      continue
    if state == IDL:
      source = Class()
      idl_list = ('idlfile', 'imfile', 'ibfile', 'icfile', 'iifile')
      idl_type = fields[0]
      if (not idl_type in idl_list):
        print('%s - not a valid - not in %s' % (idl_type, repr(idl_list)))
        continue
      source.name = fixname(fields[1])
      source.lastmod = lastmod(source.name)
      if idl_type == 'idlfile':
        switches['idlTarget'] = source.name
        continue
      if idl_type == 'imfile':
        switches['idlModule'] = source.name
        continue
      if idl_type not in project.idls:
        project.idls[idl_type] = []
      project.idls[idl_type].append(source)
      continue
  return project

def add_target(source, file):
  target = Class() #Target()
  target.name = fixname(file)
  target.lastmod = lastmod(target.name, False)
  source.targets.append(target)
  source.noTargets = len(source.targets)

def get_targets(source, name, mask, project):
  masks = project.masks[JPORTAL][mask]
  for wildcard in masks:
    check_it = False
    if wildcard.find('%l') >= 0:
      wildcard = wildcard.replace('%l', name.lower())
    elif wildcard.find('%u') >= 0:
      wildcard = wildcard.replace('%u', name.upper())
    elif wildcard.find('%a') >= 0:
      wildcard = wildcard.replace('%a', name)
    elif wildcard.find('%i') >= 0:
      check_it = True
      empty = wildcard.replace('%i', name.upper())
      wildcard = wildcard.replace('%i', '?'*len(name))
    files = glob.glob('%s/%s' % (mask, wildcard))
    if len(files) == 0:
      if check_it == True:
        file = '%s/%s' % (mask, empty)
      else:
        file = '%s/%s' % (mask, wildcard)
      add_target(source, file)
      continue
    for file in files:
      if check_it == True:
        _, base = os.path.split(file)
        fname, _ = os.path.splitext(base)
        if fname.upper() != name.upper():
          continue
      add_target(source, file)

def derive_targets(project):
  mask_keys = sorted(project.masks[JPORTAL])
  for source in project.sources:
    _, base = os.path.split(source.name)
    name, _ = os.path.splitext(base)
    for mask in mask_keys:
      get_targets(source, name, mask, project)

def add_to_group(groups, type, filename):
  if os.path.exists(filename) ==  True:
    flist = filename.split('/')
    marker = ''
    if type == 'TARGET':
      marker = flist[-2]
      groupname = r'%s-%s Files' % (flist[-3].upper(), flist[-2].upper())
    else:
      groupname = r'%s-%s Files' % (type.upper(), flist[-2].upper())
    if not groupname in groups:
      groups[groupname] = [marker]
    groups[groupname].append(filename)    
      
def build_outfile(outfile_name):
  outfile = open(fixname(outfile_name), 'wt')
  groups = {}
  if options.sources == True:
    outfile.write('set (sources\n')  
    for source in project.sources:
      outfile.write('  %s\n' % (source.name))
      add_to_group(groups, 'JPORTAL', source.name)
    if 'idlTarget' in switches:
      target_name = fixname(switches['idlTarget'])
      if 'idlModule' in switches:
        module_name = fixname(switches['idlModule'])    
        outfile.write('  %s\n' % (module_name))
        add_to_group(groups, 'CRACKLE', module_name)
      else:
        outfile.write('  %s\n' % (target_name)) 
        add_to_group(outfile, groups, 'CRACKLE', target_name)
      for key in project.idls: 
        for source in project.idls[key]:
          outfile.write('  %s\n' % (source.name))
          add_to_group(groups, 'CRACKLE', source.name)
    if 'appTarget' in switches:          
      target_name = fixname(switches['appTarget'])  
      if 'appModule' in switches:
        module_name = fixname(switches['appModule'])    
        outfile.write('  %s\n' % (module_name))
        add_to_group(groups, 'PICKLE', module_name)
      else:
        outfile.write('  %s\n' % (target_name)) 
        add_to_group(groups, 'PICKLE', target_name)
      for key in project.apps: 
        for source in project.apps[key]:
          outfile.write('  %s\n' % (source.name))
          add_to_group(groups, 'PICKLE', source.name)
    outfile.write(')\n\n')
  if options.targets == True:
    outfile.write('set (targets\n')  
    for source in project.sources:
      for target in source.targets:  
        if os.path.exists(target.name) ==  True:  
          outfile.write('  %s\n' % (target.name))
          add_to_group(groups, 'TARGET', target.name)
    if 'idlTarget' in switches and 'idlModule' in switches:
      target_name = fixname(switches['idlTarget'])
      outfile.write('  %s\n' % (target_name)) 
      add_to_group(groups, 'CRACKLE', target_name)
    if 'appModule' in switches and 'appTarget' in switches:
      target_name = fixname(switches['appTarget'])
      outfile.write('  %s\n' % (target_name)) 
      add_to_group(groups, 'PICKLE', target_name)
    outfile.write(')\n\n')
    for groupname in sorted(groups):
      files = groups[groupname]
      marker = files[0]
      if len(marker) > 0:
        r = f'.*/{marker}/.*'
      else:
        r = '.*'  
      files = files[1:]
      exts = []
      for file in files:
        _, ext = os.path.splitext(file)
        if not ext in exts:
          exts.append(ext)
      regex = f'REGULAR_EXPRESSION "{r}[.](' 
      pipe = ''         
      for ext in exts:
        regex += '%s%s' % (pipe, ext[1:])
        pipe = '|'
      regex += ')$"'  
      outfile.write('source_group ("%s" %s\n' % (groupname, regex))
      outfile.write('  FILES\n')
      for filename in sorted(files):
        outfile.write('  %s\n' % (filename))
      outfile.write('  )\n\n')  
    outfile.write('set_source_files_properties (${targets} PROPERTIES GENERATED TRUE)\n')
  outfile.close() 

project = parse_anydb(sourceFile)
derive_targets(project)
projmod = lastmod(sourceFile)
jportalJarMod = lastmod(jportalJar)
crackleJarMod = lastmod(crackleJar)
pickleJarMod = lastmod(pickleJar)
sourceList = []
reasons = {}
if 'ibfile' not in project.idls:
  project.idls['ibfile'] = []
if 'icfile' not in project.idls:
  project.idls['icfile'] = []
ibFiles = project.idls['ibfile']
icFiles = project.idls['icfile']
iiFiles = project.idls['iifile']
if 'prfile' not in project.apps:
  project.apps['prfile'] = []
prFiles = project.apps['prfile']
piFiles = project.apps['pifile']
#-------------------------------------------------------
if len(options.outfile) > 0:
  build_outfile(options.outfile)
if options.nobuild == True:
  exit(0)
#-------------------------------------------------------
for source in project.sources:
  if source.noTargets == 0:
    reasons[source.name] = 'no targets'
    log('%s %s' % (source.name, reasons[source.name]))
    sourceList.append(source.name)
    continue
  if options.build == True:
    reasons[source.name] = 'option always build'
    compile=True
  else:
    compile=False
    for target in source.targets:
      if source.lastmod > target.lastmod:
        reasons[source.name] = 'source newer than target %s' % (target.name)
        compile=True
        break
      if jportalJarMod > target.lastmod:
        reasons[source.name] = 'jar newer than target %s' % (target.name)
        compile=True
        break
  if compile == True:
    log('%s %s' % (source.name, reasons[source.name]))
    sourceList.append(source.name)
    for target in source.targets:
      if os.path.exists(target.name) == True:
        print('removing %s' % (target.name))
        try:
          os.remove(target.name)
        except:
          log('failed to remove %s' % (target.name))  
  else:
    log(source.name, 'up to date')
    for target in  source.targets:
      head, tail = os.path.split(target.name)
      root, ext = os.path.splitext(tail)
      if ext == '.ii':
        iiFile = Class()
        iiFile.name = fixname(target.name)
        iiFile.lastmod = lastmod(iiFile.name)
        iiFiles.append(iiFile)
if len(sourceList) > 0:
  fname = '%s.~tmp' % (sourceFile)
  temp = open(fname, 'wt')
  #fd, fname = tempfile.mkstemp('.~tmp', text=True)
  for source in sourceList:
    if len(reasons[source]) > 0:
      print('%s --- %s' % (source, reasons[source]))
    temp.write('%s\n' % (source))
  temp.close()
  jportal('-f %s' % (fname), switches[JPORTAL], iiFiles, piFiles)
  os.remove(fname)
#------------------------------------------------------------------
compile = False
if 'idlModule' in switches and 'idlTarget' in switches:
  idlTarget = Class()
  idlTarget.name = fixname(switches['idlTarget'])
  idlTarget.lastmod = lastmod(idlTarget.name)
  idlModule = Class()
  idlModule.name = fixname(switches['idlModule'])
  idlModule.lastmod = lastmod(idlModule.name)
  if idlModule.lastmod > idlTarget.lastmod:
    compile = True
  if crackleJarMod > idlTarget.lastmod:
    compile = True
  for iiFile in iiFiles:
    if iiFile.lastmod > idlTarget.lastmod:
      compile = True
  for ibFile in ibFiles:
    if ibFile.lastmod > idlTarget.lastmod:
      compile = True
  for icFile in icFiles:
    if icFile.lastmod > idlTarget.lastmod:
      compile = True
  if compile == True:
    outfile = open(idlTarget.name, 'wt')
    ifile = open(idlModule.name, 'rt')
    outfile.write(ifile.read())
    ifile.close() 
    for iiFile in iiFiles:
      outfile.write('// *** %s\n' % (iiFile.name))
      ifile = open(iiFile.name, 'rt')
      outfile.write(ifile.read())
      ifile.close()
    for ibFile in ibFiles:
      outfile.write('// *** %s\n' % (ibFile.name))
      ifile = open(ibFile.name, 'rt')
      outfile.write(ifile.read())
      ifile.close()
    outfile.close()
elif 'idlTarget' in switches:
  idlTarget = Class()
  idlTarget.name = fixname(switches['idlTarget'])
  idlTarget.lastmod = lastmod(idlTarget.name)
  compile = True
if compile == True:
  crackle(idlTarget.name, switches[CRACKLE])
#----------------------------------------------------------------
compile = False
if 'appModule' in switches and 'appTarget' in switches:
  appTarget = Class()
  appTarget.name = fixname(switches['appTarget'])
  appTarget.lastmod = lastmod(appTarget.name)
  appModule = Class()
  appModule.name = fixname(switches['appModule'])
  appModule.lastmod = lastmod(appModule.name)
  if appModule.lastmod > appTarget.lastmod:
    compile = True
  if pickleJarMod > appTarget.lastmod:
    compile = True
  for piFile in piFiles:
    if piFile.lastmod > appTarget.lastmod:
      compile = True
  for prFile in prFiles:
    if prFile.lastmod > appTarget.lastmod:
      compile = True
  if compile == True:
    outfile = open(appTarget.name, 'wt')
    ifile = open(appModule.name, 'rt')
    outfile.write(ifile.read())
    ifile.close() 
    for prFile in prFiles:
      outfile.write('// *** %s\n' % (prFile.name))
      ifile = open(prFile.name, 'rt')
      outfile.write(ifile.read())
      ifile.close()
    for piFile in piFiles:
      outfile.write('// *** %s\n' % (piFile.name))
      ifile = open(piFile.name, 'rt')
      outfile.write(ifile.read())
      ifile.close()
    outfile.close()
elif 'appTarget' in switches:
  appTarget = Class()
  appTarget.name = fixname(switches['appTarget'])
  appTarget.lastmod = lastmod(appTarget.name)
  compile = True
if compile == True:
  pickle(appTarget.name, switches[PICKLE])

xxx = '''\
 BlankPadded(0)=0
 CharZ(0)=0
 ConnReqd(1)=1
 ControlDB()=
 ExitReqd(0)=0
 IDLUbi(0)=0
 Internal(0)=0
 LogDir()=
 LogExt(.log)=.log
 OneSQLScript(0)=0
 UConnect()=
 UnderScore(0)=0
 EightByte(0)=0
 ExtendedPAS(0)=0
 ExtendedVB(0)=0
 IDLModule()=
 NoDomain(0)=0
 PARMSDescr()=
 PARMSLookup()=
 PrefixVBClasses(0)=0
 Show()=
 TargetVBforADOR(0)=0
 ViewOnly(0)=0
 ExtendedC(1)=1
 LittleTrue(1)=1
 Version2Bin(1)=1
 UseCSFields(0)=0
 SqlAuditExt(.aud)=.aud
 SqlConExt(.con)=.con
 SqlGrantExt(.gra)=.gra
 SqlIdxExt(.idx)=.idx
 SqlProcExt(.pro)=.pro
 SqlSnapExt(.pop)=.pop
 SqlTableExt(.tab)=.tab
 SqlViewsExt(.vws)=.vws
 TargetARCHIVE(0)=0
 ArchiveDir()=
 ArchiveExt(.arc)=.arc
 TargetC(0)=0
 CDir()=
 CExt(.sh)=.sh
 TargetCSAdoNet(0)=0
 CSAdoNetDir()=
 CSAdoNetExt(.cs)=.cs
 TargetCSIDL2(0)=0
 CSIDL2Dir()=
 CSIDL2Ext(.cs)=.cs
 TargetCSNet7(0)=0
 CSNet7Dir()=
 CSNet7Ext(.cs)=.cs
 TargetCSRW(0)=0
 CSRWDir()=
 CSRWExt(.cs)=.cs
 TargetIDL(0)=0
 IDLDir()=
 IDLExt(.ii)=.ii
 TargetPARMS(0)=0
 PARMSDir()=
 PARMSExt(.pi)=.pi
 TargetPAS(0)=0
 PASDir()=
 PASExt(.pas)=.pas
 TargetPython(0)=0
 PythonDir()=
 PythonExt(.py)=.py
 TargetSQL(0)=0
 SqlDir()=
 SqlExt(.sql)=.sql
 TargetSO(0)=0
 SODir()=
 SOExt(.so)=.so
 TargetVB(0)=0
 VBDir()=
 VBExt(.bas)=.bas
 TargetVBforIDL(0)=0
 VBforIDLDir()=
 VBforIDLExt(.bas)=.bas
 TargetVB5(0)=0
 VB5Dir()=
 VB5Ext(.bas)=.bas
 TargetVBCode3(0)=0
 VBCode3Dir()=
 VBCode3Ext(.bas)=.bas
 TargetVBNet7(0)=0
 VBNet7Dir()=
 VBNet7Ext(.vb)=.vb
'''
    