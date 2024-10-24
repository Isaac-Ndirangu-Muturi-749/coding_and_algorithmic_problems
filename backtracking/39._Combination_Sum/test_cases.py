from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected_output1 = [[2, 2, 3], [7]]
    assert sorted(solution.combinationSum(candidates1, target1)) == sorted(expected_output1), \
        f"Test case 1 failed: expected {expected_output1}, got {solution.combinationSum(candidates1, target1)}"

    # Test case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    expected_output2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert sorted(solution.combinationSum(candidates2, target2)) == sorted(expected_output2), \
        f"Test case 2 failed: expected {expected_output2}, got {solution.combinationSum(candidates2, target2)}"

    # Test case 3
    candidates3 = [2]
    target3 = 1
    expected_output3 = []
    assert solution.combinationSum(candidates3, target3) == expected_output3, \
        f"Test case 3 failed: expected {expected_output3}, got {solution.combinationSum(candidates3, target3)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
