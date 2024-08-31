To traverse a matrix in spiral order, we need to simulate the movement along the boundaries of the matrix: right, down, left, and up. We continue this process, gradually narrowing the boundaries until all elements have been visited.

### Approach:

1. **Initialize Boundaries**: Start with four boundaries:
   - `top`: initially 0
   - `bottom`: initially `m-1` (last row)
   - `left`: initially 0
   - `right`: initially `n-1` (last column)

2. **Spiral Traversal**:
   - Traverse from `left` to `right` along the `top` boundary and then move the `top` boundary down.
   - Traverse from `top` to `bottom` along the `right` boundary and then move the `right` boundary left.
   - Traverse from `right` to `left` along the `bottom` boundary and then move the `bottom` boundary up.
   - Traverse from `bottom` to `top` along the `left` boundary and then move the `left` boundary right.
   - Repeat this process until the boundaries overlap or cross each other.

3. **Stop Condition**: The loop stops when the `top` boundary crosses the `bottom` or the `left` boundary crosses the `right`.

### Implementation:

```python
def spiralOrder(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

### Explanation:

1. **Initial Boundaries**:
   - `top = 0`
   - `bottom = m - 1`
   - `left = 0`
   - `right = n - 1`

2. **Traversal**:
   - First, move right across the `top` row, then move down the `right` column, left across the `bottom` row, and up the `left` column.
   - After each pass, the corresponding boundary is moved inward.

3. **Edge Cases**:
   - If `matrix` is empty, we return an empty list.
   - The code handles matrices with different shapes (e.g., single row, single column).

### Examples:

- **Example 1**:
  - Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
  - Output: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

- **Example 2**:
  - Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
  - Output: `[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]`

### Complexity Analysis:

- **Time Complexity**: O(m * n), where `m` is the number of rows and `n` is the number of columns. Every element is visited exactly once.
- **Space Complexity**: O(1) additional space, if we do not count the output list. The space used by the output list is proportional to the number of elements in the matrix.
