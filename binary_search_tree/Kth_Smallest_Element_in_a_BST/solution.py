# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root
        count = 0

        # Iterate until we find the kth smallest or exhaust the tree
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the node at the top of the stack
            current = stack.pop()
            count += 1

            # If we've reached the kth smallest element, return its value
            if count == k:
                return current.val

            # Move to the right subtree
            current = current.right
