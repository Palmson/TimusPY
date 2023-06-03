import math as m
n = int(input())
d = m.sqrt(n)
s = 0
j = 2
while j <= d and j <= 2000000:
    while n % j == 0:
        s += 1
        n //= j
    j += 1
if s == 20 and n == 1:
    print("Yes")
elif s == 19 and n > 1:
    print("Yes")
else:
    print("No")

