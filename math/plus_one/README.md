To solve this problem, we need to increment the large integer represented by the `digits` array by one. Here's the plan:

### Steps:
1. **Start from the last digit**: Traverse the array from the last element (least significant digit) backward to the first.
2. **Handle carry**:
   - If the current digit is less than `9`, simply increment the digit and return the array.
   - If the current digit is `9`, change it to `0` and move to the next significant digit (to the left). This creates a carry that needs to be handled by the next digit.
3. **Edge Case**: If all digits are `9` (e.g., `[9, 9, 9]`), you'll need to prepend `1` at the start of the array and set all digits to `0` (e.g., `[1, 0, 0, 0]`).

### Solution Code:

```python
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        # Traverse the digits starting from the least significant one (rightmost)
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue the loop
            digits[i] = 0

        # If all digits were 9, we need to add 1 at the start
        return [1] + digits
```

### Explanation:
- **Traversing from the end**: We iterate the array backward (from the least significant digit). If we find a digit less than 9, we simply increment it and return the updated array.
- **Handle digit 9**: If the digit is `9`, we set it to `0` and continue to the next digit. This creates a carry for the next more significant digit.
- **Edge case (all 9s)**: If we exit the loop, it means all the digits were `9`. In this case, we prepend `1` to the array and fill the rest of the digits with `0`.

### Example Walkthrough:

#### Example 1:
- Input: `digits = [1, 2, 3]`
  - Start from the rightmost digit `3`. Increment it: `3 + 1 = 4`.
  - Output: `[1, 2, 4]`.

#### Example 2:
- Input: `digits = [4, 3, 2, 1]`
  - Start from the rightmost digit `1`. Increment it: `1 + 1 = 2`.
  - Output: `[4, 3, 2, 2]`.

#### Example 3:
- Input: `digits = [9]`
  - The rightmost digit is `9`, so it becomes `0`.
  - Prepend `1` because there was a carry.
  - Output: `[1, 0]`.

### Time Complexity:
- **Time Complexity**: O(n), where `n` is the number of digits. We may need to traverse all the digits in the worst case.
- **Space Complexity**: O(1) (excluding the space required for the output array).

This solution efficiently handles the problem, including edge cases where all digits are `9`.
