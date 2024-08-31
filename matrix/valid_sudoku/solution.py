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
