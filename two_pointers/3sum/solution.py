class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums) - 2):  # Step 2: Iterate over the array
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach to find the two numbers that sum to -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:  # We found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum

        return res
