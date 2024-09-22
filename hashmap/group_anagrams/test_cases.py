from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    result1 = solution.groupAnagrams(strs1)
    assert sorted([sorted(group) for group in result1]) == sorted([sorted(group) for group in expected1]), f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    strs2 = [""]
    expected2 = [[""]]
    result2 = solution.groupAnagrams(strs2)
    assert sorted([sorted(group) for group in result2]) == sorted([sorted(group) for group in expected2]), f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test Case 3
    strs3 = ["a"]
    expected3 = [["a"]]
    result3 = solution.groupAnagrams(strs3)
    assert sorted([sorted(group) for group in result3]) == sorted([sorted(group) for group in expected3]), f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
