from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    output1 = solution.searchRange(nums1, target1)
    print(f"Test case 1 output: {output1} (Expected: [3, 4])")

    # Test case 2
    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    output2 = solution.searchRange(nums2, target2)
    print(f"Test case 2 output: {output2} (Expected: [-1, -1])")

    # Test case 3
    nums3 = []
    target3 = 0
    output3 = solution.searchRange(nums3, target3)
    print(f"Test case 3 output: {output3} (Expected: [-1, -1])")

if __name__ == '__main__':
    run_tests()
