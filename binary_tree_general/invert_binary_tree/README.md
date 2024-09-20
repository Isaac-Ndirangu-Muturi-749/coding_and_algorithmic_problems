To invert a binary tree, you can recursively swap the left and right children of each node, starting from the root. This operation continues down to the leaf nodes, effectively mirroring the tree.

### Approach:
1. **Recursive Inversion**:
   - If the current node is `None`, return `None`.
   - Swap the left and right subtrees of the current node.
   - Recursively invert the left and right subtrees.

2. **Base Case**:
   - If the tree is empty (`root` is `None`), return `None`.

### Code Implementation:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

### Explanation:

1. **Base Case**:
   - If `root` is `None` (empty tree), return `None`. This handles the edge case of an empty tree.

2. **Swap Operation**:
   - For each node, swap its left and right children. This step mirrors the tree at each level.

3. **Recursive Call**:
   - After swapping, recursively call `invertTree` on the left and right subtrees to invert the entire tree.

4. **Return**:
   - Finally, return the root of the inverted tree.

### Example Walkthrough:

**Example 1:**
```plaintext
Input: root = [4,2,7,1,3,6,9]

Step 1: Invert the root node (4)
    Swap left (2) and right (7) subtrees

Step 2: Invert subtree rooted at node (7)
    Swap left (6) and right (9)

Step 3: Invert subtree rooted at node (2)
    Swap left (1) and right (3)

Final tree:
        4
      /   \
     7     2
    / \   / \
   9   6 3   1
```

**Example 2:**
```plaintext
Input: root = [2,1,3]

Step 1: Invert the root node (2)
    Swap left (1) and right (3)

Final tree:
    2
   / \
  3   1
```

**Example 3:**
```plaintext
Input: root = []
Output: []
Explanation: Since the tree is empty, the result is also an empty tree.
```

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. We visit each node exactly once.
- **Space Complexity**: O(h), where `h` is the height of the tree. In the worst case, the recursion stack will take O(h) space. For a balanced tree, `h = O(log n)` and for a skewed tree, `h = O(n)`.
