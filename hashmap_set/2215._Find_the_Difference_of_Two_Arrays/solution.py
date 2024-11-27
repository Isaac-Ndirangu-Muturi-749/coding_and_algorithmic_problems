class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        # Convert nums1 and nums2 to sets to remove duplicates and enable set operations
        set1 = set(nums1)
        set2 = set(nums2)

        # Find elements in set1 not in set2 and vice versa
        diff1 = list(set1 - set2)
        diff2 = list(set2 - set1)

        # Return the result as a list of two lists
        return [diff1, diff2]
