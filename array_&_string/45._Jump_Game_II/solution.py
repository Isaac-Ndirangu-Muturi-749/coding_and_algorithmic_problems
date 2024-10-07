class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # If the list has only one element, no jump is needed
        if n == 1:
            return 0

        # Initialize variables
        jumps = 0  # Number of jumps taken
        current_end = 0  # The end of the current range of indices we can jump to
        farthest = 0  # The farthest point we can reach

        # Loop through the array, but not to the last element (we want to stop before reaching n-1)
        for i in range(n - 1):
            # Update the farthest point we can reach
            farthest = max(farthest, i + nums[i])

            # If we reach the end of the current jump range, we must jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # If we've reached or passed the last index, break
                if current_end >= n - 1:
                    break

        return jumps
