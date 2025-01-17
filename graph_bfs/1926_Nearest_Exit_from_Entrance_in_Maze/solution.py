class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add((entrance[0], entrance[1]))

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            row, col, steps = queue.popleft()

            # Check if this cell is an exit (not the entrance and on the border)
            if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and [row, col] != entrance:
                return steps

            # Explore neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is valid and not visited
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))

        # If no exit is found
        return -1
