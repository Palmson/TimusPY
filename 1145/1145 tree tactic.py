from datetime import datetime
start_time = datetime.now()
import sys
class Node:
   def __init__(self, value, child = None) -> None:
      self.val = value
      self.children = []
      if child != None:
         for value in child:
            self.children.append(value)
ans = 1
def depth(root):
    global ans
    if not root:
        return 0
    children = [0, 0]
    temp_children = [depth(child) for child in root.children]
    if len(temp_children) > 0:
        children = temp_children
    ans = max(ans, sum(sorted(children)[-2:]) + 1)

    return max(children) + 1
def solve(root):
    depth(root)
    return ans-1

def tree(mat, queue, x, y):

    global R
    global C

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

R, C = [int(x) for x in sys.stdin.readline().split()]
mat = [[0] * R for i in range(C)]
q = [[0] * R for i in range(C)]
rightx = []
righty = []

for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            mat[i][j] = 1
            rightx.append(i)
            righty.append(j)

root = tree(mat, q, rightx[0], righty[0])
print(solve(root))
end_time = datetime.now()
print(end_time-start_time)

