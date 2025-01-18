To solve this problem in O(log n) time, we can use a **binary search** approach. The key observation here is that if an element is smaller than its next neighbor, then a peak must exist on the right side, and if an element is larger than its next neighbor, then a peak must exist on the left side. By exploiting this property, we can apply a binary search to efficiently find the peak element.

### Approach:

1. **Binary Search**:
   - Start by initializing two pointers, `left` and `right`, at the start and end of the array, respectively.
   - In each iteration, compute the middle index `mid`.
   - If the middle element `nums[mid]` is greater than its next element `nums[mid + 1]`, it means that the peak is either at `mid` or somewhere on the left side of `mid`. So, we reduce our search space to the left half by setting `right = mid`.
   - Otherwise, if `nums[mid]` is smaller than `nums[mid + 1]`, it means that a peak must exist on the right side of `mid`, so we move our search space to the right half by setting `left = mid + 1`.
   - The search ends when `left == right`, and we return that index as the peak element.

### Code Implementation:

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Compare mid with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # The peak is on the left, including mid
                right = mid
            else:
                # The peak is on the right, excluding mid
                left = mid + 1

        # When left == right, we have found a peak
        return left
```

### Explanation:

- **Binary Search**: The algorithm performs a binary search to find a peak element.
  - In each iteration, we look at the middle element and decide which half of the array to search next based on the relationship between `nums[mid]` and `nums[mid + 1]`.
  - If `nums[mid] > nums[mid + 1]`, we know that a peak exists on the left side, so we set `right = mid`.
  - Otherwise, if `nums[mid] < nums[mid + 1]`, we know that a peak exists on the right side, so we set `left = mid + 1`.
  - The loop continues until `left` and `right` converge, and at that point, `left` (or `right`) will be the index of a peak element.

### Time Complexity:
- **O(log n)**: Since we are halving the search space in each step of the binary search, the time complexity is logarithmic with respect to the size of the input array `n`.

### Space Complexity:
- **O(1)**: The algorithm only uses a constant amount of extra space.

### Example Walkthrough:

1. **Example 1**:
   - Input: `nums = [1, 2, 3, 1]`
   - Initial `left = 0`, `right = 3`
   - `mid = (0 + 3) // 2 = 1`
     - `nums[1] = 2` and `nums[2] = 3`, so `nums[1] < nums[2]`, move `left = mid + 1 = 2`
   - Now `left = 2`, `right = 3`
   - `mid = (2 + 3) // 2 = 2`
     - `nums[2] = 3` and `nums[3] = 1`, so `nums[2] > nums[3]`, move `right = mid = 2`
   - Now `left = right = 2`, return `2`, which is the index of the peak element.

2. **Example 2**:
   - Input: `nums = [1, 2, 1, 3, 5, 6, 4]`
   - Initial `left = 0`, `right = 6`
   - `mid = (0 + 6) // 2 = 3`
     - `nums[3] = 3` and `nums[4] = 5`, so `nums[3] < nums[4]`, move `left = mid + 1 = 4`
   - Now `left = 4`, `right = 6`
   - `mid = (4 + 6) // 2 = 5`
     - `nums[5] = 6` and `nums[6] = 4`, so `nums[5] > nums[6]`, move `right = mid = 5`
   - Now `left = right = 5`, return `5`, which is the index of the peak element.

### Example Outputs:

```python
sol = Solution()

# Example 1:
print(sol.findPeakElement([1, 2, 3, 1]))  # Output: 2

# Example 2:
print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Output: 5
```

This binary search solution efficiently finds a peak element with a time complexity of O(log n).



Here's a breakdown of the peak-finding algorithm in the `findPeakElement` method step by step:

### Problem Statement:
You are given an integer array `nums` where `nums[i]` ≠ `nums[i+1]` (all elements are distinct). A **peak element** is an element that is greater than its neighbors. The goal is to find **any** peak element, meaning the algorithm should return an index where `nums[index]` is a peak. It's important to note that the array may have multiple peaks, and you just need to find one.

