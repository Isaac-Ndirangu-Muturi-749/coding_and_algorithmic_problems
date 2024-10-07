To solve the problem of removing all occurrences of a given value `val` from an array `nums` in place, and returning the number of remaining elements, we can use a two-pointer approach. This technique allows us to efficiently update the array without requiring additional space.

### Approach:

1. **Two-Pointer Technique**:
   - Use one pointer, `i`, to iterate through the array.
   - Use another pointer, `k`, to keep track of the position where the next valid element (an element not equal to `val`) should be placed.
   - As you iterate through the array with `i`, whenever you encounter an element not equal to `val`, you move it to the position indicated by `k` and increment `k`.

2. **In-Place Modification**:
   - Modify the array in place by moving non-`val` elements to the beginning.
   - The elements after the first `k` positions are irrelevant, as the problem specifies that the remaining elements don't matter.

3. **Return Value**:
   - Return `k`, the number of elements that are not equal to `val`.

### Example Walkthrough:

#### Example 1:
- **Input**: `nums = [3, 2, 2, 3]`, `val = 3`
- **Process**:
  - Start with `k = 0`.
  - Iterate through `nums`:
    - At `i = 0`, `nums[0]` is `3`, which equals `val`, so do nothing.
    - At `i = 1`, `nums[1]` is `2`, which is not `val`, so set `nums[k] = nums[1]`, and increment `k` to 1.
    - At `i = 2`, `nums[2]` is `2`, which is not `val`, so set `nums[k] = nums[2]`, and increment `k` to 2.
    - At `i = 3`, `nums[3]` is `3`, which equals `val`, so do nothing.
  - **Output**: `k = 2`, `nums = [2, 2, _, _]` (where `_` represents irrelevant elements).

#### Example 2:
- **Input**: `nums = [0, 1, 2, 2, 3, 0, 4, 2]`, `val = 2`
- **Process**:
  - Start with `k = 0`.
  - Iterate through `nums`:
    - Place non-`val` elements in the first `k` positions.
  - **Output**: `k = 5`, `nums = [0, 1, 3, 0, 4, _, _, _]`.

### Implementation in Python:

```python
class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        k = 0  # Pointer to store the position of the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k  # k is the number of elements not equal to val
```

### Explanation:

- **Time Complexity**: O(n), where n is the length of the `nums` array. We iterate through the array exactly once.
- **Space Complexity**: O(1), since we are modifying the array in place and not using any extra space proportional to the input size.

### Testing:

```python
solution = Solution()

# Test case 1
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
assert k == 2
assert sorted(nums[:k]) == [2, 2]

# Test case 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
assert k == 5
assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

print("All test cases passed!")
```

This solution effectively removes all occurrences of `val` from `nums` and returns the count of elements that remain, ensuring that the array is modified in place as required.
