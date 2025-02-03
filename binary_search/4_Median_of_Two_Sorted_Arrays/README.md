Optimal Solution: Finding the Median of Two Sorted Arrays (O(log (m+n)))

We need to find the median of two sorted arrays nums1 and nums2 in O(log (m+n)) time. The optimal approach is to use binary search.


---

Approach: Binary Search on the Smaller Array

1. Divide the Arrays:

Instead of merging the arrays, we partition them into two halves such that the left half contains smaller elements and the right half contains larger elements.

We apply binary search on the smaller array to find the correct partition.



2. Partitioning Strategy:

We find a partition index i in nums1 and j in nums2 such that:




\max(\text{Left1}, \text{Left2}) \leq \min(\text{Right1}, \text{Right2})

- `Left1 = nums1[i-1]` and `Right1 = nums1[i]`
 - `Left2 = nums2[j-1]` and `Right2 = nums2[j]`

We adjust i using binary search to ensure this condition holds.


3. Finding the Median:

If the total number of elements (m+n) is even, the median is:




\frac{\max(\text{Left1}, \text{Left2}) + \min(\text{Right1}, \text{Right2})}{2}

\max(\text{Left1}, \text{Left2})


---

Time Complexity Analysis

Since we perform binary search on the smaller array, the time complexity is O(log(min(m, n))).

Since m + n <= 2000, log-based approaches are optimal.



---

Python Code Implementation

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2  # Partition index in nums1
            j = (m + n + 1) // 2 - i  # Partition index in nums2
            
            # Handle edge cases (out-of-bounds)
            Left1 = float('-inf') if i == 0 else nums1[i - 1]
            Right1 = float('inf') if i == m else nums1[i]
            Left2 = float('-inf') if j == 0 else nums2[j - 1]
            Right2 = float('inf') if j == n else nums2[j]
            
            # Found correct partition
            if Left1 <= Right2 and Left2 <= Right1:
                # If total length is odd
                if (m + n) % 2 == 1:
                    return max(Left1, Left2)
                # If total length is even
                return (max(Left1, Left2) + min(Right1, Right2)) / 2
            
            # Adjust binary search range
            elif Left1 > Right2:
                right = i - 1  # Move left
            else:
                left = i + 1  # Move right


---

Explanation

1. Ensure nums1 is the smaller array (for efficient binary search).


2. Use binary search to find the correct partition index.


3. Check conditions to find the valid partition and compute the median.


4. If partition is incorrect, adjust the binary search range.


5. Return the median based on the total number of elements (odd/even).




---

Complexity Analysis

🚀 Binary search makes this problem efficient even for large inputs!


Understanding the Indexing Decisions in findMedianSortedArrays

This algorithm finds the median of two sorted arrays using binary search on the smaller array (nums1). The key idea is to partition both arrays such that the left half contains the smaller elements, and the right half contains the larger elements.


---

Step-by-Step Explanation

1. Ensure nums1 is the smaller array

if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1

This ensures binary search runs on the smaller array (nums1) for efficiency.

If nums1 is larger, we swap them.


2. Define binary search range

m, n = len(nums1), len(nums2)
left, right = 0, m

m = length of nums1, n = length of nums2.

We search within nums1 using binary search from index left = 0 to right = m.


3. Binary search for correct partitioning

i = (left + right) // 2  # Partition index in nums1
j = (m + n + 1) // 2 - i  # Partition index in nums2

i is the partition index for nums1 (midpoint in binary search).

j is the corresponding partition index in nums2, ensuring equal split of total elements.


4. Define partition values

Left1 = float('-inf') if i == 0 else nums1[i - 1]
Right1 = float('inf') if i == m else nums1[i]
Left2 = float('-inf') if j == 0 else nums2[j - 1]
Right2 = float('inf') if j == n else nums2[j]

Left1: Last element of nums1's left partition (nums1[i-1]).

Right1: First element of nums1's right partition (nums1[i]).

Left2: Last element of nums2's left partition (nums2[j-1]).

Right2: First element of nums2's right partition (nums2[j]).

If i == 0, it means nums1’s left partition is empty, so we set Left1 = -inf.

If i == m, it means nums1’s right partition is empty, so we set Right1 = inf.

The same logic applies for nums2.


5. Check if the partition is correct

if Left1 <= Right2 and Left2 <= Right1:

This condition ensures that all left partition elements are ≤ right partition elements.

If true, we found the correct partition.


6. Determine the median

if (m + n) % 2 == 1:
    return max(Left1, Left2)
return (max(Left1, Left2) + min(Right1, Right2)) / 2

If the total number of elements is odd, the median is max(Left1, Left2), the largest value in the left partition.

If the total number of elements is even, the median is the average of the two middle elements:
max(Left1, Left2) (largest left element) and min(Right1, Right2) (smallest right element).


7. Adjust binary search

elif Left1 > Right2:
    right = i - 1  # Move left
else:
    left = i + 1  # Move right

If Left1 > Right2, it means nums1[i-1] is too large, so we need to move the partition left (right = i - 1).

Otherwise, Left2 > Right1, meaning nums2[j-1] is too large, so we move the partition right (left = i + 1).



---

Example Walkthrough

Example 1

nums1 = [1, 3]
nums2 = [2]

1. m = 2, n = 1


2. i = 1, j = (2+1+1)//2 - 1 = 1


3. Left1 = nums1[0] = 1, Right1 = nums1[1] = 3


4. Left2 = nums2[0] = 2, Right2 = inf


5. Since Left1 (1) <= Right2 (inf) and Left2 (2) <= Right1 (3), partition is correct.


6. Since (m + n) % 2 == 1, the median is max(Left1, Left2) = max(1, 2) = 2.



Example 2

nums1 = [1, 2]
nums2 = [3, 4]

1. m = 2, n = 2


2. i = 1, j = (2+2+1)//2 - 1 = 1


3. Left1 = nums1[0] = 1, Right1 = nums1[1] = 2


4. Left2 = nums2[0] = 3, Right2 = nums2[1] = 4


5. Since Left1 (1) <= Right2 (4) and Left2 (3) <= Right1 (2) fails, move right.


6. i = 2, j = 0


7. Left1 = nums1[1] = 2, Right1 = inf


8. Left2 = -inf, Right2 = nums2[0] = 3


9. Condition holds. Median is (2 + 3) / 2 = 2.5.




---

Key Takeaways

1. Binary search is done on the smaller array for efficiency.


2. Partitioning ensures that left half contains smaller elements and right half contains larger elements.


3. Edge cases (out-of-bounds) are handled using float('-inf') and float('inf').


4. Odd-length case: Median is the max of left partition.


5. Even-length case: Median is the average of max(left) and min(right).


