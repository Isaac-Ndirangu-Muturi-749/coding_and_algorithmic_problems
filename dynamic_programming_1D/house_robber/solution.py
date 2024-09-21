class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = 0  # This will store dp[i-2]
        prev1 = 0  # This will store dp[i-1]

        for i in range(n):
            current = max(prev1, prev2 + nums[i])  # Calculate dp[i]
            prev2 = prev1  # Update dp[i-2] to dp[i-1] for next iteration
            prev1 = current  # Update dp[i-1] to dp[i] for next iteration

        return prev1
