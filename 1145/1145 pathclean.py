from datetime import datetime
start_time = datetime.now()

import sys

class Pair:

    def __init__(self, found, value):
        self.found = found
        self.value = value

def findLongestPathUtil(mat, i, j, x, y, visited):

    if (i == x and j == y):
        p = Pair(True, 0)
        return p

    if (i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]):
        p = Pair(False, sys.maxsize)
        return p

    visited[i][j] = True

    res = -sys.maxsize - 1

    sol = findLongestPathUtil(mat, i, j - 1, x, y, visited)

    if (sol.found):
        res = max(res, sol.value)

    sol = findLongestPathUtil(mat, i, j + 1, x, y, visited)

    if (sol.found):
        res = max(res, sol.value)

    sol = findLongestPathUtil(mat, i - 1, j, x, y, visited)

    if (sol.found):
        res = max(res, sol.value)

    sol = findLongestPathUtil(mat, i + 1, j, x, y, visited)

    if (sol.found):
        res = max(res, sol.value)

    visited[i][j] = False

    if (res != -sys.maxsize - 1):
        p = Pair(True, 1 + res)
        return p

    else:
        p = Pair(False, sys.maxsize)
        return p


def findLongestPath(mat, i, j, x, y):

    visited = [[False for i in range(C)] for j in range(R)]

    p = findLongestPathUtil(mat, i, j, x, y, visited)
    if (p.found):
        return int(p.value)
    else:
        return 0


R, C = [int(x) for x in sys.stdin.readline().split()]
mat = [[0] * R for i in range(C)]
q = [[0] * R for i in range(C)]
rightx = []
righty = []
n = -1
for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            mat[i][j] = 1
            rightx.append(i)
            righty.append(j)
            n += 1


maxD = 0
for i in range(n):
    for j in range(n):
        chek = findLongestPath(mat, rightx[i], righty[i], rightx[j], righty[j])
        maxD = max(maxD, chek)
print(maxD)
end_time = datetime.now()
print(end_time-start_time)