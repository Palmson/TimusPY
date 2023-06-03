n = int(input())
m = 0
c = 0
L = []
for i in range(n):
    m = int(input())
    if m == 3:
        print('None')
        c += 1
        break
    else:
        L.append(m)

if c == 0:
    c = sum(L) / len(L)
    if c == 5:
        print('Named')
    elif c >= 4.5:
        print('High')
    else:
        print('Common')
