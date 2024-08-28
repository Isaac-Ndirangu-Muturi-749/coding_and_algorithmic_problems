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
