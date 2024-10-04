from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    s1_1 = "aabcc"
    s2_1 = "dbbca"
    s3_1 = "aadbbcbcac"
    expected_output1 = True
    result1 = solution.isInterleave(s1_1, s2_1, s3_1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    s1_2 = "aabcc"
    s2_2 = "dbbca"
    s3_2 = "aadbbbaccc"
    expected_output2 = False
    result2 = solution.isInterleave(s1_2, s2_2, s3_2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3
    s1_3 = ""
    s2_3 = ""
    s3_3 = ""
    expected_output3 = True
    result3 = solution.isInterleave(s1_3, s2_3, s3_3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

if __name__ == '__main__':
    run_tests()
