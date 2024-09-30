class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        def count_live_neighbors(r, c):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):  # Check for live cells
                    live_neighbors += 1
            return live_neighbors

        # First pass: update the board in-place with the transition states (2 and 3)
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)

                if board[i][j] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Live to dead
                elif board[i][j] == 0:  # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 3  # Dead to live

        # Second pass: finalize the board by converting 2->0 and 3->1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
