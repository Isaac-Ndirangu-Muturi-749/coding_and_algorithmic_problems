### **Solution Approach**
We need to partition the string into the **minimum number of substrings**, ensuring that **each substring contains unique characters**.

**Key Idea:**
- As we iterate through the string, we maintain a **set of seen characters**.
- If we encounter a **duplicate character**, we must start a new substring.
- The process continues until we reach the end of the string.

### **Efficient Approach (O(n))**
We iterate through the string and keep track of characters using a **set**:
1. **Initialize an empty set** to store characters of the current substring.
2. **Iterate through the string**:
   - If the character is **already in the set**, start a new substring and reset the set.
   - Add the character to the set.
3. **Count the number of times a new substring starts**.

### **Implementation**
```python
class Solution:
    def minPartitions(self, s: str) -> int:
        unique_chars = set()
        partitions = 1  # At least one substring is needed

        for char in s:
            if char in unique_chars:  # Start a new substring if char repeats
                partitions += 1
                unique_chars.clear()
            unique_chars.add(char)

        return partitions
```

### **Complexity Analysis**
- **Time Complexity:** \(O(n)\) → We iterate through the string once.
- **Space Complexity:** \(O(1)\) → At most 26 characters stored in the set.

---

### **Example Walkthrough**
#### **Example 1**
```python
Input: s = "abacaba"
Output: 4
```
- Partition 1: `"ab"`
- Partition 2: `"a"`
- Partition 3: `"ca"`
- Partition 4: `"ba"`

#### **Example 2**
```python
Input: s = "ssssss"
Output: 6
```
- Each `"s"` must be in its own substring.

---

### **Edge Cases Considered**
- **Single character strings:** `"a"` → output `1`
- **All distinct characters:** `"abcdef"` → output `1`
- **All repeated characters:** `"aaaaa"` → output `5`

🚀 **Optimized greedy solution with O(n) complexity!** 🚀
