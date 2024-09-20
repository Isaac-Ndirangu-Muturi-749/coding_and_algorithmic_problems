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
