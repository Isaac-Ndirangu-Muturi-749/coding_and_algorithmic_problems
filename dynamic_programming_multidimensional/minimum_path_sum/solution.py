class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Get the number of rows and columns
        m, n = len(grid), len(grid[0])

        # Create a dp array with the same dimensions as grid
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left corner
        dp[0][0] = grid[0][0]

        # Fill the first row (only can come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the first column (only can come from the top)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # The answer is in the bottom-right corner of the dp array
        return dp[m-1][n-1]
