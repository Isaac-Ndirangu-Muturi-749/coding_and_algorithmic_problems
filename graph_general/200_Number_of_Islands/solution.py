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
