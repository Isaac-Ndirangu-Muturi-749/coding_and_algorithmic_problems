from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    result1 = solution.threeSum(nums1)
    assert sorted(result1) == sorted(expected1), f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    nums2 = [0, 1, 1]
    expected2 = []
    result2 = solution.threeSum(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test Case 3
    nums3 = [0, 0, 0]
    expected3 = [[0, 0, 0]]
    result3 = solution.threeSum(nums3)
    assert sorted(result3) == sorted(expected3), f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
