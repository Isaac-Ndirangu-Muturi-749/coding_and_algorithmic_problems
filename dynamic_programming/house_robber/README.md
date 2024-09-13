To solve the problem of maximizing the amount of money you can rob without alerting the police, we can use **dynamic programming**. The key constraint is that you cannot rob two adjacent houses.

### Approach:
Let’s define a dynamic programming approach where at each step, you either:
- Rob the current house, but skip the previous house.
- Skip the current house and keep the best amount you got from the previous houses.

Let `dp[i]` represent the maximum amount of money you can rob from the first `i` houses. At each house `i`, you have two options:
1. Rob the house `i` (and add its money to the maximum money you can rob up to house `i-2`).
2. Skip the house `i` and take the maximum money from house `i-1`.

Thus, the recurrence relation becomes:
- `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

Where:
- `dp[i-1]` means you skip the current house.
- `dp[i-2] + nums[i]` means you rob the current house.

### Base cases:
- `dp[0] = nums[0]` (If there is only one house, rob it.)
- `dp[1] = max(nums[0], nums[1])` (Rob the house with the larger amount between house 0 and house 1.)

### Time Complexity:
- **O(n)**: We only loop through the list once.

### Space Complexity:
- **O(1)**: We don't need to store the entire `dp` array, as we only need the last two states at any time.

### Code Implementation:

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = 0  # This will store dp[i-2]
        prev1 = 0  # This will store dp[i-1]

        for i in range(n):
            current = max(prev1, prev2 + nums[i])  # Calculate dp[i]
            prev2 = prev1  # Update dp[i-2] to dp[i-1] for next iteration
            prev1 = current  # Update dp[i-1] to dp[i] for next iteration

        return prev1

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
print(solution.rob(nums1))  # Output: 4

# Example 2
nums2 = [2, 7, 9, 3, 1]
print(solution.rob(nums2))  # Output: 12
```

### Explanation:
1. We maintain two variables `prev1` and `prev2`, which correspond to the maximum amount of money robbed up to house `i-1` and `i-2`, respectively.
2. As we iterate over each house, we calculate the maximum money that can be robbed up to the current house based on whether we rob it or skip it.
3. After processing all the houses, `prev1` will hold the maximum amount that can be robbed.

### Example Walkthrough:
#### Example 1:
- Input: `nums = [1, 2, 3, 1]`
- Rob house 1 (`1`), skip house 2, rob house 3 (`3`).
- Maximum amount = `1 + 3 = 4`.

#### Example 2:
- Input: `nums = [2, 7, 9, 3, 1]`
- Rob house 1 (`2`), skip house 2, rob house 3 (`9`), skip house 4, rob house 5 (`1`).
- Maximum amount = `2 + 9 + 1 = 12`.



**Dynamic Programming (DP)** is a technique for solving complex problems by breaking them down into simpler subproblems and solving each subproblem just once, storing the results to avoid redundant calculations. It is particularly useful for optimization problems where overlapping subproblems and optimal substructure properties are present.

### Key Concepts of Dynamic Programming:

1. **Optimal Substructure**:
   - A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. In other words, the solution to the problem can be constructed from solutions to its subproblems.

2. **Overlapping Subproblems**:
   - A problem exhibits overlapping subproblems if the same subproblems are solved multiple times during the computation of the solution. By solving each subproblem only once and storing its result, DP avoids redundant computations.

### Approach to Dynamic Programming:

1. **Define the State**:
   - Define what the subproblems are and how they can be represented. This usually involves determining the parameters that uniquely define each subproblem.

2. **Formulate the Recurrence Relation**:
   - Establish a relationship between the solution of the current subproblem and the solutions of smaller subproblems. This recurrence relation is used to build up the solution to the original problem from the solutions to subproblems.

3. **Compute the Solution**:
   - Solve the subproblems and store their results. This is typically done in a bottom-up fashion (iteratively filling up a table) or top-down fashion (using memoization).

4. **Retrieve the Solution**:
   - Extract the solution to the original problem from the computed results.

### Types of Dynamic Programming:

1. **Top-Down Approach (Memoization)**:
   - Start with the original problem and recursively solve subproblems as they are needed.
   - Store the results of subproblems in a cache (e.g., a dictionary or list) to avoid redundant calculations.
   - Example: Recursive implementation with memoization.

2. **Bottom-Up Approach (Tabulation)**:
   - Solve all possible subproblems in a specific order and store their results in a table (e.g., a 2D array).
   - Build up the solution to the original problem from the solutions to the smaller subproblems.
   - Example: Iterative implementation using a table or array.

### Example Problem: Fibonacci Numbers

**Problem**: Compute the nth Fibonacci number.

- **Recursive Formula**: \( F(n) = F(n-1) + F(n-2) \)

**Top-Down Approach**:
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

**Bottom-Up Approach**:
```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Example Problem: 0/1 Knapsack

**Problem**: Given weights and values of items, and a knapsack with a weight capacity, find the maximum value that can be obtained by putting items in the knapsack without exceeding the capacity.

**Top-Down Approach**:
```python
def knapsack(weights, values, capacity, n, memo={}):
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        result = knapsack(weights, values, capacity, n-1, memo)
    else:
        result = max(knapsack(weights, values, capacity, n-1, memo),
                     values[n-1] + knapsack(weights, values, capacity-weights[n-1], n-1, memo))
    memo[(n, capacity)] = result
    return result
```

**Bottom-Up Approach**:
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]
```

### Advantages of Dynamic Programming:

- **Efficiency**: Reduces the time complexity by avoiding redundant calculations, often resulting in polynomial time complexity.
- **Optimal Solutions**: Guarantees finding the optimal solution to problems with optimal substructure and overlapping subproblems.

### Disadvantages:

- **Space Complexity**: May require additional space to store intermediate results, which can be significant for large problems.
- **Complexity**: Can be complex to implement and understand, especially for problems with intricate relationships between subproblems.

Dynamic programming is a powerful technique used in various algorithms and problems, including optimization, scheduling, and combinatorial problems.



