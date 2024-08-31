To determine whether a given string `s` is a palindrome, we'll follow these steps:

### Steps:

1. **Normalize the String**:
   - Convert all characters in the string to lowercase.
   - Remove all non-alphanumeric characters (i.e., remove anything that is not a letter or a number).

2. **Check for Palindrome**:
   - After normalization, check if the string reads the same forwards and backwards.

### Example Walkthrough:

Let's go through the examples provided:

1. **Example 1**:
   - **Input**: `s = "A man, a plan, a canal: Panama"`
   - **Normalization**: Convert to lowercase and remove non-alphanumeric characters. The resulting string is `"amanaplanacanalpanama"`.
   - **Check**: This string reads the same forwards and backwards.
   - **Output**: `true`

2. **Example 2**:
   - **Input**: `s = "race a car"`
   - **Normalization**: The normalized string is `"raceacar"`.
   - **Check**: This string does not read the same forwards and backwards.
   - **Output**: `false`

3. **Example 3**:
   - **Input**: `s = " "`
   - **Normalization**: After removing non-alphanumeric characters, the resulting string is an empty string `""`.
   - **Check**: An empty string is considered a palindrome.
   - **Output**: `true`

### Implementation in Python:

Here’s how you could implement the solution in Python:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: convert to lowercase and filter alphanumeric characters
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())

        # Check if the normalized string is the same forward and backward
        return normalized_str == normalized_str[::-1]
```

### Explanation of the Code:

1. **Normalization**:
   - We use a generator expression to iterate over each character in the string.
   - `char.lower()` converts each character to lowercase.
   - `char.isalnum()` checks if the character is alphanumeric.
   - The `''.join(...)` concatenates the filtered characters into a new string.

2. **Palindrome Check**:
   - `normalized_str[::-1]` creates a reversed version of the normalized string.
   - We then check if the normalized string is equal to its reversed version.

### Test Cases:

```python
solution = Solution()

# Test case 1
assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

# Test case 2
assert solution.isPalindrome("race a car") == False

# Test case 3
assert solution.isPalindrome(" ") == True

print("All test cases passed!")
```

### Complexity Analysis:

- **Time Complexity**: O(n), where n is the length of the string `s`. We process each character at most twice (once for filtering and once for comparison).
- **Space Complexity**: O(n) for storing the normalized string.

This solution efficiently checks whether the input string is a palindrome by handling edge cases like spaces, punctuation, and mixed case characters.
