from solution import Solution

def run_tests():
    solution = Solution()

    # Define test cases
    test_cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "1", "10"),
        ("1101", "1011", "11000"),
        ("111", "1", "1000"),
        ("1111", "1111", "11110")
    ]

    # Run and check each test case
    for a, b, expected in test_cases:
        result = solution.addBinary(a, b)
        assert result == expected, f"Test failed for a={a}, b={b}. Expected {expected}, got {result}"

    print("All tests passed!")

if __name__ == '__main__':
    run_tests()
