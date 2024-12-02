Here’s a solution for reversing the order of words in a string, ensuring no leading or trailing spaces and reducing multiple spaces between words to a single space.

---

### **Python Implementation**

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by spaces to extract words
        words = s.split()

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join the reversed list with a single space
        return " ".join(reversed_words)
```

---

### **Explanation**

1. **Split the String**:
   - The `split()` method removes any leading/trailing spaces and splits the string into words, automatically handling multiple spaces between words.

2. **Reverse the Words**:
   - Use slicing `[::-1]` to reverse the list of words.

3. **Join the Words**:
   - Use `" ".join()` to concatenate the reversed list into a single string with words separated by a single space.

---

### **Examples**

#### Example 1:
```python
s = "the sky is blue"
solution = Solution()
print(solution.reverseWords(s))  # Output: "blue is sky the"
```

#### Example 2:
```python
s = "  hello world  "
solution = Solution()
print(solution.reverseWords(s))  # Output: "world hello"
```

#### Example 3:
```python
s = "a good   example"
solution = Solution()
print(solution.reverseWords(s))  # Output: "example good a"
```

---

### **Constraints**

1. **Time Complexity**: \( O(n) \), where \( n \) is the length of the input string. The string is processed once to split into words and once to join them.
2. **Space Complexity**: \( O(n) \), for storing the list of words.

---

### **Follow-up: In-Place Solution**

If the string data type is mutable (e.g., a character array), we can reverse the entire string, reverse each word, and clean up extra spaces. However, Python strings are immutable, so achieving \( O(1) \) extra space isn't possible in standard Python without special handling.
