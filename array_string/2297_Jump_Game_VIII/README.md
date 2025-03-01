### **Solution Approach:**
The problem requires us to find the minimum cost to reach the last index (`n-1`) from index `0` while following specific jump rules. Since we need the shortest path with weighted edges (costs), **Dijkstra's algorithm (or a priority queue-based approach)** is well-suited for this problem.

---

### **Key Observations:**
1. We can only jump **forward** (`i < j`).
2. A valid jump `(i → j)` occurs if:
   - **Increasing case:** `nums[i] <= nums[j]` and every number between them (`nums[k]` for `i < k < j`) is **strictly smaller** than `nums[i]`.
   - **Decreasing case:** `nums[i] > nums[j]` and every number between them is **greater than or equal** to `nums[i]`.
3. The goal is to **find the minimum-cost path** from `0` to `n-1`.

---

### **Efficient Approach using a Priority Queue (Dijkstra's Algorithm)**
- **Graph Representation:**
  - Treat `nums` as nodes and valid jumps as directed weighted edges with `costs[j]` as the edge weight.
- **Priority Queue (`min-heap`) to find the minimum-cost path:**
  - The priority queue stores `(current_cost, index)`, and we always expand the **minimum-cost** option first.
- **Processing:**
  1. Start at `index 0` with cost `0`.
  2. Try jumping to all valid `j > i` and update the cost if it's lower than the previously found cost.
  3. Use a **priority queue (heap)** to always process the node with the **lowest current cost** first.
  4. If we reach `index n-1`, return the cost.

---

### **Implementation:**
```python
from heapq import heappop, heappush
from collections import deque

class Solution:
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        n = len(nums)
        min_cost = [float('inf')] * n  # Store min cost to reach each index
        min_cost[0] = 0  # Cost to reach index 0 is 0
        pq = [(0, 0)]  # (current cost, index)

        # Maintain two monotonic stacks to find valid jumps efficiently
        increasing_stack = deque()  # Monotonic increasing
        decreasing_stack = deque()  # Monotonic decreasing

        while pq:
            current_cost, i = heappop(pq)

            if i == n - 1:
                return current_cost  # Found the minimum cost to reach the last index

            # Process increasing valid jumps
            while increasing_stack and nums[increasing_stack[-1]] < nums[i]:
                j = increasing_stack.pop()
                new_cost = current_cost + costs[j]
                if new_cost < min_cost[j]:
                    min_cost[j] = new_cost
                    heappush(pq, (new_cost, j))

            increasing_stack.append(i)

            # Process decreasing valid jumps
            while decreasing_stack and nums[decreasing_stack[-1]] >= nums[i]:
                j = decreasing_stack.pop()
                new_cost = current_cost + costs[j]
                if new_cost < min_cost[j]:
                    min_cost[j] = new_cost
                    heappush(pq, (new_cost, j))

            decreasing_stack.append(i)

        return -1  # Should never reach here if there's always a valid path
```

---

### **Complexity Analysis:**
- **Heap operations (`O(log n)`)**: Each node is pushed/popped at most once, leading to `O(n log n)`.
- **Monotonic Stack Processing (`O(n)`)**: Each element is processed at most once in the stacks.
- **Total Complexity:** **`O(n log n)`** (Dijkstra’s with monotonic stacks).

---

### **Example Walkthrough**
#### **Example 1:**
**Input:**
```plaintext
nums = [3,2,4,4,1], costs = [3,7,6,4,2]
```
**Valid jumps:**
- `0 → 2` (`3 → 4` with cost `6`)
- `2 → 4` (`4 → 1` with cost `2`)

**Output:**
```plaintext
8
```

---

### **Why This Works Efficiently**
- **Avoids checking all `O(n^2)` pairs** by using **monotonic stacks**.
- **Uses Dijkstra’s algorithm** to ensure we **always expand the lowest-cost path first**.
- **Ensures `O(n log n)` complexity** instead of brute-force `O(n^2)`.

This approach guarantees the **minimum cost** while efficiently processing valid jumps. 🚀



