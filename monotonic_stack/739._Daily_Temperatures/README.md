To solve this problem efficiently, we can use a **monotonic decreasing stack**. This approach allows us to compute the number of days to wait for a warmer temperature in \( O(n) \) time complexity.

---

### **Approach**
1. Use a stack to store the indices of temperatures in decreasing order.
2. Iterate through the `temperatures` array:
   - For each day \( i \), check if the current temperature is warmer than the temperature at the indices stored in the stack:
     - If it is, calculate the difference in days (i.e., \( i - \text{stack.pop()} \)) and store it in the result array.
   - Push the current day \( i \) onto the stack.
3. At the end of the iteration, any remaining indices in the stack will have a result of `0` (no warmer day exists).

---

### **Algorithm**
1. Initialize an array `answer` of size \( n \) (length of `temperatures`) with all elements as `0`.
2. Use a stack to store indices of the days.
3. Iterate over the array:
   - While the stack is not empty and the current temperature is greater than the temperature at the index on top of the stack:
     - Pop the index from the stack.
     - Compute the difference between the current index and the popped index and store it in the `answer` array.
   - Push the current index onto the stack.
4. Return the `answer` array.

---

### **Implementation**

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stack to store indices of temperatures

        for i in range(n):
            # While the current temperature is warmer than the temperature at stack[-1]
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            # Push the current index onto the stack
            stack.append(i)

        return answer
```

---

### **Explanation with Examples**

#### Example 1:
Input:
```plaintext
temperatures = [73,74,75,71,69,72,76,73]
```

Steps:
1. Initialize `answer = [0, 0, 0, 0, 0, 0, 0, 0]` and `stack = []`.
2. Process each day:
   - Day 0: Stack becomes `[0]` (no warmer day yet).
   - Day 1: 74 > 73 → `answer[0] = 1`, stack becomes `[1]`.
   - Day 2: 75 > 74 → `answer[1] = 1`, stack becomes `[2]`.
   - Day 3: 71 <= 75 → Stack becomes `[2, 3]`.
   - Day 4: 69 <= 71 → Stack becomes `[2, 3, 4]`.
   - Day 5: 72 > 69 → `answer[4] = 1`, 72 > 71 → `answer[3] = 2`, stack becomes `[2, 5]`.
   - Day 6: 76 > 72 → `answer[5] = 1`, 76 > 75 → `answer[2] = 4`, stack becomes `[6]`.
   - Day 7: 73 <= 76 → Stack becomes `[6, 7]`.
3. Final `answer = [1, 1, 4, 2, 1, 1, 0, 0]`.

Output:
```plaintext
[1, 1, 4, 2, 1, 1, 0, 0]
```

#### Example 2:
Input:
```plaintext
temperatures = [30,40,50,60]
```

Steps:
1. Day 0: Stack becomes `[0]`.
2. Day 1: 40 > 30 → `answer[0] = 1`, stack becomes `[1]`.
3. Day 2: 50 > 40 → `answer[1] = 1`, stack becomes `[2]`.
4. Day 3: 60 > 50 → `answer[2] = 1`, stack becomes `[3]`.
5. Final `answer = [1, 1, 1, 0]`.

Output:
```plaintext
[1, 1, 1, 0]
```

---

### **Complexity Analysis**
1. **Time Complexity**: \( O(n) \)
   - Each temperature is pushed and popped from the stack at most once.
2. **Space Complexity**: \( O(n) \)
   - The stack stores at most \( n \) indices in the worst case.

This is the optimal solution for the problem.


A **monotonic decreasing stack** is a stack data structure where the elements are stored in a **decreasing order** from top to bottom. This means that when pushing a new element onto the stack, elements at the top of the stack are popped if they are smaller than or equal to the incoming element.

---

### **How It Works:**

1. **Maintaining Decreasing Order**:
   - When a new element is pushed:
     - If the top of the stack has elements smaller than or equal to the current element, pop those elements (to maintain the decreasing order).
     - Then, push the current element onto the stack.

2. **Purpose**:
   - It helps solve problems where the previous larger element or other comparisons need to be tracked efficiently.
   - Commonly used in **sliding window**, **next greater/smaller element**, or **range-related problems**.

---

### **Key Characteristics**:
- The stack always stores elements in decreasing order (e.g., `[7, 5, 3, 2]` from bottom to top).
- If an element violates the decreasing property, it is removed from the stack.

---

### **Example Code: Next Greater Element (Right)**

Given an array `nums`, find the **next greater element** for every element in the array. Return `-1` if no greater element exists.

```python
def nextGreaterElements(nums):
    stack = []  # Monotonic decreasing stack
    result = [-1] * len(nums)  # Initialize result array with -1

    for i in range(len(nums) - 1, -1, -1):  # Traverse from right to left
        # Pop smaller or equal elements from the stack
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # If stack is not empty, the top element is the next greater element
        if stack:
            result[i] = stack[-1]

        # Push the current element into the stack
        stack.append(nums[i])

    return result
```

---

### **Example Walkthrough**

#### Input:
```python
nums = [4, 5, 2, 10, 8]
```

#### Step-by-Step Execution:
1. Start with `stack = []` and `result = [-1, -1, -1, -1, -1]`.

2. **Traverse in reverse (right to left):**
   - **i = 4 (nums[4] = 8):**
     - `stack` is empty, so no next greater element exists.
     - Push `8` onto the stack: `stack = [8]`.

   - **i = 3 (nums[3] = 10):**
     - `8 <= 10`, so pop `8` (maintain decreasing order).
     - Stack becomes empty; no next greater element exists.
     - Push `10` onto the stack: `stack = [10]`.

   - **i = 2 (nums[2] = 2):**
     - `10 > 2`, so the next greater element is `10`.
     - Update `result[2] = 10`.
     - Push `2` onto the stack: `stack = [10, 2]`.

   - **i = 1 (nums[1] = 5):**
     - `2 <= 5`, pop `2`.
     - `10 > 5`, so the next greater element is `10`.
     - Update `result[1] = 10`.
     - Push `5` onto the stack: `stack = [10, 5]`.

   - **i = 0 (nums[0] = 4):**
     - `5 > 4`, so the next greater element is `5`.
     - Update `result[0] = 5`.
     - Push `4` onto the stack: `stack = [10, 5, 4]`.

#### Final Result:
```python
result = [5, 10, 10, -1, -1]
```

---

### **Advantages of Monotonic Stacks**:
1. **Efficient**: Each element is pushed and popped from the stack once, resulting in \(O(n)\) time complexity.
2. **Simplifies Problems**: It avoids nested loops for problems involving comparisons across elements.

---

### **Other Applications**:
1. **Daily Temperatures Problem** (Find the number of days until a warmer temperature).
2. **Largest Rectangle in Histogram** (Find the largest rectangle in a histogram using heights).
3. **Trapping Rain Water** (Calculate water trapped between bars of varying heights).
