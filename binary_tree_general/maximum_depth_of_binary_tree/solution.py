class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty
        if root is None:
            return 0

        # Recursive case: calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # The maximum depth is the larger of the two depths plus one for the current node
        return 1 + max(left_depth, right_depth)
