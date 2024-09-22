from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    expected1 = 7
    result1 = solution.minPathSum(grid1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6]]
    expected2 = 12
    result2 = solution.minPathSum(grid2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
