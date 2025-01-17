To solve the problem, we can use **Breadth-First Search (BFS)**, which is ideal for finding the shortest path in an unweighted graph-like structure (here, the maze).

---

### Approach:
1. **Initialization**:
   - Use a queue to store the current position and the steps taken so far.
   - Keep track of visited cells to avoid cycles and redundant exploration.

2. **Exit Conditions**:
   - A cell is considered an exit if it is on the border of the maze (row or column is at the edge) and is not the entrance.

3. **BFS Traversal**:
   - Start from the `entrance` position and explore all valid neighboring cells (up, down, left, right).
   - Stop as soon as an exit is found, returning the number of steps taken to reach it.

4. **Edge Cases**:
   - If there are no exits, return `-1`.
   - Handle small mazes where the entrance is on the border but should not count as an exit.

---

### Implementation:

```python
from collections import deque

def nearestExit(maze, entrance):
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
```

---

### Complexity Analysis:
1. **Time Complexity**: \(O(m \times n)\), where \(m\) is the number of rows and \(n\) is the number of columns.
   - In the worst case, we may visit all cells in the maze.
2. **Space Complexity**: \(O(m \times n)\) for the `visited` set and queue storage.

---

### Example Walkthrough:

#### Example 1:
Input:
```python
maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]
```

Output:
```python
1
```

**Steps**:
1. Start at `(1, 2)` with 0 steps.
2. Explore neighbors:
   - `(1, 1)` and `(0, 2)` are valid.
3. Move to `(0, 2)`, which is an exit. Return `1`.

---

#### Example 2:
Input:
```python
maze = [["+","+","+"],
        [".",".","."],
        ["+","+","+"]]
entrance = [1,0]
```

Output:
```python
2
```

**Steps**:
1. Start at `(1, 0)` with 0 steps.
2. Explore neighbors:
   - `(1, 1)` is valid.
3. Move to `(1, 1)` (1 step), then to `(1, 2)` (2 steps).
4. `(1, 2)` is an exit. Return `2`.

---

This implementation effectively handles the constraints and guarantees an optimal solution using BFS.
