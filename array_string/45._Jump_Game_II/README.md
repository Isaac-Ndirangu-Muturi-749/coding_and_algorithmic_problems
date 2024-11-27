To solve the problem of finding the minimum number of jumps to reach the last index of the array `nums`, we can use a **greedy approach**.

### Approach:

1. **Greedy Strategy**:
   - The idea is to always make the farthest jump possible at each step, while tracking the current range of indices that can be reached with the available jumps.
   - We'll iterate through the array and keep updating the farthest index we can reach. At each step, we also check if we've reached the end of the current jump range. If we have, we make a jump and continue.

2. **Steps**:
   - Track the farthest point we can reach with the current jump.
   - Each time we exceed the current range (i.e., when `i > current_end`), increment the jump count and update the range to the new farthest point.
   - Repeat this process until we reach the last index of the array.

### Code Implementation:

```python
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
```

### Explanation:
- **Initialization**:
  - `jumps`: Counts the number of jumps made.
  - `current_end`: Keeps track of the farthest index we can reach with the current jump.
  - `farthest`: The farthest index that can be reached at any given point during the iteration.

- **Main Logic**:
  - As we iterate over each index `i`, we update the `farthest` point we can reach by calculating `i + nums[i]`.
  - Whenever we reach the end of the current jump's range (`i == current_end`), we increment the `jumps` count and update the `current_end` to the `farthest` value we've seen so far.
  - If the `current_end` reaches or exceeds the last index (`n-1`), we can stop, as we've found the minimum number of jumps to get to the end.

### Time Complexity:
- **O(n)**: We are iterating through the array once.

### Space Complexity:
- **O(1)**: Only constant space is used for variables `jumps`, `current_end`, and `farthest`.

### Example Walkthrough:

#### Example 1:
- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `2`
  - Step 1: At index `0`, we can jump up to `2` indices (i.e., `nums[0] = 2`). The farthest point we can reach is `2`, so we jump to index `1`.
  - Step 2: At index `1`, we can jump up to `3` indices (`nums[1] = 3`), allowing us to reach the last index. So, we make another jump from index `1` to index `4`.

#### Example 2:
- Input: `nums = [2, 3, 0, 1, 4]`
- Output: `2`
  - Step 1: At index `0`, we can jump up to `2` indices (i.e., `nums[0] = 2`). The farthest point we can reach is `2`, so we jump to index `1`.
  - Step 2: At index `1`, we can jump up to `3` indices, allowing us to reach the last index. So, we make another jump from index `1` to index `4`.

This solution efficiently finds the minimum number of jumps to reach the last index with a greedy approach that runs in linear time.
