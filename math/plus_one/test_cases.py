from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    digits1 = [1, 2, 3]
    expected1 = [1, 2, 4]
    result1 = solution.plusOne(digits1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    digits2 = [4, 3, 2, 1]
    expected2 = [4, 3, 2, 2]
    result2 = solution.plusOne(digits2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    # Test Case 3
    digits3 = [9]
    expected3 = [1, 0]
    result3 = solution.plusOne(digits3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
