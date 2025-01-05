class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10**9 + 7

        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize dp and f arrays
        dp = [0] * (n + 1)
        f = [0] * (n + 1)

        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            f[i - 1] = (f[i - 2] + dp[i - 3]) % MOD
            dp[i] = (dp[i - 1] + dp[i - 2] + 2 * f[i - 1]) % MOD

        return dp[n]
