# Python3 implementation of
# the above approach

# Node structure for
# Binary Tree
class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to return
# root index of a
# binary tree
def getRootIndex(arr : list) -> int:
	root_index = -1

	for j in range(len(arr)):
		count = 0
		for i in range(len(arr)):
			if (arr[i][j] == 0):
				count += 1

		if (count == len(arr)):
			root_index = j
			break

	return root_index

# Function to print
# in-order traversal of
# a tree
def printInorder(node : Node) -> None:

	if (node is None):
		return

	printInorder(node.left)
	print(node.data, end = " ")
	printInorder(node.right)

# Function to generate binary
# tree from parent matrix
def createTreeRec(arr : list,
				index : int) -> Node:

	node = Node(index)

	# If left is 1 then create
	# left child. (for 1st one in row)
	# If left is 2 then create
	# right child.(for 1st one in row)
	left = 1

	for j in range(len(arr[index])):
		if (arr[index][j] == 1):
			# recur for left sub-tree
			if (left == 1):
				node.left = createTreeRec(arr, j)

			# recur for right sub-tree
			elif (left == 2):
				node.right = createTreeRec(arr, j)

			left += 1

	return node

# Driver code


# Assuming leftmost 1 in a
# row is left child, if exists
# and rightmost 1 in a row
# is right child, if exists
import sys

R, C = [int(x) for x in sys.stdin.readline().split()]
arr = [[0] * R for i in range(C)]
for i in range(C):
    line = sys.stdin.readline()
    for j in range(R):
        if line[j] == '.':
            arr[i][j] = 1
print(arr)
root_index = getRootIndex(arr)
root = createTreeRec(arr, root_index)

# Printing inorder traversal
# of tree to check the output
printInorder(root)

# This code is contributed by sanjeev2552
