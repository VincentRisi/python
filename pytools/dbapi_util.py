import zlib, base64
from datetime import datetime, date, time
from struct import unpack, pack

def decompress(length, data):
    sign = unpack('!L', data[:4])[0]
    if sign == 0xEDACACED:
        result = "".join(chr(x) for x in zlib.decompress(data[4:]))
        return result
    sign = unpack('!L', data[4:8])[0]
    if sign == 0xEDACACED:
        result = "".join(chr(x) for x in zlib.decompress(data[8:]))
        return result
    result = "".join(chr(x) for x in data)
    return result

def compress(data):
    bbb = zlib.compress(data)
    n = len(bbb)
    format = '!LL' 
    pdata = pack(format,n,0xEDACACED)
    return pdata+bbb

def a85encode(data):
    asascii = base64.a85encode(data)
    return asascii

def a85decode(data):
    asbytes = base64.a85decode(data)
    return asbytes

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
