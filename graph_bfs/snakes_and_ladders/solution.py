from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(s):
            """Convert square number to 2D board coordinates."""
            quot, rem = divmod(s-1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        queue = deque([(1, 0)])  # (square, move count)
        visited = set([1])

        while queue:
            square, moves = queue.popleft()

            # Try all possible dice rolls
            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square == n * n:
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1
