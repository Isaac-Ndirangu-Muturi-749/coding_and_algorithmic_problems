To solve the problem of finding all unique triplets in the array that sum up to zero, we can use a combination of sorting and the two-pointer technique. This approach ensures an efficient O(n²) solution, which is optimal given the constraints.

### Approach:

1. **Sort the Array**: First, we sort the array. This helps in efficiently finding pairs that sum to a specific target by using two pointers.

2. **Iterate and Use Two Pointers**:
   - For each element `nums[i]`, we will try to find two other elements that sum to `-nums[i]`. This is done by setting two pointers: one starting just after `i` (`left`) and one at the end of the array (`right`).
   - If the sum of the three elements equals 0, we record the triplet and move both pointers inward, skipping duplicates to avoid recording the same triplet multiple times.

3. **Skip Duplicates**: To ensure we do not record duplicate triplets, we skip over duplicate elements when choosing the first element in the triplet (`nums[i]`) and also when moving the two pointers.

### Code Implementation:

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array

        for i in range(len(nums) - 2):  # Step 2: Iterate over the array
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach to find the two numbers that sum to -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:  # We found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum

        return res
```

### Explanation:

1. **Sorting**:
   - The array `nums` is sorted, which allows us to easily skip duplicates and apply the two-pointer technique.

2. **Main Loop**:
   - We loop through each element `nums[i]` as the first element of the triplet.
   - For each `i`, we use two pointers (`left` and `right`) to find the two other numbers that sum to `-nums[i]`.

3. **Two-pointer Approach**:
   - If the sum of `nums[i] + nums[left] + nums[right]` is zero, we add the triplet to the result.
   - If the sum is less than zero, we move the `left` pointer to the right to increase the sum.
   - If the sum is greater than zero, we move the `right` pointer to the left to decrease the sum.

4. **Handling Duplicates**:
   - We skip over duplicate elements by ensuring that we don't process the same value of `nums[i]`, `nums[left]`, or `nums[right]` more than once.

### Time Complexity:
- **Sorting**: O(n log n)
- **Main Loop**: O(n²) because for each element in the array, the two-pointer scan runs in O(n) time.
Thus, the overall time complexity is O(n²).

### Space Complexity:
- O(1) additional space is used (not counting the input and output). The space complexity is determined by the sorting step if we don't consider the result list.

### Example Walkthrough:

#### Example 1:
Input: `nums = [-1, 0, 1, 2, -1, -4]`

1. After sorting: `nums = [-4, -1, -1, 0, 1, 2]`
2. Iteration with `i = 0`: `nums[i] = -4`
   - Two-pointer search between `left = 1` and `right = 5` doesn't find any valid triplet.
3. Iteration with `i = 1`: `nums[i] = -1`
   - Two-pointer search between `left = 2` and `right = 5` finds `[-1, -1, 2]` and `[-1, 0, 1]`.
4. Iteration with `i = 2`: Skip duplicate `-1`.
5. Iteration with `i = 3`: `nums[i] = 0`
   - Two-pointer search doesn't find any valid triplet.

Output: `[[ -1, -1, 2], [-1, 0, 1]]`

#### Example 2:
Input: `nums = [0, 1, 1]`
- After sorting: `nums = [0, 1, 1]`
- No valid triplet found.

Output: `[]`

#### Example 3:
Input: `nums = [0, 0, 0]`
- After sorting: `nums = [0, 0, 0]`
- One valid triplet: `[[0, 0, 0]]`.

Output: `[[0, 0, 0]]`

### Conclusion:
This algorithm efficiently finds all unique triplets that sum to zero using sorting and the two-pointer technique, ensuring O(n²) time complexity and handling duplicate elements correctly.```````````````````````
