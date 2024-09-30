from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Happy number
    n1 = 19
    expected_output1 = True
    assert solution.isHappy(n1) == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {solution.isHappy(n1)}"
    print("Test case 1 passed")

    # Test case 2: Not a happy number
    n2 = 2
    expected_output2 = False
    assert solution.isHappy(n2) == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {solution.isHappy(n2)}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
