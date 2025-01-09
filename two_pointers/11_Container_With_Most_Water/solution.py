class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = current_height * width

            # Update the maximum area found
            max_area = max(max_area, current_area)

            # Move the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
