To solve this problem, we can use the **two-pointer sliding window approach** or directly make use of Python's built-in string operations to efficiently find the first occurrence of `needle` in `haystack`.

### Approach:
1. **Sliding Window**: We'll use two pointers to slide over the `haystack` string and compare the substring of length equal to `needle` with `needle`.
2. **Edge Cases**:
   - If the `needle` is an empty string, we should return 0 (as per convention).
   - If the length of `needle` is greater than `haystack`, return -1 because `needle` can't possibly be in `haystack`.

### Algorithm:
1. Loop through the `haystack` with a pointer `i` that goes from `0` to `len(haystack) - len(needle)`.
2. In each iteration, check if the substring starting at `i` with length equal to `needle` matches `needle`.
3. If a match is found, return `i` (the index of the first occurrence).
4. If no match is found after completing the loop, return -1.

### Code Implementation:

```python
def strStr(haystack: str, needle: str) -> int:
    # Edge case: if needle is an empty string, return 0
    if not needle:
        return 0

    # Get the lengths of both strings
    haystack_len = len(haystack)
    needle_len = len(needle)

    # Loop through the haystack and check for needle's first occurrence
    for i in range(haystack_len - needle_len + 1):
        # If the substring of haystack from i to i + needle_len matches the needle, return i
        if haystack[i:i + needle_len] == needle:
            return i

    # If no match is found, return -1
    return -1
```

### Explanation:
1. **Edge Case**: If `needle` is an empty string, it returns 0 by default.
2. **Sliding Window**: The for-loop checks every substring of length equal to `needle` in `haystack`. The loop runs from `0` to `len(haystack) - len(needle)` to ensure that we do not check past the length of `haystack`.
3. **Return the index**: As soon as a match is found, the index `i` is returned.
4. **If no match**: If the loop completes without finding a match, return -1.

### Example Walkthrough:

#### Example 1:
```plaintext
Input: haystack = "sadbutsad", needle = "sad"

Steps:
- Check substring "sad" starting at index 0 → Match found.
- Return 0.
```

#### Example 2:
```plaintext
Input: haystack = "leetcode", needle = "leeto"

Steps:
- Check "leetc" at index 0 → No match.
- Check "eetco" at index 1 → No match.
- Continue sliding the window...
- No match is found, return -1.
```

### Time and Space Complexity:

- **Time Complexity**: O(n * m), where `n` is the length of `haystack` and `m` is the length of `needle`. In the worst case, the algorithm compares `needle` with all substrings of `haystack` of the same length.
- **Space Complexity**: O(1) as we are not using any extra space apart from variables for tracking indices.

This approach should work efficiently for the given input constraints.
