from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected1 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    solution.rotate(matrix1)
    assert matrix1 == expected1, f"Test case 1 failed: Expected {expected1}, got {matrix1}"

    # Test case 2
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    expected2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    solution.rotate(matrix2)
    assert matrix2 == expected2, f"Test case 2 failed: Expected {expected2}, got {matrix2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
