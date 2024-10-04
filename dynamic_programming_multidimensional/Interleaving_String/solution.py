class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the lengths don't match, we can return false right away
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize the DP table
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Base case: empty strings
        dp[0][0] = True

        # Fill the DP table
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                # If current character of s3 matches s1
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                # If current character of s3 matches s2
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        # The final answer is in dp[len(s1)][len(s2)]
        return dp[len(s1)][len(s2)]
