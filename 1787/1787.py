k, n = map(int, (input().split()))
A = [int(x) for x in input().split()]
x = 0
for i in range(n):
    x += A[i] - k
    if x < 0:
        x = 0
print(x)
