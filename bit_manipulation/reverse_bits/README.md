To reverse the bits of a given 32-bit unsigned integer, you can follow a bit-manipulation approach. The idea is to process each bit of the input number, reverse its position, and then accumulate the result.

### Steps:
1. **Initialize the result**: Start with a `result` initialized to `0`.
2. **Iterate through all 32 bits**: For each bit in the input number `n`, do the following:
   - Shift `result` to the left by one bit to make space for the new bit.
   - Extract the least significant bit of `n` and add it to the result.
   - Shift `n` to the right by one bit to process the next bit.
3. **Return the result**: After processing all 32 bits, the `result` will contain the reversed bits.

### Code Implementation:

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift result to the left to make space for the next bit
            result <<= 1
            # Add the least significant bit of n to result
            result |= n & 1
            # Shift n to the right to process the next bit
            n >>= 1
        return result

# Example usage:
solution = Solution()

# Example 1
n1 = 0b00000010100101000001111010011100  # Input as binary
print(solution.reverseBits(n1))  # Output: 964176192

# Example 2
n2 = 0b11111111111111111111111111111101  # Input as binary
print(solution.reverseBits(n2))  # Output: 3221225471
```

### Explanation of the Code:
- `result <<= 1`: Shifts `result` left by 1 bit, creating space for the next bit.
- `n & 1`: Extracts the least significant bit (rightmost) of `n`.
- `result |= n & 1`: Adds the extracted bit to the least significant bit of `result`.
- `n >>= 1`: Shifts `n` to the right by 1 bit, effectively removing the bit we've just processed.

### Example Walkthrough:

For `n = 0b00000010100101000001111010011100`:
1. Start with `n = 43261596`, result = 0.
2. Iterate 32 times, shifting bits from `n` into `result` one by one.
3. After 32 iterations, the `result` will contain `0b00111001011110000010100101000000` which is `964176192`.

### Time Complexity:
- The time complexity is \(O(1)\), because the number of bits (32) is constant.

### Space Complexity:
- The space complexity is \(O(1)\), as we only use a few integer variables.


The expression `result |= n & 1` is a bitwise operation that can be broken down as follows:

### 1. **`n & 1`** (Bitwise AND):
- This operation checks whether the least significant bit (rightmost bit) of the integer `n` is `1` or `0`.
- The `&` operator compares each bit of `n` with `1`. Since `1` is `0001` in binary, only the least significant bit of `n` is compared with `1`.
  - If the least significant bit of `n` is `1`, `n & 1` will result in `1`.
  - If the least significant bit of `n` is `0`, `n & 1` will result in `0`.

### 2. **`result |=`** (Bitwise OR and Assignment):
- The `|=` operator is a shorthand for **bitwise OR** followed by assignment.
  - It first performs a bitwise OR operation between `result` and the value of `n & 1`.
  - The result of this OR operation is then assigned back to `result`.

The `|` (bitwise OR) operation works as follows:
- If either of the bits being compared is `1`, the result will be `1`. If both bits are `0`, the result will be `0`.

### Example:
```python
n = 5  # Binary: 101
result = 0

# n & 1 checks the least significant bit of n:
n & 1  # 101 & 001 -> 1

# result |= 1 means:
result = result | 1  # 0 | 1 -> 1
```

This operation is commonly used in algorithms that manipulate bits, such as checking or extracting specific bits from a number, often in a loop.

