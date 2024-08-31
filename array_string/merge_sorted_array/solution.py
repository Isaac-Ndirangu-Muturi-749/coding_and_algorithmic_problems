class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize the pointers for nums1, nums2, and the merged array.
        i = m - 1  # Pointer for the last element in nums1 that should be considered
        j = n - 1  # Pointer for the last element in nums2
        k = m + n - 1  # Pointer for the last position in nums1

        # Merge the arrays from the end to the beginning.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, add them.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

