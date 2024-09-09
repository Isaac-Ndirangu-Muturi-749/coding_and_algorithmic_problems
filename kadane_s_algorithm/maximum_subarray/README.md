To solve the problem of finding the subarray with the largest sum in an array, we can use **Kadane's Algorithm**, which is an efficient approach with a time complexity of O(n). Here's how it works:

### Explanation of Kadane's Algorithm:

1. **Initialize two variables**:
   - `current_sum`: The sum of the current subarray.
   - `max_sum`: The maximum sum encountered so far.

2. **Iterate over the array**:
   - For each element in the array, update `current_sum` as the maximum between the current element and the sum of `current_sum` and the current element.
   - Update `max_sum` to be the maximum of `max_sum` and `current_sum`.

3. The idea is to decide at each step whether to continue the current subarray or start a new subarray from the current element.

### Python Code Implementation:

```python
class Solution:
    def maxSubArray(self, nums):
        # Initialize the current sum and maximum sum to the first element
        current_sum = max_sum = nums[0]

        # Traverse the rest of the array
        for num in nums[1:]:
            # Update current_sum
            current_sum = max(num, current_sum + num)
            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)

        return max_sum
```

### Example Usage:

```python
solution = Solution()

# Test case 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums1))  # Output: 6

# Test case 2
nums2 = [1]
print(solution.maxSubArray(nums2))  # Output: 1

# Test case 3
nums3 = [5, 4, -1, 7, 8]
print(solution.maxSubArray(nums3))  # Output: 23
```

### Explanation of Example Outputs:
- **Test case 1**: The subarray `[4, -1, 2, 1]` gives the maximum sum of `6`.
- **Test case 2**: The only element in the array is `1`, so the maximum sum is `1`.
- **Test case 3**: The entire array `[5, 4, -1, 7, 8]` gives the maximum sum of `23`.

### Time Complexity:
- **O(n)** where `n` is the number of elements in the array. We only traverse the array once.

### Space Complexity:
- **O(1)** because we only use a constant amount of extra space regardless of the size of the input array.


Let's break down the `maxSubArray` function, which solves the **maximum subarray sum** problem using **Kadane's Algorithm**. This algorithm finds the maximum sum of a contiguous subarray in a given array of integers.

### 1. **Initialization**:
```python
current_sum = max_sum = nums[0]
```
- The `current_sum` and `max_sum` are both initialized to the first element of the array (`nums[0]`). This is because the subarray can start with just the first element.

### 2. **Iterate through the Array**:
```python
for num in nums[1:]:
```
- We iterate through the rest of the array, starting from the second element (`nums[1]`), since the first element is already used to initialize `current_sum` and `max_sum`.

### 3. **Update the Current Sum**:
```python
current_sum = max(num, current_sum + num)
```
- For each element `num`, we calculate whether it's better to start a new subarray at this element or to continue the existing subarray:
  - If `num` is larger than `current_sum + num`, it's better to start a new subarray from `num`.
  - Otherwise, we continue the current subarray by adding `num` to `current_sum`.

### 4. **Update the Maximum Sum**:
```python
max_sum = max(max_sum, current_sum)
```
- After updating `current_sum`, we check if it's larger than the current `max_sum`. If it is, we update `max_sum`.

### 5. **Return the Maximum Sum**:
```python
return max_sum
```
- Finally, after processing all elements, we return the maximum sum found.

### Example Walkthrough:

Let's use the input `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]` to illustrate how the algorithm works:

1. **Initialization**:
   - `current_sum = max_sum = nums[0] = -2`.

2. **Iteration**:
   - **Step 1** (`num = 1`):
     - `current_sum = max(1, -2 + 1) = 1`.
     - `max_sum = max(-2, 1) = 1`.
   - **Step 2** (`num = -3`):
     - `current_sum = max(-3, 1 + -3) = -2`.
     - `max_sum = max(1, -2) = 1`.
   - **Step 3** (`num = 4`):
     - `current_sum = max(4, -2 + 4) = 4`.
     - `max_sum = max(1, 4) = 4`.
   - **Step 4** (`num = -1`):
     - `current_sum = max(-1, 4 + -1) = 3`.
     - `max_sum = max(4, 3) = 4`.
   - **Step 5** (`num = 2`):
     - `current_sum = max(2, 3 + 2) = 5`.
     - `max_sum = max(4, 5) = 5`.
   - **Step 6** (`num = 1`):
     - `current_sum = max(1, 5 + 1) = 6`.
     - `max_sum = max(5, 6) = 6`.
   - **Step 7** (`num = -5`):
     - `current_sum = max(-5, 6 + -5) = 1`.
     - `max_sum = max(6, 1) = 6`.
   - **Step 8** (`num = 4`):
     - `current_sum = max(4, 1 + 4) = 5`.
     - `max_sum = max(6, 5) = 6`.

3. **Return the Maximum Sum**:
   - After processing all elements, the `max_sum` is `6`, which is the maximum sum of a contiguous subarray (`[4, -1, 2, 1]`).

### Final Output:
The function returns `6` as the maximum sum.
