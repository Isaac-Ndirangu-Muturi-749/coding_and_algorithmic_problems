To determine if two binary trees are leaf-similar, we need to compare the sequences of leaf values from left to right for both trees. We can do this using a depth-first search (DFS) approach to extract the leaf sequences for both trees and then compare them.

---

### **Python Implementation**

```python
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to collect leaf values
        def get_leaves(root):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:  # Check if it's a leaf node
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        # Get leaf sequences for both trees
        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)

        # Compare leaf sequences
        return leaves1 == leaves2
```

---

### **Explanation**

1. **Helper Function `get_leaves`**:
   - This function performs a DFS to extract all leaf nodes of a tree.
   - A node is considered a leaf if it has no left or right child.
   - We traverse the tree recursively and add leaf values to a `leaves` list.

2. **Main Function `leafSimilar`**:
   - Call `get_leaves` on both `root1` and `root2` to collect their respective leaf sequences.
   - Compare the two lists to check if the leaf sequences are identical.

---

### **Complexity Analysis**

- **Time Complexity**: \(O(n_1 + n_2)\), where \(n_1\) and \(n_2\) are the number of nodes in `root1` and `root2`, respectively. Each node is visited once.
- **Space Complexity**: \(O(h_1 + h_2)\), where \(h_1\) and \(h_2\) are the heights of the two trees, due to the recursion stack.

---

### **Examples**

#### Example 1:
Input:
```python
root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
```

Execution:
- Leaf sequence for `root1`: `[6, 7, 4, 9, 8]`
- Leaf sequence for `root2`: `[6, 7, 4, 9, 8]`
Output: `True`

#### Example 2:
Input:
```python
root1 = [1, 2, 3]
root2 = [1, 3, 2]
```

Execution:
- Leaf sequence for `root1`: `[2, 3]`
- Leaf sequence for `root2`: `[3, 2]`
Output: `False`

---

This solution is efficient and adheres to the constraints provided.
