To calculate the Tribonacci sequence efficiently, we can use dynamic programming or an iterative approach to avoid redundant calculations. Here’s how:

---

### **Approach**

1. **Base Cases**:
   - \(T_0 = 0\), \(T_1 = 1\), \(T_2 = 1\).

2. **Recursive Relation**:
   - \(T_{n+3} = T_n + T_{n+1} + T_{n+2}\) for \(n \geq 0\).

3. **Iterative Calculation**:
   - Use three variables to keep track of the last three Tribonacci numbers and update them iteratively until \(T_n\) is computed.

---

### **Implementation**

```python
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Initialize the first three Tribonacci numbers
    t0, t1, t2 = 0, 1, 1

    # Compute Tribonacci numbers iteratively
    for _ in range(3, n + 1):
        t_next = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t_next

    return t2
```

---

### **Explanation**

1. **Base Cases**:
   - Return the precomputed values for \(n = 0, 1, 2\).

2. **Iterative Update**:
   - Start with \(T_0, T_1, T_2\).
   - Use the formula \(T_{n+3} = T_n + T_{n+1} + T_{n+2}\) to calculate each subsequent value.
   - Update \(T_0, T_1, T_2\) to reflect the next numbers in the sequence.

3. **Result**:
   - When the loop ends, \(T_2\) holds the value of \(T_n\).

---

### **Complexity Analysis**

1. **Time Complexity**:
   - \(O(n)\): We compute each Tribonacci number up to \(n\) once.

2. **Space Complexity**:
   - \(O(1)\): We use only three variables to store intermediate results.

---

### **Examples**

#### Example 1:
**Input**:
```python
n = 4
```

**Output**:
```python
4
```

**Explanation**:
- \(T_3 = 0 + 1 + 1 = 2\)
- \(T_4 = 1 + 1 + 2 = 4\)

#### Example 2:
**Input**:
```python
n = 25
```

**Output**:
```python
1389537
```

---

This approach ensures optimal performance for all valid inputs within the constraints.


To compute the Tribonacci sequence using dynamic programming (DP), we use an array to store intermediate results. This approach avoids redundant calculations while keeping track of all previously computed values.

---

### **Dynamic Programming Approach**

1. **Base Cases**:
   - \(T_0 = 0\), \(T_1 = 1\), \(T_2 = 1\).

2. **Recursive Relation**:
   - \(T_n = T_{n-1} + T_{n-2} + T_{n-3}\) for \(n \geq 3\).

3. **Use a DP Array**:
   - Store the values of \(T_0, T_1, \dots, T_n\) in a list.

---

### **Implementation**

```python
def tribonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # Initialize DP array
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, 1, 1

    # Fill the DP array
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]
```

---

### **Explanation**

1. **Base Initialization**:
   - \(dp[0] = 0\), \(dp[1] = 1\), \(dp[2] = 1\).

2. **DP Transition**:
   - For \(i \geq 3\), compute \(dp[i] = dp[i-1] + dp[i-2] + dp[i-3]\).

3. **Final Result**:
   - The value \(dp[n]\) holds the \(n\)-th Tribonacci number.

---

### **Complexity Analysis**

1. **Time Complexity**:
   - \(O(n)\): We compute each Tribonacci number up to \(n\) once.

2. **Space Complexity**:
   - \(O(n)\): We store all Tribonacci numbers in the DP array.

---

### **Examples**

#### Example 1:
**Input**:
```python
n = 4
```

**Output**:
```python
4
```

**Explanation**:
- \(dp = [0, 1, 1, 2, 4]\)
- \(dp[4] = 4\)

#### Example 2:
**Input**:
```python
n = 25
```

**Output**:
```python
1389537
```

---

### **Optimization**

If you want to optimize the space usage further, you can use only three variables to keep track of the last three values (as shown in the iterative approach above). This reduces the space complexity to \(O(1)\).
