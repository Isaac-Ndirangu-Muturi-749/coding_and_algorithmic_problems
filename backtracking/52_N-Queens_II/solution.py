class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diags, antiDiags):
            if row == n:  # All queens placed successfully
                return 1
            
            count = 0
            for col in range(n):
                diag = row - col + n - 1  # Shifted main diagonal
                antiDiag = row + col  # Anti-diagonal

                # Check if column, main diagonal, or anti-diagonal is occupied
                if (cols & (1 << col)) or (diags & (1 << diag)) or (antiDiags & (1 << antiDiag)):
                    continue  # Skip invalid placements
                
                # Place the queen (mark the bit)
                count += backtrack(row + 1, cols | (1 << col), diags | (1 << diag), antiDiags | (1 << antiDiag))

            return count

        return backtrack(0, 0, 0, 0)
