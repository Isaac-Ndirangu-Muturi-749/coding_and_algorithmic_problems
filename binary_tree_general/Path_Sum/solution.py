# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        # If the root is None, there is no path, so return False
        if not root:
            return False

        # If we are at a leaf node, check if the current targetSum matches the node's value
        if not root.left and not root.right:
            return targetSum == root.val

        # Recursively check left and right subtrees with the reduced targetSum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
