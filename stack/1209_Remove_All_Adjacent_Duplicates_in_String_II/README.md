This problem can also be solved efficiently using a **stack**, where the stack stores pairs of characters and their consecutive counts. When a character's count reaches \( k \), it is removed from the stack.

---

### Algorithm
1. Initialize an empty stack.
   - Each element in the stack will be a pair: `(char, count)`, where `char` is the character and `count` is the number of consecutive occurrences of that character.
2. Iterate through the characters in the string:
   - If the stack is not empty and the top element's character matches the current character:
     - Increment the count of the top element.
     - If the count equals \( k \), remove the element from the stack (as \( k \)-duplicates are removed).
   - Otherwise, push the current character with a count of `1` onto the stack.
3. After processing all characters, reconstruct the result string using the stack by repeating each character by its count.
4. Return the reconstructed string.

---

### Python Code
```python
def removeDuplicates(s: str, k: int) -> str:
    stack = []

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1] = (char, stack[-1][1] + 1)  # Increment count
            if stack[-1][1] == k:
                stack.pop()  # Remove when count equals k
        else:
            stack.append((char, 1))  # Add new character with count 1

    # Reconstruct the string from the stack
    return ''.join(char * count for char, count in stack)
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
s = "abcd"
k = 2
print(removeDuplicates(s, k))  # Output: "abcd"
```
- Stack simulation:
  - Push 'a': Stack = [('a', 1)]
  - Push 'b': Stack = [('a', 1), ('b', 1)]
  - Push 'c': Stack = [('a', 1), ('b', 1), ('c', 1)]
  - Push 'd': Stack = [('a', 1), ('b', 1), ('c', 1), ('d', 1)]
- Result: "abcd"

---

#### Example 2
```python
s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k))  # Output: "aa"
```
- Stack simulation:
  - Push 'd': Stack = [('d', 1)]
  - Push 'e': Stack = [('d', 1), ('e', 1)]
  - Push 'e': Stack = [('d', 1), ('e', 2)]
  - Push 'e': Remove 'e': Stack = [('d', 1)]
  - Push 'd': Stack = [('d', 2)]
  - Push 'b': Stack = [('d', 2), ('b', 1)]
  - Push 'b': Stack = [('d', 2), ('b', 2)]
  - Push 'b': Remove 'b': Stack = [('d', 2)]
  - Push 'c': Stack = [('d', 2), ('c', 1)]
  - Push 'c': Stack = [('d', 2), ('c', 2)]
  - Push 'c': Remove 'c': Stack = [('d', 2)]
  - Push 'd': Stack = [('d', 3)]
  - Remove 'd': Stack = []
  - Push 'a': Stack = [('a', 1)]
  - Push 'a': Stack = [('a', 2)]
- Result: "aa"

---

#### Example 3
```python
s = "pbbcggttciiippooaais"
k = 2
print(removeDuplicates(s, k))  # Output: "ps"
```
- Stack simulation:
  - Push 'p': Stack = [('p', 1)]
  - Push 'b': Stack = [('p', 1), ('b', 1)]
  - Push 'b': Remove 'b': Stack = [('p', 1)]
  - Push 'c': Stack = [('p', 1), ('c', 1)]
  - Push 'g': Stack = [('p', 1), ('c', 1), ('g', 1)]
  - Push 'g': Remove 'g': Stack = [('p', 1), ('c', 1)]
  - Push 't': Stack = [('p', 1), ('c', 1), ('t', 1)]
  - Push 't': Remove 't': Stack = [('p', 1), ('c', 1)]
  - Push 'c': Stack = [('p', 1), ('c', 2)]
  - Push 'i': Stack = [('p', 1), ('c', 2), ('i', 1)]
  - Push 'i': Remove 'i': Stack = [('p', 1), ('c', 2)]
  - Push 'p': Stack = [('p', 1), ('c', 2), ('p', 1)]
  - Push 'p': Remove 'p': Stack = [('p', 1), ('c', 2)]
  - Push 'o': Stack = [('p', 1), ('c', 2), ('o', 1)]
  - Push 'o': Remove 'o': Stack = [('p', 1), ('c', 2)]
  - Push 'a': Stack = [('p', 1), ('c', 2), ('a', 1)]
  - Push 'a': Remove 'a': Stack = [('p', 1), ('c', 2)]
  - Push 'i': Stack = [('p', 1), ('c', 2), ('i', 1)]
  - Push 's': Stack = [('p', 1), ('c', 2), ('i', 1), ('s', 1)]
- Result: "ps"

---

This solution is efficient, meeting the problem's constraints while maintaining clarity and correctness.
