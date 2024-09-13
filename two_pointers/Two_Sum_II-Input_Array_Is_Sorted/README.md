To solve this problem, we can take advantage of the fact that the array is sorted in non-decreasing order. This allows us to use the **two-pointer technique** to find the two numbers that sum up to the target. The key advantage of this approach is that it only requires **O(1)** extra space and runs in **O(n)** time.

### Approach:

1. **Initialize two pointers**:
   - One pointer `left` at the start of the array (`left = 0`).
   - Another pointer `right` at the end of the array (`right = len(numbers) - 1`).

2. **Check the sum**:
   - Calculate the sum of `numbers[left] + numbers[right]`.
   - If the sum equals the target, return `[left + 1, right + 1]` (because the array is 1-indexed).
   - If the sum is less than the target, increment the `left` pointer to increase the sum.
   - If the sum is greater than the target, decrement the `right` pointer to decrease the sum.

3. **Repeat the process** until you find the two numbers that add up to the target.

Since the array is sorted, moving the pointers in this manner ensures that we efficiently find the solution without needing extra space or a second pass through the array.

### Code Implementation:

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # return 1-based indices
            elif current_sum < target:
                left += 1  # move the left pointer to the right
            else:
                right -= 1  # move the right pointer to the left
```

### Explanation:

- **Initialization**: Start with two pointers, one at the beginning (`left`) and one at the end (`right`).
- **Iteration**: In each step, calculate the sum of `numbers[left]` and `numbers[right]`.
  - If the sum matches the target, return the current indices (adjusted for 1-based indexing).
  - If the sum is less than the target, increase the `left` pointer to explore larger numbers.
  - If the sum is greater than the target, decrease the `right` pointer to explore smaller numbers.
- **Termination**: Since the problem guarantees exactly one solution, the loop will eventually find the correct pair of indices.

### Time Complexity:
- **O(n)**: Each element is processed at most once because the `left` pointer can only move right and the `right` pointer can only move left.

### Space Complexity:
- **O(1)**: We are only using a constant amount of extra space, regardless of the size of the input array.

### Example Walkthrough:

#### Example 1:
```python
numbers = [2, 7, 11, 15], target = 9
```
1. Start with `left = 0` (`numbers[0] = 2`) and `right = 3` (`numbers[3] = 15`).
2. Calculate `2 + 15 = 17` (greater than 9), so move `right` to 2.
3. Calculate `2 + 11 = 13` (greater than 9), so move `right` to 1.
4. Calculate `2 + 7 = 9` (equal to target), so return `[1, 2]`.

#### Example 2:
```python
numbers = [2, 3, 4], target = 6
```
1. Start with `left = 0` (`numbers[0] = 2`) and `right = 2` (`numbers[2] = 4`).
2. Calculate `2 + 4 = 6` (equal to target), so return `[1, 3]`.

#### Example 3:
```python
numbers = [-1, 0], target = -1
```
1. Start with `left = 0` (`numbers[0] = -1`) and `right = 1` (`numbers[1] = 0`).
2. Calculate `-1 + 0 = -1` (equal to target), so return `[1, 2]`.

This approach is efficient and meets the problem's constraints of constant space and logarithmic time complexity when leveraging the sorted array structure.


