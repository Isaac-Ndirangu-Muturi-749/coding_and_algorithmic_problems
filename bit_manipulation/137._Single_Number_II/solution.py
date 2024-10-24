class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Initialize two variables to keep track of bits.
        ones, twos = 0, 0

        for num in nums:
            # 'ones' will hold the bits which have appeared exactly 1 time (mod 3)
            ones = (ones ^ num) & ~twos

            # 'twos' will hold the bits which have appeared exactly 2 times (mod 3)
            twos = (twos ^ num) & ~ones

        # After processing all numbers, 'ones' will have the unique number
        return ones
