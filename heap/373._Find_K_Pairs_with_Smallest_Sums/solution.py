import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        # Min-heap
        min_heap = []
        # Start by adding the pair (nums1[0], nums2[0]) and others with nums1[0] and every element of nums2
        for j in range(min(len(nums2), k)):  # Only push k elements for optimization
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        result = []

        # Process the heap to get the smallest sums
        while min_heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # If there is a next element in nums1, add the pair (nums1[i+1], nums2[j])
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i + 1, j))

        return result
