To solve the problem of finding if a word exists in a given grid (`board`), we can use **backtracking**. The idea is to traverse the grid, starting from each cell, and check if we can find the word by moving to adjacent cells (horizontally or vertically) while respecting the constraints that each cell can only be used once.

### Approach:

1. **DFS (Depth-First Search)**: We will perform DFS starting from each cell in the grid. For each cell, we'll check if the current character matches the first character of the word. If it matches, we explore the neighboring cells (up, down, left, right) to find the next character of the word. We repeat this until either the entire word is found, or the search fails for that starting position.

2. **Backtracking**: Since each cell can only be used once in a particular path, we'll need to mark cells as visited. After exploring each path, we'll unmark the cell to allow for other potential paths in subsequent searches.

3. **Pruning**: To optimize, we stop searching as soon as we realize the current path can't lead to a solution (i.e., the characters don't match, or we've gone out of bounds).

### Algorithm:

1. Traverse every cell in the grid as a starting point.
2. For each cell, initiate a DFS to explore possible paths.
3. Mark the current cell as visited during the DFS.
4. For each recursive DFS call, explore the neighboring cells in the four possible directions.
5. If the word is found, return `True`.
6. If no path from a particular starting point leads to the word, backtrack and try other cells.

### Code Implementation:

```python
def exist(board, word):
    # Define dimensions of the board
    rows, cols = len(board), len(board[0])

    # Directions for moving in the grid (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # DFS function to explore the grid
    def dfs(r, c, idx):
        # If we've matched all characters of the word
        if idx == len(word):
            return True

        # If we're out of bounds or characters don't match
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False

        # Mark the current cell as visited by temporarily altering its value
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all four directions
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if dfs(new_r, new_c, idx + 1):
                return True

        # Restore the current cell's value (backtrack)
        board[r][c] = temp

        return False

    # Try starting DFS from each cell
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:  # Optimization: Start DFS only if the first letter matches
                if dfs(i, j, 0):
                    return True

    return False

# Example usage
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
print(exist(board1, word1))  # Output: True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(exist(board2, word2))  # Output: True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(exist(board3, word3))  # Output: False
```

### Explanation:

- **DFS function**:
  - We use DFS to explore the grid starting from any cell that matches the first character of the word.
  - During the DFS, we move in the four possible directions: right, left, down, and up.
  - If at any point the characters don't match or we go out of bounds, the search backtracks.

- **Backtracking**:
  - After each move, we mark the current cell as visited by changing its value (temporarily marking it as `#`). Once we've finished exploring from that cell, we backtrack by restoring its original value.

- **Base case**:
  - If we have successfully matched all characters (i.e., `idx == len(word)`), we return `True`.
  - If the current path doesn't match, we backtrack and explore other possible paths.

### Complexity Analysis:

- **Time Complexity**:
  - In the worst case, we might explore every cell in the grid for every character in the word, leading to a time complexity of `O(m * n * 4^L)`, where `m` and `n` are the dimensions of the grid, and `L` is the length of the word. The `4^L` comes from the fact that in each DFS step, we have four possible directions to explore.

- **Space Complexity**:
  - The space complexity is `O(L)` due to the recursion stack depth, where `L` is the length of the word.

This solution should work efficiently within the problem's constraints.



Using a set can help improve the efficiency of marking visited cells in the grid for backtracking. Instead of modifying the board directly (by changing the character of a cell temporarily), we can maintain a set to track which cells have been visited. This keeps the grid intact and avoids extra operations of restoring the values after backtracking. Here’s how you can implement the solution with a set.

### Updated Approach:

1. Use a set to keep track of visited cells during the DFS traversal. Each cell's coordinates `(row, col)` will be added to the set when we visit it, and removed after exploring all possible paths from that cell.
2. We’ll use the set to check whether a cell is already visited or not, rather than modifying the board directly.

### Code Implementation with a Set:

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    # Directions for moving in the grid (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # DFS function to explore the grid
    def dfs(r, c, idx, visited):
        # If we've matched all characters of the word
        if idx == len(word):
            return True

        # If we're out of bounds, characters don't match, or the cell is visited
        if (r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[idx] or (r, c) in visited):
            return False

        # Mark the current cell as visited
        visited.add((r, c))

        # Explore all four directions
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if dfs(new_r, new_c, idx + 1, visited):
                return True

        # Backtrack by removing the current cell from visited
        visited.remove((r, c))

        return False

    # Try starting DFS from each cell
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:  # Start DFS only if the first letter matches
                visited = set()  # Set to keep track of visited cells
                if dfs(i, j, 0, visited):
                    return True

    return False

# Example usage
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
print(exist(board1, word1))  # Output: True

board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
print(exist(board2, word2))  # Output: True

board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"
print(exist(board3, word3))  # Output: False
```

### Explanation:

- **Visited set**:
  - We use a set called `visited` to track the cells we have visited during a particular DFS path.
  - Before visiting a cell, we check if it's in the `visited` set. If it is, we skip that cell to prevent cycles.
  - After finishing exploring from a cell, we remove it from the `visited` set, effectively backtracking.

- **Backtracking**:
  - The DFS will explore all four directions (right, left, down, up) from each cell.
  - If the current path doesn't lead to a solution, the DFS backtracks, i.e., it removes the cell from the `visited` set and explores other directions.

### Complexity Analysis:

- **Time Complexity**:
  - In the worst case, the DFS might visit each cell for each character of the word, leading to a time complexity of `O(m * n * 4^L)`, where `m` and `n` are the dimensions of the grid, and `L` is the length of the word.
  - The `4^L` comes from the fact that in each DFS step, we have four possible directions to explore.

- **Space Complexity**:
  - The space complexity is `O(L)` due to the recursion stack and the size of the `visited` set, where `L` is the length of the word.

### Conclusion:

Using a set to track visited cells is an alternative way to handle backtracking efficiently. It avoids modifying the board directly and keeps the implementation clean. This method should work within the given problem's constraints.
