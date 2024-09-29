from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    nums1 = [2, 2, 1]
    output1 = solution.singleNumber(nums1)
    expected1 = 1
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    output2 = solution.singleNumber(nums2)
    expected2 = 4
    print(f"Test case 2: {output2} == {expected2}")

    # Test case 3
    nums3 = [1]
    output3 = solution.singleNumber(nums3)
    expected3 = 1
    print(f"Test case 3: {output3} == {expected3}")

if __name__ == '__main__':
    run_tests()
