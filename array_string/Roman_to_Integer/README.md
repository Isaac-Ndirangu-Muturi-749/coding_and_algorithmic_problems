To convert a Roman numeral to an integer, you can follow a simple rule-based approach. Each symbol in the Roman numeral either adds or subtracts its value depending on whether it is followed by a larger or smaller symbol.

### Approach:
1. **Roman Numeral Values**:
   - I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.

2. **Subtractive Cases**:
   - When a smaller symbol appears before a larger symbol, it is subtracted (e.g., IV = 4, IX = 9, etc.).

3. **General Algorithm**:
   - Traverse the Roman numeral from left to right.
   - For each symbol, if its value is less than the value of the next symbol, subtract it. Otherwise, add it.

### Algorithm:
1. Create a dictionary to map each Roman numeral character to its corresponding integer value.
2. Initialize the result to 0.
3. Iterate through the string:
   - If the current symbol's value is less than the next symbol, subtract it from the result.
   - Otherwise, add it to the result.
4. At the end of the loop, you will have the integer equivalent of the Roman numeral.

### Code Implementation:

```python
def romanToInt(s: str) -> int:
    # Roman numeral to integer mapping
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    n = len(s)

    for i in range(n):
        # If current value is less than next value, subtract it, otherwise add it
        if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            result -= roman_to_int[s[i]]
        else:
            result += roman_to_int[s[i]]

    return result
```

### Explanation:
1. **Mapping**: The `roman_to_int` dictionary maps Roman numeral characters to their integer values.
2. **Looping Through the String**:
   - The loop checks each Roman numeral character.
   - If the current symbol is less than the next one (e.g., IV, IX), it subtracts its value from the result.
   - Otherwise, it adds its value to the result.
3. **Final Result**: After processing all characters, `result` holds the integer equivalent.

### Example 1:

```python
s = "III"
print(romanToInt(s))  # Output: 3
```
Explanation: `III` = 1 + 1 + 1 = 3.

### Example 2:

```python
s = "LVIII"
print(romanToInt(s))  # Output: 58
```
Explanation: `L` = 50, `V` = 5, `III` = 1 + 1 + 1 = 58.

### Example 3:

```python
s = "MCMXCIV"
print(romanToInt(s))  # Output: 1994
```
Explanation: `M` = 1000, `CM` = 900, `XC` = 90, `IV` = 4. Thus, 1000 + 900 + 90 + 4 = 1994.

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the length of the input string. We process each character once.
- **Space Complexity**: O(1), since the dictionary and the variables used take constant space.

This approach efficiently handles valid Roman numeral inputs within the constraints given.
