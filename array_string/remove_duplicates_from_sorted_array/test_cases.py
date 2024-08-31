from solution import Solution

def run_tests():
    solution = Solution()

    nums1 = [1,1,2]
    assert solution.removeDuplicates(nums1) == 2
    assert nums1[:2] == [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums2) == 5
    assert nums2[:5] == [0, 1, 2, 3, 4]

    nums3 = [1, 2, 3, 4, 5]
    assert solution.removeDuplicates(nums3) == 5
    assert nums3[:5] == [1, 2, 3, 4, 5]

    nums4 = []
    assert solution.removeDuplicates(nums4) == 0

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
