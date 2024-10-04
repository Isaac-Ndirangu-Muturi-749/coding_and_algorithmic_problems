from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    n1 = 3
    expected_output1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    result1 = solution.generateParenthesis(n1)
    assert sorted(result1) == sorted(expected_output1), f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    n2 = 1
    expected_output2 = ["()"]
    result2 = solution.generateParenthesis(n2)
    assert sorted(result2) == sorted(expected_output2), f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
