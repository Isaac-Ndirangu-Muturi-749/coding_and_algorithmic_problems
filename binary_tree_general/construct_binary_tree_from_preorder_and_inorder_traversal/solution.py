# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Dictionary to store the index of each value in the inorder list
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to recursively build the tree
        def buildSubTree(pre_left, pre_right, in_left, in_right):
            # Base case: if there are no elements to construct the subtree
            if pre_left > pre_right or in_left > in_right:
                return None

            # The first element of preorder is the root of the subtree
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Root's index in the inorder traversal
            inorder_root_index = inorder_index_map[root_val]

            # Number of elements in the left subtree
            left_subtree_size = inorder_root_index - in_left

            # Recursively build the left and right subtrees
            root.left = buildSubTree(pre_left + 1, pre_left + left_subtree_size, in_left, inorder_root_index - 1)
            root.right = buildSubTree(pre_left + left_subtree_size + 1, pre_right, inorder_root_index + 1, in_right)

            return root

        # Build the tree using the entire range of preorder and inorder arrays
        return buildSubTree(0, len(preorder) - 1, 0, len(inorder) - 1)
