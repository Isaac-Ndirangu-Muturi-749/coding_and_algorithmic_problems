Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # Helper function to collect leaf values
        def get_leaves(root):
            leaves = []

            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:  # Check if it's a leaf node
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return leaves

        # Get leaf sequences for both trees
        leaves1 = get_leaves(root1)
        leaves2 = get_leaves(root2)

        # Compare leaf sequences
        return leaves1 == leaves2
