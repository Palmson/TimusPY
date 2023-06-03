#class to create nodes of a tree
class Node:
    def __init__(self, data):
        self.left = None
        self.middle = None
        self.right = None
        self.data = data
#height function to calculate height of left subtree and right subtree
def printInorder(node : Node) -> None:

	if (node is None):
		return

	printInorder(node.left)
	print(node.data, end = " ")
	printInorder(node.right)

def height(node):
    if node is None:
        return 0
    #it returns left height and right height and one root node
    return 1+max(height(node.left),height(node.right),height(node.middle))
#function to calculate diameter of a binary tree
def diameter(node):
    if node is None:
        return 0
    lheight=height(node.left)
    mheight = height(node.middle)
    rheight=height(node.right)
    #recursive call for left,right diameters
    ldiameter=diameter(node.left)
    mdiameter = diameter(node.middle)
    rdiameter=diameter(node.right)
    return max(lheight+rheight+mheight+1,max(ldiameter,rdiameter,mdiameter))
#main function
if __name__=="__main__":
    root=Node(1)
    root.middle = Node(4)
    root.left=Node(2)
    root.left.left=Node(5)
    root.left.right=Node(6)
    root.left.right.left=Node(7)
    root.right=Node(3)
    printInorder(root)
    print("diameter of given binary tree is", diameter(root))