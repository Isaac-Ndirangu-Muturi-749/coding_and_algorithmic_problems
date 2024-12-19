class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

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
