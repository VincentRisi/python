import intrinsicMethods
import xml.etree.ElementTree as ET
from xml.dom import minidom

import time
from DEPRECATED_STRING import *
import sys
import os

class PuttyConst:
    XML = 0
    Text = 1
    File = 2

class LogLevelConst(object):
   Debug    = 0
   Info     = 1
   Warning  = 2
   Error    = 3

connect = None

tracking = False
logs = []
streams = []
replies = []
messages = []
files = []
comments = []
currentFile = ''
currentFilePos = 0
puttyTrace = 1
env = 0

def cleanUp():
    global logs
    global streams
    global replies
    global messages
    global comments
    logs = []
    streams = []
    replies = []
    messages = []
    comments = []

def setFiles(fileList):
    global tracking
    global files

    tracking = True
    files = fileList
    

def printCaller():
    if puttyTrace == 1:
        sf = sys._getframe(2)
        print('#',sf.f_code.co_filename.split('\\\\')[-1],'(' + str(sf.f_lineno) + ')->',sys._getframe(1).f_code.co_name)

def setEnvironment(mode):
    global env
    if mode == 0:
        print('Running in DEV mode')
    else:
        print('Running in PROD mode')
    
    env = mode

def sysdate(delim=''):
    return time.strftime('%Y' + delim + '%m' + delim + '%d',time.localtime(time.time()))
def systime(delim=''):
    return time.strftime('%H' + delim + '%M' + delim + '%S',time.localtime(time.time()))

def log(text, LogType = LogLevelConst.Info):
   global connect
   if connect != None:
      intrinsicMethods._log(LogType, text)
   else:
      print (text)

def logDebug(text):
   global connect
   if connect != None:
      intrinsicMethods._log(LogLevelConst.Debug, str(text))
   else:
      print (text)

def logInfo(text):
   global connect
   if connect != None:
      intrinsicMethods._log(LogLevelConst.Warning, str(text))
   else:
      print (text)

def logWarning(text):
   global connect
   if connect != None:
      intrinsicMethods._log(LogLevelConst.Warning, str(text))
   else:
      print (text)

def logError(text):
   global connect
   if connect != None:
      intrinsicMethods._log(LogLevelConst.Error, str(text))
   else:
      print (text)

def printline(s):
    logs.append(s)
    intrinsicMethods._printline(s)

def printerrline(s):
    intrinsicMethods._printerrline(s)

def inputline():
    return intrinsicMethods._inputline()

def readModuleLines(module):
    return intrinsicMethods._readModuleLines(module).splitlines()

def displayModuleLine(module,line):
    return intrinsicMethods._displayModuleLine(module,line)

def xmlparse(s):
    return intrinsicMethods._xmlparse(s)

def xmlbuild(s):
    xml = intrinsicMethods._xmlbuild(s)
    return xml

def readNextFile():
    global currentFilePos
    global currentFile
    currentFile = files[currentFilePos]
    print(f'==> reading file {currentFile}')
    fp = open(currentFile, 'r')
    data = ''
    if fp.mode == 'r':
        cleanUp()
        contents = fp.read()
        xdoc = ET.fromstring(contents)        
        data = xdoc.text
        attr = xdoc.attrib
        missing = {'Id', 'RelatedId', 'Queue', 'MessageType'} - set(attr)
        if len(missing) > 0:
           raise Exception(f'file does not contain the attribute {missing}')
        intrinsicMethods._setMessage(int(xdoc.attrib['Id']), int(xdoc.attrib['RelatedId']), xdoc.attrib['Queue'],  xdoc.attrib['Queue'], data, int(xdoc.attrib['MessageType']), 17)
    else:
        raise Exception('cannot open file ' + f)
    currentFilePos = currentFilePos + 1
    return (data, int(xdoc.attrib['MessageType']))

