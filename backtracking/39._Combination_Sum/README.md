To solve this problem, we can use **backtracking** to explore all possible combinations of candidates that sum up to the target. The idea is to recursively build combinations by picking candidates and reducing the target until it either reaches zero (a valid combination is found) or becomes negative (invalid combination).

### Approach:

1. **Sort the Candidates**: Sorting the candidates helps in managing the recursive calls efficiently. It allows us to avoid unnecessary computations by stopping early when the target becomes negative.

2. **Backtracking**: For each candidate, we try to include it in the current combination and call the function recursively with the updated target (target reduced by the value of the candidate). We can use a candidate multiple times, so we don't need to move to the next candidate after including the current one.

3. **Stopping Condition**:
   - If the target becomes 0, we have found a valid combination, so we add it to the result.
   - If the target becomes negative, we stop exploring that path because it can't lead to a valid combination.

4. **Avoid Duplicates**: To ensure the uniqueness of combinations, we only move to the next candidate when we choose not to include the current one.

### Solution:

```python
def combinationSum(candidates, target):
    def backtrack(start, target, path):
        # If target becomes 0, we found a valid combination
        if target == 0:
            result.append(list(path))
            return

        # If target becomes negative, stop further exploration
        if target < 0:
            return

        # Explore all candidates starting from 'start' to avoid duplicates
        for i in range(start, len(candidates)):
            # Include the candidate and move forward
            path.append(candidates[i])
            # Continue the recursion with reduced target and same 'i' (allow repeats)
            backtrack(i, target - candidates[i], path)
            # Backtrack to explore other possibilities
            path.pop()

    candidates.sort()  # Optional, but helps with pruning
    result = []
    backtrack(0, target, [])
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]
```

### Explanation:

1. **Backtracking Function**:
   - `start`: The index from which we start considering candidates to avoid duplicates.
   - `target`: The remaining sum we need to match.
   - `path`: The current combination being explored.

2. **Recursive Call**:
   - We explore each candidate starting from `start` to avoid revisiting earlier candidates, and we include the candidate multiple times by calling `backtrack(i, ...)` (i.e., keeping the same index).

3. **Base Cases**:
   - When `target == 0`, we found a valid combination and add it to the result.
   - When `target < 0`, we stop exploring further as we overshot the target.

4. **Backtracking**:
   - After exploring a candidate, we "backtrack" by removing it from the path (`path.pop()`) and explore the next candidate.

### Example Walkthrough:

#### Input:
```python
candidates = [2, 3, 6, 7]
target = 7
```

#### Output:
```python
[[2, 2, 3], [7]]
```

- We start with an empty path and a target of 7.
- We first include 2 and reduce the target to 5. We include 2 again (target becomes 3), and then 2 again (target becomes 1), which is not valid. So, we backtrack and try 3 next.
- This leads to a valid combination `[2, 2, 3]`.
- After that, we explore the candidate 7 directly, which results in the combination `[7]`.

### Time Complexity:

- The time complexity is difficult to express exactly due to the recursive nature of the solution and the pruning. However, in the worst case, the algorithm generates all possible combinations of numbers that sum to the target. This gives a time complexity of approximately O(2^n), where `n` is the number of candidates.

### Space Complexity:

- The space complexity is O(target) due to the depth of the recursive call stack and the space used by the current path.

This solution efficiently finds all unique combinations that sum up to the target using backtracking.
