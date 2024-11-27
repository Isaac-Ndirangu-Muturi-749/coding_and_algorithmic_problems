from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    strs1 = ["flower", "flow", "flight"]
    expected_output1 = "fl"
    result1 = solution.longestCommonPrefix(strs1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    strs2 = ["dog", "racecar", "car"]
    expected_output2 = ""
    result2 = solution.longestCommonPrefix(strs2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    strs3 = ["interview", "internet", "internal"]
    expected_output3 = "inte"
    result3 = solution.longestCommonPrefix(strs3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

    # Test case 4
    strs4 = ["apple", "apricot", "ape"]
    expected_output4 = "ap"
    result4 = solution.longestCommonPrefix(strs4)
    assert result4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {result4}"
    print("Test case 4 passed")

    # Test case 5: Empty input
    strs5 = []
    expected_output5 = ""
    result5 = solution.longestCommonPrefix(strs5)
    assert result5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {result5}"
    print("Test case 5 passed")

if __name__ == '__main__':
    run_tests()
