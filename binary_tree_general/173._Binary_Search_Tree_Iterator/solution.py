# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Initialize the iterator with the root of the BST.
        """
        self.stack = []
        self._push_left(root)  # Populate the stack with the leftmost nodes.

    def _push_left(self, node: TreeNode):
        """
        Helper function to push all the leftmost nodes of a subtree to the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        """
        # Pop the top element from the stack.
        curr = self.stack.pop()
        # If the current node has a right child, process its leftmost subtree.
        if curr.right:
            self._push_left(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        """
        Return True if there are more nodes to traverse, otherwise False.
        """
        return len(self.stack) > 0
