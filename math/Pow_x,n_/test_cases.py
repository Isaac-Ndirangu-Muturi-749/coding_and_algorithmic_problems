from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    x1 = 2.00000
    n1 = 10
    expected_output1 = 1024.00000
    result1 = solution.myPow(x1, n1)
    assert abs(result1 - expected_output1) < 1e-5, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    x2 = 2.10000
    n2 = 3
    expected_output2 = 9.26100
    result2 = solution.myPow(x2, n2)
    assert abs(result2 - expected_output2) < 1e-5, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    x3 = 2.00000
    n3 = -2
    expected_output3 = 0.25000
    result3 = solution.myPow(x3, n3)
    assert abs(result3 - expected_output3) < 1e-5, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

if __name__ == '__main__':
    run_tests()
