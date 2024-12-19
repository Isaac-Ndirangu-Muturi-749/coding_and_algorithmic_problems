class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table initialized with 0
        dp = [[0] * n for _ in range(m)]

        # Fill the first row and first column with 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Return the value at the bottom-right corner
        return dp[m-1][n-1]
