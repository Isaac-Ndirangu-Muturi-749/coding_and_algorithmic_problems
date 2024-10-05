# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

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
