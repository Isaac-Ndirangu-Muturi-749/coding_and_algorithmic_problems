# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function to validate the tree recursively
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True

            # The current node's value must be in the range (low, high)
            if not (low < node.val < high):
                return False

            # Recursively validate the left subtree and right subtree
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Start with the entire range of valid values for the root
        return validate(root, float('-inf'), float('inf'))
