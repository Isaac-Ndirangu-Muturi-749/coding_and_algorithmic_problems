from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    expected_output1 = 0
    result1 = solution.strStr(haystack1, needle1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    expected_output2 = -1
    result2 = solution.strStr(haystack2, needle2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3: needle is an empty string
    haystack3 = "hello"
    needle3 = ""
    expected_output3 = 0  # According to the problem definition, if needle is an empty string, we return 0.
    result3 = solution.strStr(haystack3, needle3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

    # Test case 4: needle is at the end of haystack
    haystack4 = "hello"
    needle4 = "lo"
    expected_output4 = 3
    result4 = solution.strStr(haystack4, needle4)
    assert result4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {result4}"
    print("Test case 4 passed")

    # Test case 5: needle does not appear in haystack
    haystack5 = "hello"
    needle5 = "world"
    expected_output5 = -1
    result5 = solution.strStr(haystack5, needle5)
    assert result5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {result5}"
    print("Test case 5 passed")

if __name__ == '__main__':
    run_tests()
