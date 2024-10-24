To solve this problem, we need to compute the bitwise AND of all integers in the range `[left, right]`. A key observation is that as we move through the range, the lower bits (least significant bits) of the numbers in the range will vary between `0` and `1`, causing those bits to be reset to `0` when performing a bitwise AND operation over the entire range. Thus, what remains are the common higher-order bits between `left` and `right`.

### Approach:

1. **Bit-shifting approach**:
   - We keep shifting both `left` and `right` to the right until they are equal. This process essentially finds the common prefix (most significant bits) of `left` and `right`.
   - After finding the common prefix, we shift back to the left to restore the number to its original magnitude. The remaining bits after this operation are all `0`.

### Solution:

```python
def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    # Find the common prefix by shifting right until left equals right
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    # Shift left to restore the common prefix to its original magnitude
    return left << shift

# Example usage:
print(rangeBitwiseAnd(5, 7))  # Output: 4
print(rangeBitwiseAnd(0, 0))  # Output: 0
print(rangeBitwiseAnd(1, 2147483647))  # Output: 0
```

### Explanation:

1. **Shifting to Find Common Prefix**:
   - We shift both `left` and `right` to the right until they are equal. This effectively removes the differing least significant bits. What remains is the common prefix in the binary representation of the numbers within the range.

2. **Restoring the Value**:
   - Once we find the common prefix, we shift it back to the left to restore its original magnitude. The bits we shifted out are filled with `0`s, which ensures that the bitwise AND of the numbers in the range results in the correct answer.

### Example Walkthrough:

#### Example 1: `left = 5`, `right = 7`
- Binary representation:
  - `5` = `101`
  - `6` = `110`
  - `7` = `111`

  As we can see, the numbers differ in their lower 2 bits. Only the most significant bit `1xx` is common among all three numbers.

- We shift both `left` and `right` to the right until they are equal:
  - `5 >> 1 = 2`
  - `7 >> 1 = 3`
  - Continue shifting:
    - `2 >> 1 = 1`
    - `3 >> 1 = 1`
  Now `left == right`.

- After finding the common prefix (`1`), we shift it back left by 2 bits to get `100`, which is `4` in decimal.

#### Example 2: `left = 0`, `right = 0`
- Both numbers are the same, so the result is simply `0`.

#### Example 3: `left = 1`, `right = 2147483647`
- The difference between `left` and `right` is so large that all bits will get reset to `0` after the shifting process, so the result is `0`.

### Time Complexity:
- The time complexity is **O(log n)**, where `n` is the range between `left` and `right`. This is because we are shifting both numbers to the right until they are equal, which takes logarithmic time in terms of the number of bits.

### Space Complexity:
- The space complexity is **O(1)**, as we are only using a constant amount of space for variables.

This approach efficiently solves the problem with both linear time complexity in terms of the number of bits and constant space usage.
