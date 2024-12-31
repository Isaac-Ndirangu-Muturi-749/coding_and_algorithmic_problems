Here is an efficient implementation of the `SmallestInfiniteSet` class:

### Key Idea:
1. Use a **min-heap** to store integers that have been added back to the set.
2. Keep track of the smallest number that hasn't been removed yet using a pointer (`next_smallest`).
3. When `popSmallest` is called:
   - First, check if the heap has any numbers. If it does, pop the smallest number from the heap.
   - Otherwise, return `next_smallest` and increment it.
4. When `addBack` is called:
   - If the number is smaller than `next_smallest` and not already in the heap, add it back to the heap.

---

### Implementation:
```python
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
```

---

### Example Walkthrough:
```python
# Initialize
smallestInfiniteSet = SmallestInfiniteSet()

# Add back 2 (no effect because it's already in the infinite set)
smallestInfiniteSet.addBack(2)

# Pop smallest: 1 is returned and removed from the set
print(smallestInfiniteSet.popSmallest())  # Output: 1

# Pop smallest: 2 is returned and removed from the set
print(smallestInfiniteSet.popSmallest())  # Output: 2

# Pop smallest: 3 is returned and removed from the set
print(smallestInfiniteSet.popSmallest())  # Output: 3

# Add back 1
smallestInfiniteSet.addBack(1)

# Pop smallest: 1 is returned again (added back earlier)
print(smallestInfiniteSet.popSmallest())  # Output: 1

# Pop smallest: 4 is returned
print(smallestInfiniteSet.popSmallest())  # Output: 4

# Pop smallest: 5 is returned
print(smallestInfiniteSet.popSmallest())  # Output: 5
```

---

### Explanation of Output:
1. `addBack(2)` - No change because 2 is already in the infinite set.
2. `popSmallest()` - Returns `1` and removes it.
3. `popSmallest()` - Returns `2` and removes it.
4. `popSmallest()` - Returns `3` and removes it.
5. `addBack(1)` - Adds `1` back to the set.
6. `popSmallest()` - Returns `1` (which was added back).
7. `popSmallest()` - Returns `4`.
8. `popSmallest()` - Returns `5`.

---

### Complexity:
1. **Time Complexity**:
   - `popSmallest`: \(O(\log k)\), where \(k\) is the size of the heap.
   - `addBack`: \(O(\log k)\), where \(k\) is the size of the heap.
2. **Space Complexity**:
   - \(O(k)\) for the heap and set, where \(k\) is the number of elements added back.

This solution is efficient and satisfies the constraints.
