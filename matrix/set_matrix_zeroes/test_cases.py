from solution import Solution

def run_tests():
    solution = Solution()

    # Test Case 1
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    expected1 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    solution.setZeroes(matrix1)
    assert matrix1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {matrix1}"

    # Test Case 2
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    expected2 = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    solution.setZeroes(matrix2)
    assert matrix2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {matrix2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
