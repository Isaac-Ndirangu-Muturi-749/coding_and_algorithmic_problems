class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        # Helper function to convert array to BST
        def convert_to_bst(left, right):
            if left > right:
                return None

            # Choose the middle element as the root
            mid = (left + right) // 2
            node = TreeNode(nums[mid])

            # Recursively build the left and right subtrees
            node.left = convert_to_bst(left, mid - 1)
            node.right = convert_to_bst(mid + 1, right)

            return node

        # Start with the full range of the array
        return convert_to_bst(0, len(nums) - 1)
