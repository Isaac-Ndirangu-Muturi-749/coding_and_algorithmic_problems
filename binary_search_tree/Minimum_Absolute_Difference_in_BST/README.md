To find the minimum absolute difference between the values of any two different nodes in a Binary Search Tree (BST), we can leverage the properties of the BST. Since the BST is sorted, the minimum absolute difference will always occur between adjacent nodes in an in-order traversal of the tree.

### Approach:

1. **In-Order Traversal**: Perform an in-order traversal of the BST. This will give us the values of the nodes in sorted order.
2. **Calculate Minimum Difference**: As we traverse the tree, we can keep track of the previous node's value and compute the absolute difference with the current node's value. We'll update the minimum difference as we go along.

### Implementation:

Here’s a step-by-step implementation of the above approach:

```python
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = -1  # To store the value of the previous node
        self.min_diff = float('inf')  # Initialize min_diff to a large value

        def in_order_traversal(node):
            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Process the current node
            if self.prev != -1:  # Check if this is not the first node
                # Update the minimum difference
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update prev to the current node's value

            # Traverse the right subtree
            in_order_traversal(node.right)

        # Start the in-order traversal from the root
        in_order_traversal(root)

        return self.min_diff
```

### Explanation:

1. **In-Order Traversal**: The `in_order_traversal` function visits nodes in the order of left child, current node, and then right child. This gives us the node values in sorted order.
2. **Minimum Difference Calculation**:
   - The variable `self.prev` keeps track of the previous node's value.
   - For each node, after the left subtree has been processed, we calculate the difference between the current node's value and `self.prev`.
   - We update `self.min_diff` if the current difference is smaller than the previously recorded minimum difference.
3. **Final Result**: Once the traversal is complete, `self.min_diff` will contain the minimum absolute difference between any two nodes in the BST.

### Complexity Analysis:
- **Time Complexity**: O(n), where n is the number of nodes in the tree, since we visit each node exactly once.
- **Space Complexity**: O(h), where h is the height of the tree, due to the recursion stack. In the worst case (for a skewed tree), this could be O(n).

### Example Outputs:

```python
# Example usage:
sol = Solution()

# Example 1:
root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(sol.getMinimumDifference(root1))  # Output: 1

# Example 2:
root2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(sol.getMinimumDifference(root2))  # Output: 1
```

This approach effectively finds the minimum absolute difference between node values in a Binary Search Tree.
