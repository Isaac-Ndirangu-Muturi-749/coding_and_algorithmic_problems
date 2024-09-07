To solve the problem of counting the number of islands in a 2D binary grid, we can use a Depth-First Search (DFS) approach. The idea is to traverse the grid and each time we find a '1' (which represents land), we perform a DFS to mark all connected land pieces (horizontally and vertically) as visited by changing them to '0'. Each DFS call represents finding an island, so we increment our island count.

### Steps:

1. **Iterate Over the Grid**:
   - Traverse through each cell in the grid.
   - When a '1' is found, it indicates the start of a new island. We then initiate a DFS to mark all connected '1's to '0'.
   - After marking, increment the island count.

2. **DFS Function**:
   - For a given cell, mark it as visited by setting it to '0'.
   - Recursively apply the DFS for all adjacent cells (up, down, left, right) that are still '1'.

3. **Edge Cases**:
   - Ensure that the DFS doesn’t go out of the grid boundaries.
   - The function should handle grids of varying sizes, including small grids.

### Python Implementation:

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            # Boundary check
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return

            # Mark the current cell as visited
            grid[i][j] = '0'

            # Apply DFS in all 4 directions
            dfs(i+1, j)  # Down
            dfs(i-1, j)  # Up
            dfs(i, j+1)  # Right
            dfs(i, j-1)  # Left

        num_islands = 0

        # Iterate through the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an island
                    dfs(i, j)  # Mark the entire island as visited
                    num_islands += 1  # Increase the count of islands

        return num_islands

# Example usage
solution = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))  # Output: 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid2))  # Output: 3
```

### Explanation:

- **DFS Functionality**: The `dfs` function is crucial. It checks the boundaries and the cell's value. If it’s a '1', it marks the cell as '0' to signify that it has been visited. Then, it calls itself recursively on the adjacent cells (up, down, left, right).

- **Count Islands**: We maintain a counter `num_islands` that increments each time we find a new island (i.e., a new '1' that hasn't been visited yet).

### Complexity Analysis:

- **Time Complexity**: `O(m * n)`, where `m` is the number of rows and `n` is the number of columns in the grid. In the worst case, each cell is visited once.

- **Space Complexity**: `O(m * n)` in the worst case due to the recursive stack space used by the DFS calls.

This solution efficiently counts the number of islands in a grid using DFS and ensures that all connected lands are marked as visited to avoid counting them multiple times.
