from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    num = 3749
    expected_output = "MMMDCCXLIX"
    assert solution.intToRoman(num) == expected_output, "Test case 1 failed"

    # Example 2
    num = 58
    expected_output = "LVIII"
    assert solution.intToRoman(num) == expected_output, "Test case 2 failed"

    # Example 3
    num = 1994
    expected_output = "MCMXCIV"
    assert solution.intToRoman(num) == expected_output, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
