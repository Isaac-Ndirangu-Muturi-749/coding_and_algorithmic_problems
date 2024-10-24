from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    left1 = 5
    right1 = 7
    expected_output1 = 4
    assert solution.rangeBitwiseAnd(left1, right1) == expected_output1, \
        f"Test case 1 failed: expected {expected_output1}, got {solution.rangeBitwiseAnd(left1, right1)}"

    # Test case 2
    left2 = 0
    right2 = 0
    expected_output2 = 0
    assert solution.rangeBitwiseAnd(left2, right2) == expected_output2, \
        f"Test case 2 failed: expected {expected_output2}, got {solution.rangeBitwiseAnd(left2, right2)}"

    # Test case 3
    left3 = 1
    right3 = 2147483647
    expected_output3 = 0
    assert solution.rangeBitwiseAnd(left3, right3) == expected_output3, \
        f"Test case 3 failed: expected {expected_output3}, got {solution.rangeBitwiseAnd(left3, right3)}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
