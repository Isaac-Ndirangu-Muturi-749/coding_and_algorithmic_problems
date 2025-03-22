class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_position = max_position = 0  # Initialize positions of min and max elements

        # Find positions of smallest and largest elements
        for index, value in enumerate(nums):
            if value < nums[min_position] or (value == nums[min_position] and index < min_position):
                min_position = index
            if value > nums[max_position] or (value == nums[max_position] and index > max_position):
                max_position = index

        swaps = min_position + (len(nums) - 1 - max_position)

        if min_position > max_position:
            swaps -= 1  # Avoid double counting when max is left of min

        return swaps
