class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        water = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    water += maxRight - height[right]
                right -= 1

        return water
