To solve this problem, we need to maximize the capital after selecting at most \(k\) projects. Since projects have constraints on the initial capital required, and we want to maximize the profit, we can efficiently use a greedy approach with a combination of heaps.

---

### **Key Idea**

1. **Constraints**:
   - At any given time, we can only pick projects for which the required capital (\(capital[i]\)) is less than or equal to our current capital (\(w\)).
   - Once we pick a project, its profit (\(profits[i]\)) is added to \(w\).

2. **Optimization Strategy**:
   - Use a **min-heap** to store projects based on their required capital.
   - Use a **max-heap** to pick the project with the maximum profit among those that can be started.

---

### **Algorithm**

1. **Sort Projects by Capital**:
   - Pair each project as \((capital[i], profits[i])\) and sort them based on \(capital[i]\).

2. **Use a Min-Heap and Max-Heap**:
   - Use the **min-heap** to manage projects that can’t yet be started (sorted by capital).
   - Use the **max-heap** to manage projects that can be started (sorted by profit).

3. **Select at Most \(k\) Projects**:
   - Iterate \(k\) times:
     - Push all projects from the **min-heap** into the **max-heap** whose \(capital[i] \leq w\).
     - If the **max-heap** is empty, break (no project can be started).
     - Pop the project with the highest profit from the **max-heap** and update \(w\).

4. **Return the Final Capital**:
   - After \(k\) iterations or when no more projects can be started, return \(w\).

---

### **Code Implementation**

Here’s the Python implementation:

```python
import heapq

def findMaximizedCapital(k, w, profits, capital):
    # Pair capital and profit, then sort by capital
    projects = sorted(zip(capital, profits), key=lambda x: x[0])
    
    # Min-heap for capital and max-heap for profits
    min_heap = []
    max_heap = []
    
    # Index to keep track of projects in the sorted list
    i = 0
    n = len(projects)
    
    for _ in range(k):
        # Add all projects that can be started to the max-heap
        while i < n and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])  # Push profit as negative for max-heap
            i += 1
        
        # If no projects can be started, break
        if not max_heap:
            break
        
        # Pick the most profitable project
        w += -heapq.heappop(max_heap)  # Pop the max profit (negated)
    
    return w
```

---

### **Explanation of the Code**

1. **Sorting Projects by Capital**:
   - Sorting ensures that we can efficiently push projects into the max-heap in order of their required capital.

2. **Min-Heap to Max-Heap Transition**:
   - The min-heap keeps track of projects that require more capital than we currently have.
   - Once a project's \(capital[i] \leq w\), it’s moved to the max-heap.

3. **Picking the Most Profitable Project**:
   - The max-heap ensures that we always select the project with the highest profit that can currently be started.

4. **Stopping Conditions**:
   - If no more projects can be started (max-heap is empty), we terminate early.

---

### **Complexity Analysis**

#### **Time Complexity**:
1. Sorting projects: \(O(n \log n)\).
2. Adding projects to heaps:
   - Each project is pushed/popped into/from the heaps at most once.
   - Heap operations are \(O(\log n)\), so overall heap operations: \(O(n \log n)\).
3. Iterating \(k\) times: \(O(k)\).

**Total Time Complexity**: \(O(n \log n + k \log n)\).

#### **Space Complexity**:
- Max-heap and min-heap store at most \(n\) projects: \(O(n)\).

---

### **Example Walkthrough**

#### Example 1:
```python
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
```

1. **Input Processing**:
   - Projects: `[(0, 1), (1, 2), (1, 3)]`.

2. **First Iteration**:
   - Current capital: \(w = 0\).
   - Add projects with \(capital[i] \leq 0\) to max-heap: `[(-1)]`.
   - Pick project with max profit: profit = 1.
   - Update capital: \(w = 0 + 1 = 1\).

3. **Second Iteration**:
   - Current capital: \(w = 1\).
   - Add projects with \(capital[i] \leq 1\) to max-heap: `[(-2), (-3)]`.
   - Pick project with max profit: profit = 3.
   - Update capital: \(w = 1 + 3 = 4\).

**Output**: \(4\).

---

#### Example 2:
```python
k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]
```

1. **Input Processing**:
   - Projects: `[(0, 1), (1, 2), (2, 3)]`.

2. **First Iteration**:
   - Current capital: \(w = 0\).
   - Add projects with \(capital[i] \leq 0\) to max-heap: `[(-1)]`.
   - Pick project with max profit: profit = 1.
   - Update capital: \(w = 0 + 1 = 1\).

3. **Second Iteration**:
   - Current capital: \(w = 1\).
   - Add projects with \(capital[i] \leq 1\) to max-heap: `[(-2)]`.
   - Pick project with max profit: profit = 2.
   - Update capital: \(w = 1 + 2 = 3\).

4. **Third Iteration**:
   - Current capital: \(w = 3\).
   - Add projects with \(capital[i] \leq 3\) to max-heap: `[(-3)]`.
   - Pick project with max profit: profit = 3.
   - Update capital: \(w = 3 + 3 = 6\).

**Output**: \(6\).

---

### **Final Notes**

This solution ensures that we always maximize the capital at each step by leveraging efficient heap operations, which is crucial given the large constraints.