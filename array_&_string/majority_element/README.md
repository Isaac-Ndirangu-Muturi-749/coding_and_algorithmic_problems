To solve the majority element problem, where we need to find the element that appears more than ⌊n / 2⌋ times, we can use **Boyer-Moore Voting Algorithm**, which provides an efficient solution with O(n) time complexity and O(1) space complexity.

### Boyer-Moore Voting Algorithm:

1. **Key Idea**:
   - We will keep a `candidate` element and a `count` variable.
   - The algorithm works by maintaining a count that tracks the occurrence of the current candidate.
   - If the count becomes 0, we pick a new candidate.
   - Since the majority element appears more than half the time, it will always survive as the final candidate after the array is processed.

2. **Steps**:
   - Initialize `candidate` as `None` and `count` as `0`.
   - Traverse the array:
     - If `count` is 0, set the current element as the `candidate`.
     - If the current element matches the `candidate`, increment `count`. Otherwise, decrement `count`.
   - After processing the entire array, the `candidate` will be the majority element.

### Code Implementation:

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        # Phase 1: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Since the problem guarantees that a majority element always exists,
        # the candidate found after the first pass is the majority element.
        return candidate
```

### Explanation:

- **Initialization**: We start with `candidate = None` and `count = 0`.
- **First pass through the array**:
  - When `count` is 0, we set the current element as the `candidate`.
  - We then increment or decrement the `count` based on whether the current element matches the `candidate`.
- **Majority element**:
  - After the loop, the `candidate` will be the majority element because the majority element occurs more than `n // 2` times, ensuring that it will dominate the `count` variable over time.

### Example Walkthrough:

#### Example 1:
- **Input**: `nums = [3, 2, 3]`
- **Process**:
  - Start with `candidate = None`, `count = 0`
  - First number is 3: Set `candidate = 3`, `count = 1`
  - Second number is 2: `count = 0` (decrement since 2 != candidate)
  - Third number is 3: Set `candidate = 3`, `count = 1`
- **Output**: `3`

#### Example 2:
- **Input**: `nums = [2,2,1,1,1,2,2]`
- **Process**:
  - Start with `candidate = None`, `count = 0`
  - First number is 2: Set `candidate = 2`, `count = 1`
  - Second number is 2: `count = 2` (increment)
  - Third number is 1: `count = 1` (decrement)
  - Fourth number is 1: `count = 0` (decrement)
  - Fifth number is 1: Set `candidate = 1`, `count = 1`
  - Sixth number is 2: `count = 0` (decrement)
  - Seventh number is 2: Set `candidate = 2`, `count = 1`
- **Output**: `2`

### Time and Space Complexity:
- **Time Complexity**: O(n), where `n` is the number of elements in the array. We only make one pass through the array.
- **Space Complexity**: O(1), since we only use a few extra variables (`candidate` and `count`).

This algorithm is optimal because it solves the problem in linear time with constant space.
