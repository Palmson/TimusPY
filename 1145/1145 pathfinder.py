# Python program to find Longest Possible Route in a
# matrix with hurdles
import sys

R, C = [int(x) for x in sys.stdin.readline().split()]


# A Pair to store status of a cell. found is set to
# True of destination is reachable and value stores
# distance of longest path
class Pair:

    def __init__(self, found, value):
        self.found = found
        self.value = value


# Function to find Longest Possible Route in the
# matrix with hurdles. If the destination is not reachable
# the function returns false with cost sys.maxsize.
# (i, j) is source cell and (x, y) is destination cell.
def findLongestPathUtil(mat, i, j, x, y, visited):
    # if (i, j) itself is destination, return True
    if (i == x and j == y):
        p = Pair(True, 0)
        return p

    # if not a valid cell, return false
    if (i < 0 or i >= R or j < 0 or j >= C or mat[i][j] == 0 or visited[i][j]):
        p = Pair(False, sys.maxsize)
        return p

    # include (i, j) in current path i.e.
    # set visited(i, j) to True
    visited[i][j] = True

    # res stores longest path from current cell (i, j) to
    # destination cell (x, y)
    res = -sys.maxsize - 1

    # go left from current cell
    sol = findLongestPathUtil(mat, i, j - 1, x, y, visited)

    # if destination can be reached on going left from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # go right from current cell
    sol = findLongestPathUtil(mat, i, j + 1, x, y, visited)

    # if destination can be reached on going right from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # go up from current cell
    sol = findLongestPathUtil(mat, i - 1, j, x, y, visited)

    # if destination can be reached on going up from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # go down from current cell
    sol = findLongestPathUtil(mat, i + 1, j, x, y, visited)

    # if destination can be reached on going down from
    # current cell, update res
    if (sol.found):
        res = max(res, sol.value)

    # Backtrack
    visited[i][j] = False

    # if destination can be reached from current cell,
    # return True
    if (res != -sys.maxsize - 1):
        p = Pair(True, 1 + res)
        return p

    # if destination can't be reached from current cell,
    # return false
    else:
        p = Pair(False, sys.maxsize)
        return p


# A wrapper function over findLongestPathUtil()
def findLongestPath(mat, i, j, x, y):
    # create a boolean matrix to store info about
    # cells already visited in current route
    # initialize visited to false
    visited = [[False for i in range(C)] for j in range(R)]

    # find longest route from (i, j) to (x, y) and
    # print its maximum cost
    p = findLongestPathUtil(mat, i, j, x, y, visited)
    if (p.found):
        return int(p.value)
    else:
        return 0


# Driver code

# input matrix with hurdles shown with number 0
mat = [[0] * R for i in range(C)]

for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            mat[i][j] = True
# find longest path with source (0, 0) and
# destination (1, 7)
maxD = 0
for i in range(C):
    for j in range(R):
        if mat[i][j] == True:
            for l in range(C):
                for k in range(R):
                    if mat[l][k] == True:
                        chek = findLongestPath(mat, i, j, l, k)
                        maxD = max(maxD, chek)
print(maxD)

# This code is contributed by shinjanpatra