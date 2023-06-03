import math
n = int(input())
r = 4
for i in range(int(math.sqrt(n))):
    for j in range(int(math.sqrt(n))):
        if n-i*i-j*j > 0 and int(math.sqrt(n-i*i-j*j)) == math.sqrt(n-i*i-j*j):
            r = 3
for i in range(int(math.sqrt(n))):
    if n-i*i > 0 and int(math.sqrt(n-i*i)) == math.sqrt(n-i*i):
        r = 2
if int(math.sqrt(n)) == math.sqrt(n):
    r = 1
print(r)
