### **Optimal Solution: Counting Patterns**

We need to select **3 buildings** such that:
- No two consecutive buildings have the same type.
- Types are represented as:
  - `'0'`: Office
  - `'1'`: Restaurant

---

### **Observations**

1. The valid patterns for the 3 selected buildings are:
   - **"010"** → Office, Restaurant, Office
   - **"101"** → Restaurant, Office, Restaurant

2. To form these patterns:
   - We need to count:
     - Number of `0`s before and after each `1`
     - Number of `1`s before and after each `0`

---

### **Approach**

1. **Precompute Counts:**
   - `count_0_before[i]`: Number of `0`s before index `i`.
   - `count_1_before[i]`: Number of `1`s before index `i`.
   - `count_0_after[i]`: Number of `0`s after index `i`.
   - `count_1_after[i]`: Number of `1`s after index `i`.

2. **Calculate Valid Combinations:**
   - For every `1` at index `i`:
     - Count `"010"` patterns as: `count_0_before[i] * count_0_after[i]`
   - For every `0` at index `i`:
     - Count `"101"` patterns as: `count_1_before[i] * count_1_after[i]`

3. **Sum All Valid Patterns:**
   - Add up all the valid combinations.

---

### **Complexity Analysis**
- **Time Complexity:** \( O(N) \)
  - One pass to compute counts.
  - Another pass to calculate valid combinations.
- **Space Complexity:** \( O(N) \)
  - For storing counts.

---

### **Python Code Implementation**

```python
def numberOfWays(s: str) -> int:
    n = len(s)

    # Precompute counts
    count_0_before = [0] * n
    count_1_before = [0] * n
    count_0_after = [0] * n
    count_1_after = [0] * n

    # Calculate count before
    for i in range(1, n):
        count_0_before[i] = count_0_before[i-1] + (s[i-1] == '0')
        count_1_before[i] = count_1_before[i-1] + (s[i-1] == '1')

    # Calculate count after
    for i in range(n-2, -1, -1):
        count_0_after[i] = count_0_after[i+1] + (s[i+1] == '0')
        count_1_after[i] = count_1_after[i+1] + (s[i+1] == '1')

    # Calculate total ways
    total_ways = 0

    for i in range(n):
        if s[i] == '1':  # Count "010" pattern
            total_ways += count_0_before[i] * count_0_after[i]
        if s[i] == '0':  # Count "101" pattern
            total_ways += count_1_before[i] * count_1_after[i]

    return total_ways
```

---

### **Example Walkthrough**

#### **Example 1**
```python
s = "001101"
print(numberOfWays(s))  # Output: 6
```
- Valid patterns:
  - `[0,2,4]` → `"010"`
  - `[0,3,4]` → `"010"`
  - `[1,2,4]` → `"010"`
  - `[1,3,4]` → `"010"`
  - `[2,4,5]` → `"101"`
  - `[3,4,5]` → `"101"`
- Total: `6` ways

---

#### **Example 2**
```python
s = "11100"
print(numberOfWays(s))  # Output: 0
```
- No valid patterns found.
- Output: `0`

---

### **Why This Solution is Efficient**
- The solution precomputes counts efficiently using prefix and suffix arrays.
- This allows the main logic to run in linear time, avoiding nested loops.

This approach is optimized for the constraint of \( 10^5 \) length strings, ensuring both time and space efficiency. 🚀

In this solution, the multiplication in the lines below counts the number of specific patterns ("010" and "101") in the string:

```python
if s[i] == '1':  # Count "010" pattern
    total_ways += count_0_before[i] * count_0_after[i]
if s[i] == '0':  # Count "101" pattern
    total_ways += count_1_before[i] * count_1_after[i]
```

---

### **How the Multiplication Works**

1. **When `s[i]` is '1'**:
   - We're looking for the pattern **"010"**.
     - The `1` is at position `i`.
     - We need a `0` **before** and a `0` **after** it.

   - `count_0_before[i]` → Number of `0`s that appear **before** index `i`.
   - `count_0_after[i]` → Number of `0`s that appear **after** index `i`.

   - To form "010", we can pair each `0` before `i` with each `0` after `i`.
     - Therefore, the total number of ways to form this pattern with `1` at position `i` is:
       \[
       \text{Number of ways} = \text{count_0_before[i]} \times \text{count_0_after[i]}
       \]
     - This is because each `0` before can pair with any `0` after to form "010".

---

2. **When `s[i]` is '0'**:
   - We're looking for the pattern **"101"**.
     - The `0` is at position `i`.
     - We need a `1` **before** and a `1` **after** it.

   - `count_1_before[i]` → Number of `1`s that appear **before** index `i`.
   - `count_1_after[i]` → Number of `1`s that appear **after** index `i`.

   - To form "101", we can pair each `1` before `i` with each `1` after `i`.
     - Therefore, the total number of ways to form this pattern with `0` at position `i` is:
       \[
       \text{Number of ways} = \text{count_1_before[i]} \times \text{count_1_after[i]}
       \]
     - This is because each `1` before can pair with any `1` after to form "101".

---

### **Example for Better Understanding**

Consider the input:
```python
s = "01010"
```

- Precomputed counts:
    ```
    count_0_before = [0, 1, 1, 2, 2]
    count_1_before = [0, 0, 1, 1, 2]
    count_0_after  = [2, 1, 1, 0, 0]
    count_1_after  = [2, 2, 1, 1, 0]
    ```

