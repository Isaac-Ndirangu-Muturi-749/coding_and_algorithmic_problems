from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    output1 = solution.two_sum(nums1, target1)
    print(f"Test case 1 output: {output1} (Expected: [0, 1])")

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    output2 = solution.two_sum(nums2, target2)
    print(f"Test case 2 output: {output2} (Expected: [1, 2])")

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    output3 = solution.two_sum(nums3, target3)
    print(f"Test case 3 output: {output3} (Expected: [0, 1])")

if __name__ == '__main__':
    run_tests()
