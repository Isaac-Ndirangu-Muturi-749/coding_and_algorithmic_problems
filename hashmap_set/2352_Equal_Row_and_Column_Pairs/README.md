Here’s how you can solve the problem without using `collections.Counter`. Instead, we manually count the occurrences of rows and compare them with columns.

---

### Implementation

```python
def equalPairs(grid):
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
```

---

### Explanation

1. **Count Rows**:
   - Convert each row into a tuple and store it in a dictionary (`row_count`) with its frequency. This manual counting replaces `Counter`.

2. **Transpose Columns**:
   - Use `zip(*grid)` to transpose the grid, making columns accessible as tuples.

3. **Match Rows and Columns**:
   - Check if each column (as a tuple) exists in the `row_count` dictionary. If it does, add its frequency to the result.

---

### Complexity

- **Time Complexity**: \(O(n^2)\)
  - Constructing the `row_count` dictionary takes \(O(n^2)\).
  - Matching columns against rows also takes \(O(n^2)\).

- **Space Complexity**: \(O(n^2)\)
  - Storing the rows as tuples in the dictionary.

---

### Example Outputs

```python
print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))  # Output: 1
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))  # Output: 3
```
