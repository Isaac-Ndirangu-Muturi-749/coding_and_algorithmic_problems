To solve this problem, we can approach it using a **Depth First Search (DFS)** traversal technique. The idea is to traverse the binary tree from the root to the leaf nodes while keeping track of the number formed by the values along the path. At each node, we append the node's value to the current path value (treating it as digits), and when we reach a leaf node, we add the number to the total sum.

### Steps to solve the problem:

1. **DFS Traversal**:
   - Starting from the root, at each node, we compute the current number formed by adding the node's value as a new digit to the current path.
   - The current path value can be computed as `current_number = current_number * 10 + node.val`.

2. **Leaf Node Check**:
   - When we reach a leaf node (a node with no children), we add the number formed by the current path to the total sum.

3. **Recursion**:
   - We recursively perform the above steps for the left and right children of each node.

4. **Return the Total Sum**:
   - After traversing all the root-to-leaf paths, return the total sum.

### Code Implementation:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_number):
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Update the current number by appending the node's value
            current_number = current_number * 10 + node.val

            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number

            # Recursively calculate the sum from the left and right children
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)

            # Return the total sum from both sides
            return left_sum + right_sum

        # Start the DFS traversal with an initial current_number of 0
        return dfs(root, 0)
```

### Explanation:

1. **TreeNode Class**:
   - This class defines the structure of a node in the binary tree. Each node contains a value (`val`) and two pointers to its left and right children (`left` and `right`).

2. **sumNumbers Function**:
   - The `sumNumbers` function is the main entry point that takes the root of the binary tree as input. It starts the DFS traversal with an initial `current_number` of 0.

3. **dfs Function**:
   - The `dfs` function performs a depth-first traversal of the tree.
   - For each node, it appends the node's value to the current number and checks if the node is a leaf node.
   - If it is a leaf node, the current number is returned as part of the sum.
   - If not, the function continues to traverse the left and right children recursively and sums up the results.

### Example Walkthrough:

#### Example 1:
**Input: root = [1,2,3]**

- Root-to-leaf paths: `1 -> 2` (forms 12), `1 -> 3` (forms 13).
- Total sum: `12 + 13 = 25`.

#### Example 2:
**Input: root = [4,9,0,5,1]**

- Root-to-leaf paths: `4 -> 9 -> 5` (forms 495), `4 -> 9 -> 1` (forms 491), `4 -> 0` (forms 40).
- Total sum: `495 + 491 + 40 = 1026`.

### Time Complexity:
- **O(n)**, where `n` is the number of nodes in the binary tree. Each node is visited once during the DFS traversal.

### Space Complexity:
- **O(h)**, where `h` is the height of the tree. This is the space required for the recursive call stack. In the worst case, the height of the tree can be the number of nodes, making the space complexity O(n), but typically it's O(log n) for a balanced tree.