- For `i = 2`, `s[i] = '1'`:
  - Looking for **"010"** pattern.
  - `count_0_before[2] = 1` (one `0` before index 2)
  - `count_0_after[2] = 1` (one `0` after index 2)
  - Number of "010" patterns with `1` at index 2:
    \[
    \text{Ways} = 1 \times 1 = 1
    \]

- For `i = 1`, `s[i] = '0'`:
  - Looking for **"101"** pattern.
  - `count_1_before[1] = 0` (no `1` before index 1)
  - `count_1_after[1] = 2` (two `1`s after index 1)
  - Number of "101" patterns with `0` at index 1:
    \[
    \text{Ways} = 0 \times 2 = 0
    \]

---

### **Why Multiplication Works Efficiently**
- Multiplication effectively pairs all possible combinations:
  - Any `0` before with any `0` after to form "010".
  - Any `1` before with any `1` after to form "101".
- This avoids nested loops and provides an efficient **O(n)** solution.


Let's go through another example to see how the multiplication works!

---

### Example Input:
```python
s = "10101"
```

### Step 1: Precompute Counts
1. **`count_0_before`** → Number of `0`s before each index.
2. **`count_1_before`** → Number of `1`s before each index.
3. **`count_0_after`** → Number of `0`s after each index.
4. **`count_1_after`** → Number of `1`s after each index.

After processing the string, the arrays look like this:

```
index:            0  1  2  3  4
s:                1  0  1  0  1

count_0_before = [0, 0, 1, 1, 2]
count_1_before = [0, 1, 1, 2, 2]

count_0_after  = [2, 1, 1, 0, 0]
count_1_after  = [2, 2, 1, 1, 0]
```

---

### Step 2: Calculate Patterns

We look at each character and calculate the possible patterns:

1. **`i = 0`, `s[0] = '1'`**:
    - Looking for **"010"** pattern:
      - `count_0_before[0] = 0` (No `0` before index 0)
      - `count_0_after[0] = 2` (Two `0`s after index 0)
      - Number of "010" patterns:
        \[
        \text{Ways} = 0 \times 2 = 0
        \]

---

2. **`i = 1`, `s[1] = '0'`**:
    - Looking for **"101"** pattern:
      - `count_1_before[1] = 1` (One `1` before index 1)
      - `count_1_after[1] = 2` (Two `1`s after index 1)
      - Number of "101" patterns:
        \[
        \text{Ways} = 1 \times 2 = 2
        \]
      - These patterns are:
        - "101" with indices `[0, 1, 2]`
        - "101" with indices `[0, 1, 4]`

---

3. **`i = 2`, `s[2] = '1'`**:
    - Looking for **"010"** pattern:
      - `count_0_before[2] = 1` (One `0` before index 2)
      - `count_0_after[2] = 1` (One `0` after index 2)
      - Number of "010" patterns:
        \[
        \text{Ways} = 1 \times 1 = 1
        \]
      - This pattern is:
        - "010" with indices `[1, 2, 3]`

---

4. **`i = 3`, `s[3] = '0'`**:
    - Looking for **"101"** pattern:
      - `count_1_before[3] = 2` (Two `1`s before index 3)
      - `count_1_after[3] = 1` (One `1` after index 3)
      - Number of "101" patterns:
        \[
        \text{Ways} = 2 \times 1 = 2
        \]
      - These patterns are:
        - "101" with indices `[0, 3, 4]`
        - "101" with indices `[2, 3, 4]`

---

5. **`i = 4`, `s[4] = '1'`**:
    - Looking for **"010"** pattern:
      - `count_0_before[4] = 2` (Two `0`s before index 4)
      - `count_0_after[4] = 0` (No `0` after index 4)
      - Number of "010" patterns:
        \[
        \text{Ways} = 2 \times 0 = 0
        \]

---

### Step 3: Total Count
Adding all the patterns:
- At `i=0`: `0`
- At `i=1`: `2`
- At `i=2`: `1`
- At `i=3`: `2`
- At `i=4`: `0`

\[
\text{Total Ways} = 0 + 2 + 1 + 2 + 0 = 5
\]

---

### **Summary of Patterns Found:**
- "101" at indices `[0, 1, 2]`
- "101" at indices `[0, 1, 4]`
- "010" at indices `[1, 2, 3]`
- "101" at indices `[0, 3, 4]`
- "101" at indices `[2, 3, 4]`

---

### **Why Multiplication Works Efficiently:**
- Multiplication efficiently pairs all combinations:
  - `count_0_before[i]` represents the number of choices for the first `0` in "010".
  - `count_0_after[i]` represents the number of choices for the second `0` in "010".
  - Similarly for "101".
- This avoids nested loops and achieves an **O(n)** complexity, making the solution efficient.

This problem is classified as a **"Prefix Sum / Precomputation"** problem on LeetCode.

### Why?
- It involves **precomputing counts** (`count_0_before`, `count_1_before`, `count_0_after`, `count_1_after`) to efficiently calculate the number of patterns without redundant calculations.
- It uses a technique similar to **prefix sums** to maintain cumulative counts, which is a common pattern in problems involving subarrays, substrings, or sequences.

### Other Related Categories:
- **Array**: It manipulates arrays to store cumulative counts.
- **String**: It deals with patterns within a string.
- **Dynamic Programming (DP)**: Although it doesn't use typical DP states, the precomputed arrays can be viewed as a form of memoization for subproblems.
- **Combinatorics**: The multiplication of counts pairs combinations of indices efficiently.
