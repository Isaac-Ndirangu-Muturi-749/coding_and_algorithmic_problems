To solve this problem, we need to compute the product of all elements of the array except for the element at the current index, without using division. We will do this in an **O(n)** time complexity.

### Approach:
1. **Two-pass approach**:
   - We'll compute the product of all elements to the **left** of each index in one pass.
   - We'll compute the product of all elements to the **right** of each index in another pass.
   - Then, we'll multiply the left and right products together to get the desired result.

### Plan:
- Use two arrays:
  1. **Left product array** (`left_prod`): For each index `i`, `left_prod[i]` will store the product of all elements to the left of `i`.
  2. **Right product array** (`right_prod`): For each index `i`, `right_prod[i]` will store the product of all elements to the right of `i`.
- Finally, multiply these arrays to get the desired result for each index.

### Optimized Solution:
- Instead of using two additional arrays, we can compute the result directly using a single output array and by maintaining cumulative products from left to right and right to left.

### Algorithm:
1. **First pass (left to right)**: Compute the cumulative product of elements to the left of each index.
2. **Second pass (right to left)**: Compute the cumulative product of elements to the right of each index and multiply it with the current value in the result array.

### Code Implementation:

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # First pass: compute left product for each element
        left_prod = 1
        for i in range(n):
            result[i] = left_prod
            left_prod *= nums[i]

        # Second pass: compute right product and multiply with result
        right_prod = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result
```

### Explanation:
1. **First pass (left product)**:
   - We initialize `left_prod = 1` and iterate over the array from left to right.
   - For each element at index `i`, we store the current `left_prod` in `result[i]`, then update `left_prod` by multiplying it with `nums[i]`.

2. **Second pass (right product)**:
   - We initialize `right_prod = 1` and iterate over the array from right to left.
   - For each element at index `i`, we multiply the current value in `result[i]` (which already contains the left product) by `right_prod`. Then we update `right_prod` by multiplying it with `nums[i]`.

### Example Walkthrough:

#### Example 1:
- **Input**: `nums = [1, 2, 3, 4]`

  **Left product pass**:
  - `result = [1, 1, 1, 1]` (initial result array)
  - `left_prod = 1`
  - At index 0: `result[0] = 1`, `left_prod = 1 * 1 = 1`
  - At index 1: `result[1] = 1`, `left_prod = 1 * 2 = 2`
  - At index 2: `result[2] = 2`, `left_prod = 2 * 3 = 6`
  - At index 3: `result[3] = 6`, `left_prod = 6 * 4 = 24`

  After first pass: `result = [1, 1, 2, 6]`

  **Right product pass**:
  - `right_prod = 1`
  - At index 3: `result[3] = 6 * 1 = 6`, `right_prod = 1 * 4 = 4`
  - At index 2: `result[2] = 2 * 4 = 8`, `right_prod = 4 * 3 = 12`
  - At index 1: `result[1] = 1 * 12 = 12`, `right_prod = 12 * 2 = 24`
  - At index 0: `result[0] = 1 * 24 = 24`, `right_prod = 24 * 1 = 24`

  After second pass: `result = [24, 12, 8, 6]`

  **Output**: `[24, 12, 8, 6]`

#### Example 2:
- **Input**: `nums = [-1, 1, 0, -3, 3]`

  **Left product pass**:
  - `result = [1, 1, 1, 1, 1]` (initial result array)
  - `left_prod = 1`
  - At index 0: `result[0] = 1`, `left_prod = 1 * (-1) = -1`
  - At index 1: `result[1] = -1`, `left_prod = -1 * 1 = -1`
  - At index 2: `result[2] = -1`, `left_prod = -1 * 0 = 0`
  - At index 3: `result[3] = 0`, `left_prod = 0 * (-3) = 0`
  - At index 4: `result[4] = 0`, `left_prod = 0 * 3 = 0`

  After first pass: `result = [1, -1, -1, 0, 0]`

  **Right product pass**:
  - `right_prod = 1`
  - At index 4: `result[4] = 0 * 1 = 0`, `right_prod = 1 * 3 = 3`
  - At index 3: `result[3] = 0 * 3 = 0`, `right_prod = 3 * (-3) = -9`
  - At index 2: `result[2] = -1 * (-9) = 9`, `right_prod = -9 * 0 = 0`
  - At index 1: `result[1] = -1 * 0 = 0`, `right_prod = 0 * 1 = 0`
  - At index 0: `result[0] = 1 * 0 = 0`, `right_prod = 0 * (-1) = 0`

  After second pass: `result = [0, 0, 9, 0, 0]`

  **Output**: `[0, 0, 9, 0, 0]`

### Time Complexity:
- **O(n)**: We iterate through the array twice, once for the left product and once for the right product.

### Space Complexity:
- **O(1)**: We use only constant extra space for variables `left_prod` and `right_prod` (not counting the result array). Thus, the algorithm satisfies the follow-up requirement of **O(1)** extra space complexity.
