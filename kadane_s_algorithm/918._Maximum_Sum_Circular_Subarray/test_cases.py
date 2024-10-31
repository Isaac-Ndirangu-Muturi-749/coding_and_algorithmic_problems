from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [1, -2, 3, -2]
    expected_output1 = 3
    assert solution.maxSubarraySumCircular(nums1) == expected_output1, \
        f"Test case 1 failed: expected {expected_output1}, got {solution.maxSubarraySumCircular(nums1)}"

    # Test case 2
    nums2 = [5, -3, 5]
    expected_output2 = 10
    assert solution.maxSubarraySumCircular(nums2) == expected_output2, \
        f"Test case 2 failed: expected {expected_output2}, got {solution.maxSubarraySumCircular(nums2)}"

    # Test case 3
    nums3 = [-3, -2, -3]
    expected_output3 = -2
    assert solution.maxSubarraySumCircular(nums3) == expected_output3, \
        f"Test case 3 failed: expected {expected_output3}, got {solution.maxSubarraySumCircular(nums3)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
