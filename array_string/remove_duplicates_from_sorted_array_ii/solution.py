class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2  # Start from the third element position

        # Iterate over the array from the third element onwards
        for i in range(2, len(nums)):
            # If the current element is different from the element two steps back, keep it
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1

        return write
