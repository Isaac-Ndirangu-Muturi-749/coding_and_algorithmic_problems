To convert an integer to a Roman numeral, we'll follow the rules for Roman numeral representation and implement a greedy approach. Roman numerals are formed by subtracting the largest possible values (based on Roman numeral symbols) from the number, appending the corresponding Roman symbols, and repeating the process until the number becomes 0.

### Steps:
1. **Mapping**: Define a mapping of Roman numerals to their integer values, starting from the largest possible value to the smallest. This will help us select the largest symbol that can be subtracted from the input number.
2. **Greedy Approach**: Subtract the largest possible value from the input number, append the corresponding Roman numeral symbol, and continue until the number becomes zero.
3. **Special Subtractive Cases**: Handle cases like 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM) explicitly in the mapping.

### Roman Numeral Mapping:
- 1000 -> "M"
- 900  -> "CM"
- 500  -> "D"
- 400  -> "CD"
- 100  -> "C"
- 90   -> "XC"
- 50   -> "L"
- 40   -> "XL"
- 10   -> "X"
- 9    -> "IX"
- 5    -> "V"
- 4    -> "IV"
- 1    -> "I"

### Algorithm:
- Start from the largest value in the mapping and subtract as many times as possible, appending the corresponding Roman numeral symbol.
- Move to the next smaller value and repeat the process until the input number becomes zero.

### Code Implementation:

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples with Roman numeral symbols and their corresponding values
        value_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman = []  # List to accumulate the Roman numeral result

        # Iterate over the value-symbol pairs
        for value, symbol in value_to_roman:
            # While num is greater than or equal to the value, subtract the value and append the symbol
            while num >= value:
                num -= value
                roman.append(symbol)

        # Join all Roman numeral parts into a single string and return
        return "".join(roman)
```

### Explanation:
- **`value_to_roman`**: A list of tuples containing integer values and their corresponding Roman numeral symbols, sorted in descending order.
- **`roman`**: A list that accumulates the Roman numeral symbols.
- **Loop through `value_to_roman`**:
  - For each tuple `(value, symbol)`, while `num >= value`, subtract `value` from `num` and append `symbol` to the result list `roman`.
- Finally, we join the list `roman` to form the final Roman numeral string.

### Time Complexity:
- **O(1)**: Since the number of iterations is fixed (there are a constant number of Roman symbols and values), the algorithm runs in constant time, despite appearing to iterate over the input `num`.

### Space Complexity:
- **O(1)**: We use a fixed amount of extra space (the list of Roman numeral symbols and the result list), making it constant in space complexity.

### Example Walkthrough:

#### Example 1:
- Input: `num = 3749`
- Output: `MMMDCCXLIX`
  - 3000: `MMM`
  - 700: `DCC`
  - 40: `XL`
  - 9: `IX`
  - Final: `MMMDCCXLIX`

#### Example 2:
- Input: `num = 58`
- Output: `LVIII`
  - 50: `L`
  - 8: `VIII`
  - Final: `LVIII`

#### Example 3:
- Input: `num = 1994`
- Output: `MCMXCIV`
  - 1000: `M`
  - 900: `CM`
  - 90: `XC`
  - 4: `IV`
  - Final: `MCMXCIV`

This approach ensures that the number is correctly converted to Roman numerals following all the rules for Roman numeral notation.
