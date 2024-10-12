class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Directions for moving in the grid (right, left, down, up)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS function to explore the grid
        def dfs(r, c, idx, visited):
            # If we've matched all characters of the word
            if idx == len(word):
                return True

            # If we're out of bounds, characters don't match, or the cell is visited
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or board[r][c] != word[idx] or (r, c) in visited):
                return False

            # Mark the current cell as visited
            visited.add((r, c))

            # Explore all four directions
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if dfs(new_r, new_c, idx + 1, visited):
                    return True

            # Backtrack by removing the current cell from visited
            visited.remove((r, c))

            return False

        # Try starting DFS from each cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Start DFS only if the first letter matches
                    visited = set()  # Set to keep track of visited cells
                    if dfs(i, j, 0, visited):
                        return True

        return False
