To determine if an integer `x` is a palindrome, we need to check if the number reads the same forward and backward. A simple way to do this is to reverse the integer and compare it to the original value.

### Key Points:
1. Negative numbers are not palindromes because the minus sign will be at the front when read forward, and at the back when reversed.
2. Numbers that end in zero (except zero itself) cannot be palindromes because their reversed versions will have leading zeros, which aren't valid in integer representation.

### Approach:
1. **Negative check**: If `x` is negative, immediately return `false`.
2. **Reverse the integer**: Reverse the digits of `x` and compare the reversed number to the original.
3. **Edge cases**: Handle special cases such as zero and numbers that end with zero.

### Code Implementation:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative or ends with 0 (but not 0 itself), it can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original = x

        # Reverse the digits of the number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # Check if the original number is the same as the reversed number
        return original == reversed_num

# Example usage:
solution = Solution()

# Example 1
print(solution.isPalindrome(121))  # Output: True

# Example 2
print(solution.isPalindrome(-121))  # Output: False

# Example 3
print(solution.isPalindrome(10))  # Output: False
```

### Explanation:
- **Initial Checks**:
   - Negative numbers (`x < 0`) are immediately ruled out as non-palindromes.
   - Numbers that end in `0` (except `0` itself) are not palindromes since reversing them would result in leading zeros.
- **Reversing the Number**:
   - We repeatedly extract the last digit from `x` and build `reversed_num` by appending this digit.
   - After processing all digits, we compare the reversed number to the original.

### Example Walkthrough:
1. **Example 1**:
   - Input: `x = 121`
   - Reversing: `1 -> 12 -> 121`
   - Comparison: `121 == 121`, so it's a palindrome.
2. **Example 2**:
   - Input: `x = -121`
   - It's negative, so return `False`.
3. **Example 3**:
   - Input: `x = 10`
   - Reversing: `0 -> 01`, which results in `1`.
   - Comparison: `10 != 1`, so it's not a palindrome.

### Time Complexity:
- \(O(\log_{10}(x))\): The number of digits in `x` determines the number of iterations needed to reverse the number.

### Space Complexity:
- \(O(1)\): Only a few integer variables are used regardless of the size of `x`.


The code snippet `while x > 0` is part of an algorithm to reverse the digits of an integer `x`. Here's a step-by-step breakdown of how it works:

### 1. **Initialization**:
   - `reversed_num` is typically initialized to 0 outside the loop.
   - `x` is the integer whose digits we want to reverse.

### 2. **`while x > 0:`**:
   - This loop continues to execute as long as `x` is greater than 0. Once all the digits have been processed (i.e., when `x` becomes 0), the loop stops.

### 3. **`reversed_num = reversed_num * 10 + x % 10`**:
   - This step updates `reversed_num` by appending the last digit of `x` to it.
   - **`x % 10`** extracts the last digit of `x`. For example, if `x = 123`, `x % 10 = 3`.
   - **`reversed_num * 10`** shifts the existing digits of `reversed_num` to the left by one position (because multiplying by 10 adds a zero to the end of the number).
     - Initially, `reversed_num` is `0`, so `0 * 10 + 3 = 3`. The last digit (`3`) becomes the first digit of `reversed_num`.
     - In the next iteration, the extracted digit (`2` from `x = 12`) is appended to `reversed_num`, now making it `3 * 10 + 2 = 32`.
     - The process continues until all digits are appended.

### 4. **`x //= 10`**:
   - This step removes the last digit of `x` by performing an integer division of `x` by `10`.
     - For example, if `x = 123`, after this operation, `x = 12`.
   - This allows the next iteration of the loop to extract the next-to-last digit of `x`.

### Example:
Let's break down the process with an example where `x = 1234`.

- **Iteration 1**:
  - `x = 1234`
  - `reversed_num = 0`
  - `x % 10 = 4`
  - `reversed_num = 0 * 10 + 4 = 4`
  - `x //= 10 → x = 123`

- **Iteration 2**:
  - `x = 123`
  - `reversed_num = 4`
  - `x % 10 = 3`
  - `reversed_num = 4 * 10 + 3 = 43`
  - `x //= 10 → x = 12`

- **Iteration 3**:
  - `x = 12`
  - `reversed_num = 43`
  - `x % 10 = 2`
  - `reversed_num = 43 * 10 + 2 = 432`
  - `x //= 10 → x = 1`

- **Iteration 4**:
  - `x = 1`
  - `reversed_num = 432`
  - `x % 10 = 1`
  - `reversed_num = 432 * 10 + 1 = 4321`
  - `x //= 10 → x = 0`

At the end of the loop, `reversed_num = 4321`, which is the reverse of the original number `1234`.
