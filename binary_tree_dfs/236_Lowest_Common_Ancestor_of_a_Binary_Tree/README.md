Here is the Python solution for finding the **Lowest Common Ancestor (LCA)** of two nodes in a binary tree. This uses a recursive approach.

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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor (LCA) of two nodes in a binary tree.
        """
        # Base case: if root is None, or root matches either p or q, return root
        if not root or root == p or root == q:
            return root

        # Recur for left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, this is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null value
        return left if left else right
```

---

### **Explanation**

1. **Base Case**:
   - If the `root` is `None`, return `None`.
   - If the `root` matches either `p` or `q`, return `root`.

2. **Recursive Calls**:
   - Recursively find the LCA in the left subtree.
   - Recursively find the LCA in the right subtree.

3. **Determine the LCA**:
   - If both left and right subtrees return non-null values, it means `p` and `q` are found in different subtrees, so the current `root` is their LCA.
   - If only one subtree returns a non-null value, the LCA lies in that subtree.

---

### **Complexity Analysis**

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes in the tree. Each node is visited once.
- **Space Complexity**: \(O(h)\), where \(h\) is the height of the tree. This is due to the recursive call stack.

---

### **Example Walkthrough**

#### **Input Tree**:
```
        3
       / \
      5   1
     / \  / \
    6   2 0  8
       / \
      7   4
```

#### Example 1:
- `p = 5`, `q = 1`
- LCA is `3` because both nodes are in different subtrees of `3`.

#### Example 2:
- `p = 5`, `q = 4`
- LCA is `5` because `5` is an ancestor of `4`.

---

This solution is efficient and handles all edge cases, including when one of the nodes is an ancestor of the other.
