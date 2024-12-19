This problem can be solved using a **greedy algorithm**. The goal is to minimize the number of overlapping intervals by removing the fewest possible intervals.

---

### **Approach**

1. **Sort the intervals**:
   - Sort the intervals by their ending times (`end`) in ascending order. This allows us to always consider the interval with the earliest ending time first, which leaves the most room for subsequent intervals.

2. **Iterate and Compare**:
   - Use a variable `prev_end` to track the ending time of the last interval that was added to the non-overlapping set.
   - For each interval:
     - If the current interval's start time is greater than or equal to `prev_end`, it means the current interval does not overlap with the last interval. Update `prev_end` to the current interval's ending time.
     - Otherwise, if the current interval overlaps with the last one, increment a counter (`removal_count`) to record the need to remove the current interval.

3. **Return the result**:
   - At the end of the iteration, `removal_count` will contain the minimum number of intervals to remove.

---

### **Algorithm**

```python
def eraseOverlapIntervals(intervals):
    # Sort intervals by their ending times
    intervals.sort(key=lambda x: x[1])

    # Initialize variables
    prev_end = float('-inf')  # Tracks the end of the last non-overlapping interval
    removal_count = 0         # Tracks the number of intervals to remove

    # Iterate through the sorted intervals
    for start, end in intervals:
        # If the current interval overlaps with the previous one
        if start < prev_end:
            removal_count += 1
        else:
            # Update prev_end to the end of the current interval
            prev_end = end

    return removal_count
```

---

### **Complexity Analysis**

1. **Time Complexity**:
   - Sorting the intervals takes \(O(n \log n)\), where \(n\) is the number of intervals.
   - The iteration through the intervals takes \(O(n)\).
   - Overall complexity: \(O(n \log n)\).

2. **Space Complexity**:
   - Sorting uses \(O(\log n)\) space for the sort operation.
   - Additional variables use \(O(1)\) space.
   - Overall complexity: \(O(\log n)\).

---

### **Examples**

#### Example 1:
**Input**:
```python
intervals = [[1,2],[2,3],[3,4],[1,3]]
```

**Execution**:
1. Sort intervals: `[[1,2], [2,3], [1,3], [3,4]]` → `[[1,2], [2,3], [3,4], [1,3]]`.
2. Initialize `prev_end = -inf`, `removal_count = 0`.
3. Process intervals:
   - `[1,2]`: No overlap (`1 >= -inf`). Update `prev_end = 2`.
   - `[2,3]`: No overlap (`2 >= 2`). Update `prev_end = 3`.
   - `[3,4]`: No overlap (`3 >= 3`). Update `prev_end = 4`.
   - `[1,3]`: Overlap (`1 < 4`). Increment `removal_count = 1`.
4. Return `removal_count = 1`.

**Output**:
```python
1
```

#### Example 2:
**Input**:
```python
intervals = [[1,2],[1,2],[1,2]]
```

**Execution**:
1. Sort intervals: `[[1,2], [1,2], [1,2]]`.
2. Initialize `prev_end = -inf`, `removal_count = 0`.
3. Process intervals:
   - First `[1,2]`: No overlap (`1 >= -inf`). Update `prev_end = 2`.
   - Second `[1,2]`: Overlap (`1 < 2`). Increment `removal_count = 1`.
   - Third `[1,2]`: Overlap (`1 < 2`). Increment `removal_count = 2`.
4. Return `removal_count = 2`.

**Output**:
```python
2
```

#### Example 3:
**Input**:
```python
intervals = [[1,2],[2,3]]
```

**Execution**:
1. Sort intervals: `[[1,2], [2,3]]`.
2. Initialize `prev_end = -inf`, `removal_count = 0`.
3. Process intervals:
   - `[1,2]`: No overlap (`1 >= -inf`). Update `prev_end = 2`.
   - `[2,3]`: No overlap (`2 >= 2`). Update `prev_end = 3`.
4. Return `removal_count = 0`.

**Output**:
```python
0
```

This algorithm efficiently calculates the minimum number of intervals to remove to make the rest non-overlapping.
