def nsqrt(no, guess=0):
    if no < 1: return 0
    if guess == 0: guess = no / 2
    while True:
        r1 = no / guess
        if r1 * r1 == no: return r1
        guess = (r1 + guess) / 2


def qsqrt(no):
    x = repr(no)
    y = len(x) % 2
    if y == 1: x = '0'+x
    no = int(len(x) /2)
    parts = []
    for i in range(no):
        p = i*2
        parts.append(int(x[p:p+2]))
    print (parts)
    pass

class Class: pass
obj = Class()
obj.pick = 1
print (obj.pick)

#print (nsqrt(144164, 1))
qsqrt(141414)

