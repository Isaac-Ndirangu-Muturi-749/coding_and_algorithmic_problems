from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Positive palindrome
    assert solution.isPalindrome(121) == True, "Test case 1 failed"

    # Test case 2: Negative number (not a palindrome)
    assert solution.isPalindrome(-121) == False, "Test case 2 failed"

    # Test case 3: Non-palindrome
    assert solution.isPalindrome(10) == False, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
