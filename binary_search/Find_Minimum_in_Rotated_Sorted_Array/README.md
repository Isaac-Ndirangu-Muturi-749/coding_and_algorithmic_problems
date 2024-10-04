To find the minimum element in a rotated sorted array in O(log n) time, we can use a **modified binary search** approach. The key observation is that even though the array is rotated, one half of the array will still be sorted.

### Approach:

1. **Binary Search Setup**: We use two pointers, `left` and `right`, to perform binary search. The goal is to shrink the search space while determining which half of the array contains the minimum element.

2. **Compare mid with the right end**:
   - If `nums[mid]` is greater than `nums[right]`, it means the minimum element is in the right half (because the left half is sorted, but the smallest element is in the unsorted portion).
   - If `nums[mid]` is less than or equal to `nums[right]`, it means the minimum element is in the left half (or `mid` could be the minimum itself).

3. **Edge case**: If the array is not rotated (i.e., it is fully sorted), the first element will be the minimum. This is naturally handled by the algorithm.

### Algorithm:

1. Start with `left = 0` and `right = n - 1`.
2. Compute `mid = (left + right) // 2`.
3. Compare `nums[mid]` with `nums[right]`:
   - If `nums[mid] > nums[right]`, the minimum must be in the right half, so move `left` to `mid + 1`.
   - Otherwise, the minimum is in the left half (or `mid` itself), so move `right` to `mid`.
4. Continue until `left == right`. At this point, `left` will be the index of the minimum element.

### Code Implementation:

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Binary search loop
        while left < right:
            mid = (left + right) // 2

            # Compare mid element with the rightmost element
            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Minimum is in the left half (including mid)
                right = mid

        # When left == right, we found the minimum element
        return nums[left]
```

### Explanation:

- **Initialization**: We set `left` to the beginning of the array and `right` to the end.
- **Binary Search**:
  - We compute `mid` and compare `nums[mid]` with `nums[right]`.
  - If `nums[mid] > nums[right]`, the minimum is in the right half, so we adjust `left`.
  - If `nums[mid] <= nums[right]`, the minimum is in the left half, so we adjust `right`.
- **Termination**: When `left == right`, the minimum element has been found, and it is located at index `left`.

### Example Walkthrough:

#### Example 1:
- **Input**: `nums = [3,4,5,1,2]`
- Initial `left = 0`, `right = 4`
  - `mid = 2`, `nums[mid] = 5`, `nums[right] = 2`
  - Since `5 > 2`, the minimum is in the right half, so we set `left = 3`.
- Now `left = 3`, `right = 4`
  - `mid = 3`, `nums[mid] = 1`, `nums[right] = 2`
  - Since `1 <= 2`, the minimum is in the left half, so we set `right = 3`.
- Now `left == right`, so `nums[3] = 1` is the minimum element.
- **Output**: `1`

#### Example 2:
- **Input**: `nums = [4,5,6,7,0,1,2]`
- Initial `left = 0`, `right = 6`
  - `mid = 3`, `nums[mid] = 7`, `nums[right] = 2`
  - Since `7 > 2`, the minimum is in the right half, so we set `left = 4`.
- Now `left = 4`, `right = 6`
  - `mid = 5`, `nums[mid] = 1`, `nums[right] = 2`
  - Since `1 <= 2`, the minimum is in the left half, so we set `right = 5`.
- Now `left = 4`, `right = 5`
  - `mid = 4`, `nums[mid] = 0`, `nums[right] = 1`
  - Since `0 <= 1`, the minimum is in the left half, so we set `right = 4`.
- Now `left == right`, so `nums[4] = 0` is the minimum element.
- **Output**: `0`

### Time and Space Complexity:

- **Time Complexity**: O(log n) — We halve the search space at each step, resulting in logarithmic time complexity.
- **Space Complexity**: O(1) — We only use a few variables to keep track of the indices, so the space complexity is constant.

### Summary:
This approach leverages binary search to efficiently find the minimum element in a rotated sorted array. By comparing the mid-point element with the rightmost element, we can determine which half contains the minimum element and reduce the search space accordingly.
