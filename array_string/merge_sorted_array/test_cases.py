from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: General case with overlapping elements
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6], f"Test case 1 failed: {nums1}"

    # Test case 2: No elements in nums2, nums1 remains unchanged
    nums1 = [1]
    nums2 = []
    m = 1
    n = 0
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Test case 2 failed: {nums1}"

    # Test case 3: No elements in nums1, nums1 should become nums2
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1], f"Test case 3 failed: {nums1}"

    # Test case 4: All elements in nums1 are smaller than those in nums2
    nums1 = [1,2,3,0,0,0]
    nums2 = [4,5,6]
    m = 3
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6], f"Test case 4 failed: {nums1}"

    # Test case 5: All elements in nums1 are larger than those in nums2
    nums1 = [4,5,6,0,0,0]
    nums2 = [1,2,3]
    m = 3
    n = 3
    solution.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,3,4,5,6], f"Test case 5 failed: {nums1}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
