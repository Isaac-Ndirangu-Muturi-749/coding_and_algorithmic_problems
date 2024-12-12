# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:  # Base case: Node not found
            return None
        if root.val == val:  # Node with the target value found
            return root
        elif val < root.val:  # Search in the left subtree
            return self.searchBST(root.left, val)
        else:  # Search in the right subtree
            return self.searchBST(root.right, val)
