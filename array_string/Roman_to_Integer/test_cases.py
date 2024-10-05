from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    s1 = "III"
    expected_output1 = 3
    result1 = solution.romanToInt(s1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    s2 = "LVIII"
    expected_output2 = 58
    result2 = solution.romanToInt(s2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    s3 = "MCMXCIV"
    expected_output3 = 1994
    result3 = solution.romanToInt(s3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

    # Additional test case 4
    s4 = "CDXLIV"
    expected_output4 = 444
    result4 = solution.romanToInt(s4)
    assert result4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {result4}"
    print("Test case 4 passed")

    # Additional test case 5: Smallest Roman numeral
    s5 = "I"
    expected_output5 = 1
    result5 = solution.romanToInt(s5)
    assert result5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {result5}"
    print("Test case 5 passed")

if __name__ == '__main__':
    run_tests()
