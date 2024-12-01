import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # Pair elements and sort by nums2 in descending order
        pairs = sorted(zip(nums2, nums1), reverse=True)

        min_heap = []  # Min-heap for the largest k values in nums1
        max_score = 0
        current_sum = 0

        for num2, num1 in pairs:
            # Add nums1 value to the heap and current sum
            heapq.heappush(min_heap, num1)
            current_sum += num1

            # If heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            # If we have exactly k elements, calculate the score
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
