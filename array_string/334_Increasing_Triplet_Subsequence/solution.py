class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')  # Smallest number
        second = float('inf')  # Second smallest number

        for num in nums:
            if num <= first:
                first = num  # Update smallest number
            elif num <= second:
                second = num  # Update second smallest number
            else:
                return True  # Found a number greater than both first and second

        return False  # No such triplet exists
