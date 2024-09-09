from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target1 = 3
    result1 = solution.searchMatrix(matrix1, target1)
    assert result1 == True, f"Test case 1 failed: Expected True but got {result1}"

    # Test case 2
    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    result2 = solution.searchMatrix(matrix2, target2)
    assert result2 == False, f"Test case 2 failed: Expected False but got {result2}"

    # Test case 3: Edge case with empty matrix
    matrix3 = []
    target3 = 1
    result3 = solution.searchMatrix(matrix3, target3)
    assert result3 == False, f"Test case 3 failed: Expected False but got {result3}"

    # Test case 4: Edge case with single element matrix (element present)
    matrix4 = [[5]]
    target4 = 5
    result4 = solution.searchMatrix(matrix4, target4)
    assert result4 == True, f"Test case 4 failed: Expected True but got {result4}"

    # Test case 5: Edge case with single element matrix (element not present)
    matrix5 = [[10]]
    target5 = 5
    result5 = solution.searchMatrix(matrix5, target5)
    assert result5 == False, f"Test case 5 failed: Expected False but got {result5}"

    # Test case 6: Target is greater than all elements
    matrix6 = [[1,2,3],[4,5,6],[7,8,9]]
    target6 = 10
    result6 = solution.searchMatrix(matrix6, target6)
    assert result6 == False, f"Test case 6 failed: Expected False but got {result6}"

    # Test case 7: Target is less than all elements
    matrix7 = [[1,2,3],[4,5,6],[7,8,9]]
    target7 = 0
    result7 = solution.searchMatrix(matrix7, target7)
    assert result7 == False, f"Test case 7 failed: Expected False but got {result7}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
