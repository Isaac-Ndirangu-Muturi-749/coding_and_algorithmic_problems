from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.maxDepth(root) == 3, "Test case 1 failed"

    # Test case 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    assert solution.maxDepth(root) == 2, "Test case 2 failed"

    # Test case 3: Empty tree
    root = None
    assert solution.maxDepth(root) == 0, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
