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
