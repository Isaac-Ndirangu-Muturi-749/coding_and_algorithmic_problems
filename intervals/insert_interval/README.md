To solve the problem of inserting a new interval into a sorted list of non-overlapping intervals, we need to handle the following cases:

1. **No Overlap**: The new interval either comes entirely before or after the existing intervals.
2. **Overlap**: The new interval overlaps with one or more existing intervals, in which case we need to merge them.

### Approach:

1. **Iterate Through the Intervals**:
   - For intervals that end before the `newInterval` starts, just append them to the result.
   - For intervals that overlap with `newInterval`, merge them into `newInterval`.
   - For intervals that start after the merged interval, append them to the result.

2. **Edge Cases**:
   - If `intervals` is empty, simply return `[newInterval]`.
   - After merging, ensure that the final result still follows the non-overlapping rule and is in sorted order.

### Steps:
1. Traverse through the existing intervals and append those that end before the `newInterval` begins.
2. Merge overlapping intervals with the `newInterval`.
3. Append intervals that start after the merged interval.

### Code Implementation:

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that come before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval
        result.append(newInterval)

        # Step 3: Add the remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
```

### Explanation:

1. **Before Overlapping Intervals**: We first handle intervals that end before the `newInterval` starts and append them to the result.
2. **Merging Overlapping Intervals**: For each interval that overlaps with `newInterval`, we update the boundaries of `newInterval` to merge them.
3. **After Merging**: We append all remaining intervals that come after the merged interval.

### Time Complexity:
- **O(n)**, where `n` is the number of intervals. We only traverse the list once, making it linear.

### Space Complexity:
- **O(n)**, since we are using an extra list to store the result.

### Example Walkthrough:

#### Example 1:

```python
intervals = [[1,3], [6,9]]
newInterval = [2,5]
```

- We first append `[1,3]` since it partially overlaps with `[2,5]` and we merge them into `[1,5]`.
- Then we append the next interval `[6,9]` as it doesn't overlap with the merged interval.
- **Output**: `[[1,5], [6,9]]`

#### Example 2:

```python
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

- The first interval `[1,2]` is appended since it doesn't overlap.
- We merge the intervals `[3,5]`, `[6,7]`, and `[8,10]` with `newInterval`, resulting in `[3,10]`.
- Finally, append `[12,16]` as it doesn't overlap with the merged interval.
- **Output**: `[[1,2], [3,10], [12,16]]`
