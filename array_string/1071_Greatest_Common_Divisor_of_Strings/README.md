If you want to solve the problem without using libraries like `math.gcd`, you can manually compute the greatest common divisor (GCD) of the lengths of the strings. Here's how:

### Approach:
1. Use the **Euclidean Algorithm** to calculate the GCD of the lengths of `str1` and `str2`.
2. Follow the same logic as before to check if `str1 + str2` equals `str2 + str1`.

### Implementation:

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def gcdOfStrings(str1: str, str2: str) -> str:
    # Check if str1 + str2 is equal to str2 + str1
    if str1 + str2 != str2 + str1:
        return ""
    # Calculate the GCD of the lengths of str1 and str2
    gcd_length = gcd(len(str1), len(str2))
    # Return the substring of length gcd_length from str1
    return str1[:gcd_length]

# Example 1
str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))  # Output: "ABC"

# Example 2
str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))  # Output: "AB"

# Example 3
str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))  # Output: ""
```

### Explanation:
1. **Manual GCD Calculation**:
   - The Euclidean algorithm repeatedly replaces \(a\) with \(b\) and \(b\) with \(a \mod b\) until \(b = 0\).
   - At this point, \(a\) is the GCD of the two numbers.
2. **String Validation**:
   - If `str1 + str2` is not equal to `str2 + str1`, return `""` because there's no common divisor string.
3. **Extract GCD Substring**:
   - Use the GCD of the lengths to determine the length of the common substring.

### Complexity:
- **Time Complexity**: \(O(n + m + \log(\min(n, m)))\), where \(n\) and \(m\) are the lengths of `str1` and `str2`. The \(\log(\min(n, m))\) factor is for the GCD computation.
- **Space Complexity**: \(O(1)\).


Yes, there are alternative ways to calculate the greatest common divisor (GCD) of two numbers besides the Euclidean algorithm. Here are a few methods:

---

### 1. **Iterative Method**
You can find the GCD by iterating from the smaller of the two numbers down to 1 and returning the first number that divides both.

```python
def gcd(a: int, b: int) -> int:
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1  # This handles the case where a and b are co-prime
```

---

### 2. **Subtraction Method**
Instead of using modulo (`%`), repeatedly subtract the smaller number from the larger number until the two numbers are equal.

```python
def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```

This approach works because subtracting the smaller number doesn't change the GCD. However, it can be slower than the Euclidean algorithm for larger numbers.

---

### 3. **Binary GCD (Stein's Algorithm)**
Stein's algorithm uses bitwise operations to compute the GCD efficiently, particularly for very large numbers. Here's the logic:
- If both numbers are even, divide both by 2 and multiply the result by 2 later.
- If one number is even, divide it by 2.
- If both numbers are odd, subtract the smaller number from the larger and repeat.

```python
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    # Count common factors of 2
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a // 2, b // 2)
    elif a % 2 == 0:
        return gcd(a // 2, b)
    elif b % 2 == 0:
        return gcd(a, b // 2)
    else:
        return gcd(abs(a - b), min(a, b))
```

---

### Comparison of Methods

| **Method**          | **Advantages**                                                                                      | **Disadvantages**                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Euclidean**        | Fast and simple to implement. Works well for large numbers.                                        | None. It is generally the most efficient method.                                 |
| **Iterative**        | Straightforward, easy to understand.                                                              | Inefficient for large numbers due to the loop iterating down to 1.               |
| **Subtraction**      | Intuitive and easy to implement without modulo.                                                   | Slow for large numbers since subtraction takes more steps than modulo.           |
| **Binary GCD**       | Efficient for large integers; uses only subtraction, shifts, and comparisons (no division/modulo). | Slightly more complex to implement than the Euclidean algorithm.                 |

The Euclidean algorithm remains the most widely used because it is simple and efficient, but the binary GCD method is a great alternative if you want to avoid division.
