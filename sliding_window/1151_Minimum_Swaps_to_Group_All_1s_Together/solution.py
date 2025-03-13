class Solution:
    def min_swaps(self, data: List[int]) -> int:
        # Calculate the total number of 1s needed to form a continuous subarray.
        k= data.count(1)

        # Initialize the current count of 1s in the first window of size 'k'.
        current_count = sum(data[:k])

        # Initialize the maximum count of 1s found so far to the current count of the initial window.
        max_ones = current_count

        # Iterate over the array starting from the end of the first window to the end of the array.
        for i in range(k, len(data)):
            # Include the next element in the window and remove the trailing element to slide the window forward.
            current_count += data[i]
            current_count -= data[i - k]

            # Update the maximum count of 1s if the current window has more 1s than any previous ones.
            max_ones = max(max_ones, current_count)

        # The minimum number of swaps equals the number of 0s in the largest window of 1s (size of the window - max count of 1s).
        return k- max_ones
