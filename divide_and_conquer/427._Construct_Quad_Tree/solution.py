# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def is_uniform(x1, y1, x2, y2):
            """Check if all elements in the sub-grid from (x1, y1) to (x2, y2) are the same."""
            val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def build(x1, y1, x2, y2):
            """Recursive function to build the Quad-Tree."""
            uniform, val = is_uniform(x1, y1, x2, y2)
            if uniform:
                # If the grid section is uniform, create a leaf node
                return Node(val == 1, True)

            # Otherwise, split the grid into four quadrants
            midX, midY = (x1 + x2) // 2, (y1 + y2) // 2
            topLeft = build(x1, y1, midX, midY)
            topRight = build(x1, midY, midX, y2)
            bottomLeft = build(midX, y1, x2, midY)
            bottomRight = build(midX, midY, x2, y2)

            # Return a non-leaf node with children
            return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)

        n = len(grid)
        return build(0, 0, n, n)
