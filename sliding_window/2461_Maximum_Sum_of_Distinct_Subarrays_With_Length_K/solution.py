class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        window_sum = 0
        max_sum = 0
        window_set = set()
        left = 0

        for right in range(len(nums)):
            # If we see a duplicate, move the left pointer to maintain distinct elements
            while nums[right] in window_set:
                window_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1

            # Add the current element to the window
            window_set.add(nums[right])
            window_sum += nums[right]

            # If the window length equals k, check the sum
            if (right - left + 1) == k:
                max_sum = max(max_sum, window_sum)
                # Move left pointer to slide the window
                window_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1

        return max_sum
