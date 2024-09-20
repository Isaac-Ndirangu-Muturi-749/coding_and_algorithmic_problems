from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Input [1, 2, 3, 1]
    nums1 = [1, 2, 3, 1]
    result1 = solution.findPeakElement(nums1)
    expected1 = 2  # 3 is a peak at index 2
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Input [1, 2, 1, 3, 5, 6, 4]
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    result2 = solution.findPeakElement(nums2)
    expected2 = 5  # 6 is a peak at index 5 (but index 1 with value 2 is also valid)
    assert result2 == expected2 or result2 == 1, f"Test case 2 failed: Expected {expected2} or 1, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
