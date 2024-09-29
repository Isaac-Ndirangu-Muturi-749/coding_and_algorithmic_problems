class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary to store the index of each number
        num_to_index = {}

        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num

            # If the complement is already in the dictionary, return the indices
            if complement in num_to_index:
                return [num_to_index[complement], i]

            # Otherwise, store the current number and its index in the dictionary
            num_to_index[num] = i
