To determine whether `s3` is an interleaving of `s1` and `s2`, we can use **Dynamic Programming (DP)** to build a solution. Let's break down the problem and the approach step-by-step:

### Problem Breakdown:

- `s1` and `s2` are two strings, and `s3` is formed by interleaving `s1` and `s2`.
- Interleaving means that the characters from `s1` and `s2` appear in `s3` in the same relative order as they appear in `s1` and `s2`.

  For example, for `s1 = "abc"` and `s2 = "def"`, the string `"adbcef"` is a valid interleaving of `s1` and `s2`.

- The key observation is that at each position in `s3`, the character must either come from `s1` or `s2`.

### Approach:

We use **Dynamic Programming** to solve this problem efficiently. Let `dp[i][j]` be a boolean value that represents whether the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i + j` characters of `s3`.

### Conditions:
- **Base Case**: If both `s1` and `s2` are empty (`i = 0` and `j = 0`), then `s3` must also be empty, and the answer is `True`.
- **Transitions**: For any `i` and `j`:
  - If the current character of `s3` matches the current character of `s1`, i.e., `s3[i+j-1] == s1[i-1]`, then we check if we can form the first `i-1` characters of `s1` and the first `j` characters of `s2` to match the first `i+j-1` characters of `s3`.
  - Similarly, if `s3[i+j-1] == s2[j-1]`, we check if we can form the first `i` characters of `s1` and the first `j-1` characters of `s2` to match the first `i+j-1` characters of `s3`.

### Steps:

1. **Initialization**:
   - Create a DP table `dp[i][j]` where `i` and `j` represent the number of characters considered from `s1` and `s2` respectively.
   - Set `dp[0][0]` to `True` because if both `s1` and `s2` are empty, `s3` must also be empty.

2. **Filling the DP Table**:
   - Loop through all possible lengths of substrings of `s1` and `s2`.
   - For each cell `dp[i][j]`, check if the character of `s3` matches either `s1[i-1]` or `s2[j-1]`, and update `dp[i][j]` accordingly.

3. **Final Answer**:
   - After filling the DP table, the value of `dp[len(s1)][len(s2)]` will tell us if `s3` can be formed by interleaving `s1` and `s2`.

### Code Implementation:

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # If the lengths don't match, we can return false right away
    if len(s1) + len(s2) != len(s3):
        return False

    # Initialize the DP table
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Base case: empty strings
    dp[0][0] = True

    # Fill the DP table
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # If current character of s3 matches s1
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            # If current character of s3 matches s2
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]

    # The final answer is in dp[len(s1)][len(s2)]
    return dp[len(s1)][len(s2)]
```

### Explanation of the Code:
1. **Base case**: `dp[0][0] = True`, meaning that an empty `s1` and `s2` can interleave to form an empty `s3`.
2. **Filling the DP table**:
   - For each `i` and `j`, check if the current character of `s3` matches the current character from `s1` or `s2`. If it does, propagate the result from previous states (`dp[i-1][j]` or `dp[i][j-1]`).
3. **Final result**: The value at `dp[len(s1)][len(s2)]` will tell us if we can interleave `s1` and `s2` to form `s3`.

### Time and Space Complexity:
- **Time Complexity**: `O(n * m)` where `n` is the length of `s1` and `m` is the length of `s2`. We compute the result for each pair `(i, j)` of indices.
- **Space Complexity**: `O(n * m)` for the DP table.

### Follow-up: Reduce Space Complexity

To reduce space complexity to `O(m)` (where `m` is the length of `s2`), we can use a **1D DP array** because at each step, we only need the current row and the previous row of the DP table. This optimization keeps the approach efficient without sacrificing the algorithm's correctness.

Here's an optimized version using a 1D DP array:

```python
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [False] * (len(s2) + 1)
    dp[0] = True

    # Initialize the first row (s1 = "")
    for j in range(1, len(s2) + 1):
        dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    # Iterate over s1 and fill the dp array
    for i in range(1, len(s1) + 1):
        dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[len(s2)]
```

- **Space Complexity**: `O(m)`, because we are using a 1D array to store results only for the current and previous states.

### Conclusion:
We can efficiently determine if `s3` is an interleaving of `s1` and `s2` using Dynamic Programming. We also showed how to optimize the space complexity to use only O(m) space.


This explanation is about how you use dynamic programming (DP) to check if a string `s3` can be formed by interleaving two other strings, `s1` and `s2`, while maintaining their original character order.

### Problem Context:
You want to check if it's possible to form the string `s3` by taking characters from `s1` and `s2` in such a way that:
1. The characters from `s1` appear in the same order as in `s1`.
2. The characters from `s2` appear in the same order as in `s2`.

