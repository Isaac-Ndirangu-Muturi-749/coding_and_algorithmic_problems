from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [3, 4, 5, 1, 2]
    expected_output1 = 1
    result1 = solution.findMin(nums1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    expected_output2 = 0
    result2 = solution.findMin(nums2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    nums3 = [11, 13, 15, 17]
    expected_output3 = 11
    result3 = solution.findMin(nums3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

if __name__ == '__main__':
    run_tests()
