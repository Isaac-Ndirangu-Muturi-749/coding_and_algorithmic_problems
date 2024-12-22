This problem can be solved by using a two-pointer approach to traverse the array and compress it in place. Here's the solution:

### Algorithm
1. **Two Pointers**:
   - Use a pointer `write` to indicate where to write the compressed result in the `chars` array.
   - Use another pointer `read` to traverse the array and group consecutive characters.
2. **Count Consecutive Characters**:
   - For each group of consecutive characters, write the character to `chars[write]`.
   - If the group size is greater than 1, write its length as digits into `chars`.
3. **Update the Input Array**:
   - Modify the input array in place and return the length of the compressed array.

### Python Code
```python
def compress(chars: list[str]) -> int:
    write = 0  # Pointer to write the compressed result
    read = 0   # Pointer to read through the input array

    while read < len(chars):
        char = chars[read]
        count = 0

        # Count consecutive characters
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1

        # Write the character to the array
        chars[write] = char
        write += 1

        # If count > 1, write the digits of the count
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write
```

### Explanation
1. **Initialization**:
   - Start with `write = 0` and `read = 0`.
2. **Count Characters**:
   - For each group of consecutive repeating characters, count their occurrences and move the `read` pointer forward.
3. **Write Characters**:
   - Write the character and, if the count is greater than 1, write the digits of the count.
4. **Return the Length**:
   - Return the `write` pointer, which gives the length of the compressed array.

### Complexity
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the `chars` array. We traverse the array once.
- **Space Complexity**: \(O(1)\), as the compression is done in place.

### Example Runs
#### Example 1
```python
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))  # Output: 6
print(chars[:6])        # Output: ["a", "2", "b", "2", "c", "3"]
```

#### Example 2
```python
chars = ["a"]
print(compress(chars))  # Output: 1
print(chars[:1])        # Output: ["a"]
```

#### Example 3
```python
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars))  # Output: 4
print(chars[:4])        # Output: ["a", "b", "1", "2"]
```
