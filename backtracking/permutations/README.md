To solve the problem of finding all permutations of an array of distinct integers, we can use **backtracking**. This method explores all possible permutations by generating them step by step and then backtracking once all elements for a specific permutation have been used.

### Approach:
1. **Backtracking**:
   - We can build each permutation by choosing an element from the list, then recursively choosing the next element from the remaining unused elements.
   - When a permutation of the required length is formed (i.e., it contains all elements of the input array), we add it to the result.

2. **Base Case**:
   - When the permutation contains all elements, we store it in our results list.

3. **Recursive Exploration**:
   - At each step, we try adding an element from the remaining elements to our current permutation, and we mark it as used.

### Code Implementation:

```python
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
```

### Explanation:

1. **Backtracking Function** (`backtrack`):
   - The function `backtrack` takes two arguments:
     - `path`: the current permutation being formed.
     - `used`: a boolean list indicating whether each number has been used in the current permutation.
   - If the `path` contains all elements of `nums`, it is a valid permutation, and we append a copy of it to `result`.
   - Otherwise, we try adding each unused element of `nums` to `path`, mark it as used, and recursively explore further possibilities. After exploring, we backtrack by removing the element and marking it as unused again.

2. **Initial Call**:
   - We start by calling `backtrack` with an empty path and a `used` array initialized to `False` for all elements.

3. **Base Case**:
   - When the length of `path` equals the length of `nums`, we have formed a complete permutation.

### Example Walkthrough:

For `nums = [1, 2, 3]`:
- Start with an empty `path = []` and `used = [False, False, False]`.
- Try adding `1` to `path` -> `path = [1]`, `used = [True, False, False]`.
  - Try adding `2` to `path` -> `path = [1, 2]`, `used = [True, True, False]`.
    - Try adding `3` to `path` -> `path = [1, 2, 3]`, `used = [True, True, True]`.
      - We have a valid permutation, add `[1, 2, 3]` to `result`.
    - Backtrack by removing `3` -> `path = [1, 2]`, `used = [True, True, False]`.
  - Try adding `3` to `path` -> `path = [1, 3]`, `used = [True, False, True]`.
    - Continue similarly until all permutations are generated.

### Time Complexity:

- **Time Complexity**: The time complexity is O(n! * n), where n is the length of the input array `nums`. This is because there are `n!` permutations, and for each permutation, we are copying the path (which takes O(n)).

- **Space Complexity**: The space complexity is O(n! * n) due to the space needed to store all the permutations in the result list, and also due to the recursion stack and the temporary storage for each path.

### Example Outputs:

```python
sol = Solution()

# Example 1:
print(sol.permute([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Example 2:
print(sol.permute([0, 1]))
# Output: [[0, 1], [1, 0]]

# Example 3:
print(sol.permute([1]))
# Output: [[1]]
```

This approach effectively generates all possible permutations using backtracking.
