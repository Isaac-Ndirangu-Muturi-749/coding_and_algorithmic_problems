This problem can be solved using a **sliding window** approach to efficiently calculate the sum of subarrays of size \( k \) and find the one with the maximum average.

---

### Algorithm
1. **Sliding Window for Fixed-Size Subarrays**:
   - Start by calculating the sum of the first \( k \) elements of the array.
   - Slide the window over the array: add the next element to the current sum and subtract the first element of the previous window.
   - Keep track of the maximum sum encountered.

2. **Compute the Maximum Average**:
   - Divide the maximum sum by \( k \) to get the maximum average.

---

### Python Code
```python
def findMaxAverage(nums: list[int], k: int) -> float:
    # Calculate the initial sum of the first 'k' elements
    current_sum = sum(nums[:k])
    max_sum = current_sum

    # Sliding window: adjust the sum by adding the next element and removing the previous one
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    # Return the maximum average
    return max_sum / k
```

---

### Complexity
- **Time Complexity**: \(O(n)\)
  - We traverse the array once to compute the initial sum and slide the window across the array.
- **Space Complexity**: \(O(1)\)
  - Only a few variables are used; no additional space is required.

---

### Example Runs

#### Example 1
```python
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))  # Output: 12.75000
```
- Initial sum: \( 1 + 12 - 5 - 6 = 2 \)
- Sliding window updates:
  - Add \( 50 \), remove \( 1 \): \( 2 + 50 - 1 = 51 \)
  - Add \( 3 \), remove \( 12 \): \( 51 + 3 - 12 = 42 \)
- Maximum sum: \( 51 \)
- Maximum average: \( 51 / 4 = 12.75 \)

---

#### Example 2
```python
nums = [5]
k = 1
print(findMaxAverage(nums, k))  # Output: 5.00000
```
- Single element \( 5 \): Average is \( 5 \).

---

This approach ensures efficient computation for large arrays, as required by the constraints.
