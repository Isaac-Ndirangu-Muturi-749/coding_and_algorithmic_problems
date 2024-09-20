from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1: Insert [2,5] into [[1,3],[6,9]]
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    result1 = solution.insert(intervals1, newInterval1)
    expected1 = [[1, 5], [6, 9]]
    assert result1 == expected1, f"Test case 1 failed: Expected {expected1}, got {result1}"

    # Test case 2: Insert [4,8] into [[1,2],[3,5],[6,7],[8,10],[12,16]]
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    result2 = solution.insert(intervals2, newInterval2)
    expected2 = [[1, 2], [3, 10], [12, 16]]
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
