class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0
        left, right = 1, x  # Start the search range from 1 to x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # If we find the exact square root, return it
            elif mid * mid < x:
                left = mid + 1  # Search the right half
            else:
                right = mid - 1  # Search the left half

        return right  # right is the largest integer such that right^2 <= x
