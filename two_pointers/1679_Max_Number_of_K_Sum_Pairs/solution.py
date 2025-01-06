class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        count_map = {}
        operations = 0

        for num in nums:
            complement = k - num
            if count_map.get(complement, 0) > 0:
                # Pair found, use one instance of complement
                operations += 1
                count_map[complement] -= 1
            else:
                # Store num for future pairing
                count_map[num] = count_map.get(num, 0) + 1

        return operations
