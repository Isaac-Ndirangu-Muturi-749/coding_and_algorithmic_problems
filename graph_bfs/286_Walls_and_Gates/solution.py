from collections import deque

def wallsAndGates(rooms):
    if not rooms or not rooms[0]:
        return

    rows, cols = len(rooms), len(rooms[0])
    INF = 2147483647
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Initialize the BFS queue with all gates (cells with value 0)
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    # Perform BFS
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check if the new position is within bounds and unvisited
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1  # Update distance
                queue.append((nr, nc))
