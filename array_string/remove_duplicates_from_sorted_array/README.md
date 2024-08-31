To solve the problem of removing duplicates from a sorted array `nums` in-place, we can use a two-pointer approach. The idea is to iterate through the array with one pointer, and use another pointer to track the position where the next unique element should be placed.

### Approach:
1. **Edge Case**: If the array is empty, return 0 since there are no elements to process.

2. **Initialize Pointers**:
   - `i = 0`: This pointer will be used to place the next unique element in the array.
   - `j = 1`: This pointer will be used to iterate through the array and find unique elements.

3. **Iterate Through the Array**:
   - Start with `j = 1` and iterate through the array.
   - If `nums[j]` is different from `nums[i]` (meaning it's a unique element), increment `i` and copy `nums[j]` to `nums[i]`.
   - Continue this process until the end of the array.

4. **Return the Length of Unique Elements**:
   - After the loop, `i + 1` will be the number of unique elements.

### Example Walkthrough:
For `nums = [0,0,1,1,1,2,2,3,3,4]`:
- Initially, `i = 0`, `j = 1`.
- `nums[j]` (0) is equal to `nums[i]` (0), so move `j` to the next index.
- When `j = 2`, `nums[j]` (1) is different from `nums[i]` (0), increment `i` and set `nums[i] = nums[j]`.
- Continue this process until `j` reaches the end of the array.

### Code Implementation:

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

### Explanation:

- **Initial Setup**: Start with `i = 0`, meaning the first unique element is already in place.
- **Loop Through Array**: For each subsequent element, compare it with the element at `i`.
  - If it's unique (i.e., different from `nums[i]`), increment `i` and copy `nums[j]` to `nums[i]`.
- **Return the Length**: After the loop, `i + 1` gives the total count of unique elements.

### Test Cases:

```python
def run_tests():
    solution = Solution()

    nums1 = [1,1,2]
    assert solution.removeDuplicates(nums1) == 2
    assert nums1[:2] == [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums2) == 5
    assert nums2[:5] == [0, 1, 2, 3, 4]

    nums3 = [1, 2, 3, 4, 5]
    assert solution.removeDuplicates(nums3) == 5
    assert nums3[:5] == [1, 2, 3, 4, 5]

    nums4 = []
    assert solution.removeDuplicates(nums4) == 0

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
```

### Key Points:
- **In-Place Modification**: The array `nums` is modified in-place to contain only the unique elements at the beginning.
- **Space Complexity**: The algorithm uses O(1) additional space.
- **Time Complexity**: The algorithm runs in O(n) time, where `n` is the length of the array.

This method efficiently removes duplicates while maintaining the order of unique elements in the array.


Let's break down the `removeDuplicates` function step by step to understand how it works.

### Problem Context:
- **Objective**: Remove duplicates from a sorted array in place, such that each element appears only once. The function should return the new length of the array after removing duplicates, and the array itself should have the unique elements in the beginning, followed by any leftover elements (which don't matter).
- **Input**: A sorted list of integers `nums`.
- **Output**: The length of the list after duplicates are removed.

### Code Breakdown:
```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
```

### Step-by-Step Explanation:

1. **Initial Check for Empty List**:
    ```python
    if not nums:
        return 0
    ```
    - The function first checks if `nums` is empty. If it is, the function returns 0 immediately, as there are no elements to process.

2. **Initialization**:
    ```python
    i = 0
    ```
    - `i` is initialized to 0. This pointer will be used to track the position where the next unique element should be placed in the array.

3. **Iterate Over the Array**:
    ```python
    for j in range(1, len(nums)):
    ```
    - The function then iterates over the array starting from the second element (`j = 1`). The variable `j` serves as the pointer that scans through the array, checking for duplicates.

4. **Check for Duplicates**:
    ```python
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
    ```
    - Inside the loop, the function compares the current element `nums[j]` with the last unique element found `nums[i]`.
    - If `nums[j] != nums[i]`, it means that `nums[j]` is a new unique element:
        - `i` is incremented by 1 to move to the next position where the unique element should be placed.
        - `nums[i] = nums[j]` assigns the new unique element to this position.
    - If `nums[j] == nums[i]`, it means `nums[j]` is a duplicate, and nothing needs to be done; the loop simply moves to the next element.

5. **Return the New Length**:
    ```python
    return i + 1
    ```
    - After the loop finishes, `i` will be pointing to the last unique element's index. Since `i` is zero-based, the length of the array with unique elements is `i + 1`.
    - The function returns this value as the new length of the array after duplicates have been removed.

### Example Walkthrough:
Let's go through an example to see how the function works.

#### Example:
- Input: `nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5]`

1. **Initial State**:
   - `i = 0`
   - `nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 5]`

2. **Iteration Process**:
   - `j = 1`: `nums[1]` is `1`, which is the same as `nums[0]` (duplicate). No changes.
   - `j = 2`: `nums[2]` is `2`, which is different from `nums[0]` (new unique element).
     - Increment `i` to 1: `i = 1`.
     - Assign `nums[1] = 2`: `nums = [1, 2, 2, 2, 3, 3, 3, 4, 4, 5]`.
   - `j = 3`: `nums[3]` is `2`, which is the same as `nums[1]` (duplicate). No changes.
   - `j = 4`: `nums[4]` is `3`, which is different from `nums[1]` (new unique element).
     - Increment `i` to 2: `i = 2`.
     - Assign `nums[2] = 3`: `nums = [1, 2, 3, 2, 3, 3, 3, 4, 4, 5]`.
   - Continue this process until all elements are processed.

3. **Final State**:
   - `nums = [1, 2, 3, 4, 5, 3, 3, 4, 4, 5]`
   - `i = 4` (points to the last unique element).
   - The new length is `i + 1 = 5`.

- **Output**: The function returns `5`, which is the length of the array with unique elements. The first 5 elements in `nums` are now `[1, 2, 3, 4, 5]`.

### Summary:
- The `removeDuplicates` function uses two pointers (`i` and `j`) to efficiently remove duplicates in place in a sorted array.
- The time complexity is O(n), where `n` is the number of elements in the array, since each element is processed exactly once.
- The function modifies the input list to ensure that the first part of the list contains only unique elements, and it returns the length of this unique section.


Let's continue from where we left off in the example to see what happens in the next iteration.

### Current State Recap:
- `nums = [1, 2, 3, 2, 3, 3, 3, 4, 4, 5]`
- `i = 2` (the index of the last unique element, which is `3`).
- `j = 4` (we just processed `nums[4]` which was `3`).

### Next Iteration (`j = 5`):
1. **Check the Next Element**:
   - `j = 5`: `nums[5]` is `3`.

2. **Comparison**:
   - We compare `nums[5]` with `nums[i]` (where `i = 2`).
   - `nums[5]` is `3`, and `nums[2]` is `3`.
   - Since `nums[5]` is equal to `nums[2]`, it indicates that `nums[5]` is a duplicate of the last unique element.

3. **No Changes**:
   - Since `nums[5]` is a duplicate, the pointer `i` remains unchanged.
   - We do not modify `nums`, and the loop simply moves on to the next iteration.

### Next Iteration (`j = 6`):
1. **Check the Next Element**:
   - `j = 6`: `nums[6]` is `3`.

2. **Comparison**:
   - We compare `nums[6]` with `nums[i]` (where `i = 2`).
   - `nums[6]` is `3`, and `nums[2]` is `3`.
   - Since `nums[6]` is equal to `nums[2]`, it is also a duplicate.

3. **No Changes**:
   - The pointer `i` remains unchanged.
   - We do not modify `nums`, and the loop moves on to the next iteration.

### Next Iteration (`j = 7`):
1. **Check the Next Element**:
   - `j = 7`: `nums[7]` is `4`.

2. **Comparison**:
   - We compare `nums[7]` with `nums[i]` (where `i = 2`).
   - `nums[7]` is `4`, and `nums[2]` is `3`.
   - Since `nums[7]` is different from `nums[2]`, it indicates that `nums[7]` is a new unique element.

3. **Update `i` and Modify `nums`**:
   - Increment `i` to `3`: `i = 3`.
   - Assign `nums[3] = 4`: The array `nums` becomes `[1, 2, 3, 4, 3, 3, 3, 4, 4, 5]`.

### Summary of State after `j = 7`:
- `nums = [1, 2, 3, 4, 3, 3, 3, 4, 4, 5]`
- `i = 3` (the index of the last unique element, which is `4`).

The process will continue similarly until all elements are processed. In the next iterations, the function will continue to identify new unique elements and move them to the correct position in the array. Eventually, the array will have all unique elements in the first `i + 1` positions, and the function will return this length as the result.
