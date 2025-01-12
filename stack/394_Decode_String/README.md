To decode the encoded string, we can use a **stack-based approach** to handle the nested structure of brackets effectively.

---

### Approach:
1. Use two stacks:
   - One to store numbers (`k`) for repetition.
   - Another to store strings being built (`current_string`) before encountering a closing bracket (`]`).

2. Traverse the string:
   - If a digit is encountered, extract the full number (which might be multiple digits).
   - If an opening bracket (`[`) is encountered, push the current string and repetition number onto their respective stacks, and reset the `current_string`.
   - If a closing bracket (`]`) is encountered, pop from the stacks to retrieve the previous string and repetition number, repeat the current string `k` times, and append it to the previous string.
   - If a character is encountered, append it to `current_string`.

3. Return the final `current_string` after processing the entire input string.

---

### Implementation:
```python
def decodeString(s):
    num_stack = []  # Stack to store numbers (k values)
    str_stack = []  # Stack to store strings
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            # Build the current number (could be multi-digit)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push the current number and string onto stacks
            num_stack.append(current_num)
            str_stack.append(current_string)
            # Reset current number and string
            current_num = 0
            current_string = ""
        elif char == ']':
            # Pop from stacks and construct the decoded string
            repeat_count = num_stack.pop()
            previous_string = str_stack.pop()
            current_string = previous_string + current_string * repeat_count
        else:
            # Append the current character to the current string
            current_string += char

    return current_string
```

---

### Examples:

#### Example 1:
```python
s = "3[a]2[bc]"
print(decodeString(s))  # Output: "aaabcbc"
```

#### Example 2:
```python
s = "3[a2[c]]"
print(decodeString(s))  # Output: "accaccacc"
```

#### Example 3:
```python
s = "2[abc]3[cd]ef"
print(decodeString(s))  # Output: "abcabccdcdcdef"
```

---

### Complexity:
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the input string. Each character is processed once, and string concatenation is optimized for this problem.
- **Space Complexity**: \(O(n)\), for the stacks storing intermediate results.

This approach efficiently handles nested and repeated patterns in the encoded string.
