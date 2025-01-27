import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # Pair capital and profit, then sort by capital
        projects = sorted(zip(capital, profits), key=lambda x: x[0])

        # Min-heap for capital and max-heap for profits
        min_heap = []
        max_heap = []

        # Index to keep track of projects in the sorted list
        i = 0
        n = len(projects)

        for _ in range(k):
            # Add all projects that can be started to the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Push profit as negative for max-heap
                i += 1

            # If no projects can be started, break
            if not max_heap:
                break

            # Pick the most profitable project
            w += -heapq.heappop(max_heap)  # Pop the max profit (negated)

        return w
