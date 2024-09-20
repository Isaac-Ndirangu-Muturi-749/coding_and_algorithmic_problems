To compute the average value of nodes at each level in a binary tree, a breadth-first traversal approach (also known as level-order traversal) can be used. This ensures that all nodes on the same level are processed together.

### Approach:

1. **Breadth-First Search (BFS)**:
   - Use a queue to traverse the tree level by level.
   - For each level, calculate the sum of all node values and divide by the number of nodes at that level to get the average.

2. **Process**:
   - Start with the root node in the queue.
   - For each level, calculate the sum of the node values and compute the average.
   - Add the child nodes of the current level to the queue for the next level.

3. **Return**:
   - Return the computed averages as an array.

### Code Implementation:

```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the average value of the current level
            result.append(level_sum / level_count)

        return result
```

### Explanation:

1. **Initialization**:
   - A deque (double-ended queue) is initialized with the root node for BFS.
   - An empty `result` list is created to store the average values of each level.

2. **BFS Traversal**:
   - While the queue is not empty, process each level:
     - Compute `level_sum` by summing up all node values at that level.
     - Track `level_count`, the number of nodes at the current level, to calculate the average.

3. **Queue Operations**:
   - For each node at the current level, its left and right children (if they exist) are added to the queue for processing the next level.

4. **Average Calculation**:
   - After processing all nodes at the current level, the average is calculated as `level_sum / level_count` and appended to the `result` list.

5. **Return the Result**:
   - Once all levels are processed, the `result` list, containing the average of each level, is returned.

### Example Walkthrough:

**Example 1**:
```plaintext
Input: root = [3,9,20,null,null,15,7]

Level 0:
Nodes: [3]
Average: 3 / 1 = 3.00000

Level 1:
Nodes: [9, 20]
Average: (9 + 20) / 2 = 14.50000

Level 2:
Nodes: [15, 7]
Average: (15 + 7) / 2 = 11.00000

Output: [3.00000, 14.50000, 11.00000]
```

**Example 2**:
```plaintext
Input: root = [3,9,20,15,7]

Level 0:
Nodes: [3]
Average: 3 / 1 = 3.00000

Level 1:
Nodes: [9, 20]
Average: (9 + 20) / 2 = 14.50000

Level 2:
Nodes: [15, 7]
Average: (15 + 7) / 2 = 11.00000

Output: [3.00000, 14.50000, 11.00000]
```

### Time and Space Complexity:

- **Time Complexity**: O(n), where `n` is the number of nodes in the tree. We visit each node exactly once during the BFS traversal.
- **Space Complexity**: O(m), where `m` is the maximum number of nodes at any level. In the worst case, `m` can be O(n) if the tree is completely unbalanced (i.e., a skewed tree). For a balanced tree, `m` is O(n/2) at the deepest level.

This solution ensures an efficient computation of the average value at each level in the binary tree.
