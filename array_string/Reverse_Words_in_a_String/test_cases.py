from solution import Solution

def run_tests():
    solution = Solution()

    # Example 1
    s = "the sky is blue"
    expected_output = "blue is sky the"
    assert solution.reverseWords(s) == expected_output, "Test case 1 failed"

    # Example 2
    s = "  hello world  "
    expected_output = "world hello"
    assert solution.reverseWords(s) == expected_output, "Test case 2 failed"

    # Example 3
    s = "a good   example"
    expected_output = "example good a"
    assert solution.reverseWords(s) == expected_output, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
