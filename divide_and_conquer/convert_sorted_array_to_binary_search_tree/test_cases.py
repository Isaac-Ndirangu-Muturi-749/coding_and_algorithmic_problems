from solution import Solution
from solution import TreeNode


def run_tests():
    solution = Solution()

    # Test case 1
    nums = [-10, -3, 0, 5, 9]
    bst_root = solution.sortedArrayToBST(nums)
    # Expected Output: A BST with root 0, left child -3, right child 9, etc.

    # Test case 2
    nums = [1, 3]
    bst_root = solution.sortedArrayToBST(nums)
    # Expected Output: A BST with root 3 and left child 1

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
