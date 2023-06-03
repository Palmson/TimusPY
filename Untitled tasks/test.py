n = int(input())
p = 1 << n
d = {}
for _ in range(p):
    _, key = input().split()
    d[key] = d.get(key, 0) + 1
m = max(d.values())
for i in range(n):
    p //= 2
    if m > p:
        print(i)
        break
else:
    print(n)