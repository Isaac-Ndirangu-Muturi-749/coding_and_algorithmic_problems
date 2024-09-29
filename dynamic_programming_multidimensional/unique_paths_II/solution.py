class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If the starting point or the ending point is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        # Initialize the dp array with 0s
        dp = [[0] * n for _ in range(m)]

        # Start point
        dp[0][0] = 1

        # Fill the dp array
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # No path through obstacles
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]  # Paths from above
                    if j > 0:
                        dp[i][j] += dp[i][j-1]  # Paths from the left

        # Return the number of ways to reach the bottom-right corner
        return dp[m-1][n-1]
