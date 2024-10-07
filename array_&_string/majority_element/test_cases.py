from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    nums1 = [3, 2, 3]
    expected1 = 3
    result1 = solution.majorityElement(nums1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    expected2 = 2
    result2 = solution.majorityElement(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
