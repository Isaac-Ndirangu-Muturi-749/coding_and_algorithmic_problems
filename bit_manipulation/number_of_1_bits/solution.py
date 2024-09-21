class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Check if the least significant bit is 1
            count += n & 1
            # Right shift by 1 to check the next bit
            n >>= 1
        return count
