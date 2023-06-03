def fastfib(n):
    binn = bin(n)[2:] #бинарная запись числа n
    f = [0, 1]

    for b in binn:
        f2i1 = f[1] ** 2 + f[0] ** 2
        f2i = f[0] * (2 * f[1] - f[0])

        if b == '0':
            f[0], f[1] = f2i, f2i1
        else:
            f[0], f[1] = f2i1, f2i1 + f2i

    return f[0]


n = int(input())
fib = fastfib(n)
print(fib*2)