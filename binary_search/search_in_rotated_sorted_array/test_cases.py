from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    output1 = solution.search(nums1, target1)
    expected1 = 4
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3
    output2 = solution.search(nums2, target2)
    expected2 = -1
    print(f"Test case 2: {output2} == {expected2}")

    # Test case 3
    nums3 = [1]
    target3 = 0
    output3 = solution.search(nums3, target3)
    expected3 = -1
    print(f"Test case 3: {output3} == {expected3}")

if __name__ == '__main__':
    run_tests()
