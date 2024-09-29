class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the target is at the mid position
            if nums[mid] == target:
                return mid

            # Determine which part of the array is sorted
            if nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left part
                else:
                    left = mid + 1  # Target is in the right part
            else:
                # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the right part
                else:
                    right = mid - 1  # Target is in the left part

        # Target was not found
        return -1
