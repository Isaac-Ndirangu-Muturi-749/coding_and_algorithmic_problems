class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array
        ans = [0] * (n + 1)

        # Compute the number of 1's for each number
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Use the recurrence relation

        return ans
