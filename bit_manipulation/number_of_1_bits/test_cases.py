from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1: n = 11 (binary 1011)
    result1 = solution.hammingWeight(11)
    expected1 = 3
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Example 2: n = 128 (binary 10000000)
    result2 = solution.hammingWeight(128)
    expected2 = 1
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    # Example 3: n = 2147483645 (binary 1111111111111111111111111111101)
    result3 = solution.hammingWeight(2147483645)
    expected3 = 30
    assert result3 == expected3, f"Test case 3 failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
