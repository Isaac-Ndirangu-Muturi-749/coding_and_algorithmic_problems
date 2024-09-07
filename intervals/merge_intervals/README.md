To solve the problem of merging overlapping intervals, we can follow these steps:

1. **Sort the Intervals**: First, sort the intervals based on the starting times. This helps in identifying overlaps easily as overlapping intervals will now be adjacent.

2. **Merge the Intervals**: Iterate through the sorted intervals and merge them if they overlap. If the current interval overlaps with the last merged interval, update the end of the last merged interval. Otherwise, add the current interval to the merged intervals list.

Here’s the Python implementation:

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []

        for interval in intervals:
            # If merged_intervals is empty or the current interval doesn't overlap with the last one
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # There is an overlap, so we merge the current interval with the previous one
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals
```

### Explanation:

1. **Sorting the Intervals**:
   - We sort the intervals based on the starting times. Sorting helps because once sorted, overlapping intervals will be adjacent, making it easier to merge them.

2. **Iterating and Merging**:
   - We initialize an empty list `merged_intervals` to store the merged intervals.
   - For each interval in the sorted list:
     - If the list of merged intervals is empty or the current interval does not overlap with the last merged interval (i.e., the end of the last merged interval is less than the start of the current interval), we simply add the current interval to `merged_intervals`.
     - If there is an overlap (i.e., the end of the last merged interval is greater than or equal to the start of the current interval), we merge them by updating the end of the last interval in `merged_intervals` to the maximum of the current interval's end and the last merged interval's end.

3. **Return**: After processing all intervals, the `merged_intervals` list will contain all the merged, non-overlapping intervals.

### Example Usage:

```python
solution = Solution()

# Test cases
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))  # Output: [[1,5]]
print(solution.merge([[1,4],[0,4]]))  # Output: [[0,4]]
print(solution.merge([[1,4],[2,3]]))  # Output: [[1,4]]
```

### Time Complexity:
- Sorting the intervals takes \(O(n \log n)\), and the merging process takes \(O(n)\). Therefore, the overall time complexity is \(O(n \log n)\), where \(n\) is the number of intervals.

This solution efficiently merges overlapping intervals, ensuring the result is a list of non-overlapping intervals.

Your test script looks good, but there are a few improvements that can be made. The function `run_tests()` should contain the test cases and their expected outputs. Also, it should print the results and whether each test passed or failed.

Here's the revised version of the test script:

```python
from solution import Solution

def run_tests():
    solution = Solution()

    # Define test cases and expected results
    test_cases = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[1,4],[0,4]], [[0,4]]),
        ([[1,4],[2,3]], [[1,4]])
    ]

    # Iterate through test cases
    for i, (intervals, expected) in enumerate(test_cases):
        result = solution.merge(intervals)
        print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
        print(f"Input: {intervals}")
        print(f"Expected Output: {expected}")
        print(f"Your Output: {result}")
        print()  # Blank line for readability

if __name__ == '__main__':
    run_tests()
```

### Explanation:

- **Test Cases**: The test cases are stored as tuples in a list where each tuple contains the input intervals and the expected output.
- **Iteration and Comparison**: The script iterates through each test case, runs the `merge()` function, and compares the output with the expected result. It prints whether the test passed or failed based on this comparison.
- **Readability**: Additional print statements are added to display the input, expected output, and actual output for each test case.

### Example Output:

When you run this script, it will produce an output similar to the following:

```plaintext
Test case 1: Passed
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Expected Output: [[1, 6], [8, 10], [15, 18]]
Your Output: [[1, 6], [8, 10], [15, 18]]

Test case 2: Passed
Input: [[1, 4], [4, 5]]
Expected Output: [[1, 5]]
Your Output: [[1, 5]]

Test case 3: Passed
Input: [[1, 4], [0, 4]]
Expected Output: [[0, 4]]
Your Output: [[0, 4]]

Test case 4: Passed
Input: [[1, 4], [2, 3]]
Expected Output: [[1, 4]]
Your Output: [[1, 4]]
```

This output will allow you to easily verify the correctness of your solution.
