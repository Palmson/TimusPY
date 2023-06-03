n = int(input())
if n > 0:
    x = int((n*(n+1))/2)
    print(x)
elif n == 0:
    print(1)
else:
    x = int(((n * (n - 1)) / -2)+1)
    print(x)