### Method Breakdown:

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
```
- The function takes a list of integers `nums` and returns an integer, which is the index of a peak element in the array.
- The problem is approached using binary search to achieve O(log n) time complexity.

### Step 1: Initialize left and right pointers

```python
1, r = 0, len(nums) - 1
```
- `l` is the left pointer initialized to `0`, and `r` is the right pointer initialized to the last index of the list `nums`.
- The idea is to perform binary search on the list to find a peak element efficiently.

### Step 2: Perform binary search loop

```python
while l <= r:
    m = l + ((r - l) // 2)
```
- This is the binary search loop, which continues as long as `l` (left) is less than or equal to `r` (right).
- `m` is the middle index between `l` and `r`. It’s calculated using `(r - l) // 2` to avoid potential overflow from `(l + r) // 2`.

### Step 3: Check if the middle element is a peak or adjust search range

1. **Check left neighbor**

```python
if m > 0 and nums[m] < nums[m - 1]:
    r = m - 1
```
- This condition checks if the middle element (`nums[m]`) is **less than its left neighbor** (`nums[m - 1]`).
- If the middle element is smaller than the left neighbor, the peak must lie to the left of `m` (including the left neighbor). Thus, the algorithm moves the right pointer `r` to `m - 1` to search in the left half.

2. **Check right neighbor**

```python
elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
    l = m + 1
```
- If the middle element is smaller than its **right neighbor** (`nums[m + 1]`), then the peak must lie to the right of `m`. So, the algorithm moves the left pointer `l` to `m + 1` to search in the right half.

3. **Middle element is a peak**

```python
else:
    return m
```
- If neither of the above two conditions is true (meaning `nums[m]` is **greater than both its neighbors**), then `nums[m]` is a peak, and the algorithm returns the index `m`.

### Complete Code with Fixed Formatting:
Here's the corrected version of your code with proper indentation and minor fixes:

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # Left neighbor is greater
            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            # Right neighbor is greater
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            # Current element is greater than both neighbors (it's a peak)
            else:
                return m
```

### Example Walkthrough:

#### Example: `nums = [1, 2, 3, 1]`

1. Initial values: `l = 0`, `r = 3`
   - `m = 0 + (3 - 0) // 2 = 1`
   - `nums[1] = 2`, `nums[0] = 1`, `nums[2] = 3`
   - Since `nums[2] > nums[1]`, move `l` to `m + 1` (`l = 2`).

2. Now, `l = 2`, `r = 3`
   - `m = 2 + (3 - 2) // 2 = 2`
   - `nums[2] = 3`, `nums[1] = 2`, `nums[3] = 1`
   - Since `nums[2] > nums[1]` and `nums[2] > nums[3]`, return `m = 2` (peak found).

### Time Complexity:
- The time complexity is O(log n) because the binary search divides the list in half at each step.

### Space Complexity:
- The space complexity is O(1) since only a few extra variables (`l`, `r`, and `m`) are used. No additional space grows with the input size.

This efficient approach allows you to find a peak element in logarithmic time using binary search.



The difference between using `(l + r) // 2` and `l + (r - l) // 2` to calculate the middle index in a binary search is subtle but important, especially when dealing with large numbers.

### 1. `(l + r) // 2` — Potential Overflow Issue

When calculating the middle index as `(l + r) // 2`, you're directly adding the left (`l`) and right (`r`) pointers. In most programming languages, integers are stored within a fixed range. For example, in 32-bit systems, the maximum value of an integer is \( 2^{31} - 1 \).

- **Overflow Problem**: If `l` and `r` are both large, their sum (`l + r`) might exceed the maximum value that can be stored in an integer, causing an **integer overflow**. This can result in incorrect calculations and bugs.

   **Example of Overflow**:
   ```python
   l = 2**30
   r = 2**30
   middle = (l + r) // 2  # (2^30 + 2^30) = 2^31, which could exceed the integer limit.
   ```

   Here, the sum of `l` and `r` would overflow in a system with a 32-bit integer limit.

### 2. `l + (r - l) // 2` — Safe from Overflow

By calculating the middle index using the expression `l + (r - l) // 2`, you avoid the overflow issue. This approach works by **subtracting `l` from `r` first**, which ensures that the result stays within a safe range, even for large values of `l` and `r`.

- **Why it's safe**: The difference `(r - l)` will always be less than or equal to `r`, so when you divide it by 2 and add it to `l`, it prevents any large summation of `l + r` directly.

   **Example**:
   ```python
   l = 2**30
   r = 2**30 + 100
   middle = l + (r - l) // 2  # No risk of overflow here.
   ```

   Here, `r - l` is a much smaller value (100), so adding half of it to `l` won’t cause an overflow.

### Summary of Differences:
- **`(l + r) // 2`**: Directly adds `l` and `r`, which can cause overflow if both are large values.
- **`l + (r - l) // 2`**: Subtracts first, then divides and adds, which avoids overflow and is safer when handling large integers.

In modern programming environments with dynamic types or 64-bit integers, the risk of overflow is reduced, but using `l + (r - l) // 2` is a good practice, particularly in competitive programming or environments with fixed integer limits.
