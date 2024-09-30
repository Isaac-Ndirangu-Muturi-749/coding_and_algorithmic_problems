To compute the square root of a non-negative integer `x` rounded down to the nearest integer without using any built-in exponent function or operator, we can leverage **binary search**. This approach works because the square root of `x` lies between `0` and `x`, and we can efficiently find it using binary search within this range.

### Binary Search Approach:
1. The square root of `x` will be in the range `[0, x]`.
2. Use binary search to find the largest integer `m` such that `m * m <= x`.
3. If `m * m == x`, return `m`; otherwise, return `m` rounded down, which will be the last value of `m` where `m * m <= x`.

### Steps:
- Set the left boundary to `0` and the right boundary to `x`.
- Calculate the middle point `m`.
- If `m * m == x`, return `m`.
- If `m * m < x`, move the left boundary to `m + 1`.
- If `m * m > x`, move the right boundary to `m - 1`.
- Continue this until the left boundary crosses the right boundary, and the largest valid `m` will be the answer.

### Code Implementation:

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x  # Start the search range from 1 to x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid  # If we find the exact square root, return it
            elif mid * mid < x:
                left = mid + 1  # Search the right half
            else:
                right = mid - 1  # Search the left half

        return right  # right is the largest integer such that right^2 <= x
```

### Explanation:
- **Initialization**: We set `left` to `1` and `right` to `x`. If `x` is `0`, we return `0` immediately.
- **Binary Search**:
  - We calculate the middle point `mid` and check if `mid * mid` is equal to `x`.
  - If `mid * mid < x`, then we need to search the right half by setting `left = mid + 1`.
  - If `mid * mid > x`, we search the left half by setting `right = mid - 1`.
- **Termination**: When the loop ends, `right` will be the largest integer such that `right^2 <= x`.

### Example 1:
For `x = 4`:
- Initial range: `left = 1`, `right = 4`
- First mid: `mid = 2`. Since `2 * 2 = 4`, we return `2`.

### Example 2:
For `x = 8`:
- Initial range: `left = 1`, `right = 8`
- First mid: `mid = 4`. Since `4 * 4 = 16 > 8`, adjust `right = mid - 1 = 3`.
- Second mid: `mid = 2`. Since `2 * 2 = 4 < 8`, adjust `left = mid + 1 = 3`.
- Third mid: `mid = 3`. Since `3 * 3 = 9 > 8`, adjust `right = mid - 1 = 2`.
- The loop ends, and we return `right = 2`.

### Time Complexity:
- **O(log x)**: Binary search reduces the search range by half each time, so the time complexity is logarithmic in `x`.

This approach ensures that we find the square root efficiently with a time complexity of `O(log x)` without using any built-in power functions.


In this binary search algorithm to find the square root of a number `x`, you return `right` instead of `left` because the goal is to find the largest integer `n` such that `n * n <= x`.

### Detailed Explanation:

1. **Initialization**:
   - You start by defining `left = 1` and `right = x`. The binary search will narrow down this range to find the square root.

2. **Binary Search Loop**:
   - In each iteration, you calculate the midpoint `mid = (left + right) // 2`.
   - You check whether `mid * mid` is equal to, less than, or greater than `x`.

3. **If `mid * mid == x`**:
   - This is the case where you find the exact square root, and the function immediately returns `mid`.

4. **If `mid * mid < x`**:
   - This means `mid` is too small to be the square root, so you adjust `left = mid + 1` to search the right half (larger values).

5. **If `mid * mid > x`**:
   - This means `mid` is too large, so you adjust `right = mid - 1` to search the left half (smaller values).

### Why return `right`?

- **Why not return `left`**:
  After the loop finishes, `left` will point to a value that, when squared, is greater than `x`. It will be the smallest number such that `left * left > x`. This means `left` has overshot the correct square root.

- **Why return `right`**:
  At the end of the loop, `right` will point to the largest integer such that `right * right <= x`. This is what we want: the integer part of the square root, which satisfies the condition `right * right <= x`, but `right + 1` would be too large (`(right + 1) * (right + 1) > x`).

### Example: `x = 8`
- The integer square root of 8 is 2 (because \(2^2 = 4\) and \(3^2 = 9\)).
- At the end of the loop:
  - `left` will have moved past 2 (pointing to 3), but 3 is too large since \(3^2 = 9 > 8\).
  - `right` will correctly point to 2, which is the largest integer whose square is less than or equal to 8.
- Hence, `right` is returned.

In summary, you return `right` because it's the largest integer that satisfies `right * right <= x`, which is what you need when calculating the integer square root.
