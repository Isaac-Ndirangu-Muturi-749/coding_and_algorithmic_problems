from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    s1 = "babad"
    expected_output1 = "bab"  # "aba" is also a valid answer
    result1 = solution.longestPalindrome(s1)
    assert result1 == expected_output1 or result1 == "aba", f"Test case 1 failed: Expected {expected_output1} or 'aba', got {result1}"
    print("Test case 1 passed")

    # Test case 2
    s2 = "cbbd"
    expected_output2 = "bb"
    result2 = solution.longestPalindrome(s2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

if __name__ == '__main__':
    run_tests()
