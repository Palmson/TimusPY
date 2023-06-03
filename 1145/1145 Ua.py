def dfs(node, maxdepth):
    stack = [(node, 0)]
    visited = set()
    while stack:
        node, nodedepth = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        # Any other processing for this node comes here
        # ...
        if nodedepth < maxdepth:
            for child in reversed(node.children):
                stack.append((child, nodedepth + 1))