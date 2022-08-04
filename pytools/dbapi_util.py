import zlib
from datetime import datetime, date, time

def decompress(length, data):
    sign = data[:4]
    if sign == b'\xED\xAC\xAC\xED':
        return "".join(chr(x) for x in zlib.decompress(data[4:]))
    return "".join(chr(x) for x in data)

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
