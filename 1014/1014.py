n = int(input())
z = 0
t = 1
if n == 0:
    print(10)
elif 1 <= n <= 9:
    print(n)
else:
    for i in range(9, 1, -1):
        while n % i == 0:
            z += i * t
            t *= 10
            n //= i
    if n == 1:
        print(z)
    else:
        print(-1)
