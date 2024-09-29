To solve this problem, we can use **dynamic programming**. We need to calculate the number of unique paths the robot can take to move from the top-left corner to the bottom-right corner, while avoiding obstacles.

### Approach:

1. **Grid Initialization**:
   - We are given an `m x n` grid (`obstacleGrid`) where each cell either contains a `0` (space) or `1` (obstacle). The robot can only move down or right, and it can't move through an obstacle.

2. **Dynamic Programming Table**:
   - We will use a DP table (`dp`) to store the number of ways to reach each cell in the grid. The value `dp[i][j]` represents the number of ways to reach cell `(i, j)` from the top-left corner.

3. **Base Case**:
   - If the starting point `grid[0][0]` is an obstacle (`grid[0][0] == 1`), the robot can't move, so the number of paths is `0`.
   - Set `dp[0][0] = 1` if there's no obstacle at the starting point.

4. **Filling the DP Table**:
   - For each cell `(i, j)` in the grid:
     - If there's an obstacle at `(i, j)`, set `dp[i][j] = 0`.
     - Otherwise, compute `dp[i][j]` as the sum of the number of ways to reach the cell from the top (`dp[i-1][j]`, if valid) and from the left (`dp[i][j-1]`, if valid).

5. **Result**:
   - The value at `dp[m-1][n-1]` will be the number of unique paths to reach the bottom-right corner, considering all obstacles.

### Dynamic Programming Formula:

- `dp[i][j] = dp[i-1][j] + dp[i][j-1]` if `obstacleGrid[i][j] == 0`.
- If there is an obstacle at `i, j`, set `dp[i][j] = 0`.

### Code Implementation:

```python
def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # If the starting point or the ending point is blocked, return 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0

    # Initialize the dp array with 0s
    dp = [[0] * n for _ in range(m)]

    # Start point
    dp[0][0] = 1

    # Fill the dp array
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0  # No path through obstacles
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]  # Paths from above
                if j > 0:
                    dp[i][j] += dp[i][j-1]  # Paths from the left

    # Return the number of ways to reach the bottom-right corner
    return dp[m-1][n-1]
```

### Explanation:

1. **Initialization**:
   - We initialize a `dp` table of the same size as the input `obstacleGrid` with zeros.
   - We set `dp[0][0] = 1` if there is no obstacle at the starting position, meaning there's one way to be at the start (just standing there).

2. **Filling the DP Table**:
   - For each cell `(i, j)`, if there's no obstacle, we check how many ways we can come from the top (`dp[i-1][j]`) or from the left (`dp[i][j-1]`).
   - If the cell has an obstacle (`obstacleGrid[i][j] == 1`), we set `dp[i][j] = 0` because no path can go through this cell.

3. **Result**:
   - Finally, the value at `dp[m-1][n-1]` will give us the number of unique paths to reach the bottom-right corner.

### Time Complexity:
- **Time Complexity**: `O(m * n)` where `m` is the number of rows and `n` is the number of columns. We process each cell once.

### Space Complexity:
- **Space Complexity**: `O(m * n)` since we are using a DP table of size `m x n`.

### Example Walkthrough:

#### Example 1:
Input: `obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]`
- Initialize `dp` table:
  ```
  [[1, 0, 0],
   [0, 0, 0],
   [0, 0, 0]]
  ```
- After filling `dp`:
  ```
  [[1, 1, 1],
   [1, 0, 1],
   [1, 1, 2]]
  ```
- Output: `2`

#### Example 2:
Input: `obstacleGrid = [[0,1],[0,0]]`
- Initialize `dp` table:
  ```
  [[1, 0],
   [0, 0]]
  ```
- After filling `dp`:
  ```
  [[1, 0],
   [1, 1]]
  ```
- Output: `1`

This dynamic programming solution efficiently computes the number of unique paths while avoiding obstacles.
