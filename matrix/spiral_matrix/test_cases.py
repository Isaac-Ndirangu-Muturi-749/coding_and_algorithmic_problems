from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.spiralOrder(matrix1) == [1, 2, 3, 6, 9, 8, 7, 4, 5], "Test case 1 failed"

    # Test case 2: 3x4 matrix
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert solution.spiralOrder(matrix2) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "Test case 2 failed"

    # Test case 3: Single row matrix
    matrix3 = [
        [1, 2, 3, 4, 5]
    ]
    assert solution.spiralOrder(matrix3) == [1, 2, 3, 4, 5], "Test case 3 failed"

    # Test case 4: Single column matrix
    matrix4 = [
        [1],
        [2],
        [3],
        [4]
    ]
    assert solution.spiralOrder(matrix4) == [1, 2, 3, 4], "Test case 4 failed"

    # Test case 5: 2x2 matrix
    matrix5 = [
        [1, 2],
        [3, 4]
    ]
    assert solution.spiralOrder(matrix5) == [1, 2, 4, 3], "Test case 5 failed"

    # Test case 6: Empty matrix
    matrix6 = []
    assert solution.spiralOrder(matrix6) == [], "Test case 6 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
