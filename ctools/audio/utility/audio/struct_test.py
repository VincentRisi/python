from struct import pack, unpack, calcsize

lsb = pack('!LL10s',0x7f,0xacededac,b'1234567890')
s = pack('!L10s',0xacededac,b'0987654321')

def tester(bub):
    p = unpack('!L', bub[:4])[0]
    if p == 0xacededac:
        n = len(bub)-4
        t = unpack(f'!L{n}s', bub)
        return t[1]
    p = unpack('!L', bub[4:8])[0]
    if p == 0xacededac:
        n = len(bub)-8
        t = unpack(f'!LL{n}s',bub)
        return t[2]

x = tester(lsb)
y = tester(s)
print (repr(x), repr(y))

pass