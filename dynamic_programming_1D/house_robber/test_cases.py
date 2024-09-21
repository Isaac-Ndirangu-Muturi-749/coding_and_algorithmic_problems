from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1]
    assert solution.rob(nums1) == 4, "Test case 1 failed"

    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    assert solution.rob(nums2) == 12, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
