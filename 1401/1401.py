def checkside(x, y, x0, y0, size):
    a = x0 - x
    b = y0 - y
    return a >= 0 and a < size and b >= 0 and b < size

def generate(x, y, x0, y0, p):

    global A  #так лучше не делать
    global N

    size = 2**p

    if p == 1:
        N += 1
        A[x][y] = N
        A[x+1][y] = N
        A[x][y+1] = N
        A[x+1][y+1] = N
        A[x+x0][y+y0] = 0
    else:

        if checkside(0, 0, x0, y0, size//2):
            generate(x, y, x0, y0, p-1)
        else:
            generate(x, y, size//2-1, size//2-1, p-1)

        if checkside(size//2, 0, x0, y0, size//2):
            generate(x+size//2, y, x0-size//2, y0, p-1)
        else:
            generate(x+size//2, y, 0, size//2-1, p-1)

        if checkside(0, size//2, x0, y0, size//2):
            generate(x, y+size//2, x0, y0-size//2, p-1)
        else:
            generate(x, y+size//2, size//2-1, 0, p-1)

        if checkside(size//2, size//2, x0, y0, size//2):
            generate(x+size//2, y+size//2, x0-size//2, y0-size//2, p-1)
        else:
            generate(x+size//2, y+size//2, 0, 0, p-1)

        N += 1

        if A[x+size//2-1][y+size//2-1] == 0:
            A[x+size//2-1][y+size//2-1] = N

        if A[x+size//2][y+size//2-1] == 0:
            A[x+size//2][y+size//2-1] = N

        if A[x+size//2-1][y+size//2] == 0:
            A[x+size//2-1][y+size//2] = N

        if A[x+size//2][y+size//2] == 0:
            A[x+size//2][y+size//2] = N

        A[x+y0][y+y0] = 0

n = int(input())
x, y = map(int, input().split())
A = [[0]*(2**n) for i in range(2**n)]
N = 0

generate(0, 0, x-1, y-1, n)

for row in A:
    print(*row, end='\n')