class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Initialize the DP array with a large value (amount + 1)
        dp = [amount + 1] * (amount + 1)

        # Base case: no coins are needed to make amount 0
        dp[0] = 0

        # Loop over each coin and update the DP array
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        # If dp[amount] is still greater than amount, return -1
        return dp[amount] if dp[amount] != amount + 1 else -1
