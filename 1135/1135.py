n = int(input())
n1 = n
arr = ''
r = 0
b = 0
while n1 > 0:
    newbies = input()
    n1 -= len(newbies)
    arr += newbies

for i in range(n):
    if arr[n-1-i] == '>':
        r += i-b
        b += 1

print(r)
