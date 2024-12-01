To solve the problem of finding the maximum possible score for the given arrays `nums1` and `nums2`, we can use a **greedy approach** combined with a **priority queue (min-heap)** to optimize the calculation of subsequences.

---

### **Approach**

1. **Key Observations**:
   - The score is defined as the sum of elements selected from `nums1` multiplied by the minimum of corresponding elements in `nums2`.
   - To maximize the score, focus on selecting indices with:
     - Large values in `nums2` (to maximize the minimum value).
     - Large values in `nums1` (to maximize the sum).

2. **Strategy**:
   - Pair elements from `nums1` and `nums2` as `(nums2[i], nums1[i])`.
   - Sort the pairs in descending order of `nums2[i]`.
   - Iterate through the sorted pairs, maintaining a min-heap of size `k` for the largest `k` values of `nums1`.
   - For each `nums2[i]` (acting as the minimum), calculate the score using the sum of the heap elements.

3. **Steps**:
   - Sort the indices based on `nums2` in descending order.
   - Use a min-heap to maintain the top `k` largest values of `nums1`.
   - As you iterate, update the heap and calculate the score for the current `nums2[i]` as the minimum.

---

### **Python Implementation**

```python
import heapq

def maxScore(nums1, nums2, k):
    # Pair elements and sort by nums2 in descending order
    pairs = sorted(zip(nums2, nums1), reverse=True)

    min_heap = []  # Min-heap for the largest k values in nums1
    max_score = 0
    current_sum = 0

    for num2, num1 in pairs:
        # Add nums1 value to the heap and current sum
        heapq.heappush(min_heap, num1)
        current_sum += num1

        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            current_sum -= heapq.heappop(min_heap)

        # If we have exactly k elements, calculate the score
        if len(min_heap) == k:
            max_score = max(max_score, current_sum * num2)

    return max_score
```

---

### **Explanation**

1. **Sorting**:
   - The `pairs` list is sorted based on `nums2` values in descending order. This ensures that we consider the largest possible minimum values first.
2. **Heap Maintenance**:
   - A min-heap is used to track the top `k` largest values from `nums1`.
   - If the heap exceeds size `k`, remove the smallest element (ensures only the top `k` elements contribute to the score).
3. **Score Calculation**:
   - For every valid heap of size `k`, compute the score as `(current_sum of heap) * (current nums2[i])`.

---

### **Examples**

#### Example 1:
```python
nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3
print(maxScore(nums1, nums2, k))  # Output: 12
```

#### Example 2:
```python
nums1 = [4, 2, 3, 1, 1]
nums2 = [7, 5, 10, 9, 6]
k = 1
print(maxScore(nums1, nums2, k))  # Output: 30
```

---

### **Complexity Analysis**

1. **Time Complexity**:
   - Sorting the pairs: \(O(n \log n)\)
   - Iterating through pairs and maintaining the heap: \(O(n \log k)\)
   - Total: \(O(n \log n)\)

2. **Space Complexity**:
   - Min-heap space: \(O(k)\)
   - Total: \(O(k)\)

This solution is efficient and works well for the given constraints.
