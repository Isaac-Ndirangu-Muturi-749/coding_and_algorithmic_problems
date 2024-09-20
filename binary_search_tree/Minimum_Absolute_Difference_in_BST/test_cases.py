from solution import Solution, TreeNode

def build_tree(values):
    """Helper function to build a binary tree from a list of values."""
    if not values:
        return None
    nodes = [None if val is None else TreeNode(val) for val in values]
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if 2 * i + 1 < len(nodes):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def run_tests():
    solution = Solution()

    # Test case 1: Input [4,2,6,1,3]
    root1 = build_tree([4, 2, 6, 1, 3])
    result1 = solution.getMinimumDifference(root1)
    expected1 = 1
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Input [1,0,48,null,null,12,49]
    root2 = build_tree([1, 0, 48, None, None, 12, 49])
    result2 = solution.getMinimumDifference(root2)
    expected2 = 1
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
