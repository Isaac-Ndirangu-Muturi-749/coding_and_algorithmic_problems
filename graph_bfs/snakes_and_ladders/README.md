To solve the problem of finding the minimum number of moves to reach the last square on a Boustrophedon-style board with snakes and ladders, we can use a Breadth-First Search (BFS) approach. BFS is ideal for this problem because it explores all possible moves level by level, ensuring that we find the shortest path (minimum moves) to reach the target.

### Steps:

1. **Mapping the Board to a 1D Array**:
   - We first convert the 2D board into a 1D array where the index represents the square number. This makes it easier to simulate dice rolls and handle the moves.

2. **BFS Initialization**:
   - Start BFS from the first square. Use a queue to keep track of the current square and the number of moves taken to reach there.
   - Use a set to keep track of visited squares to avoid cycles.

3. **Exploring Moves**:
   - From each square, simulate the dice roll by trying to move to the next 6 possible squares.
   - If a square has a ladder or snake, move directly to its destination.
   - Continue this process until you reach the last square (n^2).

4. **Return the Result**:
   - If you reach the last square, return the number of moves.
   - If the queue is empty and you haven't reached the last square, return -1 (indicating it's not possible).

### Python Implementation:

```python
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

# Example usage:
solution = Solution()

board1 = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]
print(solution.snakesAndLadders(board1))  # Output: 4

board2 = [
    [-1,-1],
    [-1,3]
]
print(solution.snakesAndLadders(board2))  # Output: 1
```

### Explanation:

- **get_position(s)**: This helper function converts a square number into its corresponding row and column on the board. This is crucial because the board is traversed in a Boustrophedon pattern.

- **BFS Traversal**: We simulate moving across the board using BFS. Each possible dice roll (from 1 to 6) is explored, and if the destination square has a ladder or snake, we update the destination accordingly.

- **Visited Set**: The `visited` set prevents revisiting the same square, which would otherwise lead to infinite loops or redundant calculations.

### Complexity:

- **Time Complexity**: `O(n^2)`, where `n` is the length of the board. In the worst case, BFS will visit each square at most once.

- **Space Complexity**: `O(n^2)` due to the space required for the BFS queue and the visited set.

This approach ensures that you find the minimum number of moves required to reach the last square, handling both snakes and ladders efficiently.


Let's break down the `get_position` function. This function converts a square number (`s`) from a one-dimensional board numbering into two-dimensional board coordinates, given a board of size `n x n`.

### Function Breakdown:

```python
def get_position(s):
    """Convert square number to 2D board coordinates."""
    quot, rem = divmod(s - 1, n)
    row = n - 1 - quot
    col = rem if quot % 2 == 0 else n - 1 - rem
    return row, col
```

### Explanation of Steps:

1. **Input**:
   - The function takes a square number `s`, which represents the position in a linear, one-dimensional array.
   - `n` is the size of the `n x n` board (this is likely a global variable or passed into the outer function).

2. **Calculate the row and column**:
   - The goal is to map `s` to a position `(row, col)` on the board.

3. **Step 1: `divmod(s-1, n)`**:
   - `s-1` is used because the square numbers typically start from `1`, but array indexing starts from `0`.
   - `divmod(s-1, n)` returns two values:
     - `quot` (the quotient) is the number of complete rows before the square `s`.
     - `rem` (the remainder) is the position of the square in the current row.

4. **Step 2: `row = n - 1 - quot`**:
   - This calculates the **row** for the square. The reason for this formula is that board numbering often starts from the bottom, so you need to reverse the row indexing.
   - `n - 1` is the last row, and as you move up, `quot` increases, subtracting from `n-1` to give the correct row.

5. **Step 3: `col = rem if quot % 2 == 0 else n - 1 - rem`**:
   - The **column** calculation depends on whether the current row is an even or odd row (based on `quot % 2`):
     - **Even rows (`quot % 2 == 0`)**: The numbering goes left-to-right. So, the column is simply the remainder (`rem`).
     - **Odd rows (`quot % 2 != 0`)**: The numbering goes right-to-left. To reverse the column numbering, we use `n - 1 - rem`.

6. **Return the (row, col)**:
   - The function returns a tuple `(row, col)`, which gives the 2D coordinates on the board.

### Example:

#### For `n = 3` (a 3x3 board):
```
Board layout:
9  8  7
4  5  6
1  2  3
```
- `s = 5`:
  - `s-1 = 4`, so `quot, rem = divmod(4, 3) = (1, 1)`.
  - `row = 3 - 1 - 1 = 1` (2nd row from the bottom).
  - Since `quot % 2 != 0` (it's an odd row), `col = 3 - 1 - 1 = 1`.
  - Thus, the position `(row, col)` is `(1, 1)`.




Let's walk through the example with `s = 3` using the function `get_position` on a 3x3 board (`n = 3`).

### Board Layout:
```
9  8  7
4  5  6
1  2  3
```
The goal is to convert the square number `s = 3` into its corresponding 2D coordinates `(row, col)` on this board.

### Applying `get_position(3)`:

```python
def get_position(s):
    quot, rem = divmod(s - 1, n)
    row = n - 1 - quot
    col = rem if quot % 2 == 0 else n - 1 - rem
    return row, col
```

### Step-by-step:

1. **Input**: `s = 3`, and we have `n = 3`.

2. **Step 1: `divmod(s - 1, n)`**:
   - First, calculate `s - 1 = 3 - 1 = 2`.
   - Now, `divmod(2, 3)` gives:
     - `quot = 0` (the quotient: how many complete rows come before).
     - `rem = 2` (the remainder: the position within the current row).

3. **Step 2: `row = n - 1 - quot`**:
   - `n - 1 = 3 - 1 = 2` (the index of the last row).
   - Now, `row = 2 - 0 = 2` (meaning the 3rd row from the top, or the bottom row).

4. **Step 3: `col = rem if quot % 2 == 0 else n - 1 - rem`**:
   - Since `quot = 0` is even (`quot % 2 == 0`), we use `col = rem`.
   - Thus, `col = 2`.

5. **Result**:
   - The position `(row, col)` is `(2, 2)`.

### Conclusion:
For `s = 3`, the 2D board coordinates are `(2, 2)`, which is the bottom-right corner of the board, corresponding to the value `3` in the layout.
