import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.next_smallest = 1
        self.min_heap = []
        self.set_in_heap = set()  # To prevent duplicates in the heap

    def popSmallest(self) -> int:
        if self.min_heap:
            # Pop the smallest number from the heap
            smallest = heapq.heappop(self.min_heap)
            self.set_in_heap.remove(smallest)
            return smallest
        else:
            # Otherwise, return and increment `next_smallest`
            result = self.next_smallest
            self.next_smallest += 1
            return result

    def addBack(self, num: int) -> None:
        # Only add `num` if it is smaller than `next_smallest` and not already in the heap
        if num < self.next_smallest and num not in self.set_in_heap:
            heapq.heappush(self.min_heap, num)
            self.set_in_heap.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
