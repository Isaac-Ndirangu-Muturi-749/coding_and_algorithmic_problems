class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Increment zero_count if we encounter a 0
            if nums[right] == 0:
                zero_count += 1

            # If there are more than one 0, shrink the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum length (subtract 1 because we must delete one element)
            max_length = max(max_length, right - left)

        return max_length
