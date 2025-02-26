from heapq import heappop, heappush
from collections import deque

class Solution:
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        n = len(nums)
        min_cost = [float('inf')] * n  # Store min cost to reach each index
        min_cost[0] = 0  # Cost to reach index 0 is 0
        pq = [(0, 0)]  # (current cost, index)

        # Maintain two monotonic stacks to find valid jumps efficiently
        increasing_stack = deque()  # Monotonic increasing
        decreasing_stack = deque()  # Monotonic decreasing

        while pq:
            current_cost, i = heappop(pq)

            if i == n - 1:
                return current_cost  # Found the minimum cost to reach the last index

            # Process increasing valid jumps
            while increasing_stack and nums[increasing_stack[-1]] < nums[i]:
                j = increasing_stack.pop()
                new_cost = current_cost + costs[j]
                if new_cost < min_cost[j]:
                    min_cost[j] = new_cost
                    heappush(pq, (new_cost, j))

            increasing_stack.append(i)

            # Process decreasing valid jumps
            while decreasing_stack and nums[decreasing_stack[-1]] >= nums[i]:
                j = decreasing_stack.pop()
                new_cost = current_cost + costs[j]
                if new_cost < min_cost[j]:
                    min_cost[j] = new_cost
                    heappush(pq, (new_cost, j))

            decreasing_stack.append(i)

        return -1  # Should never reach here if there's always a valid path
