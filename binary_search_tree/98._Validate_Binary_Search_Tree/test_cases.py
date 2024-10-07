from solution import Solution
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(vals):
    """Helper function to build a binary tree from a list of values using BFS."""
    if not vals:
        return None

    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()

        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1

        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1

    return root

def run_tests():
    solution = Solution()

    # Test Case 1: Valid BST
    root = build_tree_from_list([2, 1, 3])
    assert solution.isValidBST(root) == True, "Test case 1 failed"

    # Test Case 2: Invalid BST
    root = build_tree_from_list([5, 1, 4, None, None, 3, 6])
    assert solution.isValidBST(root) == False, "Test case 2 failed"

    # Additional Test Case: Single Node Tree (Valid BST)
    root = build_tree_from_list([1])
    assert solution.isValidBST(root) == True, "Test case 3 failed"

    # Additional Test Case: Empty Tree (Valid BST)
    root = build_tree_from_list([])
    assert solution.isValidBST(root) == True, "Test case 4 failed"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
