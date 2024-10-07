To find the length of the last word in a string, we can solve this problem by first trimming any trailing spaces and then identifying the last word.

### Approach:

1. **Trim Trailing Spaces**: We remove any trailing spaces from the string to avoid issues with words being followed by spaces.
2. **Split the String**: We can split the string by spaces into a list of words.
3. **Return the Length of the Last Word**: The last element in the list will be the last word, so we can return its length.

### Algorithm:

1. **Trim the string**: Remove any extra spaces at the end.
2. **Split the string**: Split the string by spaces to separate words.
3. **Find the last word**: Get the last word from the split result and return its length.

### Code Implementation:

```python
def lengthOfLastWord(s: str) -> int:
    # Trim trailing spaces and split the string by spaces
    words = s.strip().split()

    # Return the length of the last word
    return len(words[-1])
```

### Explanation:

1. **`strip()`**: Removes leading and trailing spaces from the string.
2. **`split()`**: Splits the string into words based on spaces.
3. **`words[-1]`**: Accesses the last word in the list, and `len()` gives its length.

### Examples:

#### Example 1:
```python
s = "Hello World"
print(lengthOfLastWord(s))  # Output: 5
```
Explanation: The last word is "World", which has a length of 5.

#### Example 2:
```python
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))  # Output: 4
```
Explanation: The last word is "moon", which has a length of 4.

#### Example 3:
```python
s = "luffy is still joyboy"
print(lengthOfLastWord(s))  # Output: 6
```
Explanation: The last word is "joyboy", which has a length of 6.

### Time and Space Complexity:

- **Time Complexity**: O(n), where `n` is the length of the string. The `strip()` and `split()` operations each take O(n) time.
- **Space Complexity**: O(n) due to the space used to store the split words.

This solution handles cases where there are multiple spaces between words, as well as leading and trailing spaces.
