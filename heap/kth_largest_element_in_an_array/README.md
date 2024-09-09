To solve the problem of finding the kth largest element in an unsorted array without sorting, you can use a min-heap of size `k`. Here's a step-by-step explanation of the approach:

### Approach:

1. **Min-Heap of Size `k`**:
   - Use a min-heap to keep track of the largest `k` elements encountered so far.
   - The root of the min-heap will always be the smallest of these `k` elements, which effectively gives us the kth largest element when the heap size is `k`.

2. **Algorithm**:
   - Iterate through each number in the array.
   - Add the number to the heap.
   - If the heap size exceeds `k`, remove the smallest element (root of the heap).
   - After processing all numbers, the root of the heap will be the kth largest element.

### Why It Works:
- The min-heap allows us to efficiently maintain the top `k` largest elements in the array.
- Inserting and removing elements from the heap has a time complexity of \( O(\log k) \), making the overall complexity \( O(n \log k) \), where `n` is the number of elements in the array.

### Code Implementation:

Here is the implementation of the solution using the `heapq` module in Python:

```python
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Create a heap from the list

        # Iterate through the rest of the numbers
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        # The root of the min-heap is the kth largest element
        return min_heap[0]

# Example usage
solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # Output: 4
```

### Explanation of the Code:
- **Heap Initialization**: The heap is initialized with the first `k` elements of the array.
- **Processing Remaining Elements**: For each remaining element in the array, if the element is greater than the smallest element in the heap (i.e., the root), replace the smallest element with the new element and adjust the heap.
- **Result**: After processing all elements, the smallest element in the heap (root) will be the kth largest element in the array.

This method efficiently finds the kth largest element without sorting the entire array, and it works well for large arrays within the given constraints.


A **heap** is a special type of binary tree that satisfies the **heap property**. It's commonly used in computer science for efficiently managing data in a priority queue, or for algorithms like **Heapsort**.

### Types of Heaps:
1. **Max-Heap**:
   - In a max-heap, for every parent node, the value of the parent is **greater than or equal to** the values of its children.
   - The largest element is always at the root (top) of the heap.

2. **Min-Heap**:
   - In a min-heap, for every parent node, the value of the parent is **less than or equal to** the values of its children.
   - The smallest element is always at the root (top) of the heap.

### Heap Representation:
- **Binary Tree Structure**: Heaps are typically represented as complete binary trees, meaning all levels are fully filled except possibly the last, which is filled from left to right.
- **Array Representation**: Heaps are often stored in arrays. For a node at index `i`:
  - Its left child is at index `2*i + 1`.
  - Its right child is at index `2*i + 2`.
  - Its parent is at index `(i - 1) // 2`.

### Heap Operations:
1. **Insertion**:
   - When you insert a new element into the heap, it is added at the bottom of the tree (next available position) to maintain the complete binary tree property.
   - Then, the "heapify-up" process is performed:
     - In a max-heap: Compare the newly inserted element with its parent, and if it's larger, swap them. Continue this process until the heap property is restored.
     - In a min-heap: The newly inserted element is swapped upwards if it is smaller than its parent.

2. **Deletion (Extract Max/Min)**:
   - To remove the root (which is the largest in a max-heap or the smallest in a min-heap):
     - Replace the root with the last element in the heap.
     - Remove the last element and perform "heapify-down" by comparing the new root with its children and swapping it with the larger child (in a max-heap) or the smaller child (in a min-heap) until the heap property is restored.

3. **Peek**:
   - Retrieve the root element without removing it. In a max-heap, this gives the maximum value; in a min-heap, it gives the minimum value.

### Example of Max-Heap:
```plaintext
         10
       /    \
      9      8
     / \    / \
    7   6  5   4
```

- The array representation: `[10, 9, 8, 7, 6, 5, 4]`
- If you insert `11`, the array becomes `[10, 9, 8, 7, 6, 5, 4, 11]`, and after heapify-up, it becomes `[11, 10, 8, 9, 6, 5, 4, 7]`.

### Time Complexity of Heap Operations:
- **Insertion**: O(log n) because in the worst case, you need to swap the new element with its parent at every level, which takes logarithmic time.
- **Deletion (Extract Max/Min)**: O(log n) due to the "heapify-down" process.
- **Peek**: O(1) since you only need to access the root element.

