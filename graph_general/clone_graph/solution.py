# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        visited = {}

        def dfs(node):
            # If the node is already visited, return its clone
            if node in visited:
                return visited[node]

            # Create a clone for the current node
            clone = Node(node.val)
            visited[node] = clone

            # Iterate over all the neighbors and clone them
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
