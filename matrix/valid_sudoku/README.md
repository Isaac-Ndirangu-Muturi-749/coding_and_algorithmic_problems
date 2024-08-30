To determine if a given 9x9 Sudoku board is valid, we need to ensure that:

1. Each row contains the digits 1-9 without repetition.
2. Each column contains the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes contains the digits 1-9 without repetition.

### Approach:

We can approach this problem by using three sets:
- One set for rows to track the digits that have already been seen in each row.
- One set for columns to track the digits that have already been seen in each column.
- One set for 3x3 sub-boxes to track the digits that have already been seen in each box.

For each digit on the board:
1. Calculate which row, column, and 3x3 sub-box it belongs to.
2. Check if the digit has already been seen in the corresponding row, column, or sub-box. If it has, the board is invalid.
3. If it hasn’t been seen, add it to the appropriate sets.

If the entire board is processed without finding any duplicates, the board is valid.

### Implementation:

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create 9 empty sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):  # Loop through each row
            for j in range(9):  # Loop through each column
                num = board[i][j]
                if num == '.':
                    continue  # Skip empty cells

                # Calculate the index for the 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)

                # Check if the number is already in the respective row, column, or box
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[box_index]:
                    return False

                # Add the number to the respective row, column, and box sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True  # If no conflicts, the board is valid

# Example usage:
solution = Solution()
board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(board1))  # Output: True
print(solution.isValidSudoku(board2))  # Output: False
```

### Explanation:
- **Board 1** is valid: No digit repeats in any row, column, or 3x3 sub-box.
- **Board 2** is invalid: The digit '8' repeats in the top-left 3x3 sub-box.

The solution efficiently checks each digit by using sets to track seen digits, ensuring that the board is valid according to Sudoku rules. The overall time complexity is O(1) because the board size is fixed at 9x9, so the operations are constant in scale.
