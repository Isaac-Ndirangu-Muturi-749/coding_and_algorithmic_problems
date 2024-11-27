To solve the problem of reversing the order of words in a string `s`, we can follow these steps:

### Approach:
1. **Trim and Split**: Remove any leading and trailing spaces, and then split the string into words. The words will be separated by one or more spaces.
2. **Reverse the List of Words**: After splitting the string into words, reverse the order of the words.
3. **Join the Words**: Finally, join the words back into a single string with exactly one space separating the words.

### Steps in Detail:
- First, split the string into words while ignoring multiple spaces.
- Reverse the list of words.
- Join the words using a single space.

### Code Implementation:

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Strip leading and trailing spaces, split by spaces
        words = s.split()  # This also takes care of multiple spaces between words

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join the reversed words with a single space
        return ' '.join(reversed_words)
```

### Explanation:
1. **`split()`**: This function splits the string by any sequence of whitespace (default behavior). It automatically handles multiple spaces and trims the leading and trailing spaces.
2. **`[::-1]`**: This slice notation reverses the list of words.
3. **`' '.join(reversed_words)`**: This concatenates the reversed words with a single space between each word.

### Example Walkthroughs:

#### Example 1:
- **Input**: `s = "the sky is blue"`
- **Step 1**: Split the string into words: `["the", "sky", "is", "blue"]`
- **Step 2**: Reverse the words: `["blue", "is", "sky", "the"]`
- **Step 3**: Join them: `"blue is sky the"`
- **Output**: `"blue is sky the"`

#### Example 2:
- **Input**: `s = "  hello world  "`
- **Step 1**: Split into words: `["hello", "world"]`
- **Step 2**: Reverse the words: `["world", "hello"]`
- **Step 3**: Join them: `"world hello"`
- **Output**: `"world hello"`

#### Example 3:
- **Input**: `s = "a good   example"`
- **Step 1**: Split into words: `["a", "good", "example"]`
- **Step 2**: Reverse the words: `["example", "good", "a"]`
- **Step 3**: Join them: `"example good a"`
- **Output**: `"example good a"`

### Time Complexity:
- **O(n)**: Where `n` is the length of the string. Splitting the string, reversing the list, and joining the words each take linear time.

### Space Complexity:
- **O(n)**: We need extra space for storing the list of words and the resulting reversed string.

### Follow-up:
If the string's data type is mutable, solving it in-place would require reversing the string and then performing a word-by-word reversal while trimming excess spaces. However, Python strings are immutable, so we can't achieve this with O(1) extra space in Python.
