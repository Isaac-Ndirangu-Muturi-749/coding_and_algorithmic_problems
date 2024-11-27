from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    citations1 = [3, 0, 6, 1, 5]
    expected_output1 = 3
    result1 = solution.hIndex(citations1)
    assert result1 == expected_output1, f"Test case 1 failed: Expected {expected_output1}, got {result1}"
    print("Test case 1 passed")

    # Test case 2
    citations2 = [1, 3, 1]
    expected_output2 = 1
    result2 = solution.hIndex(citations2)
    assert result2 == expected_output2, f"Test case 2 failed: Expected {expected_output2}, got {result2}"
    print("Test case 2 passed")

    # Test case 3: All citations are higher than paper count
    citations3 = [10, 8, 5, 4, 3]
    expected_output3 = 4
    result3 = solution.hIndex(citations3)
    assert result3 == expected_output3, f"Test case 3 failed: Expected {expected_output3}, got {result3}"
    print("Test case 3 passed")

    # Test case 4: All citations are zero
    citations4 = [0, 0, 0, 0, 0]
    expected_output4 = 0
    result4 = solution.hIndex(citations4)
    assert result4 == expected_output4, f"Test case 4 failed: Expected {expected_output4}, got {result4}"
    print("Test case 4 passed")

    # Test case 5: Single paper with zero citation
    citations5 = [0]
    expected_output5 = 0
    result5 = solution.hIndex(citations5)
    assert result5 == expected_output5, f"Test case 5 failed: Expected {expected_output5}, got {result5}"
    print("Test case 5 passed")

    # Test case 6: Single paper with many citations
    citations6 = [100]
    expected_output6 = 1
    result6 = solution.hIndex(citations6)
    assert result6 == expected_output6, f"Test case 6 failed: Expected {expected_output6}, got {result6}"
    print("Test case 6 passed")

if __name__ == '__main__':
    run_tests()
