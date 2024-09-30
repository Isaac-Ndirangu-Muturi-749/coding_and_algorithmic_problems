class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # Initialize DP table
        dp = [[False] * n for _ in range(n)]

        start, max_len = 0, 1  # Start index and length of the longest palindrome found

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for two-character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):  # Length of the substring
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        # Return the longest palindrome substring
        return s[start:start + max_len]
