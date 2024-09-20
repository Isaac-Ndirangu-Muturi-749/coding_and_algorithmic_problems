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

    # Test case 1: BST [3,1,4,null,2], k = 1
    tree1 = list_to_tree([3, 1, 4, None, 2])
    result1 = solution.kthSmallest(tree1, 1)
    expected1 = 1
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: BST [5,3,6,2,4,null,null,1], k = 3
    tree2 = list_to_tree([5, 3, 6, 2, 4, None, None, 1])
    result2 = solution.kthSmallest(tree2, 3)
    expected2 = 3
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
