To solve the problem of counting "good nodes" in a binary tree, we can use a Depth-First Search (DFS) traversal approach, keeping track of the maximum value encountered on the path from the root to the current node.

---

### **Algorithm**

1. Start at the root node. A root node is always considered "good."
2. Use a DFS traversal (either recursive or iterative) to explore the tree.
3. Pass down the maximum value seen so far along the path to each child node.
4. A node is "good" if its value is greater than or equal to the maximum value seen so far.
5. Increment the count of "good" nodes whenever we find one.

---

### **Python Implementation**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            # Check if the current node is a "good" node
            is_good = node.val >= max_val
            count = 1 if is_good else 0

            # Update the maximum value seen so far
            max_val = max(max_val, node.val)

            # Traverse left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        # Start DFS traversal from the root
        return dfs(root, root.val)
```

---

### **Explanation**

1. **Recursive Function (`dfs`)**:
   - The function takes the current node and the maximum value (`max_val`) along the path.
   - Base case: If the node is `None`, return 0.
   - Check if the node is "good" by comparing its value with `max_val`.
   - Update `max_val` for the recursive calls to the left and right subtrees.
   - Return the total count of "good" nodes for the current subtree.

2. **Initial Call**:
   - Start the DFS from the root node with its value as the initial `max_val`.

3. **Efficiency**:
   - **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the tree, as each node is visited once.
   - **Space Complexity**: \(O(h)\), where \(h\) is the height of the tree, due to the recursive call stack.

---

### **Examples**

#### Example 1:
```python
root = TreeNode(3)
root.left = TreeNode(1, TreeNode(3))
root.right = TreeNode(4, TreeNode(1), TreeNode(5))

solution = Solution()
print(solution.goodNodes(root))  # Output: 4
```

#### Example 2:
```python
root = TreeNode(3)
root.left = TreeNode(3, TreeNode(4), TreeNode(2))

solution = Solution()
print(solution.goodNodes(root))  # Output: 3
```

#### Example 3:
```python
root = TreeNode(1)

solution = Solution()
print(solution.goodNodes(root))  # Output: 1
```

---

This solution efficiently handles trees with up to \(10^5\) nodes, as required by the constraints.
