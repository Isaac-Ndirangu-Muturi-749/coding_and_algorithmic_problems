To solve the problem of finding the right side view of a binary tree, we can perform a level-order traversal (BFS). During this traversal, we will keep track of the last node at each level, as this node will be visible from the right side.

### Approach:

1. **Level-order Traversal (BFS)**:
   - We can use a queue to perform a level-order traversal.
   - For each level, the last node we encounter will be the node visible from the right side.

2. **Result List**:
   - We'll maintain a list to store the values of the nodes visible from the right side.

3. **Edge Case**:
   - If the tree is empty (`root` is `None`), return an empty list.

Here’s the Python code to implement this solution:

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        right_view = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # If it's the last node in the current level, add it to the right view
                if i == level_size - 1:
                    right_view.append(node.val)
                # Add left and then right child to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view

# Helper function to create a binary tree from a list.
def create_binary_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1

    return root

def run_tests():
    solution = Solution()

    # Test case 1
    root = create_binary_tree([1, 2, 3, None, 5, None, 4])
    assert solution.rightSideView(root) == [1, 3, 4], "Test case 1 failed"

    # Test case 2
    root = create_binary_tree([1, None, 3])
    assert solution.rightSideView(root) == [1, 3], "Test case 2 failed"

    # Test case 3
    root = create_binary_tree([])
    assert solution.rightSideView(root) == [], "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
```

### Explanation:

- **TreeNode class**: Represents a node in the binary tree.
- **rightSideView function**:
  - If the root is `None`, return an empty list.
  - Use a queue to perform level-order traversal.
  - For each level, we add the last node's value to `right_view`.
- **create_binary_tree function**: Helper function to create a binary tree from a list representation.
- **run_tests function**: Contains test cases to validate the solution. It uses assertions to check if the output is as expected.

### Test Cases:

- **Test case 1**: The tree `[1,2,3,null,5,null,4]` should return `[1, 3, 4]`.
- **Test case 2**: The tree `[1,null,3]` should return `[1, 3]`.
- **Test case 3**: An empty tree `[]` should return `[]`.

This solution performs efficiently with a time complexity of `O(N)`, where `N` is the number of nodes in the tree, since we visit each node exactly once.
