class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than the right element, the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Else, the minimum is in the left half (or it could be mid itself)
            else:
                right = mid

        # After the loop, left == right and it points to the minimum element
        return nums[left]
