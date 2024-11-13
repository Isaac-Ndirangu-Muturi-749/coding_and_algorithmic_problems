To solve the problem of constructing a Quad-Tree from a binary matrix, we'll use a recursive approach that divides the grid into four quadrants until each quadrant has a uniform value of either 0 or 1.

### Approach:
1. **Define the Quad-Tree Node Structure**:
   - Each node has a `val` attribute (either `True` or `False`) and an `isLeaf` attribute (`True` if the node has no children).
   - The node has pointers to four children: `topLeft`, `topRight`, `bottomLeft`, and `bottomRight`.

2. **Recursive Function to Build the Quad-Tree**:
   - **Base Case**: If all values within the current grid section are the same (all 0s or all 1s), create a leaf node with `isLeaf = True` and set `val` to the grid value.
   - **Recursive Case**: If the grid section has mixed values, create an internal node with `isLeaf = False`, and recursively split the grid into four equal parts:
     - `topLeft`
     - `topRight`
     - `bottomLeft`
     - `bottomRight`

3. **Helper Function to Check Uniformity**:
   - For each recursive call, check if all values in the current grid section are the same. If yes, it can be represented as a leaf node; otherwise, it must be split further.

### Solution Code:

```python
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
```

### Explanation:
1. **is_uniform**: This helper function checks if a subgrid (defined by its corners `(x1, y1)` and `(x2, y2)`) contains all the same values. If so, it returns `True` and the value (either `0` or `1`); otherwise, it returns `False`.
2. **build**: This recursive function builds the Quad-Tree by either creating a leaf node if the current subgrid is uniform or splitting the subgrid into four parts.
3. **Recursive Splitting**: `topLeft`, `topRight`, `bottomLeft`, and `bottomRight` are computed by calling `build` on each subgrid, recursively constructing the tree until all nodes are leaves.

### Complexity Analysis:
- **Time Complexity**: \(O(n^2 \log n)\) because we divide the grid into four parts at each level, leading to \(O(\log n)\) recursive levels and iterating through the grid \(O(n^2)\) for uniformity checks.
- **Space Complexity**: \(O(\log n)\) for the recursion stack due to the depth of the Quad-Tree.

This solution efficiently constructs a Quad-Tree by dividing the grid recursively and only creating non-leaf nodes when necessary, ensuring an optimal and compact representation of the grid.
