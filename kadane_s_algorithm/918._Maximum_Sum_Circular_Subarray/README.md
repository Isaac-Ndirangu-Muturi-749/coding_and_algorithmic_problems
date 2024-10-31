To solve this problem, we need to consider both **standard subarrays** (without circular wrapping) and **circular subarrays** (with circular wrapping).

### Key Approach:

1. **Standard Subarray Maximum Sum (Kadane’s Algorithm):**
   - Use Kadane’s algorithm to find the maximum sum of a non-empty subarray in the usual way, without considering circular wrapping.

2. **Circular Subarray Maximum Sum:**
   - The maximum sum of a circular subarray can be obtained by calculating the **minimum subarray sum** and then using the total sum of the array. The idea is:
     - If we take the total sum of the array and subtract the minimum subarray sum, we effectively get the sum of the elements not included in the minimum subarray.
     - This approach works because if the array has a significant subarray with minimum values, subtracting it maximizes the sum of the remaining elements.

3. **Final Calculation:**
   - Compute two potential results:
     - The **maximum sum** obtained by Kadane’s (standard maximum subarray).
     - The **circular maximum sum**, which is `total_sum - minimum_subarray_sum`.
   - If all elements in `nums` are negative, the circular sum can lead to zero, so we should only consider Kadane’s result.

4. **Edge Case:**
   - If the maximum subarray is from Kadane’s and does not involve wrapping, the final result is just Kadane’s result.

### Solution:

```python
def maxSubarraySumCircular(nums):
    # Helper function to calculate maximum subarray sum (Kadane's algorithm)
    def kadane_max(arr):
        max_current = max_global = arr[0]
        for num in arr[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global

    # Helper function to calculate minimum subarray sum
    def kadane_min(arr):
        min_current = min_global = arr[0]
        for num in arr[1:]:
            min_current = min(num, min_current + num)
            min_global = min(min_global, min_current)
        return min_global

    # Total sum of array
    total_sum = sum(nums)

    # Calculate max subarray sum without circular wrapping
    max_kadane = kadane_max(nums)

    # Calculate min subarray sum for the circular case
    min_kadane = kadane_min(nums)

    # Calculate the circular max sum
    if max_kadane < 0:
        # All elements are negative, return the max single element
        return max_kadane
    else:
        return max(max_kadane, total_sum - min_kadane)

# Example usage:
print(maxSubarraySumCircular([1, -2, 3, -2]))  # Output: 3
print(maxSubarraySumCircular([5, -3, 5]))      # Output: 10
print(maxSubarraySumCircular([-3, -2, -3]))    # Output: -2
```

### Explanation:

1. **Kadane’s Algorithm (Maximum Subarray)**:
   - Finds the maximum subarray without circular wrapping.

2. **Minimum Subarray Sum**:
   - Used to calculate the circular subarray by taking `total_sum - min_subarray_sum`.

3. **Final Calculation**:
   - Return the maximum of `max_kadane` (non-circular) and `total_sum - min_kadane` (circular).

### Complexity:
- **Time Complexity**: \(O(n)\) since we pass through the array only a few times.
- **Space Complexity**: \(O(1)\), only a constant amount of extra space.

This solution is efficient and works within the constraints.
