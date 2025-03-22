# Problem Description
You are provided with an array `nums` that is zero-indexed, meaning the indexing starts from 0. Your task is to sort the array in a specific way using only swaps between two adjacent elements. The goal is to have the smallest number positioned at the start (leftmost) of the array and the largest number at the end (rightmost) of the array. The array is considered valid when these conditions are met. Your objective is to determine the minimum number of such swaps required to make the array valid.

---

## Intuition
To solve this problem, the strategy is to find the positions of the smallest and the largest elements in the array since only their positions matter for making the array valid. Typically, a linear scan through the array allows us to identify these elements and their indices.

Once the positions of the smallest and largest elements are known, there are a few cases to consider:

1. **If the smallest element is already at the first (leftmost) position and the largest element is already at the last (rightmost) position, then no swaps are needed.**
2. **If the smallest and largest elements are not in their correct positions, they need to be swapped towards their respective ends.** However, if the largest element is to the left of the smallest element, when the largest element is moved to the end, it effectively takes one swap less since the smallest element moves one place towards the beginning in the process.

The formula:
```
i + len(nums) - 1 - j - (i > j)
```
This formula reflects the above logic, where:
- `i` is the index of the smallest element,
- `j` is the index of the largest element,
- `len(nums)` is the size of the array.
- `(i > j)` is a conditional that subtracts one from the total swap count if the largest element comes before the smallest element.

---

## Solution Approach

The solution uses a single-pass algorithm to find the indices `i` and `j`, which represent the positions of the smallest and largest elements in the `nums` array, respectively. The algorithm iterates over each element in the array and checks if the current element is smaller or larger than the respective elements found so far.

### Approach Breakdown:
- Two variables, `i` and `j`, are initialized to 0, indicating that we initially consider the first element as both the smallest and largest element.
- A `for` loop iterates over each index `k` and compares the element `nums[k]` with the current smallest (`nums[i]`) and largest (`nums[j]`).
- **For the smallest element (`nums[i]`):**
  - If `nums[k]` is less than `nums[i]`, update `i` to `k`.
  - If `nums[k]` is equal to `nums[i]` but `k` is closer to the start, update `i` to `k`.
- **For the largest element (`nums[j]`):**
  - If `nums[k]` is greater than `nums[j]`, update `j` to `k`.
  - If `nums[k]` is equal to `nums[j]` but `k` is closer to the end, update `j` to `k`.

After finding the smallest and largest elements, we calculate the minimum number of swaps needed with this formula:
```
swaps = i + len(nums) - 1 - j - (i > j)
```
- The expression `i + len(nums) - 1 - j` gives the total distance the smallest and largest elements need to move.
- The adjustment term `(i > j)` reduces the swap count by 1 if the largest element appears before the smallest element.

---

## Example Walkthrough

Consider the array:
```
nums = [3, 1, 2, 4]
```
Initial state:
- `i = 0`, `j = 0` (we start by considering the first element as both the smallest and largest).

Iterate through the array:

- For `k = 1`: `nums[1] = 1`, which is smaller than `nums[i] = 3`, so update `i = 1`.
- For `k = 2`: `nums[2] = 2` (no update needed).
- For `k = 3`: `nums[3] = 4`, which is greater than `nums[j] = 3`, so update `j = 3`.

Final positions:
- Smallest element at `i = 1` (`nums[i] = 1`)
- Largest element at `j = 3` (`nums[j] = 4`)

Calculate the number of swaps:
```
swaps = i + len(nums) - 1 - j - (i > j)
       = 1 + 4 - 1 - 3 - 0
       = 1
```
Thus, the minimum number of swaps required is 1.

---

## Solution Implementation

### Python Code
```python
from typing import List

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_position = max_position = 0  # Initialize positions of min and max elements

        # Find positions of smallest and largest elements
        for index, value in enumerate(nums):
            if value < nums[min_position] or (value == nums[min_position] and index < min_position):
                min_position = index
            if value > nums[max_position] or (value == nums[max_position] and index > max_position):
                max_position = index

        swaps = min_position + (len(nums) - 1 - max_position)
        if min_position > max_position:
            swaps -= 1  # Avoid double counting when max is left of min

        return swaps
```

---

## Time and Space Complexity

- **Time Complexity:**
  The solution uses a single loop to find the smallest and largest elements, resulting in a time complexity of **O(n)**, where `n` is the length of the input array.

- **Space Complexity:**
  The solution uses a constant amount of extra space, so the space complexity is **O(1)**.
