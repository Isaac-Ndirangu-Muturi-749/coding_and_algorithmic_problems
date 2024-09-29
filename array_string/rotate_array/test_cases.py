from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    solution.rotate(nums1, k1)
    print(f"Test case 1 output: {nums1} (Expected: [5, 6, 7, 1, 2, 3, 4])")

    # Test case 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    solution.rotate(nums2, k2)
    print(f"Test case 2 output: {nums2} (Expected: [3, 99, -1, -100])")

if __name__ == '__main__':
    run_tests()
