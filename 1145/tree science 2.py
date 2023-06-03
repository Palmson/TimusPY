class Node:
   def __init__(self, value, child = None) -> None:
      self.val = value
      self.children = []
      if child != None:
         for value in child:
            self.children.append(value)

ans = 1
def solve(root):
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
   depth(root)

   return ans -1

root = Node(1, [Node(1), Node(1), Node(1, [Node(1), Node(1)])])

print(solve(root))