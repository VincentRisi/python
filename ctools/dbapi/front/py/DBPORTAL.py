''' INTRINSICS.PY (aka DBPORTAL.py)
This version does allow for multiple connections
'''
import pyportal

_connIds = {}

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
        rc, errbuf = pyportal._dbLogoff()
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
    def action(self, proc, data):
        ociErr, rc, errbuf = pyportal._dbExec(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return data
    def query(self, proc, data):
        ociErr, rc, queryid, errbuf = pyportal._dbQuery(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return queryid
    def fetch(self, queryid):
        ociErr, rc, hasData, result, errbuf = pyportal._dbFetch(queryid)
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return hasData, result
    def close(self, queryid):
        pyportal._dbClose(queryid)
    def cancel(self, queryid):
        pyportal._dbClose(queryid)
    def commit(self):
        pyportal._dbCommit()
    def rollback(self):
        pyportal._dbRollback()
    def ping(self):
        rc, errBuf = pyportal._dbPing()
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return rc, errBuf
    def connected(self):
        rc, errBuf =  pyportal._dbConnected()   
        if rc < 0:
            raise DBError(errbuf, -rc, ociErr)
        return rc, errBuf
    def toRec(self, proc, data):
        rc, result, errbuf = pyportal._dbToRec(proc, data)
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
        return result
    def fromRec(self, proc, rec):
        rc, result, errbuf = pyportal._dbFromRec(proc, rec)
        if rc < 0:
            raise DBError(errbuf, -rc, 0)
        return result

connect = DBConnect()

def logon(binfile, user, password, server, useServer=False, usePassword=False):
    '''
    Returns a connection id
    A dict is kept by user[/password][@server] as key for connId
    useServer and usePassword options can be set True to affect key.
    '''    
    global connect
    connId, err = pyportal._dbInit()
    if connId <= 0:
        raise DBError(f'pyportal._dbInit() returned {connId} should be greater than zero', connId, f'{user}@{server} {err}')
    key = user    
    if usePassword == True:
        key = f'{key}/{password}'
    if useServer == True:
        key = f'{key}@{server}'
    _connIds[key] = connId    
    connectstr = f'{user}/{password}@{server}'
    print (f'binfile: {binfile} connectstr:{connectstr}')
    rc, errbuf = pyportal._dbLogon(binfile, connectstr)
    if rc < 0:
        raise DBError(errbuf, -rc, 0)
    connect.loggedOn = 1
    return connId

def db_set_user(key):
    ''' activate connection by key
    This is useful for multiple coonections
    depending on logon useServer and usePassword options used
    key is of user[/password][@server]format
    '''
    if not key in _connIds:
        raise DBError(f'{key} is not in connIds ', -1, 0)
    connId = _connIds[key]
    return db_set_connId(connId)

def db_set_connId(connId):
    ''' activate connection by id
    This is useful for multiple connections
    each connection is given a unique connection id.
    '''    
    pyportal._dbSetConnId(connId)    
    return connId

def db_ping(user=None, connId=None):
    ''' ping 
    If using multiple connects allows for user or connId
    a single parameter will be assumed to be user
    no parameter will use the last connect    
    '''
    global connect
    if user is not None:
        db_set_user(user)
    elif connId is not None:
        db_set_connId(connId)     
    return connect.ping()

def db_connected(user=None, connId=None):
    ''' connected 
    If using multiple connects allows for user or connId
    a single parameter will be assumed to be user
    no parameter will use the last connect    
    '''
    global connect
    if user is not None:
        db_set_user(user)
    elif connId is not None:
        db_set_connId(connId)     
    return connect.connected()

def log_open(str):
    return pyportal._logging(0, str)

def log_debug(str):
    return pyportal._logging(1, str)

def log_info(str):
    return pyportal._logging(2, str)

def log_warn(str):
    return pyportal._logging(3, str)

def log_error(str):
    return pyportal._logging(4, str)

def log_display(str):
    return pyportal._logging(5, str)

def log_level(str):
    return pyportal._logging(6, str)
 
def log_receive(str):
    return pyportal._logging(7, str)
 
def log_transmit(str):
    return pyportal._logging(8, str)

