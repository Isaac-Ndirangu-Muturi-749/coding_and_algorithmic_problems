# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

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
