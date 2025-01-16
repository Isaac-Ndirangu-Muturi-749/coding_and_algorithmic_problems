# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None  # Base case: If the root is null, return None

        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            if not root.left:  # Case 1 & 2: No left child or no child at all
                return root.right
            elif not root.right:  # Case 1 & 2: No right child
                return root.left
            else:
                # Case 3: Node has two children
                # Find the inorder successor (minimum value in the right subtree)
                successor = self.getMin(root.right)
                root.val = successor.val  # Replace value with successor's value
                root.right = self.deleteNode(root.right, successor.val)  # Delete successor

        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node
