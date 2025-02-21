from collections import defaultdict
from typing import List

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort to process elements in increasing order
        remainder_groups = defaultdict(list)

        # Group elements by their remainder when divided by k
        for num in nums:
            remainder_groups[num % k].append(num)

        total_subsets = 1  # Start with the empty subset

        # Process each remainder group independently
        for group in remainder_groups.values():
            group_size = len(group)
            dp = [0] * (group_size + 1)
            dp[0] = 1  # Base case: Empty subset
            dp[1] = 2  # Base case: Either take the first element or don't

            # Dynamic programming to count valid k-Free subsets
            for i in range(2, group_size + 1):
                if group[i - 1] - group[i - 2] == k:
                    dp[i] = dp[i - 1] + dp[i - 2]  # Exclude adjacent elements with difference k
                else:
                    dp[i] = dp[i - 1] * 2  # Each element can be included or excluded independently

            total_subsets *= dp[group_size]  # Multiply results for independent groups

        return total_subsets
