This problem can be efficiently solved using a **stack**. By simulating the removal of duplicates, the stack ensures that adjacent duplicate letters are eliminated in a single traversal of the string.

---

### Algorithm
1. Initialize an empty stack.
2. Iterate through the characters in the string:
   - If the stack is not empty and the top element of the stack equals the current character, pop the top element (remove the duplicate).
   - Otherwise, push the current character onto the stack.
3. After the loop, the stack will contain the final string with all adjacent duplicates removed.
4. Convert the stack into a string and return it.

---

### Python Code
```python
def removeDuplicates(s: str) -> str:
    stack = []

    for char in s:
        # Remove adjacent duplicates
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # Return the result as a string
    return ''.join(stack)
```

---

### Complexity
- **Time Complexity**: \( O(n) \)
  - Each character is pushed and popped from the stack at most once.
- **Space Complexity**: \( O(n) \)
  - The stack can hold up to all the characters in the worst case (no duplicates).

---

### Example Runs

#### Example 1
```python
s = "abbaca"
print(removeDuplicates(s))  # Output: "ca"
```
- Stack simulation:
  - Push 'a': Stack = ['a']
  - Push 'b': Stack = ['a', 'b']
  - Push 'b': Remove 'b': Stack = ['a']
  - Push 'a': Remove 'a': Stack = []
  - Push 'c': Stack = ['c']
  - Push 'a': Stack = ['c', 'a']
- Result: "ca"

#### Example 2
```python
s = "azxxzy"
print(removeDuplicates(s))  # Output: "ay"
```
- Stack simulation:
  - Push 'a': Stack = ['a']
  - Push 'z': Stack = ['a', 'z']
  - Push 'x': Stack = ['a', 'z', 'x']
  - Push 'x': Remove 'x': Stack = ['a', 'z']
  - Push 'z': Remove 'z': Stack = ['a']
  - Push 'y': Stack = ['a', 'y']
- Result: "ay"

---

This approach efficiently handles strings of up to \( 10^5 \) characters, as required by the constraints.
