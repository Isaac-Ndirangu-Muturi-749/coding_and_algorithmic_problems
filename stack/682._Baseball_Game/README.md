Here's a solution for the problem using a stack to maintain the record of scores efficiently:

---

### **Approach**
1. Use a stack to store the scores:
   - Push a score into the stack for each valid operation.
   - Update the stack based on the operations `C`, `D`, and `+`.
2. Iterate through the `operations` list and:
   - For an integer `x`, push it onto the stack.
   - For `'C'`, pop the last element from the stack.
   - For `'D'`, push twice the last element of the stack.
   - For `'+'`, push the sum of the last two elements of the stack.
3. Finally, return the sum of all the elements in the stack.

---

### **Implementation**

```python
def calPoints(operations):
    stack = []

    for op in operations:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))

    return sum(stack)
```

---

### **Examples**

#### Example 1:
**Input**:
```python
ops = ["5", "2", "C", "D", "+"]
```

**Output**:
```python
30
```

**Explanation**:
- Initial record: `[5]`
- After "2": `[5, 2]`
- After "C": `[5]`
- After "D": `[5, 10]`
- After "+": `[5, 10, 15]`
- Sum: `5 + 10 + 15 = 30`.

---

#### Example 2:
**Input**:
```python
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
```

**Output**:
```python
27
```

**Explanation**:
- Initial record: `[5]`
- After "-2": `[5, -2]`
- After "4": `[5, -2, 4]`
- After "C": `[5, -2]`
- After "D": `[5, -2, -4]`
- After "9": `[5, -2, -4, 9]`
- After "+": `[5, -2, -4, 9, 5]`
- After "+": `[5, -2, -4, 9, 5, 14]`
- Sum: `5 + -2 + -4 + 9 + 5 + 14 = 27`.

---

#### Example 3:
**Input**:
```python
ops = ["1", "C"]
```

**Output**:
```python
0
```

**Explanation**:
- Initial record: `[1]`
- After "C": `[]`
- Sum: `0`.

---

### **Complexity Analysis**

1. **Time Complexity**:
   - Each operation is processed in \(O(1)\).
   - The sum of the stack at the end is \(O(n)\), where \(n\) is the number of operations.
   - Overall: \(O(n)\).

2. **Space Complexity**:
   - The stack can grow to at most \(n\) elements.
   - Space complexity: \(O(n)\).

This solution efficiently handles all the operations and adheres to the problem constraints.
