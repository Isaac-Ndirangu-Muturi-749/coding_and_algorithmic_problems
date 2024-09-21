from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    expected1 = True
    result1 = solution.wordBreak(s1, wordDict1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    expected2 = True
    result2 = solution.wordBreak(s2, wordDict2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    expected3 = False
    result3 = solution.wordBreak(s3, wordDict3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
