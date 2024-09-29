To solve the problem of finding the index of a target value in a possibly rotated sorted array, we can leverage **binary search** to achieve the required `O(log n)` time complexity.

### Key Observations:
- The array is sorted but possibly rotated, so it contains two sorted parts.
- We can still apply a modified binary search to find the target efficiently by determining which part of the array is sorted at each step.

### Approach:
1. **Binary Search**: Start with two pointers, `left` and `right`, representing the start and end of the array.
2. **Identify Sorted Half**: In each step of binary search, check which half of the array (left or right) is sorted by comparing the values at `mid` and the boundaries (`left` and `right`).
   - If the left half is sorted, check if the target lies within this range. If it does, continue searching in the left half; otherwise, search in the right half.
   - If the right half is sorted, do a similar check for the target in this half.
3. **Repeat**: Adjust the `left` and `right` pointers accordingly until the target is found or the pointers cross (indicating the target is not in the array).

### Algorithm:

```python
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is at the mid position
        if nums[mid] == target:
            return mid

        # Determine which part of the array is sorted
        if nums[left] <= nums[mid]:
            # Left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is in the left part
            else:
                left = mid + 1  # Target is in the right part
        else:
            # Right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1  # Target is in the right part
            else:
                right = mid - 1  # Target is in the left part

    # Target was not found
    return -1
```

### Explanation:
1. **Initialization**: We start with `left = 0` and `right = len(nums) - 1` (the first and last indices of the array).
2. **Binary Search Loop**:
   - Compute `mid` as the middle index between `left` and `right`.
   - If `nums[mid] == target`, return `mid`.
   - If the left part (`nums[left]` to `nums[mid]`) is sorted (`nums[left] <= nums[mid]`), check if the target lies between `nums[left]` and `nums[mid]`. If yes, search in the left half by moving `right` to `mid - 1`. Otherwise, search the right half by moving `left` to `mid + 1`.
   - If the right part (`nums[mid]` to `nums[right]`) is sorted, check if the target lies between `nums[mid]` and `nums[right]`. If yes, search in the right half by moving `left` to `mid + 1`. Otherwise, search in the left half by moving `right` to `mid - 1`.
3. **Exit Condition**: If the target is not found, the loop terminates, and we return `-1`.

### Time Complexity:
- **Time complexity**: `O(log n)` because we are performing binary search, which halves the search space in each iteration.
- **Space complexity**: `O(1)` as we are only using a few extra variables for pointers and indices.

### Example Walkthrough:

#### Example 1:
Input: `nums = [4,5,6,7,0,1,2]`, `target = 0`
- Step 1: `left = 0`, `right = 6`, `mid = 3` → `nums[mid] = 7`
  - The left part `[4,5,6,7]` is sorted, and `target = 0` is not in this range, so search the right part.
  - Update `left = mid + 1 = 4`.
- Step 2: `left = 4`, `right = 6`, `mid = 5` → `nums[mid] = 1`
  - The left part `[0,1]` is sorted, and `target = 0` is in this range.
  - Update `right = mid - 1 = 4`.
- Step 3: `left = 4`, `right = 4`, `mid = 4` → `nums[mid] = 0`
  - Found the target at index `4`.

#### Example 2:
Input: `nums = [4,5,6,7,0,1,2]`, `target = 3`
- The binary search will explore both sides but will not find the target, so it returns `-1`.

#### Example 3:
Input: `nums = [1]`, `target = 0`
- The array has only one element, and since it’s not the target, the function will return `-1`.

This solution efficiently handles the rotated sorted array and finds the target in `O(log n)` time complexity using binary search principles.
