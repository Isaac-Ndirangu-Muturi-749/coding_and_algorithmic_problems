To solve the problem, we need to simulate the process of rotting oranges in a breadth-first search (BFS) fashion. Here's how we approach it:

---

### **Approach**
1. **Initialization**:
   - Use a queue to keep track of rotten oranges (`2`) and their positions in the grid.
   - Count the number of fresh oranges (`1`) initially.

2. **Breadth-First Search (BFS)**:
   - For each minute, process all the rotten oranges currently in the queue.
   - Check their 4-directionally adjacent cells. If a cell contains a fresh orange, mark it as rotten and add it to the queue.
   - Decrease the count of fresh oranges as we rot them.

3. **End Condition**:
   - If there are no fresh oranges left, return the total minutes elapsed.
   - If the queue is empty and there are still fresh oranges, return `-1`.

4. **Special Case**:
   - If there are no fresh oranges at the start, return `0`.

---

### **Algorithm**
1. Initialize a queue with the positions of all rotten oranges.
2. Count the total number of fresh oranges.
3. Use BFS to propagate the rotting process:
   - For each rotten orange in the queue, rot its adjacent fresh oranges and add them to the queue.
   - Increment a minute counter after processing all oranges at the current level.
4. After BFS, if there are fresh oranges left, return `-1`. Otherwise, return the total minutes elapsed.

---

### **Code Implementation**
```python
from collections import deque

def orangesRotting(grid):
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
```

---

### **Complexity Analysis**
1. **Time Complexity**: \(O(m \times n)\)
   - We visit each cell at most once.
2. **Space Complexity**: \(O(m \times n)\)
   - The queue can store all cells in the worst case.

---

### **Example Walkthrough**

#### Example 1:
**Input**:
```python
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
```
**Execution**:
1. Initial queue: `[(0, 0)]` (rotten orange at (0, 0)), `fresh_count = 6`.
2. Minute 1: Rot adjacent oranges: `queue = [(0, 1), (1, 0)]`, `fresh_count = 4`.
3. Minute 2: Rot adjacent oranges: `queue = [(0, 2), (1, 1)]`, `fresh_count = 2`.
4. Minute 3: Rot adjacent oranges: `queue = [(2, 1)]`, `fresh_count = 1`.
5. Minute 4: Rot adjacent oranges: `queue = [(2, 2)]`, `fresh_count = 0`.

**Output**: `4`.

---

#### Example 2:
**Input**:
```python
grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]
```
**Execution**:
1. Initial queue: `[(0, 0)]` (rotten orange at (0, 0)), `fresh_count = 5`.
2. Perform BFS. At the end, `fresh_count > 0`.

**Output**: `-1`.

---

This algorithm is efficient and works within the problem's constraints.
