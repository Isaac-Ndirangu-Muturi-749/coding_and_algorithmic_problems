the totalNQueens function while maintaining the logic.

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()  # Tracks occupied columns
        posDiag = set()  # Tracks occupied positive diagonals (r + c)
        negDiag = set()  # Tracks occupied negative diagonals (r - c)

        res = 0  # Stores the count of valid solutions

        def backtrack(r):
            nonlocal res  # Allow modification of `res`
            if r == n:  # All queens placed successfully
                res += 1
                return
            
            for c in range(n):
                # Check if the column or diagonals are occupied
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue  # Skip invalid placements
                
                # Place the queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                # Move to the next row
                backtrack(r + 1)
                
                # Remove the queen (Backtracking)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)  # Start from the first row
        return res  # Return the total count of valid solutions


---

Explanation of Fixes

1. Fixed indentation issues and improper spacing.


2. Added nonlocal res inside backtrack() so that res is modified correctly.


3. Replaced Continue with continue (Python is case-sensitive).


4. Ensured the backtracking order is correct (add elements → recurse → remove elements).


5. Improved readability with comments.




---

Time Complexity Analysis

The worst case is O(N!) since we try all possible queen placements.

The space complexity is O(N) due to the recursive call stack and sets.


🚀 This solution efficiently counts all valid N-Queens placements using backtracking!

Solution: N-Queens II (Count Distinct Solutions)

The N-Queens problem requires placing n queens on an n × n chessboard such that no two queens attack each other. Our goal is to return the number of valid solutions.


---

Approach: Backtracking with Bitmasking

Since we need to find all valid solutions, we can use backtracking to explore all possibilities efficiently.

Key Observations

1. Each row must have exactly one queen → We place queens row by row.


2. No two queens can be in the same column → Use a set to track occupied columns.


3. Diagonal constraints:

Main diagonal (row - col must be unique)

Anti-diagonal (row + col must be unique)





---

Optimized Implementation using Bitmasking

Instead of using sets for columns and diagonals, we can use bitmasking for fast lookups.

cols: Tracks occupied columns (n bits).

diags: Tracks occupied main diagonals (2n-1 bits).

antiDiags: Tracks occupied anti-diagonals (2n-1 bits).


Bitwise operations allow O(1) checks and updates.



---

Code Implementation

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


---

Explanation

1. Backtracking Function backtrack(row, cols, diags, antiDiags):

row: The current row we are placing a queen in.

cols: Bitmask tracking occupied columns.

diags: Bitmask tracking main diagonals (row - col).

antiDiags: Bitmask tracking anti-diagonals (row + col).



2. Base Case: If row == n, we found a valid solution → Return 1.


3. Iterate through columns (0 to n-1):

Check if the column, main diagonal, or anti-diagonal is already occupied.

If valid, mark the position (set the bit) and recurse for the next row.

Unmark the position (done automatically by recursion).





---

Complexity Analysis

Time Complexity: O(N!) in the worst case since we are placing N queens.

Space Complexity: O(N) for recursion stack.



---

Example Walkthrough

Example 1: n = 4

Input: n = 4
Output: 2

The two valid board configurations:

. Q . .      . . Q .
. . . Q      Q . . .
Q . . .      . . . Q
. . Q .      . Q . .

Example 2: n = 1

Input: n = 1
Output: 1

Only one way to place a single queen.


---

Why Use Bitmasking?

✅ Faster O(1) checks instead of searching sets.
✅ Less memory usage compared to arrays/lists.
✅ Improves performance for large n values (e.g., n = 9).

🚀 Optimized and efficient backtracking solution for counting N-Queens solutions!

Understanding the Bitmasking in totalNQueens

The given solution for the N-Queens II problem efficiently counts valid solutions using backtracking with bitmasking. Let's break it down step by step.


---

1. The Role of Bitmasking

Instead of using sets or lists to track attacked columns and diagonals, we use bitmasks (integers where each bit represents a column or diagonal state).

Columns (cols): Tracks occupied columns using a bitmask.

Main Diagonal (diags): Tracks occupied \ diagonals (row - col).

Anti-diagonal (antiDiags): Tracks occupied / diagonals (row + col).


Each bit in these integers represents whether a specific column or diagonal is occupied.


---

2. How the Bitmasking Works

Each column and diagonal is represented by a bit in an integer. We use bitwise operations to check and update them efficiently.

(a) Checking if a Position is Occupied

