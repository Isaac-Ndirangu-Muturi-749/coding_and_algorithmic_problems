class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        # Phase 1: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Since the problem guarantees that a majority element always exists,
        # the candidate found after the first pass is the majority element.
        return candidate
