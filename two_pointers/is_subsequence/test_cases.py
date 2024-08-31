from solution import Solution

def run_tests():
    solution = Solution()

    assert solution.isSubsequence("abc", "ahbgdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False
    assert solution.isSubsequence("", "ahbgdc") == True
    assert solution.isSubsequence("abc", "abc") == True
    assert solution.isSubsequence("abc", "") == False

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
