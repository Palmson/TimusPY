def generator(n, x, y, X0, Y0):
    global m
    global a
    if n == 2:
        m += 1
        for i in range(2):
            for j in range(2):
                if (x + i != X0) or (y + j != Y0):
                    a[int(x+i)][int(y+j)] = m
        return a
    m +=1

    for i in range(2):
        for j in range(2):
            if (x + i*n/2 > X0 or X0 >= x + i*n/2+n/2 or y + j*n/2 > Y0 or Y0 >= y + j*n/2+n/2):
                a[int(x+n/2-1+i)][int(y+n/2-1+j)] = m

    for i in range(2):
        for j in range(2):
            if(x + i*n/2 <= X0 and X0 < x + i*n/2+n/2 and y + j*n/2 <= Y0 and Y0 < y + j*n/2+n/2):
                generator(n/2, x + i*n/2, y + j*n/2, X0, Y0)
            else:
                generator(n/2, x + i*n/2, y + j*n/2, x + n/2 - 1 + i, y + n/2 - 1 + j)
n = int(input())
X, Y = map(int, input().split())
a = [[0]*(2**n) for i in range(2**n)]
m = 0
generator(2**n, 0, 0, X-1, Y-1)

for i in range(2**n):
    for j in range(2**n):
        print(a[i][j], end = " ")
    print()