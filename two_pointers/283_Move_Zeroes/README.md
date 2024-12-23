The problem can be solved efficiently using a two-pointer technique to shift all non-zero elements to the front while moving zeros to the back in place. Here's the solution:

### Algorithm
1. **Two Pointers**:
   - Use a pointer `non_zero_pos` to track where the next non-zero element should be placed.
   - Use a pointer `i` to traverse the array.
2. **Swap Non-Zero Elements**:
   - Whenever a non-zero element is encountered, place it at `non_zero_pos` and increment `non_zero_pos`.
3. **Fill Zeros**:
   - Once all non-zero elements are moved, fill the remaining elements of the array with zeros.

### Python Code
```python
def moveZeroes(nums: list[int]) -> None:
    non_zero_pos = 0  # Position to place the next non-zero element

    # Traverse the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
            non_zero_pos += 1
```

### Explanation
1. **Initialization**:
   - Start with `non_zero_pos = 0` to track the position for the next non-zero element.
2. **Traverse and Swap**:
   - Iterate through the array. If a non-zero element is found, swap it with the element at `non_zero_pos` and increment `non_zero_pos`.
3. **In-Place Modification**:
   - The array is modified in-place to meet the constraints.

### Complexity
- **Time Complexity**: \(O(n)\), where \(n\) is the length of the array. We traverse the array once.
- **Space Complexity**: \(O(1)\), as no additional space is used.

### Example Runs
#### Example 1
```python
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

#### Example 2
```python
nums = [0]
moveZeroes(nums)
print(nums)  # Output: [0]
```

### Follow-Up: Minimize Operations
- The above approach minimizes operations by only swapping when a non-zero element is found.
- This ensures that zeros are moved to the end in the most efficient way, without redundant writes.
