To solve this problem, we need to modify the input array `nums` in-place such that each unique element appears at most twice, while maintaining the relative order of the elements. The array is sorted, so duplicates will appear next to each other.

### Approach:
We can use a two-pointer approach:
1. **First Pointer (current position)**: Iterate through the array to check each element.
2. **Second Pointer (write position)**: Track the position where the next valid element should be placed.

### Steps:
1. Use a `write` pointer that starts at index 0. This pointer will track where the next valid element should be written.
2. Traverse through the `nums` array starting from index 2 (since the first two elements are automatically valid).
3. For each element `nums[i]`, check if it is the same as `nums[write-2]`:
   - If it is the same, we skip it because we would exceed the "at most twice" rule.
   - If it is different, we write it to `nums[write]` and increment `write`.
4. At the end, `write` will represent the length of the modified array with the desired properties.

### Code Implementation:

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2  # Start from the third element position

        # Iterate over the array from the third element onwards
        for i in range(2, len(nums)):
            # If the current element is different from the element two steps back, keep it
            if nums[i] != nums[write - 2]:
                nums[write] = nums[i]
                write += 1

        return write
```

### Explanation:

- **Initial Case**: We can always keep the first two elements because they are valid according to the problem's constraint of "at most twice".
- **Loop through from the third element**: For each element, compare it with the element at position `write - 2`:
  - If it's different, this means we haven't yet added more than two occurrences of this element, so we can write it to `nums[write]` and increment `write`.
  - If it's the same as `nums[write - 2]`, we skip the element because adding it would exceed the allowed number of duplicates.
- **Final Result**: After the loop, `write` will contain the length of the modified array, and the first `write` elements in `nums` will have the correct values.

### Time Complexity:
- **O(n)**: We traverse the array once.

### Space Complexity:
- **O(1)**: We do not use any additional space apart from a few variables.

### Example Walkthrough:

**Example 1**:
```python
nums = [1, 1, 1, 2, 2, 3]
```

1. Initial array: `[1, 1, 1, 2, 2, 3]`
2. Start from the third element (`nums[2] = 1`), check with `nums[0] = 1`:
   - Since they are the same, skip `nums[2]`.
3. Move to `nums[3] = 2`, check with `nums[1] = 1`:
   - Since they are different, write `nums[3] = 2` to `nums[2]`. Now, `nums = [1, 1, 2, 2, 2, 3]`.
4. Move to `nums[4] = 2`, check with `nums[2] = 2`:
   - Since they are the same, skip `nums[4]`.
5. Move to `nums[5] = 3`, check with `nums[3] = 2`:
   - Since they are different, write `nums[5] = 3` to `nums[4]`. Now, `nums = [1, 1, 2, 2, 3, 3]`.

**Example 2**:
```python
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
```

1. Initial array: `[0, 0, 1, 1, 1, 1, 2, 3, 3]`
2. Move through the elements, skipping the third and fourth occurrences of `1`, and processing the rest similarly.

### Final Result:

The solution efficiently removes extra duplicates, preserving the order, and operates in O(n) time and O(1) space.


