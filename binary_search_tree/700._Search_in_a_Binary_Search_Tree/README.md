To solve this problem, we can leverage the properties of a **Binary Search Tree (BST)**. In a BST:
1. For any node, the value of the left subtree nodes is less than the node's value.
2. The value of the right subtree nodes is greater than the node's value.

Thus, we can efficiently search for the node using a recursive or iterative approach by comparing the target value (`val`) with the current node's value.

---

### **Approach**
1. Start at the root node.
2. Compare `val` with the current node's value:
   - If `val == node.val`, return the current node (this is the root of the subtree we want).
   - If `val < node.val`, search in the left subtree (as smaller values are on the left).
   - If `val > node.val`, search in the right subtree (as larger values are on the right).
3. If the node is `null` (we reach the end of the tree without finding the value), return `null`.

---

### **Recursive Implementation**
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  # Base case: Node not found
            return None
        if root.val == val:  # Node with the target value found
            return root
        elif val < root.val:  # Search in the left subtree
            return self.searchBST(root.left, val)
        else:  # Search in the right subtree
            return self.searchBST(root.right, val)
```

---

### **Iterative Implementation**
This avoids recursion and uses a simple loop to traverse the tree:
```python
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:  # Node with the target value found
                return root
            elif val < root.val:  # Move to the left subtree
                root = root.left
            else:  # Move to the right subtree
                root = root.right
        return None  # Node not found
```

---

### **Explanation with Examples**
#### Example 1:
Input:
```plaintext
root = [4,2,7,1,3], val = 2
```
1. Start at `root` (value 4). Since `2 < 4`, move to the left subtree.
2. At the left child (value 2), `2 == 2`. Return this node.

Output:
```plaintext
[2,1,3]
```

#### Example 2:
Input:
```plaintext
root = [4,2,7,1,3], val = 5
```
1. Start at `root` (value 4). Since `5 > 4`, move to the right subtree.
2. At the right child (value 7), `5 < 7`. Move to the left subtree, which is `null`.
3. Node not found. Return `null`.

Output:
```plaintext
[]
```

---

### **Complexity Analysis**
1. **Time Complexity**: \(O(h)\), where \(h\) is the height of the tree.
   - In the worst case, \(h = n\) (skewed tree).
   - In the best case (balanced tree), \(h = \log n\).
2. **Space Complexity**:
   - Recursive approach: \(O(h)\) for the call stack.
   - Iterative approach: \(O(1)\).
