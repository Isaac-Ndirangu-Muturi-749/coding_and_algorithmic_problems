from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    x1 = 4
    expected_output1 = 2
    assert solution.mySqrt(x1) == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {solution.mySqrt(x1)}"
    print("Test case 1 passed")

    # Test case 2
    x2 = 8
    expected_output2 = 2
    assert solution.mySqrt(x2) == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {solution.mySqrt(x2)}"
    print("Test case 2 passed")

    # You can add more test cases similarly if needed

if __name__ == '__main__':
    run_tests()
