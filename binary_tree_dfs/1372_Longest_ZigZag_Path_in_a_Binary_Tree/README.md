To solve the problem of finding the longest ZigZag path in a binary tree, we can use Depth-First Search (DFS). The key idea is to traverse the tree and track the current direction (left or right) and the length of the ZigZag path.


---

Approach:

1. Use DFS to traverse the tree.


2. At each node:

If moving in the left direction, recursively call DFS for the left child while switching the direction to right.

If moving in the right direction, recursively call DFS for the right child while switching the direction to left.



3. Track the maximum ZigZag length encountered during the traversal.


4. Return the maximum length.



Implementation:

class Solution:
    def longestZigZag(self, root):
        # Variable to store the maximum length
        self.max_length = 0

        # Helper function for DFS
        def dfs(node, direction, length):
            if not node:
                return
            # Update the maximum length
            self.max_length = max(self.max_length, length)
            # Continue DFS in both directions
            if direction == "left":
                dfs(node.left, "right", length + 1)  # Move left
                dfs(node.right, "left", 1)  # Reset and move right
            else:
                dfs(node.right, "left", length + 1)  # Move right
                dfs(node.left, "right", 1)  # Reset and move left

        # Start DFS from the root in both directions
        dfs(root.left, "right", 1)
        dfs(root.right, "left", 1)

        return self.max_length


---

Explanation of the Code:

1. DFS Traversal:

The dfs function traverses the tree while maintaining the current direction (left or right) and the length of the current ZigZag path.

If a null node is reached, the recursion stops.



2. Updating the Maximum Length:

At each node, the self.max_length variable is updated to track the longest ZigZag path found so far.



3. Recursive Calls:

If moving left, continue the ZigZag path with the left child and reset when moving to the right child.

If moving right, continue the ZigZag path with the right child and reset when moving to the left child.



4. Start DFS:

DFS is initiated from the root node, considering both possible initial directions (left and right).





---

Complexity Analysis:

1. Time Complexity: 

Every node is visited once during the DFS traversal.



2. Space Complexity: 

The space used is proportional to the height of the tree due to the recursive call stack.





---

Example Walkthrough:

Example 1:

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]

The longest ZigZag path is right -> left -> right.

Output: 3.


Example 2:

Input: root = [1,1,1,null,1,null,null,1,1,null,1]

The longest ZigZag path is left -> right -> left -> right.

Output: 4.


Example 3:

Input: root = [1]

A single node has no ZigZag path.

Output: 0.



---

This approach efficiently computes the longest ZigZag path while adhering to the constraints.

The resetting logic in the longestZigZag function ensures that the zigzag pattern starts fresh when switching directions. Here's a step-by-step explanation using the logic of the code:


---

Key Variables

1. direction: Indicates whether the current direction is "left" or "right".


2. length: Tracks the length of the current zigzag path.


3. self.max_length: Keeps track of the longest zigzag path encountered so far.




---

Resetting Logic

The resetting logic happens when switching directions:

When moving in one direction (e.g., "left"), the zigzag continues if the child node in the opposite direction (e.g., "right") is visited next.

If we explore a node that would "reset" the zigzag (e.g., visiting the same direction again), the length restarts from 1.



---

Code Breakdown

Example: Resetting in the Code

if direction == "left":
    dfs(node.left, "right", length + 1)  # Continue the zigzag by moving left
    dfs(node.right, "left", 1)  # Reset the zigzag and move right
else:
    dfs(node.right, "left", length + 1)  # Continue the zigzag by moving right
    dfs(node.left, "right", 1)  # Reset the zigzag and move left

Explanation

1. Continuing the Zigzag:

For the current node:

If the direction is "left", moving to node.left continues the zigzag, so we increment the length by 1.

If the direction is "right", moving to node.right continues the zigzag, so we increment the length by 1.




2. Resetting the Zigzag:

If switching direction, the zigzag resets:

If the direction is "left", moving to node.right starts a new zigzag, so the length is reset to 1.

If the direction is "right", moving to node.left starts a new zigzag, so the length is reset to 1.






---

Example Walkthrough

Tree:

1
       / \
      2   3
       \    \
        4    5
       /      \
      6        7

Step-by-Step Execution

1. Start DFS from root.left (2) with direction "right" and length 1.

Current node: 2, direction: "right", length: 1

Move:

Right: dfs(4, "left", length + 1) (Continue the zigzag, length becomes 2).

Left: dfs(None, "right", 1) (Reset the zigzag, length becomes 1).




2. At node 4, direction: "left", length: 2.

Move:

Left: dfs(6, "right", length + 1) (Continue the zigzag, length becomes 3).

Right: dfs(None, "left", 1) (Reset the zigzag, length becomes 1).




3. At node 6, direction: "right", length: 3.

Move:

Right: dfs(None, "left", 1) (Reset the zigzag, length becomes 1).

Left: dfs(None, "right", 1) (Reset the zigzag, length becomes 1).




4. Start DFS from root.right (3) with direction "left" and length 1.

Current node: 3, direction: "left", length: 1

Move:

Left: dfs(None, "right", 1) (Reset the zigzag, length becomes 1).

Right: dfs(5, "left", length + 1) (Continue the zigzag, length becomes 2).




5. At node 5, direction: "left", length: 2.

Move:

Left: dfs(None, "right", 1) (Reset the zigzag, length becomes 1).

Right: dfs(7, "left", length + 1) (Continue the zigzag, length becomes 3).




6. At node 7, direction: "left", length: 3.

Move:

Left: dfs(None, "right", 1) (Reset the zigzag, length becomes 1).

Right: dfs(None, "left", 1) (Reset the zigzag, length becomes 1).






---

Final Result

The longest zigzag path is 3, which occurs in both:

Path: 2 → 4 → 6

Path: 3 → 5 → 7.



The resetting ensures that each potential zigzag path is independently evaluated.

