To solve the problem of finding the minimum path sum from top to bottom in a triangle array, you can use a **dynamic programming** approach. The idea is to start from the bottom of the triangle and work your way up to the top, updating each element with the minimum path sum to reach that element.

### Approach:

1. **Initialize**:
   - Start with the bottom row of the triangle since each element in the bottom row is the minimum path sum for itself (no further path).

2. **Dynamic Programming Update**:
   - Move upwards from the second-last row to the top row.
   - For each element in a row, update its value to be the sum of itself and the minimum of the two adjacent elements directly below it. This ensures that each element will store the minimum path sum to reach the bottom from that position.

3. **Result**:
   - After processing all rows, the top element of the triangle will contain the minimum path sum from top to bottom.

### Complexity:
- **Time Complexity**: \(O(n^2)\), where \(n\) is the number of rows in the triangle. This is because we process each element in the triangle once.
- **Space Complexity**: \(O(1)\) if you use the triangle itself for updates, or \(O(n)\) if you use a separate list to store the intermediate results.

### Code Implementation:

Here's how you can implement this approach in Python:

```python
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start from the second-last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current cell with the minimum path sum from the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        # The top element now contains the minimum path sum
        return triangle[0][0]

# Example usage:
solution = Solution()

# Example 1
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(solution.minimumTotal(triangle1))  # Output: 11

# Example 2
triangle2 = [[-10]]
print(solution.minimumTotal(triangle2))  # Output: -10
```

### Explanation:

1. **Initialization**:
   - We start by iterating from the second-last row to the top of the triangle.

2. **Update Rule**:
   - For each element at position `(row, col)`, update its value to be the sum of itself and the minimum of the two adjacent values in the row directly below (`triangle[row + 1][col]` and `triangle[row + 1][col + 1]`).

3. **Final Result**:
   - After processing all rows, the top element `triangle[0][0]` will contain the minimum path sum.

This approach efficiently computes the minimum path sum with optimal time and space complexity.

To achieve the solution using only **O(n)** extra space, where \( n \) is the number of rows in the triangle, we need to avoid using the entire triangle for storage or modifications. Instead, we can maintain a single **1D list** (or array) that holds the minimum path sum for each element in the current row. This list is updated iteratively as we move up the triangle.

### Approach:

1. **Initialize**:
   - Use a 1D list `dp` of size \( n \), where \( n \) is the number of rows. Initially, set `dp` to the values of the bottom row of the triangle because the minimum path sum for the elements in the bottom row is the element itself.

2. **Dynamic Programming Update**:
   - Start from the second-to-last row and move upwards. For each element, update the corresponding entry in `dp` by taking the minimum of the two adjacent elements from the previous row and adding it to the current element.

3. **Result**:
   - After processing all rows, the first element of `dp` will contain the minimum path sum.

### Code Implementation:

Here's how you can implement this approach in Python:

```python
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Initialize dp with the last row of the triangle
        dp = triangle[-1]

        # Start from the second-last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the dp array in place to store the minimum path sum
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # The first element of dp contains the minimum path sum
        return dp[0]

# Example usage:
solution = Solution()

# Example 1
triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(solution.minimumTotal(triangle1))  # Output: 11

# Example 2
triangle2 = [[-10]]
print(solution.minimumTotal(triangle2))  # Output: -10
```

### Explanation:

1. **Initialization**:
   - We initialize the `dp` array with the values from the last row of the triangle. These are the minimum path sums for the elements in the last row because there are no rows below them.

2. **Dynamic Programming Update**:
   - For each element in the current row, update the corresponding element in `dp` by adding the value of the current element from the triangle and the minimum of the two adjacent elements in `dp` (which represents the row below).

3. **Final Result**:
   - After processing all rows, `dp[0]` will contain the minimum path sum from the top to the bottom of the triangle.

### Time and Space Complexity:

- **Time Complexity**: \( O(n^2) \), where \( n \) is the number of rows. We visit each element in the triangle exactly once.

- **Space Complexity**: \( O(n) \), where \( n \) is the number of rows, because we only maintain a 1D list `dp` with size equal to the number of elements in the bottom row.

This approach reduces the space complexity to **O(n)** while maintaining the optimal time complexity.

This line of code:

```python
for row in range(len(triangle) - 2, -1, -1):
```

is part of a **bottom-up** dynamic programming approach that is often used when working with a triangle (2D array) problem, such as **minimum path sum** in a triangle.

Here’s a breakdown of the statement:

1. **`len(triangle)`**:
   - This gets the number of rows in the `triangle`. If the `triangle` has 4 rows, `len(triangle)` would return `4`.

2. **`len(triangle) - 2`**:
   - This starts the loop from the second-last row in the triangle. For example, if `len(triangle)` is 4 (i.e., 4 rows), then `len(triangle) - 2` equals `2`, which corresponds to the second-last row (since the rows are indexed from 0 to 3).

3. **`-1`**:
   - This is the stop condition of the loop, meaning that the loop continues until it reaches row `0`. In Python's `range()` function, the loop runs until the stop value is **not included**. So, the loop will stop when it reaches `-1` and won't include `-1`.

4. **`-1` (third argument)**:
   - This is the step value for the loop, indicating that the loop should iterate **backward**. A step of `-1` makes the loop move from the second-last row down to the first row.

### What this loop does:

- The loop starts from the second-last row of the triangle (i.e., `len(triangle) - 2`) and goes up to the first row (`0`), moving in reverse order (`-1` step).

### Example:

If the `triangle` is:

```
[
  [2],
  [3, 4],
  [6, 5, 7],
  [4, 1, 8, 3]
]
```

- `len(triangle)` is `4`, so the loop will start from `2` (the second-last row) and go to `0` (the first row).
- The iteration order of `row` will be: `2`, `1`, `0`.

This allows processing each row starting from the second-last row, which is common in problems where the bottom-up approach is used to calculate values by reducing the triangle’s size as you move upwards.


