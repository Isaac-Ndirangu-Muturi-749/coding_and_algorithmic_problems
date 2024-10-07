To solve the problem of zigzag level order traversal in a binary tree, we can use a breadth-first search (BFS) approach, while alternately reversing the order of nodes at each level to achieve the zigzag pattern.

### Approach:
1. **BFS Traversal**: We'll perform a level-order traversal using a queue to keep track of the nodes at each level.
2. **Direction Alternating**: For each level, we'll alternate the direction of traversal. If it's a left-to-right level, we'll append the nodes as they are; if it's a right-to-left level, we'll reverse the order of nodes before appending them to the result.

### Steps:
- Initialize a queue to start with the root node.
- Use a boolean flag (`left_to_right`) to track the direction of traversal at each level.
- For each level:
  - Process all nodes currently in the queue.
  - If `left_to_right` is `True`, add node values in normal order, otherwise add them in reverse order.
  - After processing a level, toggle the `left_to_right` flag for the next level.
- Continue until all levels are processed.

### Code Implementation:

```python
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Append the level to result in zigzag manner
        if not left_to_right:
            current_level.reverse()

        result.append(current_level)

        # Toggle the direction for the next level
        left_to_right = not left_to_right

    return result
```

### Explanation:
1. **Base Case**: If the tree is empty (`root` is `None`), return an empty list.
2. **Queue**: We initialize a queue using `deque` to store nodes at each level and process them in a breadth-first manner.
3. **Level Processing**: For each level:
   - We process all nodes currently in the queue (which belong to the same level).
   - Depending on the `left_to_right` flag, we either append the node values as they are or reverse them before adding to the result.
4. **Children Addition**: After processing a node, we enqueue its left and right children (if they exist) for the next level.
5. **Direction Switching**: After each level, we toggle the `left_to_right` flag to alternate the traversal direction for the next level.

### Example Walkthrough:

**Example 1:**

Input:
```
       3
     /   \
    9    20
        /   \
       15    7
```

- **Level 1**: `left_to_right = True`, process [3] → result = `[[3]]`
- **Level 2**: `left_to_right = False`, process [20, 9] → result = `[[3], [20, 9]]`
- **Level 3**: `left_to_right = True`, process [15, 7] → result = `[[3], [20, 9], [15, 7]]`

Output: `[[3], [20, 9], [15, 7]]`

**Example 2:**

Input: `root = [1]`
- **Level 1**: `left_to_right = True`, process [1] → result = `[[1]]`

Output: `[[1]]`

**Example 3:**

Input: `root = []`
- No nodes to process, return `[]`.

Output: `[]`

### Time Complexity:
- **O(n)** where `n` is the number of nodes in the tree, because we visit each node once.

### Space Complexity:
- **O(n)** for the queue and result list, since at most we may store all nodes of the tree in the queue (for a full binary tree).

This approach efficiently handles the zigzag level order traversal of a binary tree.