The goal is to build a DP table where each entry `dp[i][j]` is `True` if the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i + j` characters of `s3`.

### Key Idea:
For each `i` and `j`, the current character in `s3` (at index `i + j - 1`) needs to match either:
- The current character in `s1` (at index `i-1`), or
- The current character in `s2` (at index `j-1`).

If this is true, the result (whether interleaving up to that point is possible) should "propagate" from a valid previous state.

### Steps:
1. **Check if the current character of `s3` matches the current character of `s1`:**
   - If `s3[i + j - 1] == s1[i - 1]`, this means that `s1[i - 1]` can be used to match the current character of `s3`.
   - In this case, whether this interleaving is valid depends on the previous state: the first `i-1` characters of `s1` and the first `j` characters of `s2` should have already formed the first `i + j - 1` characters of `s3`. This state is stored in `dp[i-1][j]`.

2. **Check if the current character of `s3` matches the current character of `s2`:**
   - Similarly, if `s3[i + j - 1] == s2[j - 1]`, this means that `s2[j - 1]` can be used to match the current character of `s3`.
   - Whether this is valid depends on the previous state: the first `i` characters of `s1` and the first `j-1` characters of `s2` should have already formed the first `i + j - 1` characters of `s3`. This state is stored in `dp[i][j-1]`.

### Propagation Logic:
At each point, you propagate the result from the previous valid states (either `dp[i-1][j]` or `dp[i][j-1]`) if a match occurs. This means:

- If `dp[i-1][j]` is `True`, then this means that the first `i-1` characters of `s1` and the first `j` characters of `s2` correctly interleave to form the first `i + j - 1` characters of `s3`. If `s1[i-1] == s3[i+j-1]`, then `dp[i][j]` should also be `True`.
- If `dp[i][j-1]` is `True`, then the first `i` characters of `s1` and the first `j-1` characters of `s2` correctly interleave to form the first `i + j - 1` characters of `s3`. If `s2[j-1] == s3[i+j-1]`, then `dp[i][j]` should be `True`.

This propagation ensures that if the previous state (`dp[i-1][j]` or `dp[i][j-1]`) is valid, the current state (`dp[i][j]`) is also valid as long as the current character in `s3` matches the current character in `s1` or `s2`.

### Example:
Suppose:

- `s1 = "abc"`,
- `s2 = "def"`, and
- `s3 = "adbcef"`.

We will fill out the DP table like this:

- `dp[0][0]` is `True` because an empty `s1` and `s2` form an empty `s3`.
- For each `i` and `j`, you check if `s3[i+j-1]` matches `s1[i-1]` or `s2[j-1]` and propagate from either `dp[i-1][j]` or `dp[i][j-1]`.

By the end, `dp[len(s1)][len(s2)]` will tell you if the entire `s3` can be formed by interleaving `s1` and `s2`.

### Conclusion:
The idea is to use dynamic programming to store previous results, and at each step, check whether the current character in `s3` matches characters in `s1` or `s2`. If it does, and the previous state was valid, then the current state is valid, and we propagate this result forward.


This code is an implementation of dynamic programming (DP) to solve the problem of checking if a string `s3` can be formed by interleaving two strings `s1` and `s2`. The approach uses a one-dimensional DP array to optimize space complexity.

Let’s break it down step by step.

### Problem Recap:
We are trying to determine if `s3` can be formed by interleaving the characters of `s1` and `s2` while preserving the relative order of characters in `s1` and `s2`.

### Key Idea:
The solution uses dynamic programming to keep track of whether a substring of `s1` and `s2` can form a substring of `s3` up to a given point.

### DP Array:
Instead of using a 2D DP table, which would require `len(s1) + 1` rows and `len(s2) + 1` columns, this code uses a 1D DP array (`dp[j]`) where `j` ranges over the length of `s2`. It reduces space complexity from `O(m * n)` to `O(n)`, where `m = len(s1)` and `n = len(s2)`.

#### Initialize the DP Array:
```python
for j in range(1, len(s2) + 1):
    dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
```

1. **Purpose**: This loop initializes the `dp` array for the case when `s1` is empty (`i == 0`), meaning we are checking whether `s3` is formed entirely by characters from `s2` up to index `j`.
2. **Logic**: `dp[j]` is `True` if `dp[j - 1]` is `True` and the current character of `s2[j - 1]` matches the corresponding character in `s3[j - 1]`.
   - This checks if the first `j` characters of `s2` match the first `j` characters of `s3` when `s1` is not involved.
   - This is essentially initializing the first row of the 2D DP matrix for the case where `s1` is empty.

#### Iterate Over `s1` and Update `dp`:
```python
for i in range(1, len(s1) + 1):
    dp[0] = dp[0] and s1[i - 1] == s3[i - 1]  # Handles the case when s2 is empty
    for j in range(1, len(s2) + 1):
        dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
