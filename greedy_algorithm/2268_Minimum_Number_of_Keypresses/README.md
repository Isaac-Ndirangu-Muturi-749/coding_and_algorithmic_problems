### **Solution Approach:**

To minimize the number of keypresses needed to type the given string `s`, we need to optimally distribute the characters across 9 buttons. The goal is to ensure that the most frequently used characters require the fewest keypresses.

---

### **Strategy:**
1. **Count Frequency of Each Character (`O(n)`)**
   - We first determine how often each letter appears in `s`.

2. **Sort Characters by Frequency (`O(26 log 26) ≈ O(1)`)**
   - The most frequently used characters should be assigned the most accessible key positions (first on each button).
   - Sorting in descending order ensures we allocate characters optimally.

3. **Assign Characters to Buttons (`O(26) ≈ O(1)`)**
   - Distribute characters among 9 buttons:
     - The first 9 most frequent characters are assigned to the **first press** of the buttons.
     - The next 9 are assigned to the **second press** of the buttons.
     - The last 8 are assigned to the **third press** of the buttons.
   - The press cost increases based on the assignment (first row = 1 press, second row = 2 presses, third row = 3 presses).

4. **Calculate Total Keypresses (`O(26) ≈ O(1)`)**
   - For each character in `s`, find its assigned key and compute the total presses required.

---

### **Implementation:**
```python
from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # Count frequency of each letter
        char_freq = Counter(s)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(char_freq.items(), key=lambda x: -x[1])

        total_presses = 0
        for index, (char, freq) in enumerate(sorted_chars):
            # Determine press cost based on position (0-8: 1 press, 9-17: 2 presses, 18-25: 3 presses)
            press_cost = (index // 9) + 1
            total_presses += press_cost * freq

        return total_presses
```

---

### **Complexity Analysis:**
- **Counting frequency** → `O(n)`
- **Sorting characters** → `O(26 log 26) = O(1)`
- **Assigning keys and calculating total presses** → `O(26) = O(1)`
- **Total Complexity:** **`O(n)`**, since sorting and processing are constant (`O(1)`) due to a fixed character set (26 lowercase letters).

---

### **Example Walkthrough:**
#### **Example 1:**
##### **Input:**
`s = "apple"`
##### **Step 1: Frequency Count**
```
{'a': 1, 'p': 2, 'l': 1, 'e': 1}
```
##### **Step 2: Sorting by Frequency**
```
[('p', 2), ('a', 1), ('l', 1), ('e', 1)]
```
##### **Step 3: Assign to Keypad (Press Cost)**
```
'p' -> 1st key (1 press)
'a' -> 2nd key (1 press)
'l' -> 3rd key (1 press)
'e' -> 4th key (1 press)
```
##### **Total Keypresses Calculation**
```
'p' (2 * 1) + 'a' (1 * 1) + 'l' (1 * 1) + 'e' (1 * 1) = 5
```
##### **Output:**
`5`

---

### **Why This Works Efficiently**
- Prioritizing frequently used characters ensures the **minimum** total presses.
- Sorting + greedy allocation guarantees an **optimal** mapping.
- The constant number of letters (`26`) makes this approach efficient.
