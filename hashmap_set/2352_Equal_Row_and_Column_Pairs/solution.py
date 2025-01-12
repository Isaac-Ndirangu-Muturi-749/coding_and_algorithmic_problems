class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Create a dictionary to store the frequency of rows
        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1

        # Count matching rows and columns
        result = 0
        for col in zip(*grid):  # Treat columns as tuples
            col_tuple = tuple(col)
            if col_tuple in row_count:
                result += row_count[col_tuple]

        return result
