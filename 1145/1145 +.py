import sys  #add library system
n, m = map(int, input().split())#read N and M of labyrynth
laby = [[0] * n for i in range(m)]
k1 = -1

for i in range(m):
    line = sys.stdin.readline()
    for j in range(n):
        if line[j] == '.':
            k1 = i * n + j
            laby[i][j] = 1



def bfs(i, t):
    q1 = [-1] * (m * n)
    q2 = [-1] * (m * n)
    q1[0], q2[0] = i, 1
    s, e = 0, 1
    t[i] = False
    while s < e:
        j, l = q1[s], q2[s]
        s += 1
        if j % n != 0 and t[j - 1]:
            q1[e] = j - 1
            q2[e] = l + 1
            e += 1
            t[j - 1] = False
        if j % n != n - 1 and t[j + 1]:
            q1[e] = j + 1
            q2[e] = l + 1
            e += 1
            t[j + 1] = False
        if j >= n and t[j - n]:
            q1[e] = j - n
            q2[e] = l + 1
            e += 1
            t[j - n] = False
        if j <= (m - 1) * n - 1 and t[j + n]:
            q1[e] = j + n
            q2[e] = l + 1
            e += 1
            t[j + n] = False
    return j, l

print(laby)
k2, d1 = bfs(k1, laby[:][0])
k3, d2 = bfs(k2, laby[0][:])

print(max(d1, d2) - 1)

#...The next lines describe the labyrinth. The ith line of the next m lines contains n characters. Each character is either "#" or ".", with "#" indicating a forbidden cell, and "." indicating a free cell (i = 1, 2, ..., m)...
#But in sample input the last character in the 1st line of labyrinth is space.
#The problem asks you to find the diameter of a tree.
#You can speed up BFS from a source to a target by doing a bi-directional search.

#A bi-directional search is basically doing a BFS from the source and from the target at the same time, one step from each - until the two fronts meet each other.