To determine whether a binary tree is a valid binary search tree (BST), we need to ensure that the tree satisfies the following conditions at every node:

1. The value of every node in the left subtree is strictly less than the value of the current node.
2. The value of every node in the right subtree is strictly greater than the value of the current node.
3. Both the left and right subtrees must also be valid binary search trees.

### Approach:
We can use a recursive function to validate the tree. The idea is to check whether each node lies within a valid range. For each node:
- The value of the node must be greater than the maximum value allowed for nodes in its left subtree.
- The value of the node must be less than the minimum value allowed for nodes in its right subtree.
We can use `-infinity` and `+infinity` as the initial range for the root node.

### Steps:
1. Start from the root and pass a range that the node's value must satisfy.
2. For the left subtree, update the upper bound to the current node's value because all values in the left subtree must be less than the current node.
3. For the right subtree, update the lower bound to the current node's value because all values in the right subtree must be greater than the current node.
4. Recursively check all nodes to ensure that they satisfy the BST property.

### Code Implementation:

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    # Helper function to validate the tree recursively
    def validate(node, low, high):
        # An empty tree is a valid BST
        if not node:
            return True

        # The current node's value must be in the range (low, high)
        if not (low < node.val < high):
            return False

        # Recursively validate the left subtree and right subtree
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    # Start with the entire range of valid values for the root
    return validate(root, float('-inf'), float('inf'))
```

### Explanation:
- **Base Case**: If the node is `None` (i.e., we've reached a leaf node), return `True` because an empty tree is a valid BST.
- **Condition Check**: If the node's value is not within the valid range (`low < node.val < high`), return `False`.
- **Recursion**:
  - Validate the left subtree with the updated range (`low` to `node.val`).
  - Validate the right subtree with the updated range (`node.val` to `high`).

### Example Walkthrough:

**Example 1**:
Input: `root = [2,1,3]`
```
    2
   / \
  1   3
```
- For node 2, the valid range is `(-inf, inf)`. It satisfies the condition.
- For node 1, the valid range is `(-inf, 2)`. It satisfies the condition.
- For node 3, the valid range is `(2, inf)`. It satisfies the condition.

Since all nodes satisfy the BST condition, the output is `True`.

**Example 2**:
Input: `root = [5,1,4,null,null,3,6]`
```
    5
   / \
  1   4
     / \
    3   6
```
- For node 5, the valid range is `(-inf, inf)`. It satisfies the condition.
- For node 1, the valid range is `(-inf, 5)`. It satisfies the condition.
- For node 4, the valid range is `(5, inf)`, but 4 does not satisfy this (it's less than 5). So, the output is `False`.

### Time Complexity:
- **O(n)**, where `n` is the number of nodes in the tree. We visit each node exactly once.

### Space Complexity:
- **O(h)**, where `h` is the height of the tree. This is due to the recursion stack, which can go as deep as the tree's height. In the worst case (for a skewed tree), `h = n`, and in the best case (for a balanced tree), `h = log(n)`.

This approach efficiently verifies if a binary tree is a valid binary search tree.
