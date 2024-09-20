class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Result list to store all the permutations
        result = []

        # Backtracking helper function
        def backtrack(path, used):
            # If the path contains all numbers, we've found a valid permutation
            if len(path) == len(nums):
                result.append(path[:])  # Make a copy of the current path
                return

            # Try to add each unused number to the current permutation
            for i in range(len(nums)):
                if not used[i]:
                    # Mark the number as used
                    used[i] = True
                    # Add the number to the current path
                    path.append(nums[i])
                    # Recurse to build the permutation further
                    backtrack(path, used)
                    # Backtrack: undo the choice (remove the last number and mark it as unused)
                    path.pop()
                    used[i] = False

        # Call the backtracking function with an empty path and all numbers unused
        backtrack([], [False] * len(nums))

        return result
