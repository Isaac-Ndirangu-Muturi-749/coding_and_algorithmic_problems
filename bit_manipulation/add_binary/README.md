## Name: add_binary
## Type: bit_manipulation
### Problem: problem.md
### Solution: solution.py
### Tests: test_cases.py

To solve the problem of adding two binary strings and returning their sum as a binary string, you can follow these steps:

1. **Reverse Both Strings**: Start by reversing both strings to facilitate the addition from the least significant bit (rightmost bit) to the most significant bit (leftmost bit).

2. **Perform Binary Addition**: Use a carry variable to keep track of any carry-over while performing the addition bit by bit.

3. **Construct the Result**: After processing all bits, if there's a carry left, append it to the result. Finally, reverse the result to get the correct binary string.

Here is a Python function that implements this approach:

### Solution Code

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize result and carry
        result = []
        carry = 0

        # Reverse both strings
        a = a[::-1]
        b = b[::-1]

        # Determine the length of the longer string
        max_len = max(len(a), len(b))

        # Perform binary addition bit by bit
        for i in range(max_len):
            # Get the current digits or use 0 if the index is out of bounds
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0

            # Calculate the sum of bits and carry
            total = bit_a + bit_b + carry
            result_bit = total % 2  # The result bit (0 or 1)
            carry = total // 2      # The carry for the next position

            # Append the result bit to the result list
            result.append(str(result_bit))

        # If there's a carry left, append it
        if carry:
            result.append('1')

        # Reverse the result and join it to form the final binary string
        return ''.join(result[::-1])
```

### Explanation

1. **Reverse the Strings**: The `[::-1]` slicing reverses the strings so that you can add bits starting from the least significant bit.

2. **Binary Addition**:
   - For each bit position, sum the corresponding bits from both strings and the carry.
   - Calculate the result bit (`total % 2`) and update the carry (`total // 2`).
   - Append the result bit to the `result` list.

3. **Handle Remaining Carry**: If there's a carry left after processing all bits, append it to the result.

4. **Return the Final Binary String**: Reverse the `result` list to get the binary string in the correct order and join it into a single string.

This approach ensures that the binary addition is performed efficiently even for large strings, respecting the constraints given.
