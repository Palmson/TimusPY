n, m = map(int, input().split())
wheel = []
for i in range(n):
    wheel.append(input())
d = m % n
if 0 <= n - d - 10:
    for x in range(d, d + 10):
        print(wheel[x], end='')
else:
    for x in range(d, n):
        print(wheel[x], end='')
    for x in range(abs(n - d - 10)):
        print(wheel[x], end='')
