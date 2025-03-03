### **Naive Approach (O(n))**
A simple way to solve this problem is to iterate through all numbers from `1` to `n` and check if they are factors of `n`. We then store them in a list and return the `k`-th factor.

#### **Implementation**
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:  # Stop early if we reach the k-th factor
                    return i
        return -1  # If there are fewer than k factors
```

#### **Complexity Analysis**
- We iterate from `1` to `n`, checking for factors → **O(n)**.
- Space complexity is **O(1)** (since we return early when `k` factors are found).

---

### **Optimized Approach (O(√n))**
Instead of iterating up to `n`, we observe that factors come in **pairs**:
- If `i` is a factor of `n`, then `n // i` is also a factor.
- This allows us to iterate **only up to √n** and collect factor pairs.

#### **Implementation**
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        sqrt_n = int(n ** 0.5)

        # Find factors up to sqrt(n) and store them
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # Avoid duplicate factors for perfect squares
                    factors.append(n // i)

        factors.sort()  # Sorting ensures ascending order
        return factors[k - 1] if k <= len(factors) else -1
```

#### **Complexity Analysis**
- Iterating up to `√n` → **O(√n)**
- Sorting the factors → **O(√n log(√n))** (but `log(√n)` is negligible for small values)
- Overall, the complexity is **O(√n)**.

---

### **Optimized Approach Without Sorting (O(√n))**
Instead of sorting the factors explicitly, we can collect them in **two passes**:
1. Find the first `k` factors directly.
2. If needed, find factors in descending order.

#### **Implementation**
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        sqrt_n = int(n ** 0.5)

        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i

        for i in range(sqrt_n, 0, -1):
            if n % i == 0 and i != n // i:
                count += 1
                if count == k:
                    return n // i

        return -1
```

#### **Complexity Analysis**
- **First loop:** Iterates up to `√n` → **O(√n)**
- **Second loop:** Iterates up to `√n` → **O(√n)**
- **Total Complexity:** **O(√n)**, avoiding sorting overhead.

---

### **Example Walkthrough**
#### **Example 1**
```python
n = 12, k = 3
Factors: [1, 2, 3, 4, 6, 12]
Output: 3
```

#### **Example 2**
```python
n = 7, k = 2
Factors: [1, 7]
Output: 7
```

#### **Example 3**
```python
n = 4, k = 4
Factors: [1, 2, 4]
Output: -1 (since k=4 is out of bounds)
```

---

### **Final Thoughts**
- **O(n) naive approach** works but is inefficient.
- **O(√n) approach using factor pairs** is optimal.
- **Avoid sorting by using two passes**, making it efficient in practice.

🚀 The last **O(√n)** approach is the best solution! 🚀

### **Understanding the Two-Pass Approach in `kthFactor`**

The goal of this function is to **find the k-th factor of `n` in ascending order**. Instead of iterating through all numbers up to `n`, it uses an **optimized approach leveraging the square root of `n`** to reduce unnecessary checks.

---

### **Step 1: What is a Factor?**
A **factor** of `n` is a number `i` that divides `n` exactly, meaning `n % i == 0`.
Each factor `i` has a corresponding **pair**:
\[
\left(i, \frac{n}{i}\right)
\]
For example, if `n = 12`, its factors are:
\[
1, 2, 3, 4, 6, 12
\]
These pairs form from iterating up to `sqrt(n)`:
- \( (1, 12) \)
- \( (2, 6) \)
- \( (3, 4) \)

---

## **How the Two Loops Work**
The function **uses two passes** to collect factors **in increasing order**.

---

### **🔹 First Loop: Finding Small Factors (1 to sqrt(n))**
```python
for i in range(1, sqrt_n + 1):
    if n % i == 0:  # Check if i is a factor
        count += 1
        if count == k:
            return i
```
🔹 **Purpose:** Finds **small** factors of `n` (e.g., 1, 2, 3 for `n=12`).
🔹 **Why up to `sqrt(n)`?**
   - Any factor `i` found here has a **corresponding larger factor** (`n / i`).
   - Example: `2` pairs with `6`, `3` pairs with `4` for `n=12`.
🔹 **Why return early?**
   - If the `k-th` factor is within this range, **we don’t need the second loop**.

---

### **🔹 Second Loop: Finding Large Factors (Above sqrt(n))**
```python
for i in range(sqrt_n, 0, -1):
    if n % i == 0 and i != n // i:  # Ensure unique factors
        count += 1
        if count == k:
            return n // i
```
🔹 **Purpose:** Finds **large** factors by taking their pair `n // i`.
🔹 **Why iterate in reverse (`sqrt_n` to `1`)?**
   - To **continue counting in ascending order**.
   - We already counted `i`, so now we check `n // i`.
🔹 **Why check `i != n // i`?**
   - If `n` is a **perfect square**, the square root should only be counted **once**.
   - Example: For `n = 16`, `sqrt(16) = 4`, so we don’t count `4` twice.

---

## **Example Walkthrough**
### **Example 1: `n = 12, k = 4`**
Factors of `12`: **1, 2, 3, 4, 6, 12**
We need the **4th** factor.

1️⃣ **First loop (1 to sqrt(12) = 3)**
   - `i = 1`: ✅ Factor → Count = 1
   - `i = 2`: ✅ Factor → Count = 2
   - `i = 3`: ✅ Factor → Count = 3
   *(Still haven't reached `k=4`.)*

2️⃣ **Second loop (3 to 1)**
   - `i = 3`: ✅ Factor Pair → `12 // 3 = 4`, Count = 4
   - 🎯 Found 4th factor → Return `4`

✅ **Output:** `4`

---

### **Example 2: `n = 16, k = 5`**
Factors of `16`: **1, 2, 4, 8, 16**
We need the **5th** factor.

1️⃣ **First loop (1 to sqrt(16) = 4)**
   - `i = 1`: ✅ Factor → Count = 1
   - `i = 2`: ✅ Factor → Count = 2
   - `i = 4`: ✅ Factor → Count = 3
   *(Still haven't reached `k=5`.)*

2️⃣ **Second loop (4 to 1)**
   - `i = 4`: ✅ Factor Pair → `16 // 4 = 4` (skip duplicate)
   - `i = 2`: ✅ Factor Pair → `16 // 2 = 8`, Count = 4
   - `i = 1`: ✅ Factor Pair → `16 // 1 = 16`, Count = 5
   - 🎯 Found 5th factor → Return `16`

✅ **Output:** `16`

---

## **Time Complexity Analysis**
- The first loop runs **√n** times.
- The second loop also runs **√n** times.
- Overall, **O(√n) time complexity**, much faster than iterating up to `n`.

---

## **Key Takeaways**
✅ **Optimized with sqrt(n) instead of iterating all numbers**
✅ **First pass finds small factors, second pass finds large factors**
✅ **Ensures factors are counted in ascending order**
✅ **Handles perfect squares correctly**
