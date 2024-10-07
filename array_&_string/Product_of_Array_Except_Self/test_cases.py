from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4]
    expected_output = [24, 12, 8, 6]
    assert solution.productExceptSelf(nums) == expected_output, "Test case 1 failed"

    # Example 2
    nums = [-1, 1, 0, -3, 3]
    expected_output = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(nums) == expected_output, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
