To solve the problem of determining if a string `s` follows the same pattern as a given `pattern`, we can use two hash maps (or dictionaries in Python). One map will store the mapping from characters in the pattern to words in the string, and the other map will store the mapping from words in the string to characters in the pattern. The idea is to ensure that each character in the pattern maps uniquely to a word in the string and vice versa.

Here's a Python solution:

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for p, w in zip(pattern, words):
            if p in char_to_word:
                if char_to_word[p] != w:
                    return False
            else:
                if w in word_to_char:
                    if word_to_char[w] != p:
                        return False
                char_to_word[p] = w
                word_to_char[w] = p

        return True
```

### Explanation:
1. **Split the String**: We first split the string `s` by spaces to get the list of words.
2. **Check Lengths**: If the length of the pattern and the number of words are different, return `False` immediately because they can't follow the same pattern.
3. **Mapping Process**:
    - We iterate over the characters in the pattern and the words simultaneously.
    - We check if the current character is already mapped to a word:
        - If it is, we ensure that it maps to the current word.
        - If it doesn't match, we return `False`.
    - Similarly, we check if the current word is already mapped to a character:
        - If it is, we ensure that it maps to the current character.
        - If it doesn't match, we return `False`.
    - If no conflicts are found, we establish the new mappings.
4. **Final Check**: If we successfully iterate through the entire pattern and string without returning `False`, it means the string follows the pattern, and we return `True`.

### Example Usage:

```python
solution = Solution()

# Test cases
print(solution.wordPattern("abba", "dog cat cat dog"))  # Output: True
print(solution.wordPattern("abba", "dog cat cat fish"))  # Output: False
print(solution.wordPattern("aaaa", "dog cat cat dog"))  # Output: False
print(solution.wordPattern("abba", "dog dog dog dog"))  # Output: False
```

This approach ensures that the mapping is bijective, meaning each character in the pattern corresponds to exactly one word in the string and vice versa. The time complexity of this solution is O(n), where n is the number of characters in the pattern or words in the string, which is efficient for the input constraints provided.
