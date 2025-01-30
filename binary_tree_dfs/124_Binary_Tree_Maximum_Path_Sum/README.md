Solution: Maximum Path Sum in a Binary Tree

The problem requires finding the maximum path sum in a binary tree, where a path is any sequence of nodes connected by edges, appearing at most once in the sequence.


---

Key Observations

1. A path can start and end at any node—it doesn’t need to include the root.


2. Each node can contribute to the maximum path sum in two ways:

As part of a larger path that continues upwards through its parent.

As a root of a subtree, forming a new maximum path that doesn’t extend upwards.



3. The key challenge is to efficiently explore all paths and track the maximum sum encountered.




---

Approach

We use Depth-First Search (DFS) to explore all paths while maintaining a global variable for the maximum sum.

1. Define a recursive helper function that:

Computes the maximum path sum that includes the current node and at most one of its children.

Updates the global maximum path sum if a split path (left + node + right) has a higher sum.



2. Base case: If a node is None, return 0 (no contribution).


3. Recursively compute the maximum path sum for left and right subtrees.


4. Ignore negative contributions—if a subtree has a negative sum, we treat it as 0.


5. Return the maximum path sum that can be extended upwards (either left or right child plus the node value).




---

Algorithm

1. Initialize a global variable max_sum = -inf to store the maximum path sum.


2. Define a recursive function max_gain(node):

If node is None, return 0.

Compute left_gain and right_gain using max(0, max_gain(node.left)) and max(0, max_gain(node.right)) (ignore negative sums).

Compute the path sum if the current node is treated as the highest node:
new_path_sum = node.val + left_gain + right_gain

Update max_sum if new_path_sum is greater.

Return node.val + max(left_gain, right_gain) (extend the path).



3. Start DFS from the root node and return max_sum.




---

Implementation

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Step 1: Initialize global variable to track max sum
        self.max_sum = float('-inf')

        # Step 2: Define recursive function to compute max gain
        def max_gain(node):
            if not node:
                return 0  # Base case: null nodes contribute 0

            # Step 3: Compute max sum from left and right subtrees
            left_gain = max(0, max_gain(node.left))  # Ignore negative sums
            right_gain = max(0, max_gain(node.right))

            # Step 4: Compute path sum if node is treated as root
            new_path_sum = node.val + left_gain + right_gain

            # Step 5: Update global max sum if new path is greater
            self.max_sum = max(self.max_sum, new_path_sum)

            # Step 6: Return max path sum extendable upwards
            return node.val + max(left_gain, right_gain)

        # Step 7: Start recursion from root
        max_gain(root)

        # Step 8: Return the maximum path sum found
        return self.max_sum


---

Explanation of Code

Recursive Function max_gain(node)

Computes the best path sum including node that can extend to its parent.

Uses max(0, ...) to ignore negative contributions.

Updates self.max_sum if the sum of the left, right, and node is the highest so far.


Tracking the Maximum Path Sum

self.max_sum ensures we track the best path found across all recursive calls.

Even if the path doesn’t include the root, it will still be counted.



---

Complexity Analysis

Time Complexity: O(n) (Each node is visited once)

Space Complexity: O(h) (Recursive depth, h = height of the tree)

In a balanced tree, h = log(n), so O(log n)

In a skewed tree, h = n, so O(n) worst case




---

Example Walkthrough

Example 1

Input: root = [1,2,3]

       1
      / \
     2   3

Output: 6

Step-by-step:

max_gain(2) → left_gain = 0, right_gain = 0 → return 2
max_gain(3) → left_gain = 0, right_gain = 0 → return 3
max_gain(1) → left_gain = 2, right_gain = 3
  new_path_sum = 1 + 2 + 3 = 6
  Update max_sum = 6


---

Example 2

Input: root = [-10,9,20,null,null,15,7]

       -10
       /  \
      9   20
         /  \
        15   7

Output: 42

Step-by-step:

max_gain(9) → return 9
max_gain(15) → return 15
max_gain(7) → return 7
max_gain(20) → left_gain = 15, right_gain = 7
  new_path_sum = 20 + 15 + 7 = 42
  Update max_sum = 42
max_gain(-10) → left_gain = 9, right_gain = 35
  new_path_sum = -10 + 9 + 35 = 34
  max_sum remains 42

Final output: 42.


---

Edge Cases

1. Single Node

Input: root = [5]
Output: 5


2. All Negative Values

Input: root = [-3, -2, -1]
Output: -1

We take the least negative node since adding more negative values reduces the sum.



3. Skewed Tree (Linked List)

Input: root = [1,2,3,4,5]
Output: 15

The best path is the entire list.





---

Final Thoughts

DFS with a global variable ensures an efficient O(n) solution.

Handles negative values correctly using max(0, ...).

Handles all paths efficiently, including those not passing through the root.


✅ Best approach for solving Maximum Path Sum in a Binary Tree! 🚀

The right gain is 35 because it is the maximum path sum obtained from the right subtree of node -10. Let's break it down step by step.


---

Given Binary Tree (Assumption)

We assume the tree looks something like this:

-10
      /    \
    9      20
         /    \
       15      7


---

Breakdown of max_gain(node)

Step 1: Compute max_gain(9)

9 is a leaf node, so:

max_gain(9) = 9


Step 2: Compute max_gain(15)

15 is a leaf node, so:

max_gain(15) = 15


Step 3: Compute max_gain(7)

7 is a leaf node, so:

max_gain(7) = 7


Step 4: Compute max_gain(20)

left_gain = max_gain(15) = 15

right_gain = max_gain(7) = 7

Compute new_path_sum:

new_path_sum = 20 + 15 + 7 = 42

Update max_sum = 42

Return the max single-path gain:

max_gain(20) = 20 + max(15, 7) = 20 + 15 = 35


Step 5: Compute max_gain(-10)

left_gain = max_gain(9) = 9

right_gain = max_gain(20) = 35

Compute new_path_sum:

new_path_sum = -10 + 9 + 35 = 34

Since 34 is less than max_sum (42), we do not update max_sum.

Return the max single-path gain:

max_gain(-10) = -10 + max(9, 35) = -10 + 35 = 25



---

Why is right gain 35?

When computing max_gain(-10), the right child of -10 is 20.

The maximum path sum from 20 (not including both children) is:

20 + max(15, 7) = 20 + 15 = 35

This is why right_gain = 35.


Would you like me to clarify anything further?

