# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Base case: if root is None, or root matches either p or q, return root
        if not root or root == p or root == q:
            return root

        # Recur for left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, this is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null value
        return left if left else right
