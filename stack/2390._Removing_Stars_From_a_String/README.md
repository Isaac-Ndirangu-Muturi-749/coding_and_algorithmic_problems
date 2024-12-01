We can solve this problem efficiently using a **stack** to manage the removals. Each time we encounter a character, we decide whether to push it onto the stack or remove the most recent character (along with the star). This ensures a linear time solution.

---

### **Algorithm**
1. Use a stack to store characters from the string.
2. Traverse the string:
   - If the character is not a `*`, push it onto the stack.
   - If the character is a `*`, pop the top of the stack (removing the last character).
3. After the traversal, the stack contains the final string without any stars.
4. Convert the stack back to a string and return it.

---

### **Python Implementation**
```python
def removeStars(s: str) -> str:
    stack = []

    for char in s:
        if char == '*':
            if stack:  # Ensure the stack is not empty
                stack.pop()  # Remove the last character
        else:
            stack.append(char)  # Add non-star character to the stack

    return ''.join(stack)  # Convert the stack to a string
```

---

### **Examples**

#### Example 1:
```python
s = "leet**cod*e"
print(removeStars(s))
```
**Output**: `"lecoe"`

**Explanation**:
- `leet**cod*e` → Remove 't': `"lee*cod*e"`
- `"lee*cod*e"` → Remove 'e': `"lecod*e"`
- `"lecod*e"` → Remove 'd': `"lecoe"`

---

#### Example 2:
```python
s = "erase*****"
print(removeStars(s))
```
**Output**: `""`

**Explanation**:
- Remove 'e', 'r', 'a', 's', 'e' sequentially, leaving an empty string.

---

### **Complexity Analysis**
1. **Time Complexity**: \(O(n)\), where \(n\) is the length of the string. We traverse the string once.
2. **Space Complexity**: \(O(n)\) in the worst case, for the stack. If the string has no stars, all characters are pushed onto the stack.

This approach is efficient and handles the problem constraints well.
