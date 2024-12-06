class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Expand the window
            if nums[right] == 0:
                zeros_count += 1

            # Shrink the window if zeros_count exceeds k
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length
