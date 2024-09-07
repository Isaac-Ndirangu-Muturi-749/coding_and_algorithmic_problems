from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    result = solution.combine(4, 2)
    expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert result == expected, f"Test case 1 failed: {result}"

    # Test case 2
    result = solution.combine(1, 1)
    expected = [[1]]
    assert result == expected, f"Test case 2 failed: {result}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
