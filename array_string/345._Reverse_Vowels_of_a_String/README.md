To solve the problem, we can use two pointers to efficiently reverse the vowels in the string. Here's the Python implementation:

---

### **Python Implementation**

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase and uppercase)
        s = list(s)  # Convert the string to a list to allow modification
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert the list back to a string and return
```

---

### **Explanation**

1. **Two-Pointer Technique**:
   - Use two pointers (`left` and `right`) to traverse the string from both ends.
   - Increment `left` until it points to a vowel.
   - Decrement `right` until it points to a vowel.
   - Swap the vowels at the two pointers.

2. **Swap Logic**:
   - If both pointers point to vowels, swap their characters.
   - Move the pointers inward after the swap.

3. **Efficient Check**:
   - Use a set of vowels (`aeiouAEIOU`) for \(O(1)\) lookups.

4. **String Modification**:
   - Convert the string to a list for mutable operations.
   - After processing, convert the list back to a string.

---

### **Complexity Analysis**

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string. Each character is processed at most once.
- **Space Complexity**: \(O(n)\) for the list conversion. The vowel set uses constant space.

---

### **Examples**

#### Example 1:
Input:
```python
s = "IceCreAm"
```

Execution:
- Vowels: ['I', 'e', 'e', 'A']
- After reversing: ['A', 'e', 'e', 'I']
- Output: `"AceCreIm"`

#### Example 2:
Input:
```python
s = "leetcode"
```

Execution:
- Vowels: ['e', 'e', 'o', 'e']
- After reversing: ['e', 'o', 'e', 'e']
- Output: `"leotcede"`

---

### **Edge Cases**

1. **No Vowels**:
   - Input: `"bcdfg"`
   - Output: `"bcdfg"`

2. **All Vowels**:
   - Input: `"aeiou"`
   - Output: `"uoiea"`

3. **Mixed Case**:
   - Input: `"AeIoU"`
   - Output: `"UoIeA"`

This solution efficiently handles the constraints and edge cases.
