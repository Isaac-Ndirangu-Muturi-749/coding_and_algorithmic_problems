class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
            if not prices:
                return 0

            n = len(prices)

            # If k is large enough, it becomes an unlimited transactions problem
            if k >= n // 2:
                return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

            # DP table: dp[i][j] -> max profit using at most i transactions up to day j
            dp = [[0] * n for _ in range(k+1)]

            # Fill DP table
            for i in range(1, k+1):
                max_prev_profit = -prices[0]  # Best previous buy point
                for j in range(1, n):
                    dp[i][j] = max(dp[i][j-1], prices[j] + max_prev_profit)
                    max_prev_profit = max(max_prev_profit, dp[i-1][j] - prices[j])

            return dp[k][-1]
