from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    prices = [7, 1, 5, 3, 6, 4]
    expected_output = 7
    assert solution.maxProfit(prices) == expected_output, "Test case 1 failed"

    # Example 2
    prices = [1, 2, 3, 4, 5]
    expected_output = 4
    assert solution.maxProfit(prices) == expected_output, "Test case 2 failed"

    # Example 3
    prices = [7, 6, 4, 3, 1]
    expected_output = 0
    assert solution.maxProfit(prices) == expected_output, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
