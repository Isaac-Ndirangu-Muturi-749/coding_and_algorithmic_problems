To determine if the number of occurrences of each value in the array is unique, we can use a straightforward approach:

---

### **Approach**

1. **Frequency Count**:
   - Use a dictionary (hashmap) to count the occurrences of each value in the array.

2. **Check Uniqueness**:
   - Use a set to store the frequency counts.
   - If a frequency appears more than once, return `False`.

3. **Return Result**:
   - If all frequencies are unique, return `True`.

---

### **Implementation**

```python
def uniqueOccurrences(arr):
    # Count the frequency of each value in the array
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Check if frequencies are unique
    occurrences = set(freq.values())
    return len(occurrences) == len(freq)
```

---

### **Example Walkthrough**

#### Example 1:
**Input**:
```python
arr = [1, 2, 2, 1, 1, 3]
```

**Output**:
```python
True
```

**Explanation**:
- Frequencies: `{1: 3, 2: 2, 3: 1}`
- Unique frequencies: `{3, 2, 1}` (all unique).

---

#### Example 2:
**Input**:
```python
arr = [1, 2]
```

**Output**:
```python
False
```

**Explanation**:
- Frequencies: `{1: 1, 2: 1}`
- Unique frequencies: `{1}` (not all unique).

---

#### Example 3:
**Input**:
```python
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
```

**Output**:
```python
True
```

**Explanation**:
- Frequencies: `{-3: 3, 0: 2, 1: 4, 10: 1}`
- Unique frequencies: `{3, 2, 4, 1}` (all unique).

---

### **Complexity Analysis**

1. **Time Complexity**:
   - Counting frequencies: \(O(n)\), where \(n\) is the size of the array.
   - Checking uniqueness: \(O(k)\), where \(k\) is the number of unique elements in the array.
   - Overall: \(O(n)\), as \(k \leq n\).

2. **Space Complexity**:
   - \(O(k)\) for the dictionary and set to store frequencies and unique counts.

This solution is efficient and adheres to the problem's constraints.
