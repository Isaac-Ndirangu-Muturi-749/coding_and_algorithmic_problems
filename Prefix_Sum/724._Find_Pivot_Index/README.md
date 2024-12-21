Here’s how to calculate the pivot index using a single pass approach for efficiency:

---

### **Approach**

1. **Total Sum**:
   - Calculate the total sum of the array (`total_sum`).

2. **Left Sum**:
   - Traverse the array while maintaining a running sum of the elements to the left of the current index (`left_sum`).

3. **Pivot Condition**:
   - At each index, check if the `left_sum` is equal to `total_sum - left_sum - nums[i]`:
     - `left_sum`: Sum of elements to the left of the current index.
     - `total_sum - left_sum - nums[i]`: Sum of elements to the right of the current index.

4. **Return Index**:
   - If the condition is met, return the current index.
   - If no such index exists, return `-1`.

---

### **Implementation**

```python
def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i, num in enumerate(nums):
        # Check if left sum equals right sum
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num

    return -1
```

---

### **Example Walkthrough**

#### Example 1:
**Input**:
```python
nums = [1, 7, 3, 6, 5, 6]
```

**Output**:
```python
3
```

**Explanation**:
- `total_sum = 28`
- At index `3`, `left_sum = 11` and `right_sum = 11`.

#### Example 2:
**Input**:
```python
nums = [1, 2, 3]
```

**Output**:
```python
-1
```

**Explanation**:
- No index satisfies the condition.

#### Example 3:
**Input**:
```python
nums = [2, 1, -1]
```

**Output**:
```python
0
```

**Explanation**:
- At index `0`, `left_sum = 0` and `right_sum = 0`.

---

### **Complexity Analysis**

1. **Time Complexity**:
   - \(O(n)\): Single traversal of the array.

2. **Space Complexity**:
   - \(O(1)\): No additional space required.

This solution is efficient and meets the constraints provided in the problem.
