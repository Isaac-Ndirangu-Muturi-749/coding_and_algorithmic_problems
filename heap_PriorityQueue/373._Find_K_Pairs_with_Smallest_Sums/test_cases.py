from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1_1 = [1,7,11]
    nums2_1 = [2,4,6]
    k1 = 3
    expected_output1 = [[1,2],[1,4],[1,6]]
    assert solution.kSmallestPairs(nums1_1, nums2_1, k1) == expected_output1, \
        f"Test case 1 failed: expected {expected_output1}, got {solution.kSmallestPairs(nums1_1, nums2_1, k1)}"

    # Test case 2
    nums1_2 = [1,1,2]
    nums2_2 = [1,2,3]
    k2 = 2
    expected_output2 = [[1,1],[1,1]]
    assert solution.kSmallestPairs(nums1_2, nums2_2, k2) == expected_output2, \
        f"Test case 2 failed: expected {expected_output2}, got {solution.kSmallestPairs(nums1_2, nums2_2, k2)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
