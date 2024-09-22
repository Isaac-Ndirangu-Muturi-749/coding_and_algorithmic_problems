To solve this problem, we can use **dynamic programming** to find the minimum sum path in the grid. The idea is to keep track of the minimum sum needed to reach each cell, building up from the top-left to the bottom-right corner.

### Approach:
1. We will create a 2D `dp` array where `dp[i][j]` represents the minimum path sum to reach the cell `(i, j)` from `(0, 0)`.
2. The value in the first cell `dp[0][0]` is simply `grid[0][0]` since that's the starting point.
3. For the first row, the only way to move is from left to right, so we compute the sum cumulatively.
4. For the first column, the only way to move is from top to bottom, so we also compute the sum cumulatively.
5. For all other cells, the value in `dp[i][j]` will be the value of the current cell in `grid[i][j]` plus the minimum of either coming from the cell above (`dp[i-1][j]`) or the cell to the left (`dp[i][j-1]`).
6. Finally, the value in `dp[m-1][n-1]` will give the minimum sum required to reach the bottom-right corner.

### Code Implementation:

```python
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        # Get the number of rows and columns
        m, n = len(grid), len(grid[0])

        # Create a dp array with the same dimensions as grid
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left corner
        dp[0][0] = grid[0][0]

        # Fill the first row (only can come from the left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the first column (only can come from the top)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # The answer is in the bottom-right corner of the dp array
        return dp[m-1][n-1]
```

### Explanation:
1. **Initialization**: We start by initializing the `dp` array. The top-left corner `dp[0][0]` is initialized with the value of `grid[0][0]`.

2. **First Row**: For the first row, the only way to reach any cell is by moving right. Hence, `dp[0][j] = dp[0][j-1] + grid[0][j]`.

3. **First Column**: For the first column, the only way to reach any cell is by moving down. Hence, `dp[i][0] = dp[i-1][0] + grid[i][0]`.

4. **Rest of the Grid**: For each cell `(i, j)` from row 1 and column 1 onward, we take the minimum path sum from either the top cell (`dp[i-1][j]`) or the left cell (`dp[i][j-1]`) and add the value of `grid[i][j]` to it.

5. **Return Result**: Finally, the value in `dp[m-1][n-1]` contains the minimum sum to reach the bottom-right corner from the top-left corner.

### Example Walkthrough:

#### Example 1:
- **Input**: `grid = [[1,3,1],[1,5,1],[4,2,1]]`
- **dp Array**:

```
[
 [1, 4, 5],
 [2, 7, 6],
 [6, 8, 7]
]
```

- **Output**: `7`
  - The path is `1 → 3 → 1 → 1 → 1`, which sums to 7.

#### Example 2:
- **Input**: `grid = [[1,2,3],[4,5,6]]`
- **dp Array**:

```
[
 [1, 3, 6],
 [5, 8, 12]
]
```

- **Output**: `12`
  - The path is `1 → 2 → 3 → 6`, which sums to 12.

### Time and Space Complexity:

- **Time Complexity**: O(m * n), where `m` is the number of rows and `n` is the number of columns. We process each cell once.
- **Space Complexity**: O(m * n), since we are using a `dp` array of the same size as the grid.

Alternatively, the space complexity can be optimized to O(n) by reusing a single row (or column) for dynamic programming, but this solution uses the simpler O(m * n) space version.
