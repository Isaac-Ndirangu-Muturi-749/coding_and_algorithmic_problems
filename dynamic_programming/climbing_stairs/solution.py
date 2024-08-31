class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the first two steps
        first = 1
        second = 2

        # Build the solution iteratively for each step from 3 to n
        for i in range(3, n + 1):
            third = first + second  # The current number of ways to reach the i-th step
            first = second  # Update first to second for the next iteration
            second = third  # Update second to third for the next iteration

        return second
