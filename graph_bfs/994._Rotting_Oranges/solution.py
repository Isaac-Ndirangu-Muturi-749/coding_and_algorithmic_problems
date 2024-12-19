


from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0
        if fresh_count == 0:
            return 0

        # Directions for 4-adjacent neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0

        # Perform BFS
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If adjacent cell is a fresh orange, rot it
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1

            # Increment minutes after processing all current rotten oranges
            if queue:
                minutes += 1

        # If there are still fresh oranges left, return -1
        return minutes if fresh_count == 0 else -1