def writeFile():
    global currentFile

    fname = os.path.dirname(currentFile) + '\\' + os.path.basename(currentFile) + '.out'
    print(f'==> writing file {fname}')
    fp = open(fname, 'w')

    a = ET.Element('Result')
    for s in streams:
        # (queueid, outstream, streamType, description, type)
        b = ET.SubElement(a, 'Stream')
        b.text = s[1]
        b.attrib = {'type':s[2], 'queue': s[0], 'description':s[3]}
    for m in messages:
        # (queueid, responsequeueid, message, type, priority)
        b = ET.SubElement(a, 'Message')
        b.text = m[2]
        b.attrib = {'queue': m[0], 'responseQueue': m[1], 'type': str(m[3]), 'priority': str(m[4]) }
    for r in replies:
        # (what, type)
        b = ET.SubElement(a, 'Reply')
        b.text = r[0]
        b.attrib = {'type':str(r[1])}

    ls = ''
    for l in logs:
        ls = ls + l + '\r\n'

    l = ET.SubElement(a, 'Log')
    l.text = ls

    rough_string = ET.tostring(a, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    fp.write(reparsed.toprettyxml(indent="\t"))
    fp.close()


def readmessage():
    printCaller()
    global currentFilePos
    global tracking

    if tracking and files != None and len(files) > 0 and currentFilePos < len(files):
        s, t = readNextFile()
    else:
        s, t = intrinsicMethods._readmessage()
    if t == PuttyConst.XML or t == PuttyConst.File:
        d = xmlparse(s)
        if d == None:
            raise Exception('invalid xml payment message:' + s)
        else:
            return d
    return s

def readmessageraw():
    printCaller()
    global currentFilePos
    global tracking
    if tracking and files != None and len(files) > 0 and currentFilePos < len(files):
        s, t = readNextFile()
    else:
        s, t = intrinsicMethods._readmessage()
    return s, t

def wait_message():
    if files != None and len(files) > 0:
        if currentFilePos < len(files):
            return 0
        return 3
    else:
        return intrinsicMethods._waitMessage()
def run_finally(runAccessMode):
    if runAccessMode == 'ro':
        intrinsicMethods._rollback()
    return intrinsicMethods._runFinally()
def writemessage(queueid, responsequeueid, message, type, priority=17):
    printCaller()
    global tracking
    if tracking:
        messages.append((queueid, responsequeueid, message, type, priority))
    rc = intrinsicMethods._writemessage(queueid, responsequeueid, message, type, priority)
    if rc == 0:
        raise Exception('The call to writeMessage(%s,%s,%s,%s,%s) failed' % (queueid, responsequeueid, message, type, priority))
    return rc
def route(s):
    printCaller()
    rc = intrinsicMethods._routemessage(s.upper())
    if rc == 0:
        raise Exception('The call to route(%s) failed, invalid queue' % (s))
    return rc
def getInterfaceData():
    printCaller()
    if connect == None or connect.loggedOn == 0:
       return 0, 0, 0, 0, 0, 0, 0, 0
    # returns messageId, relatedMessageId, responseQueue, eventQueue, serviceQueue, toQueue, priority, MessageRef
    list = intrinsicMethods._getInterfaceData()
    return list
def setMessageStatus(queueType, id, status):
    printCaller()
    rc = intrinsicMethods._setMessageStatus(queueType, id, status)
    return rc
def setCurrentMessage(msgId):
    printCaller()
    rc = intrinsicMethods._setCurrentMessage(msgId)
    return rc
def commit():
    printCaller()
    global tracking
    if tracking:
        writeFile()
    intrinsicMethods._commit()
def rollback():
    printCaller()
    global tracking
    if tracking:
        writeFile()
    intrinsicMethods._rollback()
def stream(queueid, outstream, streamType, description, type=PuttyConst.Text):
    printCaller()
    global tracking
    if tracking:
        streams.append((queueid, outstream, streamType, description, type))
    rc = intrinsicMethods._stream(queueid, outstream, streamType, description, type)
    if rc == 0:
        raise Exception('The call to stream(%s,%s,%s,%s,%s) failed' % (queueid, outstream, streamType, description, type))
    return rc
def lastStreamIndex():
    printCaller()
    return intrinsicMethods._lastStreamIndex()
def streamAfter(queueid, outstream, streamType, description, index, type=PuttyConst.XML):
    printCaller()
    rc = intrinsicMethods._streamAfter(queueid, outstream, streamType, description, index, type)
    if rc == 0:
        raise Exception('The call to streamAfter(%s,%s,%s,%s,%s,%s) failed' % (queueid, outstream, streamType, description, index, type))
    return rc
def streamNext(queueid, outstream, streamType, description, type=PuttyConst.XML):
    printCaller()
    rc = intrinsicMethods._streamNext(queueid, outstream, streamType, description, type)
    if rc == 0:
        raise Exception('The call to streamNext(%s,%s,%s,%s,%s) failed' % (queueid, outstream, streamType, description, type))
    return rc
def reply(what, type=PuttyConst.Text):
    printCaller()
    global tracking
    if tracking:
        replies.append((what, type))
    return intrinsicMethods._reply(what, type)
def comment(what):
    printCaller()
    global tracking
    if tracking:
        comments.append(what)
    intrinsicMethods._comment(what)
def saveSummary(summaryString, type=PuttyConst.XML):
    printCaller()
    intrinsicMethods._saveSummary(summaryString, type)
def zcompress(inData, outDataLen):
    printCaller()
    return intrinsicMethods._zcompress(inData, outDataLen)
def zdecompress(inData, outDataLen):
    printCaller()
    return intrinsicMethods._zdecompress(inData, outDataLen)
def base64_encode(inData):
    printCaller()
    return intrinsicMethods._base64_encode(inData)
def base64_decode(inData):
    printCaller()
    return intrinsicMethods._base64_decode(inData)
def setMessage(Messageid, RelMessageid, QueueName, ResponseQueueName, Content, type=PuttyConst.Text, Priority=17):
    printCaller()
    return intrinsicMethods._setMessage(Messageid, RelMessageid, QueueName, ResponseQueueName, Content, type, Priority)
def logon(config):
    global connect
    connectstr = config['SqlLogonString']
    binfile = config['SqlapiBinFile']
    logfile = config['LogFile']
    loglevel = config['LogLevel']
    logdisplay = int(config['LogDisplay'])
    logmaxsize = int(config['LogMaxSize'])
    loghistext  = config['LogHistExt']
    queuename = config['QueueName'].upper()
    queuefilepath = config['QueueFilePath']
    routePlanName = config['RoutePlanName'].upper()
    routePlanType = config['RoutePlanType']
    lockfilepath = config['lockFilePath']
    trace = int(config['Trace'])
    tracefile = config['TraceFile']
    tracemaxsize = int(config['TraceMaxSize'])
    tracedisplay = int(config['TraceDisplay'])
    nodaysback = int(config['NoDaysBack'])
    rc, error = intrinsicMethods._logon(queuename, queuefilepath, binfile, connectstr, logfile, loglevel, logdisplay, logmaxsize, loghistext,
                                 routePlanName, routePlanType, lockfilepath, trace, tracefile, tracemaxsize, tracedisplay, nodaysback)
    if rc != 0:
        print ('Error: {0}:{1}'.format(rc, error))
        return rc
    connect = DBConnect()
    connect.loggedOn = 1
    return rc

class Proforma:
    def __init__(self, list):
        for i in list:
            self.__dict__[i.upper()] = None
    def __setattr__(self, n, v):
        n = n.upper()
        if n in self.__dict__:
            self.__dict__[n] = v
        else:
            raise n + ' is not a member of this class'
    def __getattr__(self, n):
        return self.__dict__[n.upper()]

class StdoutCatcher:
    def __init__(self):
        self.data = ''
    def write(self, stuff):
        self.data = self.data + stuff
        data = self.data
        if len(data) > 0 and data[-1] == '\n':
            lines = data.splitlines()
            for line in lines:
                printline(line)
            self.data = ''
    def flush(self):
        line = self.data
        if len(line) > 0:
            printline(line)

class StderrCatcher:
    def __init__(self):
        self.data = ''
    def write(self, stuff):
        self.data = self.data + stuff
        data = self.data
        if len(data) > 0 and data[-1] == '\n':
            lines = data.splitlines()
            for line in lines:
                printerrline(line)
            self.data = ''
    def flush(self):
        line = self.data
        if len(line) > 0:
            printline(line)

class StdinCatcher:
    def __init__(self):
        self.data = ''
    def read(self, size=-1):
        if len(self.data) < size:
            line = inputline()
            self.data += line
        line = self.data[0:size]
        self.data = self.data[size + 1:]
        return line
    def readline(self):
        return inputline()

class DBError(BaseException):
    def __init__(self, value, rc, ociErr):
        self.value = value
        self.rc = rc
        self.ociErr = ociErr
    def __str__(self):
        return repr(self.value)

class DBConnect(object):
    def __init__(self):
        self.loggedOn = 0
    def __del__(self):
        if self.loggedOn == 1:
            self.logoff()
    def logoff(self):
        self.loggedOn = 0
        rc, errbuf = intrinsicMethods._dbLogoff()
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
    def action(self, proc, data):
        ociErr, rc, errbuf = intrinsicMethods._dbExec(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return data
    def query(self, proc, data):
        ociErr, rc, queryid, errbuf = intrinsicMethods._dbQuery(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return queryid
    def fetch(self, queryid):
        ociErr, rc, hasData, result, errbuf = intrinsicMethods._dbFetch(queryid)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return hasData, result
    def close(self, queryid):
        intrinsicMethods._dbClose(queryid)
    def cancel(self, queryid):
        intrinsicMethods._dbClose(queryid)
    def commit(self):
        intrinsicMethods._dbCommit()
    def rollback(self):
        intrinsicMethods._dbRollback()
    def toRec(self, proc, data):
        rc, result, errbuf = intrinsicMethods._dbToRec(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
        return result
    def fromRec(self, proc, rec):
        rc, result, errbuf = intrinsicMethods._dbFromRec(proc, rec)
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
        return result

def trap_stdio():
    sys.stdout = StdoutCatcher()
    sys.stderr = StderrCatcher()
    sys.stdin = StdinCatcher()

