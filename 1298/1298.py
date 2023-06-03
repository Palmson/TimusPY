import math
def valid(x,y):
    if 0 <= x and x < n and 0 <= y and y < n and A[x][y] == 0:
        return True
    return False
def cnt(x, y):
    cnt = 0
    for i in range(8):
        if valid(x + dx[i], y + dy[i]) and A[x + dx[i]][y + dy[i]] == 0:
            cnt += 1
        return cnt
def move(x,y):
    mn = INF

n = int(input())
INF = 2000000000
EPS = 1e-9
A = []
dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [1, -1, 2, 2, -1, 1, -2, -2]
