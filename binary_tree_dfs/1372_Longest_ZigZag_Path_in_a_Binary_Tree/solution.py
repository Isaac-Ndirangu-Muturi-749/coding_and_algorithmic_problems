# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

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
