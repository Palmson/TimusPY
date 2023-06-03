def check(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    a = 3
    while a * a <= n and n % a != 0:
        a += 2
    return a * a > n

k = int(input())
N = []
i = 0
max = 0
for i in range(k):
    N.append(int(input()))
    if N[i] > max:
        max = N[i]
L = [0] * max
n = 0
j = n
while L[max-1] == 0:
    if check(n):
        L[j] = n
        j += 1
    n += 1
for i in range(k):
    N[i] = L[N[i]-1]
    print(N[i])
