from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    assert set(solution.letterCombinations("23")) == set(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]), "Test case 1 failed"

    # Test case 2
    assert solution.letterCombinations("") == [], "Test case 2 failed"

    # Test case 3
    assert set(solution.letterCombinations("2")) == set(["a", "b", "c"]), "Test case 3 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()

