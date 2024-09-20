class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Out of bounds or not 'O', stop recursion
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            # Mark the current 'O' as 'T' (temporarily marking it as safe)
            board[r][c] = 'T'

            # Explore all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Step 1: Traverse the boundary of the board and mark all connected 'O's as 'T'
        for i in range(rows):
            for j in [0, cols - 1]:  # only first and last column
                if board[i][j] == 'O':
                    dfs(i, j)

        for j in range(cols):
            for i in [0, rows - 1]:  # only first and last row
                if board[i][j] == 'O':
                    dfs(i, j)

        # Step 2: Go through the board and flip 'O' to 'X', and 'T' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Capture surrounded regions
                elif board[i][j] == 'T':
                    board[i][j] = 'O'  # Revert non-surrounded regions

