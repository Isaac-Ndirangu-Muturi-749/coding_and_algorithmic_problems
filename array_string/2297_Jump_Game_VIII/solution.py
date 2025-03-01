from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        adjacency_list = defaultdict(list)  # Stores valid jumps from each index
        increasing_stack = []  # Monotonic increasing stack
        decreasing_stack = []  # Monotonic decreasing stack

        # Build the graph for valid jumps based on increasing sequence rule
        for i in range(n - 1, -1, -1):
            # Ensure stack elements are greater than the current element
            while increasing_stack and nums[increasing_stack[-1]] < nums[i]:
                increasing_stack.pop()
            # If stack not empty, make a connection in graph
            if increasing_stack:
                adjacency_list[i].append(increasing_stack[-1])
            increasing_stack.append(i)

        # Build the graph for valid jumps based on decreasing sequence rule
        for i in range(n - 1, -1, -1):
            # Ensure stack elements are greater than or equal to the current element
            while decreasing_stack and nums[decreasing_stack[-1]] >= nums[i]:
                decreasing_stack.pop()
            # If stack not empty, make a connection in graph
            if decreasing_stack:
                adjacency_list[i].append(decreasing_stack[-1])
            decreasing_stack.append(i)

        # Dynamic Programming array to track minimum cost to reach each index
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Starting point has 0 cost

        # Traverse and update costs using DP
        for i in range(n):
            for next_index in adjacency_list[i]:
                min_cost[next_index] = min(min_cost[next_index], min_cost[i] + costs[next_index])

        return min_cost[n - 1]  # Minimum cost to reach last index
