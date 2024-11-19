# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # Get the height of the leftmost and rightmost paths
        def get_tree_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        left_depth = get_tree_depth(root.left)
        right_depth = get_tree_depth(root.right)

        if left_depth == right_depth:
            # Left subtree is perfect; its size is 2^left_depth - 1 plus the root
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is perfect; its size is 2^right_depth - 1 plus the root
            return (1 << right_depth) + self.countNodes(root.left)
