import sys  #add library system

from collections import deque

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def shortest_rope(grid):
    N = len(grid)
    M = len(grid[0])
    vis = [[False] * N for i in range(M)]
    dist = [[0] * N for i in range(M)]
    q = deque()
    q.append((0, 0))
    print(q)
    vis[0][0] = True
    while len(q):
        x, y = q.popleft()
        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy
            if new_x >= 0 and new_x < n and new_x >= 0 and new_x < m and not vis[new_x][new_y] and grid[new_x][new_y]:
                q.append((new_x, new_y))
                vis[new_x][new_y] = True
                dist[new_x][new_y] = dist[x][y]+1
    if not vis[M-1][N-1]:
        print(dist[M - 1][N - 1])
    else:
        print(dist[M-1][N-1])


m, n = map(int, input().split()) #read N and M of labyrynth

laby = [[0] * m for i in range(n)]
for i in range(n):
    line = sys.stdin.readline()
    for j in range(m):
        if line[j] == '.':
            laby[i][j] = 1

shortest_rope(laby)
#...The next lines describe the labyrinth. The ith line of the next m lines contains n characters. Each character is either "#" or ".", with "#" indicating a forbidden cell, and "." indicating a free cell (i = 1, 2, ..., m)...
#But in sample input the last character in the 1st line of labyrinth is space.
#The problem asks you to find the diameter of a tree.
#You can speed up BFS from a source to a target by doing a bi-directional search.

#A bi-directional search is basically doing a BFS from the source and from the target at the same time, one step from each - until the two fronts meet each other.