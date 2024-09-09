from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums1) == 6, f"Test case 1 failed: {solution.maxSubArray(nums1)}"

    # Test case 2
    nums2 = [1]
    assert solution.maxSubArray(nums2) == 1, f"Test case 2 failed: {solution.maxSubArray(nums2)}"

    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    assert solution.maxSubArray(nums3) == 23, f"Test case 3 failed: {solution.maxSubArray(nums3)}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
