To solve the problem efficiently in \( O(n) \), we can use **dynamic programming** based on a relationship between the number of 1's in the binary representation of a number and the numbers smaller than it.

---

### **Approach**
#### Key Observation:
The number of 1's in the binary representation of \( i \) can be derived from \( i // 2 \) (or \( i \gg 1 \), which is \( i \) shifted right by 1 bit):
- If \( i \) is even, the number of 1's in \( i \) is the same as \( i // 2 \) (because the last bit is 0).
- If \( i \) is odd, the number of 1's in \( i \) is one more than \( i // 2 \) (because the last bit is 1).

This leads to the recurrence relation:
\[
\text{ans}[i] = \text{ans}[i \gg 1] + (i \& 1)
\]
Where:
- \( i \gg 1 \): The number \( i \) divided by 2 (integer division).
- \( i \& 1 \): Checks if the last bit of \( i \) is 1.

---

### **Algorithm**
1. Initialize an array `ans` of size \( n+1 \) with all zeros.
2. Iterate from \( i = 1 \) to \( n \), using the recurrence relation to compute \( \text{ans}[i] \).
3. Return the array `ans`.

---

### **Implementation**

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array
        ans = [0] * (n + 1)

        # Compute the number of 1's for each number
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Use the recurrence relation

        return ans
```

---

### **Explanation with Examples**
#### Example 1:
Input:
```plaintext
n = 2
```

Steps:
1. Initialize `ans = [0, 0, 0]`.
2. For \( i = 1 \):
   - \( \text{ans}[1] = \text{ans}[1 \gg 1] + (1 \& 1) = \text{ans}[0] + 1 = 0 + 1 = 1 \).
3. For \( i = 2 \):
   - \( \text{ans}[2] = \text{ans}[2 \gg 1] + (2 \& 1) = \text{ans}[1] + 0 = 1 + 0 = 1 \).

Output:
```plaintext
[0, 1, 1]
```

#### Example 2:
Input:
```plaintext
n = 5
```

Steps:
1. Initialize `ans = [0, 0, 0, 0, 0, 0]`.
2. Compute iteratively:
   - \( \text{ans}[1] = \text{ans}[0] + 1 = 1 \).
   - \( \text{ans}[2] = \text{ans}[1] + 0 = 1 \).
   - \( \text{ans}[3] = \text{ans}[1] + 1 = 2 \).
   - \( \text{ans}[4] = \text{ans}[2] + 0 = 1 \).
   - \( \text{ans}[5] = \text{ans}[2] + 1 = 2 \).

Output:
```plaintext
[0, 1, 1, 2, 1, 2]
```

---

### **Complexity Analysis**
1. **Time Complexity**: \( O(n) \)
   - We iterate through numbers from 1 to \( n \), performing \( O(1) \) work for each.
2. **Space Complexity**: \( O(n) \)
   - The result array `ans` of size \( n+1 \) is used.

---

### **Follow-Up: Single Pass**
The provided solution already works in a single pass using \( O(n) \) time and space, and does not rely on built-in functions like `__builtin_popcount`.


An \( O(n \log n) \) solution to this problem can be implemented by computing the number of 1's in the binary representation of each number using repeated division by 2 (or bit manipulation). For each number \( i \), count the set bits (1's) by dividing it by 2 repeatedly and checking if the remainder is 1. This approach uses \( O(\log i) \) for each \( i \), resulting in a total time complexity of \( O(n \log n) \).

---

### **Approach**
#### Key Idea:
1. To count the number of 1's in \( i \), repeatedly divide \( i \) by 2 and count how many times the remainder is 1.
2. Use a loop to do this for all integers from 0 to \( n \).

---

### **Algorithm**
1. Create a result array `ans` of size \( n+1 \), initialized to 0.
2. For each number \( i \) from 0 to \( n \):
   - Initialize a temporary variable \( x = i \).
   - While \( x > 0 \):
     - Add \( x \% 2 \) to the count (it will be 1 if the last bit is 1).
     - Update \( x \) to \( x // 2 \) (integer division by 2).
   - Store the count in `ans[i]`.

---

### **Implementation**

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array
        ans = [0] * (n + 1)

        # Compute the number of 1's for each number
        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                count += x % 2  # Check if the last bit is 1
                x //= 2         # Divide by 2
            ans[i] = count

        return ans
```

---

### **Explanation with Examples**
#### Example 1:
Input:
```plaintext
n = 2
```

Steps:
1. \( i = 0 \): Binary = `0`, count = 0.
2. \( i = 1 \): Binary = `1`, count = 1.
3. \( i = 2 \): Binary = `10`, count = 1.

Output:
```plaintext
[0, 1, 1]
```

#### Example 2:
Input:
```plaintext
n = 5
```

Steps:
1. \( i = 0 \): Binary = `0`, count = 0.
2. \( i = 1 \): Binary = `1`, count = 1.
3. \( i = 2 \): Binary = `10`, count = 1.
4. \( i = 3 \): Binary = `11`, count = 2.
5. \( i = 4 \): Binary = `100`, count = 1.
6. \( i = 5 \): Binary = `101`, count = 2.

Output:
```plaintext
[0, 1, 1, 2, 1, 2]
```

---

### **Complexity Analysis**
1. **Time Complexity**: \( O(n \log n) \)
   - For each number \( i \), the binary representation has at most \( \log i \) bits. Thus, it takes \( O(\log i) \) to compute the number of 1's. Summing this across all numbers up to \( n \) gives \( O(n \log n) \).
2. **Space Complexity**: \( O(n) \)
   - The result array `ans` of size \( n+1 \) is used.

---

### **Comparison with \( O(n) \) Solution**
The \( O(n \log n) \) solution is less efficient than the \( O(n) \) dynamic programming solution because it repeatedly recomputes the number of 1's for each number instead of leveraging previously computed results.
