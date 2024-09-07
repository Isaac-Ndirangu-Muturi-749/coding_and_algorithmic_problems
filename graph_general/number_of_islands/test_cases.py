from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.numIslands(grid1) == 1, "Test case 1 failed"

    # Test case 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution.numIslands(grid2) == 3, "Test case 2 failed"

    print("All test cases passed!")

# Example usage
if __name__ == '__main__':
    run_tests()
