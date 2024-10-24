from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 2, 3, 2]
    expected_output1 = 3
    assert solution.singleNumber(nums1) == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {solution.singleNumber(nums1)}"

    # Test case 2
    nums2 = [0, 1, 0, 1, 0, 1, 99]
    expected_output2 = 99
    assert solution.singleNumber(nums2) == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {solution.singleNumber(nums2)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
