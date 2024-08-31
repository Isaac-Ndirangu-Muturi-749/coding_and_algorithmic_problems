To determine if two strings `s` and `t` are isomorphic, we can use a mapping approach where we map characters from `s` to `t` and ensure that the mapping is consistent throughout the strings. Here’s how you can approach the problem:

### Algorithm:
1. **Create two dictionaries**:
   - `map_s_to_t`: maps characters from `s` to `t`.
   - `map_t_to_s`: maps characters from `t` to `s`.

2. **Iterate through both strings**:
   - For each character in `s` and its corresponding character in `t`, check if:
     - The character from `s` is already mapped to a different character in `t` (using `map_s_to_t`).
     - The character from `t` is already mapped to a different character in `s` (using `map_t_to_s`).
   - If either of these mappings is inconsistent, return `False`.
   - Otherwise, establish the mapping between the characters in both directions.

3. **Return `True`** at the end if all characters map correctly.

### Code Implementation:

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s

        return True
```

### Explanation with Examples:

1. **Example 1:**
   - `s = "egg"`, `t = "add"`
   - Mapping:
     - `e` -> `a`
     - `g` -> `d`
   - Since the mappings are consistent throughout the strings, the function returns `True`.

2. **Example 2:**
   - `s = "foo"`, `t = "bar"`
   - Mapping:
     - `f` -> `b`
     - `o` -> `a` (initially), but the next `o` would need to map to `r`, which is inconsistent.
   - The function returns `False`.

3. **Example 3:**
   - `s = "paper"`, `t = "title"`
   - Mapping:
     - `p` -> `t`
     - `a` -> `i`
     - `p` -> `t` (which is consistent with the earlier mapping)
     - `e` -> `l`
     - `r` -> `e`
   - The function returns `True`.

### Constraints:
- The strings `s` and `t` are guaranteed to be of the same length, and they consist of valid ASCII characters.
- The length of the strings can go up to `5 * 10^4`, so the solution needs to be efficient. The above approach works in `O(n)` time complexity, where `n` is the length of the strings.

### Test Cases:
You can now create a test script similar to the one used in your previous questions to validate the `isIsomorphic` method. Here’s a simple example:

```python
def run_tests():
    solution = Solution()

    assert solution.isIsomorphic("egg", "add") == True, "Test case 1 failed"
    assert solution.isIsomorphic("foo", "bar") == False, "Test case 2 failed"
    assert solution.isIsomorphic("paper", "title") == True, "Test case 3 failed"
    assert solution.isIsomorphic("abc", "xyz") == True, "Test case 4 failed"
    assert solution.isIsomorphic("ab", "aa") == False, "Test case 5 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
```

This will test the `isIsomorphic` function with various scenarios, ensuring it behaves correctly.