```

- **First Line (`dp[0]`)**: This handles the case when `s2` is empty (`j == 0`), meaning we are checking whether `s3` is formed entirely by characters from `s1` up to index `i`.
   - If `dp[0]` was `True` before, and the current character of `s1[i - 1]` matches `s3[i - 1]`, then `dp[0]` remains `True`.
   - This is equivalent to initializing the first column of the 2D DP matrix.

- **Inner Loop** (`for j in range(1, len(s2) + 1)`):
   - This loop updates the `dp` array for each combination of `i` (from `s1`) and `j` (from `s2`), checking whether the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i + j` characters of `s3`.
   - **Key Transition**:
     ```python
     dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
     ```

     This line updates `dp[j]` based on two cases:
     1. **From `s1`**: If the previous state `dp[j]` was `True` (which means that the first `i-1` characters of `s1` and the first `j` characters of `s2` can form the first `i + j - 1` characters of `s3`), and the current character of `s1[i - 1]` matches `s3[i + j - 1]`, then `dp[j]` remains `True`.
     2. **From `s2`**: If the previous state `dp[j - 1]` was `True` (which means that the first `i` characters of `s1` and the first `j-1` characters of `s2` can form the first `i + j - 1` characters of `s3`), and the current character of `s2[j - 1]` matches `s3[i + j - 1]`, then `dp[j]` becomes `True`.

   - In essence, the logic checks whether the current character of `s3` can be formed by taking the current character from either `s1` or `s2`.

### Summary:
- **Outer loop (`i`)**: Iterates over the characters of `s1`.
- **Inner loop (`j`)**: Iterates over the characters of `s2`.
- **State transition**: The current `dp[j]` is updated based on whether the current character of `s3` can be matched by either the current character of `s1` or `s2`, and whether the previous state (`dp[j]` or `dp[j-1]`) was `True`.

By the end of the iteration, the last element of the `dp` array (`dp[len(s2)]`) will tell you whether `s3` can be formed by interleaving `s1` and `s2`.

### Example:
Let’s say:
- `s1 = "abc"`
- `s2 = "def"`
- `s3 = "adbcef"`

The DP array will update to reflect whether parts of `s1` and `s2` can form parts of `s3` as you iterate over the strings. If the last value in `dp` is `True`, it means `s3` is a valid interleaving of `s1` and `s2`.


Memoization is an optimization technique used primarily in dynamic programming to improve the performance of algorithms by storing the results of expensive function calls and reusing them when the same inputs occur again. Instead of recalculating the result every time the function is called with the same arguments, memoization allows you to look up the result in a cache or a lookup table, saving time and computation.

### Key Concepts of Memoization:
1. **Store Results (Cache)**: Whenever a function computes a result for a specific input, the result is stored (or "memoized") in a cache, typically a dictionary or an array.
2. **Reuse Results**: If the function is called again with the same input, the result is retrieved from the cache instead of recalculating it.
3. **Avoid Redundant Computations**: This technique helps avoid repeated work, especially in problems that involve overlapping subproblems (such as recursive solutions to Fibonacci numbers, dynamic programming, etc.).

### Example:
Memoization is commonly used to optimize recursive algorithms, like computing Fibonacci numbers. Without memoization, a recursive Fibonacci function might repeat the same calculation many times.

#### Naive Recursive Fibonacci:
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```
Without memoization, this recursive function recalculates `fib(n-1)` and `fib(n-2)` multiple times, leading to an exponential time complexity (`O(2^n)`).

#### Optimized Fibonacci with Memoization:
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]  # Return the cached result
    if n <= 1:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)  # Store the result in the cache
    return memo[n]
```
In this version:
- We use a dictionary `memo` to store results for each `n`.
- If `fib(n)` has been calculated before, we return the cached result.
- This reduces the time complexity to `O(n)` because each Fibonacci number is calculated only once.

### Characteristics of Memoization:
- **Top-Down Approach**: Memoization is typically used in a top-down approach where you start with the main problem and break it down into smaller subproblems recursively.
- **Recursive Functions**: It is often used with recursive functions that have overlapping subproblems.
- **Space Complexity**: Since memoization stores intermediate results, it can increase the space complexity depending on how many unique subproblems need to be stored.

### Use Cases:
- **Fibonacci Sequence**
- **Dynamic Programming Problems**: Knapsack problem, coin change problem, etc.
- **Graph Algorithms**: Shortest paths, longest paths, etc.
- **String Matching Problems**: Longest common subsequence, edit distance, etc.

Memoization is a powerful tool when used in problems with overlapping subproblems, as it significantly reduces redundant calculations and enhances performance.
