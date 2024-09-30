class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    # leftBias = [True/False], if false, res is rightBiased
    def binSearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        i = -1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m  # Found the target
                if leftBias:
                    r = m - 1  # Search in the left half
                else:
                    l = m + 1  # Search in the right half

        return i