### other**
```python
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        adjacency_list = defaultdict(list)  # Stores valid jumps from each index
        increasing_stack = []  # Monotonic increasing stack
        decreasing_stack = []  # Monotonic decreasing stack

        # Build the graph for valid jumps based on increasing sequence rule
        for i in range(n - 1, -1, -1):
            # Ensure stack elements are greater than the current element
            while increasing_stack and nums[increasing_stack[-1]] < nums[i]:
                increasing_stack.pop()
            # If stack not empty, make a connection in graph
            if increasing_stack:
                adjacency_list[i].append(increasing_stack[-1])
            increasing_stack.append(i)

        # Build the graph for valid jumps based on decreasing sequence rule
        for i in range(n - 1, -1, -1):
            # Ensure stack elements are greater than or equal to the current element
            while decreasing_stack and nums[decreasing_stack[-1]] >= nums[i]:
                decreasing_stack.pop()
            # If stack not empty, make a connection in graph
            if decreasing_stack:
                adjacency_list[i].append(decreasing_stack[-1])
            decreasing_stack.append(i)

        # Dynamic Programming array to track minimum cost to reach each index
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Starting point has 0 cost

        # Traverse and update costs using DP
        for i in range(n):
            for next_index in adjacency_list[i]:
                min_cost[next_index] = min(min_cost[next_index], min_cost[i] + costs[next_index])

        return min_cost[n - 1]  # Minimum cost to reach last index
```

---

### **Approach & Explanation**
This solution uses **monotonic stacks** and **dynamic programming (DP)** to efficiently determine the minimum cost path.

#### **Step 1: Construct a Graph of Valid Jumps**
We create an adjacency list (`adjacency_list`) where:
1. **Increasing case:** `nums[i] <= nums[j]`, ensuring `nums[k] < nums[i]` for `i < k < j`
2. **Decreasing case:** `nums[i] > nums[j]`, ensuring `nums[k] >= nums[i]` for `i < k < j`

- We maintain **two monotonic stacks**:
  - `increasing_stack`: Stores indices such that values are **increasing**.
  - `decreasing_stack`: Stores indices such that values are **non-increasing**.

By iterating **backwards** (`n-1` to `0`), we efficiently determine the valid jumps for each index in **O(n)**.

#### **Step 2: Compute Minimum Cost Using Dynamic Programming**
- We use `min_cost[i]` to store the minimum cost to reach index `i`.
- Start with `min_cost[0] = 0`.
- Iterate through each index and update its valid next indices using **relaxation**:
  - `min_cost[next_index] = min(min_cost[next_index], min_cost[i] + costs[next_index])`

This step ensures **we always take the least expensive path**.

#### **Time Complexity Analysis**
1. **Graph Construction (Monotonic Stack) → `O(n)`**
   - Each element is pushed/popped at most once.
2. **DP Update (Relaxation) → `O(n)`**
   - Each node is visited and relaxed at most once.

Thus, the overall complexity is **O(n)**, making this approach **efficient for large inputs** (`n ≤ 100,000`).

Time Complexity
The time complexity of the code can be analyzed by examining the two main parts of the algorithm: graph construction and dynamic programming.

Graph Construction: There are two similar loops that iterate backward through the input list nums, from n - 1 to 0. Each loop performs a constant amount of work for each element by comparing against elements in a stack and updating the graph g. The worst-case time complexity for each of these loops is O(n), because each element is pushed to and popped from the stack at most once.

Dynamic Programming: After building the graph, the algorithm iterates over each element in the list nums and updates the minimum cost for each connected node. Since each node can have at most two connections (because in the worst case, there’s a connection to the next greater element and next smaller or equal element), and there are n nodes, the loop iterates at most 2n times. Within this loop, the cost calculation is constant time.

Combining both parts, the total time complexity of the entire algorithm is O(n + 2n), which simplifies to O(n).

Space Complexity
The space complexity is determined by the additional space required for the data structures used in the algorithm:

Graph Representation (g): The graph g is represented using a defaultdict of lists, which can potentially contain up to 2n edges (in the form of list items), where n is the number of elements in the input list nums.

Stacks (stk): Two stacks are used in the graph construction, and each can contain up to n indices at any one time.

Dynamic Programming Array (f): A list f of length n is used to store the minimum cost up to that point.

Taking all these into consideration, the space complexity is O(n + 2n + n), which simplifies to O(n) since constants are dropped in Big O notation.
---

### **Example Walkthrough**
#### **Example 1**
```python
nums = [3,2,4,4,1]
costs = [3,7,6,4,2]
```
**Valid Jumps:**
- `0 → 2` (`3 → 4` with cost `6`)
- `2 → 4` (`4 → 1` with cost `2`)

**Minimum Cost Path:**
- `0 → 2 (cost = 6)`
- `2 → 4 (cost = 2)`

**Total Minimum Cost:** `8`

---

### **Why This Works Efficiently**
- **Monotonic stacks** allow us to efficiently **find valid jumps** in `O(n)`.
- **Dynamic programming** ensures we **only update each node optimally once**.
- **Graph-based approach avoids brute-force `O(n^2)` checking**, making it scalable.

This is an **optimal** and **efficient** approach to solve the problem in `O(n)`. 🚀
