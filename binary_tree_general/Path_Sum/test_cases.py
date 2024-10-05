from solution import Solution
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(lst, index=0) -> Optional[TreeNode]:
    """Helper function to build a binary tree from a list."""
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = build_tree(lst, 2 * index + 1)
    root.right = build_tree(lst, 2 * index + 2)
    return root

def run_tests():
    solution = Solution()

    # Test case 1
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    targetSum1 = 22
    expected_output1 = True
    result1 = solution.hasPathSum(root1, targetSum1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    root2 = build_tree([1,2,3])
    targetSum2 = 5
    expected_output2 = False
    result2 = solution.hasPathSum(root2, targetSum2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    root3 = build_tree([])
    targetSum3 = 0
    expected_output3 = False
    result3 = solution.hasPathSum(root3, targetSum3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

if __name__ == '__main__':
    run_tests()
