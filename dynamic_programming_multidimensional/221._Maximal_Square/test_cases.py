from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    matrix1 = [["1","0","1","0","0"],
               ["1","0","1","1","1"],
               ["1","1","1","1","1"],
               ["1","0","0","1","0"]]
    expected_output1 = 4  # The largest square has an area of 4 (2x2)
    assert solution.maximalSquare(matrix1) == expected_output1, f"Test case 1 failed. Expected {expected_output1}, got {solution.maximalSquare(matrix1)}"

    # Test case 2
    matrix2 = [["0","1"],
               ["1","0"]]
    expected_output2 = 1  # The largest square has an area of 1 (1x1)
    assert solution.maximalSquare(matrix2) == expected_output2, f"Test case 2 failed. Expected {expected_output2}, got {solution.maximalSquare(matrix2)}"

    # Test case 3
    matrix3 = [["0"]]
    expected_output3 = 0  # No square of '1's exists
    assert solution.maximalSquare(matrix3) == expected_output3, f"Test case 3 failed. Expected {expected_output3}, got {solution.maximalSquare(matrix3)}"

    print("All test cases passed!")


if __name__ == '__main__':
    run_tests()
