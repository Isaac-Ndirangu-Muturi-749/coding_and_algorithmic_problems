### **Optimal Solution: Sliding Window + HashSet**

We need to find the **maximum subarray sum** of all subarrays of length `k` where **all elements are distinct**.

---

### **Approach**

1. **Sliding Window with HashSet:**
   - Use a **sliding window** of length `k` to efficiently calculate the sum of subarrays.
   - Use a **HashSet** to check if all elements in the current window are distinct.

2. **Algorithm:**
   - Initialize:
     - `window_sum` to store the sum of the current window.
     - `max_sum` to keep track of the maximum sum of all valid windows.
     - `window_set` as a set to check for distinct elements.
   - Use two pointers:
     - `left` as the start of the window.
     - `right` as the end of the window.
   - Expand the window by moving `right` pointer.
     - If the element is **not in the set**:
       - Add it to `window_sum` and `window_set`.
       - If window size becomes `k`, check if it's the maximum sum.
     - If the element **is in the set**:
       - **Shrink the window** from the left until the element is removed.
   - Continue sliding the window until `right` reaches the end of the array.

---

### **Edge Cases to Consider**
- If no valid subarray is found, return `0`.
- If `k` is greater than the number of unique elements, no valid subarray exists.

---

### **Complexity Analysis**
- **Time Complexity:** \( O(N) \)
  - Each element is added and removed from the set at most once.
- **Space Complexity:** \( O(k) \)
  - The HashSet stores at most `k` elements.

---

### **Python Code Implementation**

```python
def maximumSubarraySum(nums: list[int], k: int) -> int:
    window_sum = 0
    max_sum = 0
    window_set = set()
    left = 0

    for right in range(len(nums)):
        # If we see a duplicate, move the left pointer to maintain distinct elements
        while nums[right] in window_set:
            window_set.remove(nums[left])
            window_sum -= nums[left]
            left += 1

        # Add the current element to the window
        window_set.add(nums[right])
        window_sum += nums[right]

        # If the window length equals k, check the sum
        if (right - left + 1) == k:
            max_sum = max(max_sum, window_sum)
            # Move left pointer to slide the window
            window_set.remove(nums[left])
            window_sum -= nums[left]
            left += 1

    return max_sum
```

---

### **Example Walkthrough**

#### **Example 1**
```python
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maximumSubarraySum(nums, k))  # Output: 15
```
- Subarrays of length `3` are:
  - `[1, 5, 4]` → Sum = `10`
  - `[5, 4, 2]` → Sum = `11`
  - `[4, 2, 9]` → Sum = `15` ✔
  - `[2, 9, 9]` → Not valid (duplicate `9`)
  - `[9, 9, 9]` → Not valid (duplicate `9`)
- Maximum valid sum = `15`

---

#### **Example 2**
```python
nums = [4, 4, 4]
k = 3
print(maximumSubarraySum(nums, k))  # Output: 0
```
- Subarray of length `3`:
  - `[4, 4, 4]` → Not valid (duplicate `4`)
- No valid subarray, return `0`.

---

### **Why This Solution is Efficient**
- The sliding window approach avoids the need to re-compute the sum from scratch, leading to **O(N)** complexity.
- Using a HashSet ensures **O(1)** time complexity for insertion and lookup, effectively managing the distinctness check.

This solution is optimal and efficiently handles the constraints, including large input sizes (`10^5`). 🚀
