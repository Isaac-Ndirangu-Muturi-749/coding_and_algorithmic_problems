To merge the two sorted arrays `nums1` and `nums2` in-place, you can start from the end of `nums1` and work your way backwards. This approach ensures that you don’t overwrite elements in `nums1` before you’ve had a chance to compare them.

Here's the Python implementation of the `merge` function:

```python
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize the pointers for nums1, nums2, and the merged array.
        i = m - 1  # Pointer for the last element in nums1 that should be considered
        j = n - 1  # Pointer for the last element in nums2
        k = m + n - 1  # Pointer for the last position in nums1

        # Merge the arrays from the end to the beginning.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2, add them.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

```

### Explanation:

- **Pointers**:
  - `i` points to the last element in the original part of `nums1`.
  - `j` points to the last element in `nums2`.
  - `k` points to the last position in `nums1`.

- **Comparing Elements**:
  - Compare `nums1[i]` and `nums2[j]`.
  - Place the larger one at the end of `nums1[k]`.
  - Move the corresponding pointer (`i` or `j`) and `k` one step to the left.

- **Handling Remaining Elements**:
  - If there are any remaining elements in `nums2`, they should be placed in `nums1`. This step is necessary because if `nums2` still has elements left (and `nums1` doesn't), those elements should occupy the remaining positions in `nums1`.

### Example Execution:

- **Example 1**:
  - Input: `nums1 = [1,2,3,0,0,0]`, `m = 3`, `nums2 = [2,5,6]`, `n = 3`
  - Process:
    - Start with `i=2`, `j=2`, and `k=5`.
    - Compare `nums1[2]` (3) with `nums2[2]` (6), place 6 at `nums1[5]`.
    - Continue comparing and placing elements until all elements are merged.
  - Output: `[1,2,2,3,5,6]`

- **Example 2**:
  - Input: `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`
  - Output: `[1]` (No merging needed)

- **Example 3**:
  - Input: `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`
  - Process:
    - Since `m = 0`, directly place `nums2` into `nums1`.
  - Output: `[1]`

This approach runs in O(m + n) time, where `m` and `n` are the lengths of `nums1` and `nums2`, respectively. It only uses O(1) extra space, meeting the problem's constraints.
