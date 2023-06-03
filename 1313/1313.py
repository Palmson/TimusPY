n = int(input())
N = []
s = ''
for i in range(n):
    line = input().split()
    N.append(line)
for i in range(n):
    c = i
    j = 0
    while c >= 0:
        s += (N[c][j] + ' ')
        j += 1
        c -= 1
for i in range(1, n):
    j = i
    c = n - 1
    while j != n:
        s += (N[c][j] + ' ')
        j += 1
        c -= 1
print(s)










