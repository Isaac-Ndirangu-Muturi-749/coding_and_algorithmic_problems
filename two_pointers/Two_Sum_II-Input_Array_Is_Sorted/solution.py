class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # return 1-based indices
            elif current_sum < target:
                left += 1  # move the left pointer to the right
            else:
                right -= 1  # move the right pointer to the left