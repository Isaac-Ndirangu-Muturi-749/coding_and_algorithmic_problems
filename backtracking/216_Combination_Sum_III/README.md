This problem can be solved using **backtracking**. The idea is to explore all possible combinations of numbers from 1 to 9, keeping track of the current sum and the number of elements in the combination. Here's the solution:

---

### Approach:
1. **Backtracking**:
   - Use a helper function to recursively build the combinations.
   - Start with the smallest number and explore numbers incrementally to avoid duplicates.
   - Track the current combination and its sum.
   - If the size of the combination reaches \( k \) and the sum is \( n \), add it to the result.
   - If the size exceeds \( k \) or the sum exceeds \( n \), backtrack.

2. **Constraints**:
   - Only numbers 1 to 9 can be used.
   - Each number can be used at most once.
   - The combination must have exactly \( k \) numbers, and their sum must equal \( n \).

---

### Implementation (Python):

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, target):
            # If we have found a valid combination
            if len(path) == k and target == 0:
                result.append(path[:])
                return
            # If the combination is invalid
            if len(path) > k or target < 0:
                return

            # Explore numbers from 'start' to 9
            for i in range(start, 10):
                path.append(i)  # Choose the number
                backtrack(i + 1, path, target - i)  # Explore further
                path.pop()  # Backtrack

        backtrack(1, [], n)
        return result
```

---

### Explanation of the Code:
1. **Base Case**:
   - If the current combination has \( k \) numbers and the target sum is 0, add it to the result.
   - If the combination is invalid (too many numbers or the sum is negative), return.

2. **Recursive Case**:
   - Iterate through numbers from `start` to 9.
   - Add the current number to the combination and reduce the target sum by the current number.
   - Recursively explore the next number.
   - Remove the last number (backtrack) to try other combinations.

3. **Optimization**:
   - Start the loop from the current number to avoid duplicate combinations.

---

### Examples:

#### Example 1:
```python
Input: k = 3, n = 7
Solution().combinationSum3(3, 7)
Output: [[1, 2, 4]]
```

#### Example 2:
```python
Input: k = 3, n = 9
Solution().combinationSum3(3, 9)
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
```

#### Example 3:
```python
Input: k = 4, n = 1
Solution().combinationSum3(4, 1)
Output: []
```

---

### Complexity Analysis:
1. **Time Complexity**:
   - The number of possible combinations is bounded by \( 2^9 \) (since each number from 1 to 9 can either be included or excluded).
   - However, the backtracking efficiently prunes invalid paths, so the actual complexity is much lower.

2. **Space Complexity**:
   - \( O(k) \): The maximum depth of the recursion is \( k \), as we only include up to \( k \) numbers in a combination.

---

### Output for the Examples:
```python
Solution().combinationSum3(3, 7)  # Output: [[1, 2, 4]]
Solution().combinationSum3(3, 9)  # Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Solution().combinationSum3(4, 1)  # Output: []
```
