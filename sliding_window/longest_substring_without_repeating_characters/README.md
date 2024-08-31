To find the length of the longest substring without repeating characters in a given string `s`, we can use the **sliding window** technique with a **hashmap** (or dictionary). This approach allows us to efficiently keep track of the characters in the current window and their most recent positions.

### Approach:

1. **Sliding Window**:
   - We use two pointers (`left` and `right`) to represent the current window of characters we're considering.
   - We expand the window by moving the `right` pointer to include new characters and update the `left` pointer to ensure there are no repeated characters.

2. **Hashmap**:
   - We use a dictionary to store the characters and their latest indices. This allows us to quickly check if a character has already been seen and to update the `left` pointer if necessary.

3. **Update the Result**:
   - As we move the `right` pointer, we calculate the current window size (which is `right - left + 1`) and update the maximum length of the substring found so far.

### Implementation:

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to the right of the last seen duplicate character
            left = char_index[s[right]] + 1

        # Update the character's last seen index
        char_index[s[right]] = right

        # Calculate the maximum length of the substring
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Explanation:

- **char_index**: This dictionary keeps track of the most recent index of each character.
- **left pointer**: It marks the beginning of the current window. If we encounter a repeating character, we move the `left` pointer to one position right of the last occurrence of the repeating character.
- **right pointer**: It expands the window by moving to the next character.
- **max_length**: It keeps track of the length of the longest substring without repeating characters that we've found so far.

### Example Walkthrough:

1. For `s = "abcabcbb"`:
   - Starting with an empty window, we expand it to include "abc".
   - When we encounter the second "a", we move the `left` pointer to start after the first "a".
   - The process continues, and the longest substring found is "abc" with a length of 3.

2. For `s = "bbbbb"`:
   - The window keeps moving as we encounter the repeating "b" characters.
   - The longest substring without repeating characters is "b" with a length of 1.

3. For `s = "pwwkew"`:
   - The window expands to "pw".
   - On encountering the second "w", we move the `left` pointer to "k".
   - The longest substring found is "wke" with a length of 3.

### Complexity Analysis:

- **Time Complexity**: O(n), where `n` is the length of the string. Each character is processed at most twice (once when expanding the window and once when contracting it).
- **Space Complexity**: O(min(m, n)), where `m` is the size of the charset (in this case, ASCII characters) and `n` is the length of the string. The dictionary stores the most recent index of each character.

This method efficiently finds the length of the longest substring without repeating characters and works well even for large input sizes.


Let's break down the `lengthOfLongestSubstring` function step by step, using an example to help understand how it works.

### Problem Context:
- **Objective**: Find the length of the longest substring without repeating characters in a given string `s`.
- **Input**: A string `s`.
- **Output**: An integer representing the length of the longest substring without repeating characters.

### Code Breakdown:

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to the right of the last seen duplicate character
            left = char_index[s[right]] + 1

        # Update the character's last seen index
        char_index[s[right]] = right

        # Calculate the maximum length of the substring
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Example Walkthrough:
Let's use the example string `s = "abcabcbb"`.

1. **Initialization**:
   - `char_index = {}`: This dictionary will store the most recent index of each character.
   - `left = 0`: The left pointer starts at the beginning of the string.
   - `max_length = 0`: This will track the length of the longest substring found.

2. **First Iteration (`right = 0`)**:
   - `s[right] = 'a'`.
   - `'a'` is not in `char_index`, so we skip the first `if` condition.
   - Update `char_index` to `{'a': 0}` (store the index of `'a'`).
   - Calculate `max_length = max(0, 0 - 0 + 1) = 1`.

3. **Second Iteration (`right = 1`)**:
   - `s[right] = 'b'`.
   - `'b'` is not in `char_index`.
   - Update `char_index` to `{'a': 0, 'b': 1}`.
   - Calculate `max_length = max(1, 1 - 0 + 1) = 2`.

4. **Third Iteration (`right = 2`)**:
   - `s[right] = 'c'`.
   - `'c'` is not in `char_index`.
   - Update `char_index` to `{'a': 0, 'b': 1, 'c': 2}`.
   - Calculate `max_length = max(2, 2 - 0 + 1) = 3`.

5. **Fourth Iteration (`right = 3`)**:
   - `s[right] = 'a'`.
   - `'a'` is in `char_index` and its last seen index `0` is `>= left` (`0 >= 0`).
   - Move `left` to `char_index['a'] + 1 = 0 + 1 = 1` (move past the last occurrence of `'a'`).
   - Update `char_index` to `{'a': 3, 'b': 1, 'c': 2}`.
   - Calculate `max_length = max(3, 3 - 1 + 1) = 3`.

6. **Fifth Iteration (`right = 4`)**:
   - `s[right] = 'b'`.
   - `'b'` is in `char_index` and its last seen index `1` is `>= left` (`1 >= 1`).
   - Move `left` to `char_index['b'] + 1 = 1 + 1 = 2`.
   - Update `char_index` to `{'a': 3, 'b': 4, 'c': 2}`.
   - Calculate `max_length = max(3, 4 - 2 + 1) = 3`.

7. **Sixth Iteration (`right = 5`)**:
   - `s[right] = 'c'`.
   - `'c'` is in `char_index` and its last seen index `2` is `>= left` (`2 >= 2`).
   - Move `left` to `char_index['c'] + 1 = 2 + 1 = 3`.
   - Update `char_index` to `{'a': 3, 'b': 4, 'c': 5}`.
   - Calculate `max_length = max(3, 5 - 3 + 1) = 3`.

8. **Seventh Iteration (`right = 6`)**:
   - `s[right] = 'b'`.
   - `'b'` is in `char_index` and its last seen index `4` is `>= left` (`4 >= 3`).
   - Move `left` to `char_index['b'] + 1 = 4 + 1 = 5`.
   - Update `char_index` to `{'a': 3, 'b': 6, 'c': 5}`.
   - Calculate `max_length = max(3, 6 - 5 + 1) = 3`.

9. **Eighth Iteration (`right = 7`)**:
   - `s[right] = 'b'`.
   - `'b'` is in `char_index` and its last seen index `6` is `>= left` (`6 >= 5`).
   - Move `left` to `char_index['b'] + 1 = 6 + 1 = 7`.
   - Update `char_index` to `{'a': 3, 'b': 7, 'c': 5}`.
   - Calculate `max_length = max(3, 7 - 7 + 1) = 3`.

### Final Result:
- The loop finishes, and the final value of `max_length` is `3`.
- **Output**: The function returns `3`, which is the length of the longest substring without repeating characters ("abc").

### Summary:
- **Sliding Window Technique**: The function uses a sliding window approach, where `left` and `right` represent the boundaries of the current substring.
- **HashMap**: The `char_index` dictionary stores the last seen index of each character, allowing the function to efficiently detect and handle duplicates.
- **Time Complexity**: The function runs in O(n) time, where `n` is the length of the string `s`, since each character is processed at most twice (once by the `right` pointer and potentially once by the `left` pointer).
