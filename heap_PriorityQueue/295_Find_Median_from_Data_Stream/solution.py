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



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
