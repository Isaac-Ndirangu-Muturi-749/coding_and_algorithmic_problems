class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the current sum and maximum sum to the first element
        current_sum = max_sum = nums[0]

        # Traverse the rest of the array
        for num in nums[1:]:
            # Update current_sum
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum
