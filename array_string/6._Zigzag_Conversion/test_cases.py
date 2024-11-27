from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    s = "PAYPALISHIRING"
    numRows = 3
    expected_output = "PAHNAPLSIIGYIR"
    assert solution.convert(s, numRows) == expected_output, "Test case 1 failed"

    # Example 2
    s = "PAYPALISHIRING"
    numRows = 4
    expected_output = "PINALSIGYAHRPI"
    assert solution.convert(s, numRows) == expected_output, "Test case 2 failed"

    # Example 3
    s = "A"
    numRows = 1
    expected_output = "A"
    assert solution.convert(s, numRows) == expected_output, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
