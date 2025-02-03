Optimal Solution: Using Two Heaps (Min-Heap & Max-Heap)

To efficiently find the median in a data stream, we use two heaps:

1. Max-Heap (left half of numbers) → Stores the smaller half of the numbers.


2. Min-Heap (right half of numbers) → Stores the larger half of the numbers.



By maintaining these two heaps, we can efficiently retrieve the median:

If the total number of elements is odd, the median is the top of the max-heap.

If the total number of elements is even, the median is the average of the tops of both heaps.



---

Approach

1. Insert a number efficiently:

If the number is less than or equal to the max of the max-heap, insert it into the max-heap.

Otherwise, insert it into the min-heap.

Balance the heaps to ensure their sizes differ by at most 1.



2. Find the median efficiently:

If max-heap has more elements → return top of max-heap.

If both heaps are of equal size → return average of both tops.





---

Python Code Implementation

import heapq

class MedianFinder:
    def __init__(self):
        # Max-Heap for the left half (negative values for min-heap behavior)
        self.left = []
        # Min-Heap for the right half
        self.right = []

    def addNum(self, num: int) -> None:
        # Add to max-heap (negate to simulate max-heap)
        heapq.heappush(self.left, -num)
        
        # Balance by moving the max of left heap to right heap
        heapq.heappush(self.right, -heapq.heappop(self.left))
        
        # If right heap has more elements, rebalance
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # If odd number of elements, return max of max-heap
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, return average of tops
        return (-self.left[0] + self.right[0]) / 2.0


---

Complexity Analysis

Overall complexity: O(log n) per insert, O(1) for median retrieval.


---

Example Execution

medianFinder = MedianFinder()
medianFinder.addNum(1)  # [1]
medianFinder.addNum(2)  # [1, 2]
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)  # [1, 2, 3]
print(medianFinder.findMedian())  # Output: 2.0


---

Follow-up Questions

1. If numbers are in [0, 100], how can we optimize?

Use a frequency array (freq[101]) instead of heaps.

Maintain a count of elements and traverse the array to get the median in O(1).



2. If 99% of numbers are in [0, 100]?

Hybrid approach: Use a bucket count for [0, 100] and only use heaps for outliers.




🚀 Efficient and scalable approach for streaming median!

