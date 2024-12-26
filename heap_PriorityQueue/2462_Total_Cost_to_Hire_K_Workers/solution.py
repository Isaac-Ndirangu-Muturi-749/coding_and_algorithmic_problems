import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n = len(costs)
        left, right = 0, n - 1
        left_heap, right_heap = [], []
        total_cost = 0

        # Add initial candidates to the heaps
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        # Hire k workers
        for _ in range(k):
            # Compare the top of both heaps and choose the smaller cost
            if left_heap and (not right_heap or left_heap[0][0] <= right_heap[0][0]):
                cost, index = heapq.heappop(left_heap)
                total_cost += cost

                # Add next worker from the left side to the heap if possible
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            elif right_heap:
                cost, index = heapq.heappop(right_heap)
                total_cost += cost

                # Add next worker from the right side to the heap if possible
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total_cost

