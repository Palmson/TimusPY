L, T, va, vb = map(int, (input().split()))
n = int(input())
t = T*va + T*vb
for j in range(n):
    i, d, ty = map(int, (input().split()))
    if 1 - i == 0:
        t -= ty*va
    else:
        t -= ty*vb
print(t//L)


