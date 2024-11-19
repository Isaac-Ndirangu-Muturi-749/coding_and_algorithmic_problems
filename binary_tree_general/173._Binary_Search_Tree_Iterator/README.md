Here’s how to implement the `BSTIterator` class efficiently using a stack to simulate the in-order traversal. This approach satisfies the requirements of \(O(h)\) memory, where \(h\) is the height of the BST, and \(O(1)\) average time complexity for `next()` and `hasNext()` calls.

---

### **Python Implementation**

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Initialize the iterator with the root of the BST.
        """
        self.stack = []
        self._push_left(root)  # Populate the stack with the leftmost nodes.

    def _push_left(self, node: TreeNode):
        """
        Helper function to push all the leftmost nodes of a subtree to the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        """
        # Pop the top element from the stack.
        curr = self.stack.pop()
        # If the current node has a right child, process its leftmost subtree.
        if curr.right:
            self._push_left(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        """
        Return True if there are more nodes to traverse, otherwise False.
        """
        return len(self.stack) > 0
```

---

### **Explanation**
1. **Initialization**:
   - The constructor initializes the stack and pushes all leftmost nodes from the root into the stack. This ensures that the smallest element is at the top of the stack.

2. **`next()`**:
   - Pop the top node from the stack, which represents the next smallest element.
   - If this node has a right child, push all the leftmost nodes of its right subtree to the stack.

3. **`hasNext()`**:
   - Simply checks if the stack is non-empty. If it is, there are more elements to process.

---

### **Example Walkthrough**

For the BST:
```
        7
       / \
      3   15
          /  \
         9    20
```

#### Initialization:
- The stack will contain `[7, 3]` (leftmost nodes).

#### Sequence of Operations:
1. `next()`:
   - Pop `3` from the stack (smallest element).
   - Stack now: `[7]`.

2. `next()`:
   - Pop `7` from the stack.
   - Push leftmost nodes of `15`: Stack becomes `[15, 9]`.

3. `hasNext()`:
   - Returns `True` (stack is not empty).

4. `next()`:
   - Pop `9` from the stack.
   - Stack now: `[15]`.

5. `hasNext()`:
   - Returns `True`.

6. `next()`:
   - Pop `15` from the stack.
   - Push leftmost nodes of `20`: Stack becomes `[20]`.

7. `hasNext()`:
   - Returns `True`.

8. `next()`:
   - Pop `20` from the stack.
   - Stack now: `[]`.

9. `hasNext()`:
   - Returns `False`.

---

### **Complexity Analysis**
- **Time Complexity**:
  - `next()`:
    - Average: \(O(1)\), as each node is pushed and popped from the stack exactly once.
    - Worst: \(O(h)\) when traversing a right subtree.
  - `hasNext()`:
    - \(O(1)\), as it only checks the stack size.

- **Space Complexity**:
  - \(O(h)\), where \(h\) is the height of the tree, as the stack contains the nodes along the path to the current node.

---

This implementation is efficient and meets the constraints for the problem.
