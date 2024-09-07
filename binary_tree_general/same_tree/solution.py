class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both trees are empty
        if not p and not q:
            return True
        # One tree is empty, and the other is not
        if not p or not q:
            return False
        # Both trees are non-empty, compare values and subtrees
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
