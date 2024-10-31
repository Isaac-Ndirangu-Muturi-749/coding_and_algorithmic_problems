class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # Helper function to calculate maximum subarray sum (Kadane's algorithm)
        def kadane_max(arr):
            max_current = max_global = arr[0]
            for num in arr[1:]:
                max_current = max(num, max_current + num)
                max_global = max(max_global, max_current)
            return max_global

        # Helper function to calculate minimum subarray sum
        def kadane_min(arr):
            min_current = min_global = arr[0]
            for num in arr[1:]:
                min_current = min(num, min_current + num)
                min_global = min(min_global, min_current)
            return min_global

        # Total sum of array
        total_sum = sum(nums)

        # Calculate max subarray sum without circular wrapping
        max_kadane = kadane_max(nums)

        # Calculate min subarray sum for the circular case
        min_kadane = kadane_min(nums)

        # Calculate the circular max sum
        if max_kadane < 0:
            # All elements are negative, return the max single element
            return max_kadane
        else:
            return max(max_kadane, total_sum - min_kadane)
