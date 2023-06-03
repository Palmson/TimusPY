from collections import deque
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

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    # Approach #4: Using recursive DFS, outside visited.
    # https://www.youtube.com/watch?v=ZixJexAaOAk
    def dfs(grid, r, c):
        # global visited - doesn't work. NameError
        # Passing visited as a variable in this call also fails
        if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or (r, c) in visited:
            return
            # Mark this node as water now (visited)
            # Since this is marked as 0 in-place,
            # the outer function won't consider this in the next loop
        if grid[r][c] == 1:
            visited.add((r, c))  # visited set instead of grid[r][c] = 0
            dfs(grid, r + 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r - 1, c)
            dfs(grid, r, c - 1)

    output = 0
    ROWS, COLUMNS = len(grid), len(grid[0])
    visited = set()

    for r in range(ROWS):
        for c in range(COLUMNS):
            if grid[r][c] == 1:
                # visit all the neighbours of this "1" and come back
                dfs(grid, r, c)
                output += 1

    return output


print(numIslands([
    ["0", "0", "0", "0", "0", "0", "0"],
    ["0", "1", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "0", "0", "0"],
    ["0", "1", "0", "1", "0", "1", "0"],
    ["0", "1", "1", "1", "1", "1", "0"]
]))
#######
#.#.###
#.#.###
#.#.#.#
#.....#
#######