n, k = map(int, (input().split()))
if k > n:
    n = k
n = n*2

if n % k == 0:
    print(n // k)
else:
    print(n // k + 1)
