To solve the problem of finding the k pairs with the smallest sums from two sorted arrays, we can approach this using a **min-heap** (or priority queue). The idea is to maintain a heap where we keep track of the smallest pairs based on their sums, ensuring we return the k smallest pairs efficiently.

### Approach:

1. **Min-Heap**:
   - Since both arrays `nums1` and `nums2` are sorted, the smallest possible pair sum will come from the first element of `nums1` and the first element of `nums2`.
   - We can push the first pair `(nums1[0], nums2[0])` into the heap along with the indices of the elements to track them.

2. **Expanding from Smallest Pair**:
   - After extracting the smallest pair, the next candidate pairs for comparison would be:
     - The next element from `nums1` paired with the current element from `nums2` (i.e., `(nums1[i+1], nums2[j])`).
     - The current element from `nums1` paired with the next element from `nums2` (i.e., `(nums1[i], nums2[j+1])`).

   - By always expanding from the smallest sum, we ensure that we only explore the necessary pairs without having to generate all possible pairs upfront.

3. **Avoid Duplicates**:
   - To avoid pushing the same pair multiple times, we can track visited pairs using a set.

### Solution:

```python
import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    # Min-heap
    min_heap = []
    # Start by adding the pair (nums1[0], nums2[0]) and others with nums1[0] and every element of nums2
    for j in range(min(len(nums2), k)):  # Only push k elements for optimization
        heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

    result = []

    # Process the heap to get the smallest sums
    while min_heap and len(result) < k:
        curr_sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        # If there is a next element in nums1, add the pair (nums1[i+1], nums2[j])
        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i + 1, j))

    return result

# Example usage:
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(kSmallestPairs(nums1, nums2, k))  # Output: [[1,2],[1,4],[1,6]]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(kSmallestPairs(nums1, nums2, k))  # Output: [[1,1],[1,1]]
```

### Explanation:

1. **Initial Pair Selection**:
   - We start by pushing the first pair formed by the first element of `nums1` with each element of `nums2` into the heap. This ensures we explore pairs in increasing order of sums.

2. **Heap Operations**:
   - Each time we pop a pair from the heap, we add it to the result list.
   - After that, we push the next possible pair formed by the next element in `nums1` with the same element in `nums2` to the heap.

3. **Optimization**:
   - We only push up to `k` elements initially because there are at most `k` smallest sums that we care about.

### Time Complexity:

- **Heap operations** take `O(log k)` for each insertion and removal.
- We insert at most `k` elements into the heap, so the overall time complexity is:
  - **O(k log k)** for extracting and inserting elements from/to the heap.

### Space Complexity:
- The space complexity is **O(k)** for the heap and the result list since we store up to `k` pairs.

This approach ensures that we find the k smallest sums efficiently without generating all possible pairs, making it feasible even for large inputs.


Let’s go through an example to understand how this algorithm works.

### Problem:
You are given two sorted arrays, `nums1` and `nums2`, and an integer `k`. Your task is to find the `k` pairs `(nums1[i], nums2[j])` with the smallest sums.

The algorithm uses a **min-heap** to efficiently find the pairs with the smallest sums. A heap always keeps track of the smallest element at the top, making it ideal for this task.

### Example:
Let’s take the following arrays and `k` value:

```python
nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
```

We want to find the `3` pairs with the smallest sums.

---

### Step-by-Step Walkthrough:

1. **Initialize the Min-Heap:**
   - First, we initialize an empty min-heap (`min_heap`).
   - Then, we push pairs from `nums1[0]` (the first element of `nums1`) with every element from `nums2`, along with their sum. We only push `k` elements to keep the heap optimized.
   - In this case, the pairs we initially push to the heap are:
     - `(nums1[0], nums2[0]) = (1, 2)`, sum = 3
     - `(nums1[0], nums2[1]) = (1, 4)`, sum = 5
     - `(nums1[0], nums2[2]) = (1, 6)`, sum = 7

   After this step, the min-heap looks like this:

   ```
   min_heap = [(3, 0, 0), (5, 0, 1), (7, 0, 2)]
   ```
   Here, the tuple `(3, 0, 0)` represents the sum of the pair `(nums1[0] + nums2[0])`, along with the indices of the elements from `nums1` and `nums2`.

2. **Process the Heap:**
   - We now start processing the heap to extract the pairs with the smallest sums.
   - The idea is to pop the smallest sum from the heap, add the corresponding pair to the result, and then push the next possible pair involving the next element from `nums1`.

---

#### Iteration 1:

- Pop the smallest element from the heap: `(3, 0, 0)` (sum of `(1, 2)`).
- Add the pair `[1, 2]` to the result list.
- Now, push the next pair involving the next element from `nums1`, i.e., `(nums1[1], nums2[0]) = (7, 2)` with sum = `9`.

After this iteration, the min-heap looks like:

   ```
   min_heap = [(5, 0, 1), (7, 0, 2), (9, 1, 0)]
   ```
   And the result is:
   ```
   result = [[1, 2]]
   ```

---

#### Iteration 2:

- Pop the smallest element from the heap: `(5, 0, 1)` (sum of `(1, 4)`).
- Add the pair `[1, 4]` to the result list.
- Now, push the next pair involving the next element from `nums1`, i.e., `(nums1[1], nums2[1]) = (7, 4)` with sum = `11`.

After this iteration, the min-heap looks like:

   ```
   min_heap = [(7, 0, 2), (9, 1, 0), (11, 1, 1)]
   ```
   And the result is:
   ```
   result = [[1, 2], [1, 4]]
   ```

---

#### Iteration 3:

- Pop the smallest element from the heap: `(7, 0, 2)` (sum of `(1, 6)`).
- Add the pair `[1, 6]` to the result list.
- Now, push the next pair involving the next element from `nums1`, i.e., `(nums1[1], nums2[2]) = (7, 6)` with sum = `13`.

After this iteration, the min-heap looks like:

   ```
   min_heap = [(9, 1, 0), (11, 1, 1), (13, 1, 2)]
   ```
   And the result is:
   ```
   result = [[1, 2], [1, 4], [1, 6]]
   ```

At this point, the result list contains `k = 3` pairs, so we stop the process and return the result.

---

### Final Output:

```python
[[1, 2], [1, 4], [1, 6]]
```

These are the 3 pairs with the smallest sums.

---

### Key Points:

- The min-heap ensures we always process the smallest sum first.
- We use a two-level index (`i` for `nums1` and `j` for `nums2`) to track which pairs have been processed.
- The process continues until we find the required `k` smallest pairs.

This is a very efficient way to solve this problem, as it avoids generating all pairs and instead only processes the top `k` pairs using the min-heap.
