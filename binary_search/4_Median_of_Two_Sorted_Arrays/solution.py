class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2  # Partition index in nums1
            j = (m + n + 1) // 2 - i  # Partition index in nums2
            
            # Handle edge cases (out-of-bounds)
            Left1 = float('-inf') if i == 0 else nums1[i - 1]
            Right1 = float('inf') if i == m else nums1[i]
            Left2 = float('-inf') if j == 0 else nums2[j - 1]
            Right2 = float('inf') if j == n else nums2[j]
            
            # Found correct partition
            if Left1 <= Right2 and Left2 <= Right1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(Left1, Left2)
                # If total length is even
                return (max(Left1, Left2) + min(Right1, Right2)) / 2
            
            # Adjust binary search range
            elif Left1 > Right2:
                right = i - 1  # Move left
            else:
                left = i + 1  # Move right

