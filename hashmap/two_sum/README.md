To solve the **two-sum problem** efficiently, we can use a **hash map** (dictionary in Python) to track the numbers we have seen so far and their corresponding indices as we iterate through the array. This allows us to reduce the time complexity to **O(n)**.

### Approach:

1. **Use a Hash Map (Dictionary)**:
   - While iterating through the array `nums`, for each number `num`, we compute the difference `target - num` (let's call it `complement`).
   - If the `complement` exists in the hash map, it means we've already seen a number that, when added to the current `num`, gives the target. In that case, we can return the indices of `complement` and `num`.
   - If the `complement` is not in the hash map, we store the current `num` and its index in the hash map, so we can check it for future numbers.

2. **Time Complexity**:
   - In the worst case, each lookup and insertion into the hash map takes **O(1)** time, and we are doing this for each element in the array. Thus, the overall time complexity is **O(n)**, where `n` is the number of elements in the array.

3. **Space Complexity**:
   - The hash map can potentially store all `n` elements, so the space complexity is **O(n)**.

### Python Code:

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    # Dictionary to store the index of each number
    num_to_index = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num

        # If the complement is already in the dictionary, return the indices
        if complement in num_to_index:
            return [num_to_index[complement], i]

        # Otherwise, store the current number and its index in the dictionary
        num_to_index[num] = i
```

### Example Walkthroughs:

1. **Example 1**:
   - Input: `nums = [2,7,11,15]`, `target = 9`
   - Iteration:
     - `i = 0`, `num = 2`, `complement = 9 - 2 = 7`. The complement `7` is not in the dictionary, so we add `2` with its index to the dictionary: `{2: 0}`.
     - `i = 1`, `num = 7`, `complement = 9 - 7 = 2`. The complement `2` is in the dictionary, so we return `[0, 1]`.
   - Output: `[0, 1]`

2. **Example 2**:
   - Input: `nums = [3,2,4]`, `target = 6`
   - Iteration:
     - `i = 0`, `num = 3`, `complement = 6 - 3 = 3`. The complement `3` is not in the dictionary, so we add `3` with its index to the dictionary: `{3: 0}`.
     - `i = 1`, `num = 2`, `complement = 6 - 2 = 4`. The complement `4` is not in the dictionary, so we add `2` with its index: `{3: 0, 2: 1}`.
     - `i = 2`, `num = 4`, `complement = 6 - 4 = 2`. The complement `2` is in the dictionary, so we return `[1, 2]`.
   - Output: `[1, 2]`

3. **Example 3**:
   - Input: `nums = [3,3]`, `target = 6`
   - Iteration:
     - `i = 0`, `num = 3`, `complement = 6 - 3 = 3`. The complement `3` is not in the dictionary, so we add `3` with its index to the dictionary: `{3: 0}`.
     - `i = 1`, `num = 3`, `complement = 6 - 3 = 3`. The complement `3` is in the dictionary, so we return `[0, 1]`.
   - Output: `[0, 1]`

### Complexity:
- **Time Complexity**: O(n) – we traverse the array once and do constant-time hash map operations.
- **Space Complexity**: O(n) – the space is used for the hash map that stores up to `n` numbers.

This approach ensures that the solution is found in linear time with a single pass through the array.


If you're looking for a solution with **O(n²)** time complexity (a brute-force approach), the idea is to simply check every possible pair of numbers in the array to see if their sum equals the target. This means using two nested loops:

- The outer loop picks one number.
- The inner loop checks every other number after it to see if they sum up to the target.

### Brute-Force Approach

1. **Iterate through each element** in the array using a loop.
2. For each element, **iterate through the rest of the array** (i.e., the elements that come after the current one) and check if the sum of the two elements equals the target.
3. If you find such a pair, return their indices.

### Python Code:

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    # Brute-force solution with O(n^2) time complexity
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # If the two numbers sum up to the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]
```

### Example Walkthrough:

1. **Example 1**:
   - Input: `nums = [2,7,11,15]`, `target = 9`
   - Iteration:
     - `i = 0`, `nums[i] = 2`
       - `j = 1`, `nums[j] = 7`: `2 + 7 = 9`, return `[0, 1]`
   - Output: `[0, 1]`

2. **Example 2**:
   - Input: `nums = [3,2,4]`, `target = 6`
   - Iteration:
     - `i = 0`, `nums[i] = 3`
       - `j = 1`, `nums[j] = 2`: `3 + 2 != 6`
       - `j = 2`, `nums[j] = 4`: `3 + 4 != 6`
     - `i = 1`, `nums[i] = 2`
       - `j = 2`, `nums[j] = 4`: `2 + 4 = 6`, return `[1, 2]`
   - Output: `[1, 2]`

3. **Example 3**:
   - Input: `nums = [3,3]`, `target = 6`
   - Iteration:
     - `i = 0`, `nums[i] = 3`
       - `j = 1`, `nums[j] = 3`: `3 + 3 = 6`, return `[0, 1]`
   - Output: `[0, 1]`

### Complexity:

- **Time Complexity**: O(n²) – The outer loop runs `n` times, and for each iteration, the inner loop runs `n-1`, `n-2`, ..., times. This leads to O(n²) in the worst case.
- **Space Complexity**: O(1) – No additional space is used other than a few variables for iteration.

This brute-force method works well for small arrays, but for large arrays, it is much slower compared to the more efficient O(n) solution with a hash map.
