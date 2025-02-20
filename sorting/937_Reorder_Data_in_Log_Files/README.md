### **Solution Approach: Sorting Logs**

To reorder the logs:
1. **Letter-logs** should come before **digit-logs**.
2. **Letter-logs** should be sorted:
   - Lexicographically by their content.
   - If contents are the same, then by identifier.
3. **Digit-logs** should maintain their relative order (stable sort).

---

### **Key Observations**

- **Letter-logs** contain lowercase English letters in their content.
- **Digit-logs** contain digits in their content.
- **Identifiers** are always the first word and are unique.

---

### **Approach**

1. **Separate Letter-logs and Digit-logs:**
   - Use `str.split()` to separate the identifier from the content.
   - Check if the first word of the content is a digit to distinguish digit-logs from letter-logs.

2. **Sort Letter-logs:**
   - By content (`log.split()[1:]`)
   - If contents are the same, then by identifier (`log.split()[0]`)

3. **Combine Logs:**
   - Place all sorted **letter-logs** before the **digit-logs**.
   - Maintain relative order for **digit-logs**.

---

### **Python Code Implementation**

```python
def reorderLogFiles(logs):
    # Custom sorting function for letter-logs
    def get_key(log):
        id_, rest = log.split(" ", 1)
        # Return a tuple: (0, content, identifier) for letter-logs
        # Return a tuple: (1, None, None) for digit-logs to maintain relative order
        return (0, rest, id_) if rest[0].isalpha() else (1, None, None)

    # Sort logs using the custom key function
    return sorted(logs, key=get_key)
```

---

### **Explanation**

1. **`get_key(log)`**:
   - Splits each log into `identifier` and `content`.
   - Returns a sorting key:
     - `(0, content, identifier)` for letter-logs → Ensures lexicographical sort.
     - `(1, None, None)` for digit-logs → Maintains relative order.

2. **`sorted(logs, key=get_key)`**:
   - Uses the custom key to sort logs.
   - Ensures letter-logs are first and sorted lexicographically.
   - Digit-logs maintain relative order due to the tuple structure.

---

### **Complexity Analysis**

- **Time Complexity:**
  - Sorting Complexity: \( O(N \log N) \), where \( N \) is the number of logs.
  - Split and check operations are \( O(1) \) per log.
  - Overall: \( O(N \log N) \)

- **Space Complexity:**
  - Extra space for sorting and the keys → \( O(N) \)

---

### **Example Walkthrough**

#### **Example 1**
```python
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
```

- **Letter-logs:**
  - `"let1 art can"` → Key: `(0, "art can", "let1")`
  - `"let2 own kit dig"` → Key: `(0, "own kit dig", "let2")`
  - `"let3 art zero"` → Key: `(0, "art zero", "let3")`

- **Digit-logs (Keep relative order):**
  - `"dig1 8 1 5 1"` → Key: `(1, None, None)`
  - `"dig2 3 6"` → Key: `(1, None, None)`

- **Sorted Result:**
```python
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

---

#### **Example 2**
```python
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(logs))
```

- **Letter-logs:**
  - `"g1 act car"` → Key: `(0, "act car", "g1")`
  - `"a8 act zoo"` → Key: `(0, "act zoo", "a8")`
  - `"ab1 off key dog"` → Key: `(0, "off key dog", "ab1")`

- **Digit-logs (Keep relative order):**
  - `"a1 9 2 3 1"` → Key: `(1, None, None)`
  - `"zo4 4 7"` → Key: `(1, None, None)`

- **Sorted Result:**
```python
["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
```

---

### **Why This Solution Works Efficiently**
- The custom key function provides a clear distinction between letter-logs and digit-logs.
- Python's built-in `sorted()` is stable, maintaining the relative order for digit-logs.
- The lexicographical sort for letter-logs ensures the correct order.

---

### **Edge Cases Considered**
- All logs are digit-logs.
- All logs are letter-logs.
- Mixture of letter-logs and digit-logs with identical contents.
- Logs with varying lengths.



The tuple in the `get_key` function determines how the logs are sorted. Let's break it down:

### **Tuple Structure:**
```python
return (0, rest, id_) if rest[0].isalpha() else (1, None, None)
```
This tuple has **three elements**:
1. **Primary sort key** (`0` for letter-logs, `1` for digit-logs)
2. **Secondary sort key** (content of the letter-log or `None` for digit-logs)
3. **Tertiary sort key** (identifier of the letter-log or `None` for digit-logs)

### **Sorting Logic:**
1. **Letter-logs (`0, rest, id_`)**:
   - The **primary key (`0`)** ensures that all letter-logs come **before** digit-logs.
   - The **secondary key (`rest`)** sorts letter-logs **lexicographically by content**.
   - The **tertiary key (`id_`)** ensures that if two letter-logs have the **same content**, they are sorted by their **identifier**.

2. **Digit-logs (`1, None, None`)**:
   - The **primary key (`1`)** ensures that all digit-logs appear **after** all letter-logs.
   - `None` values for the secondary and tertiary keys preserve **relative order** (i.e., stable sorting).

---

### **Example Walkthrough**
#### **Input Logs:**
```python
logs = [
    "dig1 8 1 5 1",
    "let1 art can",
    "dig2 3 6",
    "let2 own kit dig",
    "let3 art zero"
]
```
#### **Step 1: Mapping Logs to Sorting Keys**
| Log                 | `get_key(log)` Output       |
|---------------------|---------------------------|
| `"dig1 8 1 5 1"`   | `(1, None, None)`          |
| `"let1 art can"`   | `(0, "art can", "let1")`   |
| `"dig2 3 6"`       | `(1, None, None)`          |
| `"let2 own kit dig"` | `(0, "own kit dig", "let2")` |
| `"let3 art zero"`  | `(0, "art zero", "let3")`  |

#### **Step 2: Sorting**
1. **Letter-logs first (because their primary key is `0`)**
   - `"let1 art can"` → `"let3 art zero"` → `"let2 own kit dig"`
   - `"art can"` and `"art zero"` are sorted **lexicographically**.
   - `"let1"` and `"let3"` are compared if their content is identical.

2. **Digit-logs appear in their original order (primary key `1`)**
   - `"dig1 8 1 5 1"` and `"dig2 3 6"` maintain their original relative order.

#### **Final Sorted Order:**
```python
["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

---

### **Key Takeaways**
- The **primary key (`0` or `1`)** separates letter-logs from digit-logs.
- The **secondary key (`rest`)** sorts letter-logs lexicographically.
- The **tertiary key (`id_`)** maintains order for logs with identical content.
- Digit-logs maintain **relative order** since they all have `(1, None, None)`.
