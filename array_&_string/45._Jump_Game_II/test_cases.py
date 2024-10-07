from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    nums = [2, 3, 1, 1, 4]
    expected_output = 2
    assert solution.jump(nums) == expected_output, "Test case 1 failed"

    # Example 2
    nums = [2, 3, 0, 1, 4]
    expected_output = 2
    assert solution.jump(nums) == expected_output, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
