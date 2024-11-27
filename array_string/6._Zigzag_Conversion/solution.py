class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Special case: if numRows is 1, return the original string
        if numRows == 1:
            return s

        # Create a list to store the rows
        rows = [''] * min(numRows, len(s))

        # Variables to track the current row and direction
        cur_row = 0
        going_down = False

        # Traverse through each character in the string
        for char in s:
            # Add the current character to the current row
            rows[cur_row] += char

            # If we are at the top or bottom, change direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            cur_row += 1 if going_down else -1

        # Concatenate all rows and return the result
        return ''.join(rows)
