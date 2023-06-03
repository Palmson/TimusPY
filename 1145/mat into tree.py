# key structure to store a binary tree node
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Utility function to print binary tree nodes in-order fashion
def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)


# Function to construct a binary tree
# from specified ancestor matrix
def constructBT(mat):
    # get number of rows in the matrix
    N = len(mat)

    # create an empty multi-dict
    dict = {}

    # Use sum as key and row numbers as values in the multi-dict
    for i in range(N):
        # find the sum of the current row
        total = sum(mat[i])

        # insert the sum and row number into the dict
        dict.setdefault(total, []).append(i)

    # node[i] will store node for i in constructed tree
    node = [Node(-1)] * N
    last = 0

    # the value of parent[i] is true if parent is set for i'th node
    parent = [False] * N

    # Traverse the dictionary in sorted order (default behavior)
    for key in dict.keys():
        for row in dict.get(key):
            last = row

            # create a new node
            node[row] = Node(row)

            # if leaf node, do nothing
            if key == 0:
                continue

            # traverse row
            for i in range(N):

                # do if parent is not set and ancestor exits
                if not parent[i] and mat[row][i] == 1:

                    # check for the unoccupied node
                    if node[row].left is None:
                        node[row].left = node[i]
                    else:
                        node[row].right = node[i]

                    # set parent for i'th node
                    parent[i] = True

    # last processed node is the root
    return node[last]


# Construct a Binary Tree from Ancestor Matrix
import sys

R, C = [int(x) for x in sys.stdin.readline().split()]
mat = [[0] * R for i in range(C)]
for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            mat[i][j] = 1
print(mat)
root = constructBT(mat)
inorder(root)
