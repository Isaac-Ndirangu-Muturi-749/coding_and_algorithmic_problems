To solve this problem, we can perform a **level-order traversal** (BFS) of the binary tree. During the traversal, we'll calculate the sum of the nodes at each level and keep track of the level with the maximum sum.

---

### **Algorithm**
1. Use a queue to perform level-order traversal (BFS).
2. Maintain variables to track:
   - The current level being processed.
   - The sum of node values at each level.
   - The maximum sum encountered so far and the corresponding level.
3. For each level, compute the sum of all nodes at that level.
4. Update the maximum sum and the smallest level whenever a higher sum is found.
5. Return the level with the maximum sum.

---

### **Python Implementation**
```python
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a queue for level-order traversal
        queue = deque([root])
        max_sum = float('-inf')  # Maximum sum encountered
        max_level = 1           # Level with the maximum sum
        current_level = 1       # Start at level 1

        # Perform BFS
        while queue:
            level_sum = 0  # Sum of nodes at the current level
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max_sum and max_level if needed
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1  # Move to the next level

        return max_level
```

---

### **Explanation**
1. **Input Example 1**: `root = [1, 7, 0, 7, -8, null, null]`

   - **Level 1**:
     - Nodes: `[1]`
     - Sum: `1`
   - **Level 2**:
     - Nodes: `[7, 0]`
     - Sum: `7 + 0 = 7`
   - **Level 3**:
     - Nodes: `[7, -8]`
     - Sum: `7 + (-8) = -1`

   The maximum sum is at **Level 2**, so the output is `2`.

2. **Input Example 2**: `root = [989, null, 10250, 98693, -89388, null, null, null, -32127]`

   - **Level 1**:
     - Nodes: `[989]`
     - Sum: `989`
   - **Level 2**:
     - Nodes: `[10250]`
     - Sum: `10250`
   - **Level 3**:
     - Nodes: `[98693, -89388]`
     - Sum: `98693 + (-89388) = 9305`
   - **Level 4**:
     - Nodes: `[-32127]`
     - Sum: `-32127`

   The maximum sum is at **Level 2**, so the output is `2`.

---

### **Complexity Analysis**
1. **Time Complexity**:
   - Each node is visited exactly once, so the traversal takes \(O(n)\), where \(n\) is the number of nodes.

2. **Space Complexity**:
   - The space required for the queue is proportional to the maximum number of nodes at any level (i.e., the width of the tree), which is \(O(w)\), where \(w\) is the maximum width of the tree.

Thus, the overall complexity is:
- **Time**: \(O(n)\)
- **Space**: \(O(w)\)

This solution efficiently handles the constraints, even for large trees.
