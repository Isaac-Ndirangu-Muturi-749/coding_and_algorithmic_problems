from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_output1 = 4
    assert solution.lengthOfLIS(nums1) == expected_output1, f"Test case 1 failed. Expected {expected_output1}"

    # Test case 2
    nums2 = [0, 1, 0, 3, 2, 3]
    expected_output2 = 4
    assert solution.lengthOfLIS(nums2) == expected_output2, f"Test case 2 failed. Expected {expected_output2}"

    # Test case 3
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    expected_output3 = 1
    assert solution.lengthOfLIS(nums3) == expected_output3, f"Test case 3 failed. Expected {expected_output3}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
