To delete a node in a Binary Search Tree (BST), we must maintain the BST properties. The process involves the following steps:

---

### Steps to Delete a Node in a BST:
1. **Search for the Node**:
   - Recursively traverse the tree to locate the node with the given key.

2. **Delete the Node**:
   - If the node is a **leaf** (no children), remove it directly.
   - If the node has **one child**, replace the node with its child.
   - If the node has **two children**:
     - Replace the node's value with the **minimum value in the right subtree** (inorder successor).
     - Recursively delete the inorder successor.

---

### Implementation in Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):
    if not root:
        return None  # Base case: If the root is null, return None

    # Search for the node to delete
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node to be deleted found
        if not root.left:  # Case 1 & 2: No left child or no child at all
            return root.right
        elif not root.right:  # Case 1 & 2: No right child
            return root.left
        else:
            # Case 3: Node has two children
            # Find the inorder successor (minimum value in the right subtree)
            successor = getMin(root.right)
            root.val = successor.val  # Replace value with successor's value
            root.right = deleteNode(root.right, successor.val)  # Delete successor

    return root

def getMin(node):
    while node.left:
        node = node.left
    return node
```

---

### Explanation:

1. **Search**:
   - Recursively move left if the key is smaller than the current node's value.
   - Recursively move right if the key is larger.

2. **Delete**:
   - If the node has **no children**, simply return `None` (deleting the leaf).
   - If the node has **one child**, return the child (bypassing the node).
   - If the node has **two children**:
     - Find the **inorder successor** (smallest value in the right subtree).
     - Replace the node's value with the successor's value.
     - Delete the successor in the right subtree.

---

### Complexity Analysis:
- **Time Complexity**: \(O(h)\), where \(h\) is the height of the tree:
  - Searching for the node takes \(O(h)\).
  - Deleting the node (including finding the inorder successor) also takes \(O(h)\).
- **Space Complexity**: \(O(h)\) due to recursion stack in the worst case (unbalanced tree).

---

### Example Walkthrough:

#### Input:
```
root = [5,3,6,2,4,null,7], key = 3
```

#### Execution:
1. Search for `key = 3`:
   - Traverse left from `5` → Found node `3`.

2. Node `3` has two children:
   - Find the inorder successor: `4` (minimum in the right subtree).
   - Replace `3` with `4` and delete `4` in the right subtree.

#### Output:
```
[5,4,6,2,null,null,7]
```

---

This approach ensures we solve the problem efficiently, adhering to the \(O(h)\) complexity requirement.
