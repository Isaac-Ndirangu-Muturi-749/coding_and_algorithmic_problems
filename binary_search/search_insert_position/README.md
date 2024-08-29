To solve the problem of finding the index of a target value in a sorted array or where it would be inserted, we can use **binary search**. Binary search provides an efficient way to find an element or the insertion point in \( O(\log n) \) time complexity, which is required for this problem.

### Approach:

1. **Binary Search**:
   - Use binary search to efficiently locate the target or determine the correct insertion position.
   - Initialize two pointers, `left` and `right`, to define the search range.
   - While `left` is less than or equal to `right`:
     - Compute the middle index.
     - Compare the middle element with the target:
       - If the middle element is equal to the target, return the middle index.
       - If the target is less than the middle element, adjust the search range to the left half.
       - If the target is greater than the middle element, adjust the search range to the right half.
   - If the target is not found, `left` will point to the correct insertion position.

### Implementation:

Here's the implementation in Python:

```python
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
```

### Explanation:

- **Binary Search Process**:
  - **Initialization**: Set `left` to 0 and `right` to the last index of `nums`.
  - **Loop**: Continue while `left` is less than or equal to `right`.
    - **Mid Calculation**: Compute the middle index `mid`.
    - **Comparison**:
      - If `nums[mid]` equals the `target`, return `mid`.
      - If `nums[mid]` is less than the `target`, move the `left` pointer to `mid + 1`.
      - If `nums[mid]` is greater than the `target`, move the `right` pointer to `mid - 1`.
  - **Insertion Point**: When the loop ends, `left` is the index where `target` would be inserted.

### Examples:

1. **Example 1**:
   - **Input**: `nums = [1,3,5,6]`, `target = 5`
   - **Output**: `2` (target is found at index 2)

2. **Example 2**:
   - **Input**: `nums = [1,3,5,6]`, `target = 2`
   - **Output**: `1` (target would be inserted at index 1)

3. **Example 3**:
   - **Input**: `nums = [1,3,5,6]`, `target = 7`
   - **Output**: `4` (target would be inserted at index 4)

### Testing:

You can test the solution using the following code:

```python
def run_tests():
    solution = Solution()

    # Test case 1
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2, "Test case 1 failed"

    # Test case 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1, "Test case 2 failed"

    # Test case 3
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
```

### Conclusion:

Using binary search is efficient and meets the \( O(\log n) \) time complexity requirement. The provided implementation ensures that you either find the target's index or determine where it should be inserted in a sorted array.
