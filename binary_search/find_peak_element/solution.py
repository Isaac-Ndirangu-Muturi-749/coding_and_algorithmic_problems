class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # The peak is on the left, including mid
                right = mid
            else:
                # The peak is on the right, excluding mid
                left = mid + 1

        # When left == right, we have found a peak
        return left
