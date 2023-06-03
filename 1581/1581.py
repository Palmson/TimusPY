n = int(input())
N = [int(x) for x in input().split()]
P = []
k = 0
f = N[0]
for i in range(n):
    if N[i] == f:
        k += 1
    else:
        P.append(k)
        P.append(f)
        k = 1
    if i == n - 1:
        P.append(k)
        P.append(N[i])
    f = N[i]
print(' '.join(str(x) for x in P))


