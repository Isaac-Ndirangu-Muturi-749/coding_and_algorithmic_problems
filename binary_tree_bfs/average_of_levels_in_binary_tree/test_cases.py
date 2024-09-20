from solution import Solution
from solution import TreeNode  # Assuming TreeNode is defined in the solution file

def list_to_tree(lst):
    """Helper function to convert a list into a binary tree."""
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def run_tests():
    solution = Solution()

    # Test case 1: Average of levels in binary tree [3, 9, 20, None, None, 15, 7]
    tree1 = list_to_tree([3, 9, 20, None, None, 15, 7])
    result1 = solution.averageOfLevels(tree1)
    expected1 = [3.00000, 14.50000, 11.00000]
    assert [round(val, 5) for val in result1] == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Average of levels in binary tree [3, 9, 20, 15, 7]
    tree2 = list_to_tree([3, 9, 20, 15, 7])
    result2 = solution.averageOfLevels(tree2)
    expected2 = [3.00000, 14.50000, 11.00000]
    assert [round(val, 5) for val in result2] == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
