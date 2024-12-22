This problem can be solved by iterating through both strings, adding characters alternately to the result string. If one string is longer than the other, the remaining characters from the longer string are appended at the end.

Here’s the Python solution:

```python
def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0

    # Alternate characters from both words
    while i < len(word1) and j < len(word2):
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    # Append remaining characters from word1 (if any)
    while i < len(word1):
        merged.append(word1[i])
        i += 1

    # Append remaining characters from word2 (if any)
    while j < len(word2):
        merged.append(word2[j])
        j += 1

    return ''.join(merged)
```

### Explanation
1. **Two Pointers**: Use two pointers (`i` and `j`) to iterate through `word1` and `word2` respectively.
2. **Alternate Appending**: Add characters alternately to the `merged` list until one string is exhausted.
3. **Handle Remaining Characters**: Append the remaining characters from the longer string.
4. **Join List to String**: Use `''.join()` to convert the list to a single merged string.

### Complexity
- **Time Complexity**: \(O(n + m)\), where \(n\) and \(m\) are the lengths of `word1` and `word2`.
- **Space Complexity**: \(O(n + m)\), for the `merged` list.

### Example Runs
#### Example 1
```python
mergeAlternately("abc", "pqr")
# Output: "apbqcr"
```

#### Example 2
```python
mergeAlternately("ab", "pqrs")
# Output: "apbqrs"
```

#### Example 3
```python
mergeAlternately("abcd", "pq")
# Output: "apbqcd"
```
