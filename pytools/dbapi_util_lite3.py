from dbapi_util import *

def to_date14(data, format='%Y%m%d%H%M%S'):
    return datetime.strptime(data, format)

def to_date8(data, format='%Y%m%d'):
    return datetime.strptime(data, format)

def to_time6(data, format='%H%M%S'):
    return datetime.strptime(data, format)

def to_char14(data, format='%Y%m%d%H%M%S'):
    return datetime.strftime(data, format)

def to_char8(data, format='%Y%m%d'):
    return datetime.strftime(data, format)

def to_char6(data, format='%H%M%S'):
    return datetime.strftime(data, format)

def get_timestamp():
    return datetime
