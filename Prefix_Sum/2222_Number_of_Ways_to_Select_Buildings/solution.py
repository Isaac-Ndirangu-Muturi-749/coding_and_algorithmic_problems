class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)

        # Precompute counts
        count_0_before = [0] * n
        count_1_before = [0] * n
        count_0_after = [0] * n
        count_1_after = [0] * n

        # Calculate count before
        for i in range(1, n):
            count_0_before[i] = count_0_before[i-1] + (s[i-1] == '0')
            count_1_before[i] = count_1_before[i-1] + (s[i-1] == '1')

        # Calculate count after
        for i in range(n-2, -1, -1):
            count_0_after[i] = count_0_after[i+1] + (s[i+1] == '0')
            count_1_after[i] = count_1_after[i+1] + (s[i+1] == '1')

        # Calculate total ways
        total_ways = 0

        for i in range(n):
            if s[i] == '1':  # Count "010" pattern
                total_ways += count_0_before[i] * count_0_after[i]
            if s[i] == '0':  # Count "101" pattern
                total_ways += count_1_before[i] * count_1_after[i]

        return total_ways
