#!/usr/bin/python3
import os, datetime
date = datetime.date
today = date.today
year = today().year
dd = today().day
mm = today().month

curpath = ""
done = False    

for day in range(1, 32):
  if day > dd:
    month = (mm-1) % 12
    if month == 0:
      month = 12
      if done == False:
        year = year -1
        done = True
  else:
    month = mm    
  try:
    target = datetime.date(year, month, day)
    targ2 = '%s%02d' % (year, month)
  except:
    break  
  print (target, targ2)
  curpath = '''/firstfour/Current/%s''' % (targ2)
  if os.access('%s' % (curpath), os.R_OK) == False:
    os.system('mkdir -p "%s"' % (curpath))
  for directory in ['/new3/Science',
                    '/new3/Series',
                    '/elements/Series',
                    '/third3'
                  ]:
    for root, dirs, files in os.walk(directory):
      for name in files:
        try:
          stat = os.stat('%s/%s' % (root, name))
        except:
          print ('%s/%s failed stat' % (root, name)) 
          continue 
        file_date = date.fromtimestamp(stat.st_mtime)
        if file_date == target:
          to_name = name.replace(':','').replace('?','')
          def mksub(name):
            name = name.upper()
            if name[:4] == 'THE ' or name[:4].lower() == 'the.':
              name = name[4:]
            if name[:1] in '0123456789':
              name = '0123456789'
            elif name[:1] in 'ABC':
              name = 'ABC'
            elif name[:1] in 'DEFG':
              name = 'DEFG'    
            elif name[:1] in 'HIJKL':
              name = 'HIJKL'  
            elif name[:1] in 'MNO':
              name = 'MNO'  
            elif name[:1] in 'PQR':
              name = 'PQR'  
            elif name[:1] in 'STUV':
              name = 'STUV'  
            elif name[:1] in 'WXYZ':
              name = 'WXYZ'  
            else:
              name = name[:1]
            return name  
          subdir = '/%s' % (mksub(to_name)).strip()
          if os.access('%s%s' % (curpath, subdir), os.R_OK) == False:
            command = 'mkdir -p "%s%s"' % (curpath, subdir)
            print (command)
            os.system(command)
          if os.access('%s%s/%s' % (curpath, subdir, to_name), os.R_OK) == False:
            command = 'cp "%s/%s" "%s%s/%s"' % (root, name, curpath, subdir, to_name)
            print (command)
            os.system(command)
