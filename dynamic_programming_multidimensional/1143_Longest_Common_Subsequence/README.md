To solve this problem, we can use **Dynamic Programming (DP)**. The goal is to compute the length of the **Longest Common Subsequence (LCS)** between two strings, `text1` and `text2`.

---

### Approach:

1. **Define DP State**:
   - Let `dp[i][j]` represent the length of the LCS of the substrings `text1[0:i]` and `text2[0:j]` (both substrings are inclusive of their respective indices).

2. **Base Case**:
   - If either string is empty, the LCS length is `0`, so:
     - `dp[i][0] = 0` for all `i` (when `text2` is empty).
     - `dp[0][j] = 0` for all `j` (when `text1` is empty).

3. **Transition**:
   - If the characters match (`text1[i-1] == text2[j-1]`), then the LCS includes this character:
     - `dp[i][j] = dp[i-1][j-1] + 1`
   - If the characters do not match, we take the maximum LCS length by excluding one character from either `text1` or `text2`:
     - `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

4. **Result**:
   - The length of the LCS is stored in `dp[m][n]`, where `m = len(text1)` and `n = len(text2)`.

5. **Optimization (Space)**:
   - Since we only depend on the current row and the previous row in the DP table, we can reduce the space complexity to \( O(n) \) using a rolling array.

---

### Implementation (Python):

```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    # Initialize a 2-row DP table to save space
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

    return dp[m % 2][n]
```

---

### Example Walkthrough:

#### Example 1:
Input: `text1 = "abcde"`, `text2 = "ace"`
1. Initialize `dp` table with dimensions \((6 \times 4)\).
2. Fill the table using the rules:
   - When characters match (`text1[i-1] == text2[j-1]`), increment.
   - Otherwise, take the max of the previous results.
3. Final `dp` table:
   ```
   [[0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 2],
    [0, 1, 2, 2],
    [0, 1, 2, 3]]
   ```
4. Result: `dp[5][3] = 3`

Output: `3`

---

### Complexity Analysis:
1. **Time Complexity**:
   - Filling the DP table requires \( O(m \times n) \) operations, where \( m = \text{len(text1)} \) and \( n = \text{len(text2)} \).

2. **Space Complexity**:
   - The space complexity is \( O(n) \) since we only store two rows of the DP table at a time.

---

### Example Outputs:

```python
print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))   # Output: 3
print(longestCommonSubsequence("abc", "def"))   # Output: 0
```

If we want to use just **one row** for space optimization, we can further reduce the space complexity to \(O(n)\) without keeping two rows. The key idea is to update the current row in reverse order to ensure previous values are not overwritten before they are used.

---

### Optimized Single-Row Implementation:

```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    # Use a single row for DP
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        prev = 0  # This stores dp[i-1][j-1] for the current iteration
        for j in range(1, n + 1):
            temp = dp[j]  # Store the current dp[j] to use in the next iteration
            if text1[i - 1] == text2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp  # Update prev to the current dp[j]

    return dp[n]
```

---

### Explanation:

1. **State Variables**:
   - `dp[j]`: Represents the LCS length for `text1[0:i]` and `text2[0:j]`.
   - `prev`: Keeps track of the diagonal (previous row's value) in the DP table, which is `dp[i-1][j-1]`.

2. **How It Works**:
   - For every character in `text1` (`i` loop), update the `dp` array for every character in `text2` (`j` loop).
   - `prev` saves the diagonal value from the previous iteration, which represents `dp[i-1][j-1]` when calculating the current cell.

3. **Key Optimization**:
   - By iterating from left to right in the `j` loop and storing intermediate values in `prev`, we avoid the need for a second row.

---

### Example Walkthrough:

#### Example 1:
Input: `text1 = "abcde"`, `text2 = "ace"`

1. Initial `dp` array:
   ```
   [0, 0, 0, 0]
   ```

2. Iteration for `text1[0] = 'a'`:
   - Update `dp` for `text2[0:3] = 'ace'`:
     ```
     [0, 1, 1, 1]
     ```

3. Iteration for `text1[1] = 'b'`:
   ```
   [0, 1, 1, 1]
   ```

4. Iteration for `text1[2] = 'c'`:
   ```
   [0, 1, 2, 2]
   ```

5. Iteration for `text1[3] = 'd'`:
   ```
   [0, 1, 2, 2]
   ```

6. Iteration for `text1[4] = 'e'`:
   ```
   [0, 1, 2, 3]
   ```

Result: `dp[3] = 3`

---

### Complexity:

1. **Time Complexity**:
   - \(O(m \times n)\), as we iterate through both strings.

2. **Space Complexity**:
   - \(O(n)\), as only a single row of size \(n+1\) is used.

---

### Example Outputs:

```python
print(longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(longestCommonSubsequence("abc", "abc"))   # Output: 3
print(longestCommonSubsequence("abc", "def"))   # Output: 0
```
