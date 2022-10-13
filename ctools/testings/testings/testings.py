def nsqrt(no, guess=0):
    if no < 1: return 0
    if guess == 0: guess = no / 2
    while True:
        r1 = no / guess
        if r1 * r1 == no: return r1
        guess = (r1 + guess) / 2


def qsqrt(no):
    x = repr(no)
    print (x, len(x))


#print (nsqrt(144164, 1))
qsqrt(144164)

