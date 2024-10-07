To solve the problem of finding the length of the longest strictly increasing subsequence (LIS) in an integer array, we can use two approaches:

### 1. Dynamic Programming (O(n²) approach):
This is the classical approach to solve the LIS problem. We can use dynamic programming to keep track of the length of the longest subsequence ending at each index of the array.

#### Approach:
- Define a `dp` array where `dp[i]` represents the length of the longest increasing subsequence that ends at index `i`.
- Initialize each element of the `dp` array with `1`, as the smallest subsequence can be the number itself.
- For each index `i`, look at all previous indices `j` (where `j < i`) and if `nums[j] < nums[i]`, update `dp[i]` as `dp[i] = max(dp[i], dp[j] + 1)`.
- The answer will be the maximum value in the `dp` array.

#### Code:

```python
def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] = length of LIS ending at index i

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

#### Explanation:
- We initialize the `dp` array with `1` because every number is an increasing subsequence by itself.
- For each `i`, we compare it to all the previous elements to see if we can extend the increasing subsequence.
- Time complexity: **O(n²)**, as we have two nested loops.
- Space complexity: **O(n)**, as we store the LIS length at each index.

### 2. Binary Search (O(n log n) approach):
This is an optimized approach that leverages binary search to achieve better time complexity. The key idea is to maintain an array `tails` where `tails[i]` represents the smallest ending element of an increasing subsequence of length `i+1`.

#### Approach:
- Traverse through the array and use binary search to either replace an element in `tails` or extend the array.
- For each element in `nums`, if it is larger than the largest element in `tails`, append it. Otherwise, replace the first element in `tails` that is greater than or equal to the current element (using binary search).

#### Code:

```python
import bisect

def lengthOfLIS(nums):
    tails = []

    for num in nums:
        # Find the index where `num` can replace an element in `tails`
        idx = bisect.bisect_left(tails, num)

        # If num is larger than any element in tails, append it
        if idx == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the element at index `idx`
            tails[idx] = num

    return len(tails)
```

#### Explanation:
- We use `bisect_left` to find the first position in `tails` where the current element can replace an element or be appended.
- The `tails` array will not represent a valid subsequence but will store the smallest possible ending elements for subsequences of different lengths.
- Time complexity: **O(n log n)**, since we perform a binary search for each element.
- Space complexity: **O(n)**, as the `tails` array stores at most `n` elements.

### Example Walkthrough:

For the input `nums = [10,9,2,5,3,7,101,18]`:

1. **Step-by-step using binary search approach**:
   - Initialize `tails = []`.
   - For `10`, append to `tails`: `tails = [10]`.
   - For `9`, replace `10` with `9`: `tails = [9]`.
   - For `2`, replace `9` with `2`: `tails = [2]`.
   - For `5`, append to `tails`: `tails = [2, 5]`.
   - For `3`, replace `5` with `3`: `tails = [2, 3]`.
   - For `7`, append to `tails`: `tails = [2, 3, 7]`.
   - For `101`, append to `tails`: `tails = [2, 3, 7, 101]`.
   - For `18`, replace `101` with `18`: `tails = [2, 3, 7, 18]`.

   The final `tails` array is `[2, 3, 7, 18]`, and the length is `4`.

Thus, the length of the longest increasing subsequence is **4**.


Here’s how you can implement the **O(n log n)** solution for the **Longest Increasing Subsequence** without using the `bisect` module but still using the idea of binary search manually:

### Approach:

- The idea is still to maintain an array `tails`, where each element at index `i` represents the smallest possible tail of an increasing subsequence of length `i+1`.
- For each number in `nums`, we will perform a binary search manually on the `tails` array to either replace an element or extend the array.

### Code:

```python
def lengthOfLIS(nums):
    def binary_search(tails, target):
        # Binary search to find the first index in tails where tails[i] >= target
        left, right = 0, len(tails) - 1
        while left <= right:
            mid = (left + right) // 2
            if tails[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    tails = []

    for num in nums:
        idx = binary_search(tails, num)  # Perform binary search to find the insertion position

        # If num is larger than all elements in tails, append it
        if idx == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the element at index `idx`
            tails[idx] = num

    return len(tails)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output: 4
```

### Explanation:

1. **Binary Search Implementation**:
   - The function `binary_search` finds the index at which a given number `num` can either replace an element in `tails` or be appended. It looks for the smallest index where the value in `tails` is greater than or equal to `num`.
   - If no such value is found, the number is larger than all elements in `tails`, and it is appended to the end.

2. **Main Logic**:
   - For each number `num` in `nums`, we find the appropriate index in `tails` using binary search.
   - If `num` is larger than all elements in `tails`, we append it to the array.
   - Otherwise, we replace the first element in `tails` that is greater than or equal to `num`.

3. **Time Complexity**:
   - The binary search operation takes **O(log n)**, and since we perform this for each element in `nums`, the overall time complexity is **O(n log n)**.

4. **Space Complexity**:
   - The space complexity is **O(n)** due to the `tails` array.

### Example Walkthrough:

For `nums = [10, 9, 2, 5, 3, 7, 101, 18]`:

1. `tails = []`
2. For `10`: `tails = [10]`
3. For `9`: replace `10` with `9`, so `tails = [9]`
4. For `2`: replace `9` with `2`, so `tails = [2]`
5. For `5`: append `5`, so `tails = [2, 5]`
6. For `3`: replace `5` with `3`, so `tails = [2, 3]`
7. For `7`: append `7`, so `tails = [2, 3, 7]`
8. For `101`: append `101`, so `tails = [2, 3, 7, 101]`
9. For `18`: replace `101` with `18`, so `tails = [2, 3, 7, 18]`

Thus, the length of the longest increasing subsequence is **4** (`[2, 3, 7, 101]`).
