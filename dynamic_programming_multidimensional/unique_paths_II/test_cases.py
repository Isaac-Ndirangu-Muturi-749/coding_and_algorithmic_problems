from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    obstacleGrid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    output1 = solution.uniquePathsWithObstacles(obstacleGrid1)
    expected1 = 2
    print(f"Test case 1: {output1} == {expected1}")

    # Test case 2
    obstacleGrid2 = [[0, 1], [0, 0]]
    output2 = solution.uniquePathsWithObstacles(obstacleGrid2)
    expected2 = 1
    print(f"Test case 2: {output2} == {expected2}")

if __name__ == '__main__':
    run_tests()
