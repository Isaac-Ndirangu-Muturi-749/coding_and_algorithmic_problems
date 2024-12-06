To solve this problem, we can use the **sliding window technique**. The idea is to maintain a window in the array that contains at most `k` zeros, and expand or contract the window to maximize the count of consecutive ones.

---

### **Algorithm**

1. **Initialize Pointers**:
   - Use two pointers (`left` and `right`) to define the current window.
   - Use a variable `zeros_count` to track the number of zeros in the current window.

2. **Expand the Window**:
   - Move the `right` pointer to expand the window.
   - If the element at `nums[right]` is `0`, increment `zeros_count`.

3. **Shrink the Window**:
   - If `zeros_count` exceeds `k`, move the `left` pointer to shrink the window until `zeros_count <= k`.

4. **Update the Maximum Length**:
   - Keep track of the maximum length of the valid window during the process.

5. **Return the Maximum Length**:
   - The answer is the maximum length of the window where we have at most `k` zeros.

---

### **Python Implementation**

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros_count = 0
        max_length = 0

        for right in range(len(nums)):
            # Expand the window
            if nums[right] == 0:
                zeros_count += 1

            # Shrink the window if zeros_count exceeds k
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Update max_length
            max_length = max(max_length, right - left + 1)

        return max_length
```

---

### **Explanation**

#### Example 1:
```python
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

# Sliding window process:
# Expand right pointer:
# - Window: [1,1,1,0,0], zeros_count = 2
# - Expand further: [1,1,1,0,0,1,1,1,1], zeros_count = 2 (valid window)
# - Max length: 6
```
**Output**: `6`

#### Example 2:
```python
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

# Sliding window process:
# Expand right pointer:
# - Window: [0,0,1,1,1,1,1,1,1,1,1], zeros_count = 3
# - Expand further: [1,1,0,0,0,1,1,1,1], zeros_count = 3 (valid window)
# - Max length: 10
```
**Output**: `10`

---

### **Complexity Analysis**

1. **Time Complexity**:
   - The `right` pointer traverses the array once, and the `left` pointer moves at most once for every position of `right`.
   - Total: \(O(n)\), where \(n\) is the length of the array.

2. **Space Complexity**:
   - We use only a few variables, so the space complexity is \(O(1)\).

This solution is efficient and works well for large arrays.
