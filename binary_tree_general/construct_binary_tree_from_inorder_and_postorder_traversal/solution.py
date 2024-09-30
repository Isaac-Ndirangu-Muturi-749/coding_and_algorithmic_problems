# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        # Dictionary to store the index of each value in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to recursively build the tree
        def build(in_left, in_right):
            # If there are no elements to construct the subtree
            if in_left > in_right:
                return None

            # Pick the last element in postorder as a root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # Root splits inorder list into left and right subtrees
            index = inorder_map[root_val]

            # Build right subtree first because of postorder (L -> R -> Root)
            root.right = build(index + 1, in_right)
            # Build left subtree
            root.left = build(in_left, index - 1)

            return root

        # Start building the tree from the entire inorder range
        return build(0, len(inorder) - 1)
