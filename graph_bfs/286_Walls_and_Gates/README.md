This problem can be efficiently solved using **Breadth-First Search (BFS)**. Starting from all gates (cells with value `0`), perform a multi-source BFS to update distances in the grid.

---

### **Approach**
1. **Multi-Source BFS**:
   - Start from all gates (`0`) and push their coordinates into a queue.
   - Perform a BFS to explore adjacent cells.
   - For each cell, update its value as the distance from the nearest gate.
   - Stop updating a cell if it already has a smaller distance.

2. **Edge Cases**:
   - If the grid contains only walls (`-1`), the result should remain unchanged.
   - If there are no gates, all `INF` cells remain as they are.

3. **Time Complexity**:
   - BFS visits each cell at most once: \(O(m \times n)\).
   - Overall complexity: \(O(m \times n)\).

4. **Space Complexity**:
   - Queue storage for BFS: \(O(m \times n)\).

---

### **Implementation**

```python
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
```

---

### **Examples**

#### Example 1:
**Input**:
```python
rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]
wallsAndGates(rooms)
print(rooms)
```

**Output**:
```python
[
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
```

#### Example 2:
**Input**:
```python
rooms = [[-1]]
wallsAndGates(rooms)
print(rooms)
```

**Output**:
```python
[[-1]]
```

#### Example 3:
**Input**:
```python
rooms = [[2147483647]]
wallsAndGates(rooms)
print(rooms)
```

**Output**:
```python
[[2147483647]]
```

---

### **Explanation**

1. **Initialize BFS**:
   - All gates (`0`) are pushed into the queue.
   - Start BFS from these gates.

2. **Update Distances**:
   - For each cell, propagate the distance to its neighbors if they are empty (`INF`).

3. **Output**:
   - The grid is updated in place with the shortest distances to the nearest gate.

This approach ensures optimal performance for the given constraints.
