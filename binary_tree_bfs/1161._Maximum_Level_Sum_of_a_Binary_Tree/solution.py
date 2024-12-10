# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a queue for level-order traversal
        queue = collections.deque([root])
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
