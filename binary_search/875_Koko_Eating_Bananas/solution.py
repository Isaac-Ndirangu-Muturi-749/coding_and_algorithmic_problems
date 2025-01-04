class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Helper function to check if Koko can finish with speed k
        def canFinish(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k  # Equivalent to ceil(pile / k)
            return total_hours <= h

        # Binary search for the minimum k
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid  # Try smaller speeds
            else:
                left = mid + 1  # Increase speed
        return left
