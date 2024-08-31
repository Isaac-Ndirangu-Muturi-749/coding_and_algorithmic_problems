from solution import Solution

def run_tests():
    solution = Solution()

    assert solution.isIsomorphic("egg", "add") == True, "Test case 1 failed"
    assert solution.isIsomorphic("foo", "bar") == False, "Test case 2 failed"
    assert solution.isIsomorphic("paper", "title") == True, "Test case 3 failed"
    assert solution.isIsomorphic("abc", "xyz") == True, "Test case 4 failed"
    assert solution.isIsomorphic("ab", "aa") == False, "Test case 5 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
