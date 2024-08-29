To solve the problem of finding the maximum depth of a binary tree, we can use a recursive approach. The idea is to calculate the depth of the left and right subtrees of each node and return the maximum of those two depths plus one (which accounts for the current node).

### Solution Explanation

1. **Base Case**:
   - If the node is `None`, the depth is `0`.

2. **Recursive Case**:
   - Calculate the depth of the left subtree.
   - Calculate the depth of the right subtree.
   - The maximum depth at the current node will be `1 + max(left_depth, right_depth)`.

### Example Implementation in Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty
        if root is None:
            return 0

        # Recursive case: calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The maximum depth is the larger of the two depths plus one for the current node
        return 1 + max(left_depth, right_depth)
```

### Example Usage

You can test the function with the provided examples:

```python
def run_tests():
    solution = Solution()

    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.maxDepth(root) == 3, "Test case 1 failed"

    # Test case 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution.maxDepth(root) == 2, "Test case 2 failed"

    # Test case 3: Empty tree
    root = None
    assert solution.maxDepth(root) == 0, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
```

### Explanation of the Example Test Cases:

1. **Test Case 1**:
   - The tree structure is:
     ```
         3
        / \
       9  20
          / \
         15  7
     ```
   - The maximum depth is `3`.

2. **Test Case 2**:
   - The tree structure is:
     ```
         1
          \
           2
     ```
   - The maximum depth is `2`.

3. **Test Case 3**:
   - The tree is empty, so the maximum depth is `0`.

### Constraints:
- The number of nodes in the tree is in the range `[0, 10^4]`.
- Each node's value is between `-100` and `100`.

This solution is efficient with a time complexity of \(O(N)\), where \(N\) is the number of nodes in the tree, as each node is visited exactly once. The space complexity is \(O(H)\), where \(H\) is the height of the tree, due to the recursion stack.


Let's break down the first test case to understand how the `maxDepth` function works.

### Tree Structure:

Given the tree:

```
    3
   / \
  9  20
     / \
    15  7
```

Here's how the tree is represented in the code:

- `root = TreeNode(3)` creates the root node with value `3`.
- `root.left = TreeNode(9)` creates the left child of the root with value `9`.
- `root.right = TreeNode(20)` creates the right child of the root with value `20`.
- `root.right.left = TreeNode(15)` creates the left child of the node with value `20` with value `15`.
- `root.right.right = TreeNode(7)` creates the right child of the node with value `20` with value `7`.

### Execution Flow:

1. **Starting at the Root (`3`)**:
   - The function `maxDepth(root)` is called with the root node (`3`).
   - Since the root is not `None`, it proceeds to calculate the depth of the left and right subtrees.

2. **Left Subtree (`9`)**:
   - The function `maxDepth(root.left)` is called with the left child (`9`).
   - Since `9` is a leaf node (no children), both `maxDepth(root.left.left)` and `maxDepth(root.left.right)` return `0`.
   - The maximum depth for the node `9` is `1 + max(0, 0) = 1`.

3. **Right Subtree (`20`)**:
   - The function `maxDepth(root.right)` is called with the right child (`20`).
   - It proceeds to calculate the depth of the left and right children of `20`.

4. **Left Subtree of `20` (`15`)**:
   - The function `maxDepth(root.right.left)` is called with the node `15`.
   - Since `15` is a leaf node, both `maxDepth(root.right.left.left)` and `maxDepth(root.right.left.right)` return `0`.
   - The maximum depth for the node `15` is `1 + max(0, 0) = 1`.

5. **Right Subtree of `20` (`7`)**:
   - The function `maxDepth(root.right.right)` is called with the node `7`.
   - Since `7` is also a leaf node, both `maxDepth(root.right.right.left)` and `maxDepth(root.right.right.right)` return `0`.
   - The maximum depth for the node `7` is `1 + max(0, 0) = 1`.

6. **Calculate Maximum Depth for Node `20`**:
   - Now that we have the depths for both children of `20` (`15` and `7`), we can calculate the depth for `20`.
   - The maximum depth at `20` is `1 + max(1, 1) = 2`.

7. **Calculate Maximum Depth for Root Node (`3`)**:
   - Finally, with the depths of the left subtree (`1` from `9`) and the right subtree (`2` from `20`), we calculate the depth for the root node.
   - The maximum depth at `3` is `1 + max(1, 2) = 3`.

### Conclusion:

The function returns `3`, which is the maximum depth of the tree. This matches the expected output, and the assertion `assert solution.maxDepth(root) == 3` passes successfully.
