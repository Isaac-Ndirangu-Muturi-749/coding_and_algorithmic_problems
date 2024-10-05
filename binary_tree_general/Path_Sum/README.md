To solve the problem of finding a root-to-leaf path in a binary tree where the sum of the node values equals `targetSum`, we can use **depth-first search (DFS)** to explore all root-to-leaf paths.

### Approach:

1. **Recursive Depth-First Search (DFS)**:
   - Starting from the root node, traverse down the tree.
   - At each node, subtract the node's value from the `targetSum`.
   - If we reach a leaf node (a node with no left and right children), check if the remaining `targetSum` equals the leaf node's value. If true, we found a valid path.
   - If not a leaf node, recursively check both left and right subtrees.

2. **Base Cases**:
   - If the root is `None`, there is no path, so return `False`.
   - If the current node is a leaf (both children are `None`), check if the current node’s value equals `targetSum`.

### Recursive Algorithm:

1. Subtract the current node's value from `targetSum`.
2. If the node is a leaf, check if the adjusted `targetSum` is 0.
3. If the node is not a leaf, recursively check both left and right children.

### Code Implementation:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    # If the root is None, there is no path, so return False
    if not root:
        return False

    # If we are at a leaf node, check if the current targetSum matches the node's value
    if not root.left and not root.right:
        return targetSum == root.val

    # Recursively check left and right subtrees with the reduced targetSum
    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))
```

### Explanation:

1. **Base Case**: If the `root` is `None`, there is no tree, so return `False`.
2. **Leaf Check**: If we reach a leaf node (both `left` and `right` are `None`), check if `targetSum` equals the leaf node's value.
3. **Recursive Calls**: If the current node is not a leaf, make recursive calls to both the left and right children, adjusting the `targetSum` by subtracting the current node's value.

### Example Walkthrough:

#### Example 1:
```plaintext
       5
      / \
     4   8
    /   / \
   11  13  4
  /  \      \
 7    2      1
```
- **Input**: `root = [5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`
- **Output**: `True`
- **Explanation**: There is a valid path `5 -> 4 -> 11 -> 2` which sums to `22`.

#### Example 2:
```plaintext
   1
  / \
 2   3
```
- **Input**: `root = [1,2,3]`, `targetSum = 5`
- **Output**: `False`
- **Explanation**: No root-to-leaf path sums to `5`.

#### Example 3:
- **Input**: `root = []`, `targetSum = 0`
- **Output**: `False`
- **Explanation**: The tree is empty, so no path exists.

### Time and Space Complexity:

- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. We visit each node once.
- **Space Complexity**: O(h), where `h` is the height of the tree (due to recursive stack usage). In the worst case (skewed tree), the space complexity is O(n).

This algorithm effectively checks all root-to-leaf paths to find if any path sums up to the `targetSum`.