### Applications of Heaps:
1. **Priority Queue**: Heaps are commonly used to implement priority queues, where the highest or lowest priority element is quickly retrieved.
2. **Heapsort**: A comparison-based sorting algorithm that uses a heap to sort elements in O(n log n) time.
3. **Dijkstra’s Algorithm**: Uses a min-heap to efficiently find the shortest path in a graph.
4. **Median Maintenance**: Heaps can be used to maintain the median of a stream of numbers efficiently.

### Summary:
- **Heap** is a complete binary tree with the heap property (max-heap or min-heap).
- Efficient for priority queue operations (insert, delete, and peek).
- Key operations have logarithmic time complexity due to the tree's balanced nature.


**Heapsort** is a popular comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It works by first building a max-heap from the input data and then repeatedly extracting the largest element from the heap and placing it at the end of the list, effectively sorting the list in-place.

### Key Concepts of Heapsort:

1. **Binary Heap**:
   - Heapsort typically uses a **max-heap**, where the parent node is always larger than its children.
   - The largest element is always at the root (the top of the heap).

2. **Array Representation of Heap**:
   - Heaps are stored in arrays. If an element is at index `i`, then:
     - Left child is at index `2*i + 1`
     - Right child is at index `2*i + 2`
     - Parent is at index `(i - 1) // 2`

### Steps of Heapsort:

1. **Build a Max-Heap**:
   - Convert the unsorted array into a max-heap by organizing the elements so that the largest value is at the root. This is done using the **heapify** operation.

2. **Extract the Maximum**:
   - Once the max-heap is created, the root of the heap (the maximum element) is swapped with the last element of the array.
   - Reduce the size of the heap (i.e., exclude the last element from further heap operations because it's already in its correct place).
   - Perform **heapify-down** to restore the max-heap property for the remaining elements.

3. **Repeat the Process**:
   - Continue extracting the maximum (root), swapping it with the last unsorted element, and restoring the heap property for the remaining unsorted elements.
   - Repeat until the entire array is sorted.

### Heapsort Algorithm:

Here’s how the algorithm works step-by-step:

#### Step 1: Build Max-Heap (Heapify Process)
The goal is to build a max-heap where each parent node is larger than its children. This is done from the bottom of the tree up to the root. The array can be "heapified" in O(n) time.

#### Step 2: Sorting
Once the max-heap is built, the largest element is at the root. You swap the root element with the last element in the heap and then reduce the heap's size by one. You restore the heap property using **heapify-down** on the root.

#### Step 3: Repeat
Continue this process of extracting the largest element and reducing the heap size until the entire array is sorted.

### Heapsort Example:

Consider sorting the array `[4, 10, 3, 5, 1]` using Heapsort:

1. **Initial Array**: `[4, 10, 3, 5, 1]`

2. **Build Max-Heap**:
   - Rearrange elements to form a max-heap.
   - Max-Heap: `[10, 5, 3, 4, 1]`

3. **Extract Maximum**:
   - Swap the largest element (10) with the last element (1): `[1, 5, 3, 4, 10]`
   - Perform heapify on the reduced heap `[1, 5, 3, 4]`:
     - New Heap: `[5, 4, 3, 1, 10]`

4. **Extract Maximum Again**:
   - Swap the largest element (5) with the last element (1): `[1, 4, 3, 5, 10]`
   - Heapify the reduced heap `[1, 4, 3]`:
     - New Heap: `[4, 1, 3, 5, 10]`

5. **Continue**:
   - Repeat the process until all elements are sorted: `[1, 3, 4, 5, 10]`

### Heapsort Pseudocode:
```python
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the root element

# Example usage
arr = [4, 10, 3, 5, 1]
heapsort(arr)
print(arr)  # Output will be [1, 3, 4, 5, 10]
```

### Time Complexity:
- **Building the heap**: O(n)
- **Heapify process for each element**: O(log n)
- **Total time complexity**: O(n log n)

### Space Complexity:
- O(1) for in-place sorting (only requires a constant amount of extra memory for swapping elements).

### Advantages of Heapsort:
- **Time Complexity**: It consistently runs in O(n log n), which is efficient for large datasets.
- **In-place Sorting**: It requires only a constant amount of extra space (O(1)), unlike other algorithms like Merge Sort that require additional space.

### Disadvantages of Heapsort:
- Heapsort is not a **stable sorting algorithm**, meaning the relative order of elements with equal keys may not be preserved.

### Summary:
- **Heapsort** is an efficient comparison-based algorithm that uses a binary heap to sort an array in O(n log n) time.
- It's useful when space is constrained, and it avoids the worst-case time complexity of O(n²) seen in other sorting algorithms like quicksort.


