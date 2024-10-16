class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        # Get matrix dimensions
        m, n = len(matrix), len(matrix[0])

        # DP table initialization
        dp = [[0] * n for _ in range(m)]
        max_side = 0  # Track the largest side of the square

        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:  # First row or first column
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        # The area of the largest square is side^2
        return max_side * max_side
