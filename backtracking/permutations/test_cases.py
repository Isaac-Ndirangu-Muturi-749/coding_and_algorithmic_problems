from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Permutations of [1, 2, 3]
    nums1 = [1, 2, 3]
    result1 = solution.permute(nums1)
    expected1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Permutations of [0, 1]
    nums2 = [0, 1]
    result2 = solution.permute(nums2)
    expected2 = [[0, 1], [1, 0]]
    assert sorted(result2) == sorted(expected2), f"Test case 2 failed: Expected {expected2}, got {result2}"

    # Test case 3: Permutations of [1]
    nums3 = [1]
    result3 = solution.permute(nums3)
    expected3 = [[1]]
    assert result3 == expected3, f"Test case 3 failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
