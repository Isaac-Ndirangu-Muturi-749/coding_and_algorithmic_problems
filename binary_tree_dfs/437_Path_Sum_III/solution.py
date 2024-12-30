# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, curr_sum):
            if not node:
                return 0

            # Update the current prefix sum
            curr_sum += node.val

            # Count paths that end at the current node and sum to targetSum
            count = prefix_sums.get(curr_sum - targetSum, 0)

            # Update the prefix_sums dictionary
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            # Recurse to left and right children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove the current prefix sum from the map
            prefix_sums[curr_sum] -= 1

            return count

        # Dictionary to store the prefix sums
        prefix_sums = {0: 1}

        return dfs(root, 0)
