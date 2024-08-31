from solution import Solution

def run_tests():
    solution = Solution()
    # Add your test cases here
    solution = Solution()

    # Test cases
    assert solution.wordPattern("abba", "dog cat cat dog") == True, "Test case 1 failed"
    assert solution.wordPattern("abba", "dog cat cat fish") == False, "Test case 2 failed"
    assert solution.wordPattern("aaaa", "dog cat cat dog") == False, "Test case 3 failed"
    assert solution.wordPattern("abba", "dog dog dog dog") == False, "Test case 4 failed"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
