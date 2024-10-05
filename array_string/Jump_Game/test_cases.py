from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, 1, 1, 4]
    expected_output1 = True
    result1 = solution.canJump(nums1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    nums2 = [3, 2, 1, 0, 4]
    expected_output2 = False
    result2 = solution.canJump(nums2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Additional test case 3: Can directly jump to the end
    nums3 = [0]
    expected_output3 = True
    result3 = solution.canJump(nums3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

    # Additional test case 4: Multiple steps with max jumps
    nums4 = [1, 2, 3, 0, 4, 0, 0, 5]
    expected_output4 = True
    result4 = solution.canJump(nums4)
    assert result4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {result4}"
    print("Test case 4 passed")

if __name__ == '__main__':
    run_tests()
