from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    expected_output1 = 5
    result1 = solution.maxProfit(prices1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    expected_output2 = 0
    result2 = solution.maxProfit(prices2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
