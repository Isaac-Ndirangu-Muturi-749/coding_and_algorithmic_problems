# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            # Check if the current node is a "good" node
            is_good = node.val >= max_val
            count = 1 if is_good else 0

            # Update the maximum value seen so far
            max_val = max(max_val, node.val)

            # Traverse left and right subtrees
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count

        # Start DFS traversal from the root
        return dfs(root, root.val)
