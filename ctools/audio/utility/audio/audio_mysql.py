audio_dir = r'C:\vlab\python\ctools\audio\utility\audio'
pyasdata_dir = rf'{audio_dir}\pyasdata'
support_dir = rf'{audio_dir}\support'
dbapi_dir =  rf'{audio_dir}\dbapi'
mysql_dir =  rf'{dbapi_dir}\mysql'
import sys
sys.path.append(pyasdata_dir)
sys.path.append(support_dir)
sys.path.append(dbapi_dir)
sys.path.append(mysql_dir)
import mysql
from audio import *

main(pyasdata_dir)