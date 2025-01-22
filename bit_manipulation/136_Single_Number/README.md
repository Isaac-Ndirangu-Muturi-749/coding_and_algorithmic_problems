To solve this problem with linear time complexity (`O(n)`) and constant space complexity (`O(1)`), we can leverage a powerful bitwise operator: **XOR**.

### Key Observation:
- XOR (`^`) has some important properties:
  1. `x ^ x = 0` for any integer `x`.
  2. `x ^ 0 = x` for any integer `x`.
  3. XOR is commutative and associative, which means the order of operations doesn't matter.

### Plan:
- Since every element in the array appears twice except one element, XORing all the elements together will cancel out the numbers that appear twice (because `x ^ x = 0`). The result will be the number that appears only once, as XORing any number with `0` gives the number itself.

### Algorithm:
1. Initialize a variable `result` to `0`.
2. Iterate through each number in the array and XOR it with `result`.
3. After iterating through the entire array, `result` will contain the number that appears only once.

### Solution:

```python
def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR the current number with result
    return result
```

### Explanation:
- We initialize `result` to `0`.
- For each number in `nums`, we XOR it with `result`. Since all numbers except one appear twice, the XOR of all those numbers will cancel each other out, leaving only the number that appears once.
- Finally, `result` will hold the single number.

### Example Walkthrough:

#### Example 1:
Input: `nums = [2,2,1]`
- Initialize `result = 0`.
- XOR operations:
  - `result = 0 ^ 2 = 2`
  - `result = 2 ^ 2 = 0` (because `2 ^ 2 = 0`)
  - `result = 0 ^ 1 = 1`
- Output: `1`

#### Example 2:
Input: `nums = [4,1,2,1,2]`
- Initialize `result = 0`.
- XOR operations:
  - `result = 0 ^ 4 = 4`
  - `result = 4 ^ 1 = 5`
  - `result = 5 ^ 2 = 7`
  - `result = 7 ^ 1 = 6`
  - `result = 6 ^ 2 = 4`
- Output: `4`

#### Example 3:
Input: `nums = [1]`
- Initialize `result = 0`.
- XOR operation: `result = 0 ^ 1 = 1`
- Output: `1`

### Time and Space Complexity:
- **Time complexity**: `O(n)` where `n` is the length of the array, since we iterate through the array once.
- **Space complexity**: `O(1)` since we only use a constant amount of extra space (`result` variable).

This solution is both optimal in terms of time and space, meeting the problem's constraints.