if (cols & (1 << col)) or (diags & (1 << diag)) or (antiDiags & (1 << antiDiag)):
    continue  # Skip invalid placements

1 << col: Creates a mask with only the colth bit set.

cols & (1 << col): Checks if col is occupied (if bit is 1).

diags & (1 << diag): Checks if the main diagonal is occupied.

antiDiags & (1 << antiDiag): Checks if the anti-diagonal is occupied.


If any of these bits are set, the queen cannot be placed in this column.


---

(b) Marking a Position as Occupied

count += backtrack(row + 1, 
                   cols | (1 << col), 
                   diags | (1 << diag), 
                   antiDiags | (1 << antiDiag))

When placing a queen:

cols | (1 << col): Sets the colth bit in cols (marking the column as occupied).

diags | (1 << diag): Marks the main diagonal as occupied.

antiDiags | (1 << antiDiag): Marks the anti-diagonal as occupied.


This updates the bitmasks before making a recursive call to backtrack(row + 1).


---

(c) Unmarking the Position (Implicit)

Since the function call is recursive and doesn't modify the existing variables (it passes updated copies), no explicit unmarking is needed. When the function backtracks, the previous state is naturally restored.


---

3. Example Execution for n = 4

For n = 4, the algorithm explores placements row by row.

First Queen (Row 0)

Try placing at (0,0)

cols = 0001

diags = 0001

antiDiags = 0001

Move to row 1.



Second Queen (Row 1)

Try (1,2)

cols = 0101 (Column 2 occupied)

diags = 0011 (Diagonal \ occupied)

antiDiags = 1010 (Anti-diagonal / occupied)

Move to row 2.



Third Queen (Row 2)

Try (2,3)

cols = 1101

diags = 0111

antiDiags = 1110

Move to row 3.



Fourth Queen (Row 3)

No valid placements → Backtrack


The algorithm continues exploring until all solutions are counted.


---

4. Why is Bitmasking Efficient?

Instead of using lists or sets:

Checking availability (& operation) is O(1).

Marking/unmarking (| operation) is O(1).

The memory usage is reduced from O(n) per row to O(1).


Thus, bitmasking makes N-Queens II significantly faster than naive approaches.


Understanding diag = row - col + n - 1 (Main Diagonal Indexing)

In the N-Queens II problem, we use bitmasking to track diagonals efficiently. However, because diagonals have both negative and positive indices, we shift the indices to fit within an array or bitmask.


---

1. Understanding the Main Diagonal (\)

The main diagonals (\) have the property that for any cell (row, col), the diagonal index is:


\text{diag} = \text{row} - \text{col}

(0,0) → 0

(1,1) → 0

(2,2) → 0

(3,3) → 0

(1,0) → 1, (2,1) → 1, (3,2) → 1

(0,1) → -1, (1,2) → -1, (2,3) → -1


Why Shift the Index?

The range of row - col is from -(n-1) to (n-1), so we cannot use negative indices.

To convert negative values to valid array indices, we shift all values up by (n-1):


\text{diag} = \text{row} - \text{col} + (n - 1)


---

2. Example for n = 4


---

3. How This Helps in Bitmasking

Since all diagonal indices now range from 0 to 2n-2, we can store them in a single integer bitmask.

This allows fast O(1) lookups and updates for diagonal constraints.



---

Summary

✅ row - col gives the diagonal index, but has negative values.
✅ Shifting by (n-1) ensures all indices are non-negative.
✅ This makes it easy to use bitmasking for quick diagonal lookups.



Understanding 1 << x (Bitwise Left Shift)

The expression 1 << x means bitwise left shift of the number 1 by x positions. It effectively multiplies 1 by 2^x.

How It Works

The binary representation of 1 is:

0001 (in binary)

Left shifting it by x places means adding x zeros to the right.


Examples

Why is 1 << x Used in Bitmasking?

In bitmasking, 1 << x is commonly used to:

1. Set a bit at position x

mask = 1 << 3  # Binary: 1000 (decimal: 8)


2. Check if a bit is set at position x

if bitmask & (1 << x):
    print("Bit is set")


3. Turn on a bit at position x

bitmask |= (1 << x)  # Use OR `|` to set the bit


4. Turn off a bit at position x

bitmask &= ~(1 << x)  # Use AND `&` with NOT `~` to clear the bit



Example in the N-Queens Problem

if cols & (1 << col):  
    continue  # Skip if this column is already occupied

1 << col creates a mask with only the colth bit set.

cols & (1 << col) checks if that column is occupied.

