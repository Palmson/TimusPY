from datetime import datetime
start_time = datetime.now()
import sys
ans = 1

def tree(mat, queue, x, y):

    global R
    global C
    global ans
    if x < 0 or x >= R or y < 0 or y >= C or (x, y) in queue:
        return
    else:
        queue[x][y] = 1
        mas = []
        if mat[x-1][y] and queue[x-1][y] == 0:
            mas.append(tree(mat, queue, x-1, y))

        if mat[x+1][y] and queue[x+1][y] == 0:
            mas.append(tree(mat, queue, x + 1, y))

        if mat[x][y-1] and queue[x][y-1] == 0:
            mas.append(tree(mat, queue, x, y-1))

        if mat[x][y+1] and queue[x][y+1] == 0:
            mas.append(tree(mat, queue, x, y+1))
        return Node(1, mas)

R, C = map(int, input().split())
mat = [[0] * R for i in range(C)]

for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            mat[i][j] = 1

root = tree(mat, q, rightx[0], righty[0])
print(dfs(root, 0))
end_time = datetime.now()
print(end_time-start_time)

