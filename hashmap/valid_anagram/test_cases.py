from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Anagram of "anagram" and "nagaram"
    s1 = "anagram"
    t1 = "nagaram"
    result1 = solution.isAnagram(s1, t1)
    assert result1 == True, f"Test case 1 failed: Expected True, got {result1}"

    # Test case 2: "rat" is not an anagram of "car"
    s2 = "rat"
    t2 = "car"
    result2 = solution.isAnagram(s2, t2)
    assert result2 == False, f"Test case 2 failed: Expected False, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
