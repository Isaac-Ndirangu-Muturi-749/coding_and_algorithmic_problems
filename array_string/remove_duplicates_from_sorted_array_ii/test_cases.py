from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = solution.removeDuplicates(nums1)
    assert k1 == 5, f"Test case 1 failed: Expected 5, got {k1}"
    assert nums1[:k1] == [1, 1, 2, 2, 3], f"Test case 1 failed: Expected [1, 1, 2, 2, 3], got {nums1[:k1]}"

    # Test case 2
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k2 = solution.removeDuplicates(nums2)
    assert k2 == 7, f"Test case 2 failed: Expected 7, got {k2}"
    assert nums2[:k2] == [0, 0, 1, 1, 2, 3, 3], f"Test case 2 failed: Expected [0, 0, 1, 1, 2, 3, 3], got {nums2[:k2]}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
