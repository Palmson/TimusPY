def operation():
    global n, done, p, a, sum
    b = a
    while sum < n:
        sum += b
        b += 1
    if sum == n:
        p = b + a - 2
        done = True
    else:
        a += 1
        sum = 0
    print(a, b, p, sum)


n = int(input())
done = False
sum = 0
p = None
a = -1
while not done:
    operation()
print(a, p)