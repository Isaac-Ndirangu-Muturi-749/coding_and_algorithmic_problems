class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.prev = -1  # To store the value of the previous node
        self.min_diff = float('inf')  # Initialize min_diff to a large value

        def in_order_traversal(node):
            if not node:
                return

            # Traverse the left subtree
            in_order_traversal(node.left)

            # Process the current node
            if self.prev != -1:  # Check if this is not the first node
                # Update the minimum difference
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update prev to the current node's value

            # Traverse the right subtree
            in_order_traversal(node.right)

        # Start the in-order traversal from the root
        in_order_traversal(root)

        return self.min_diff
