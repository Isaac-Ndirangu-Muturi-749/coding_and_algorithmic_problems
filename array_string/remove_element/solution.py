class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        k = 0  # Pointer to store the position of the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k  # k is the number of elements not equal to val
