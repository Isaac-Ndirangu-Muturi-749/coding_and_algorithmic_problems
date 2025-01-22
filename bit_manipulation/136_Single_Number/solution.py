class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for num in nums:
            result ^= num  # XOR the current number with result
        return result
