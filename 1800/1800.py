import math
l, h, w = map(int, (input().split()))
g = 9.81
h = h/100
l = l/100
if l/2 > h:
    print('butter')
else:
    h += -0.5*l
    w = w/60
    t = math.sqrt(abs(2*h)/g)
    c = t*w
    if c % 1 < 0.25 or c % 1 > 0.75:
        print('butter')
    else:
        print('bread')
