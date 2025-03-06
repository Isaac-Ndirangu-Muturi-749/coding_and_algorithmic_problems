# Lowest Common Ancestor in a Binary Tree

## Problem Description
The problem is based on a fundamental concept from graph theory applied to binary trees, known as the "lowest common ancestor" (LCA). Specifically, we are given the root node of a binary tree where all node values are unique, and an array of `TreeNode` objects that are present in the tree. Our task is to determine the LCA of all of these nodes.

The **LCA** is defined as the lowest (deepest) node in the tree that has every given node in the array as a descendant (including the possibility of a node being a descendant of itself). The concept of "lowest" here refers to the deepest node in the hierarchy of the tree. In other words, we are looking for a shared ancestor of these nodes that is as far down the tree as possible.

## Flowchart Walkthrough
To analyze the problem, we follow this logical flow:

1. **Is it a graph?**
   - ✅ Yes: A binary tree is a specialized form of a graph.

2. **Is it a tree?**
   - ✅ Yes: Specifically, the problem involves a binary tree.

3. **DFS or BFS?**
   - ✅ Since the problem requires finding the lowest common ancestor, **Depth-First Search (DFS)** is suitable.
   - **Why DFS?**
     - DFS efficiently explores the tree structure from the root to leaves.
     - It helps track the presence of multiple target nodes within subtrees.

### Conclusion
DFS is the best approach as it allows us to traverse the tree efficiently and determine the lowest common ancestor of the given nodes.

## Intuition
To solve this problem, we use **DFS** in a **post-order traversal** (left, right, node) while leveraging a set for quick lookups.

### Steps:
1. If we reach a `None` node or a node in our set of target nodes, return that node.
2. Recursively call DFS on both the **left** and **right** children.
3. Process the returned results:
   - If both left and right subtrees return a non-`None` value, the current node is the LCA.
   - If only one subtree returns a non-`None` value, that subtree's node is the LCA.
   - If both subtrees return `None`, return `None` (no target nodes found in this subtree).
4. Initially, DFS is called on the root node and the set of target values.

### Key Observations:
- The algorithm efficiently **prunes** branches that do not contain any target nodes.
- The last non-`None` node returned is the **LCA** of all the target nodes.

---

## Solution Approach
The implementation consists of a **DFS function (`dfs`)** that traverses the binary tree to find the **LCA** of the given nodes.

### Implementation Details:
1. **Use a set for quick lookups**
   ```python
   s = {node.val for node in nodes}
   ```
2. **Define the recursive DFS function**
   ```python
   def dfs(root):
       if root is None or root.val in s:
           return root
       left, right = dfs(root.left), dfs(root.right)
       if left and right:
           return root
       return left or right
   ```
3. **Call `dfs` on the root**
   ```python
   return dfs(root)
   ```
### Explanation:
- **Base case:** If `root` is `None` or one of the target nodes, return `root`.
- **Recursive case:**
  - Call `dfs` on left and right children.
  - If both return non-`None`, the current node is the **LCA**.
  - If only one is non-`None`, return it (as it contains all required target nodes).
  - If both are `None`, return `None`.

### Time Complexity: **O(N)**
- DFS visits each node **once** → **O(N)**.

### Space Complexity: **O(N)**
- **Set storage:** O(N) in the worst case.
- **Recursive call stack:** O(N) in a skewed tree.

---

## Example Walkthrough
### Given Binary Tree:
```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
```
### Input: `[5, 1, 6, 2, 0]`
### Steps:
1. Create a set `{5, 1, 6, 2, 0}`.
2. Start DFS at node **3**.
   - **Left subtree** (`5`): Found in the set.
   - **Right subtree** (`1`): Found in the set.
   - Since **both sides returned nodes**, **LCA = 3**.

#### Verifying:
- **Subtree (5)**:
  - Contains `6` and `2`, making **5** their LCA.
- **Subtree (1)**:
  - Contains `0`, making **1** its LCA.
- Since `5` (left) and `1` (right) have valid LCAs, **node 3 is the LCA of the entire set**.

### Output:
```
LCA = 3
```

---

## Solution Implementation
### Python:
```python
from typing import List

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]) -> TreeNode:
        def dfs(current_node):
            if current_node is None or current_node in target_nodes_set:
                return current_node

            left_ancestor = dfs(current_node.left)
            right_ancestor = dfs(current_node.right)

            if left_ancestor and right_ancestor:
                return current_node

            return left_ancestor or right_ancestor

        target_nodes_set = set(nodes)

        return dfs(root)
```

### Notes:
- This version works **directly on `TreeNode` objects**, not just `val`.
- **Efficient lookups:** Uses a **set** for O(1) membership checks.
- **Recursive DFS approach:** Traverses tree **only once**.

---

## Complexity Analysis
### **Time Complexity: O(N)**
- Each node is visited **once**.
- Set lookups (`val in s`) take **O(1)** time.

### **Space Complexity: O(N)**
- **O(N)** for the recursion stack in the worst case (skewed tree).
- **O(N)** for the set storing target nodes.

---

## Summary
- **DFS-based recursive approach** efficiently finds **LCA**.
- **Set usage** ensures quick target node lookups.
- **Post-order traversal** determines the **lowest** ancestor.
- **Time Complexity: O(N)** (single pass through tree).
- **Space Complexity: O(N)** (recursive stack + target set).
