class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost, tank, start_index = 0, 0, 0, 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            # If the tank is negative, reset start index to i + 1
            if tank < 0:
                start_index = i + 1
                tank = 0

        # If total gas is less than total cost, return -1
        if total_gas < total_cost:
            return -1

        return start_index
