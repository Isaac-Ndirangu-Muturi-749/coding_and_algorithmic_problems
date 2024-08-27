
Dynamic programming (DP) is a technique used to solve problems that can be broken down into smaller overlapping subproblems. The key idea is to store the results of these subproblems so that we do not recompute them repeatedly, improving efficiency.

Here’s why this problem falls under dynamic programming:

### Characteristics of Dynamic Programming:

1. **Overlapping Subproblems**:
   In this problem, the number of ways to reach step `n` can be calculated by knowing the number of ways to reach steps `n-1` and `n-2`. These subproblems overlap because the solution to reaching step `n-1` is used to calculate the solution to reaching step `n`, and so on.

2. **Optimal Substructure**:
   The optimal solution to the entire problem (i.e., finding the number of ways to reach step `n`) depends on the solutions to the smaller subproblems (finding the number of ways to reach steps `n-1` and `n-2`). The optimal solution can be constructed by combining the solutions to these subproblems.

3. **Memoization or Tabulation**:
   In this problem, dynamic programming is used in an iterative approach, where we use tabulation. We start by calculating the number of ways to reach the first few steps and then build up the solution for larger steps by using the results of previously computed steps. Instead of recalculating the number of ways for each step repeatedly, we store and reuse these results.

### Dynamic Programming in this Problem:

- **Recursive Relation**: The core of dynamic programming is the recursive relation, which in this case is:
  \[
  \text{ways}(n) = \text{ways}(n-1) + \text{ways}(n-2)
  \]
  This relation states that the number of ways to reach step `n` is the sum of the number of ways to reach steps `n-1` and `n-2`.

- **Bottom-Up Calculation**: In the provided solution, instead of solving the problem recursively (which would involve redundant calculations), we calculate the result for small steps first (starting with step 1 and 2) and then build the solution up to `n` using previously computed values. This iterative approach saves computation time and space.

- **Efficiency**: The use of dynamic programming reduces the time complexity of the problem from an exponential time complexity (in a naive recursive solution) to linear time complexity O(n). This is achieved by avoiding the recomputation of values and solving each subproblem only once.

### Visual Breakdown:

Let's visualize it with `n = 5`:

- Step 1: 1 way (just one step)
- Step 2: 2 ways (1+1 steps or 2 steps)
- Step 3: 3 ways (either step from step 2 or from step 1 twice)
- Step 4: 5 ways (either step from step 3 or from step 2)
- Step 5: 8 ways (either step from step 4 or from step 3)

At each step, you are combining the results of the previous two steps. This overlap in subproblems (reusing previously computed values) and the building of the solution step-by-step is the hallmark of dynamic programming.

### Conclusion:

The problem qualifies as dynamic programming because:
1. It involves solving overlapping subproblems (the result for step `n` depends on steps `n-1` and `n-2`).
2. The problem has optimal substructure (the solution for step `n` is built from optimal solutions of smaller steps).
3. We use an efficient iterative approach (tabulation) to store the results of subproblems and avoid redundant calculations.

This is what makes the approach dynamic programming.


This problem is a classic example of dynamic programming and can be related to the Fibonacci sequence. Let’s break down the approach:

### Key Observation:
To reach the top, you can either:
1. Take one step from `(n-1)` stairs.
2. Take two steps from `(n-2)` stairs.

Thus, the total number of ways to reach step `n` is the sum of ways to reach steps `n-1` and `n-2`. This gives us a recurrence relation similar to the Fibonacci sequence.

### Approach:

1. **Base Cases**:
   - If `n = 1`, there is only 1 way to reach the top (just take 1 step).
   - If `n = 2`, there are 2 ways to reach the top (either 1 step + 1 step or 2 steps).

2. **Recursive Relation**:
   - For `n > 2`, the number of ways to reach step `n` is the sum of the ways to reach step `n-1` and step `n-2`.

3. **Dynamic Programming**:
   We will use dynamic programming to build up the solution from the base cases.

### Solution in Python:

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the first two steps
        first = 1
        second = 2

        # Build the solution iteratively for each step from 3 to n
        for i in range(3, n + 1):
            third = first + second  # The current number of ways to reach the i-th step
            first = second  # Update first to second for the next iteration
            second = third  # Update second to third for the next iteration

        return second
```

### Explanation:

1. **Base Cases**:
   - For `n == 1`, return 1 directly since there is only one way to reach the top.
   - For `n == 2`, return 2 because there are exactly two ways to reach the top.

2. **Iteration**:
   - Start with the base values: `first = 1` and `second = 2`.
   - For every step from `3` to `n`, calculate the current number of ways (`third = first + second`), and then update `first` and `second` accordingly for the next step.

3. **Final Output**:
   After the loop, the variable `second` will hold the number of ways to reach the `n`-th step, which is the answer.

### Time and Space Complexity:
- **Time Complexity**: O(n) — We iterate from step 3 to step `n`.
- **Space Complexity**: O(1) — Only a constant amount of space is used (three variables).

### Example:

For `n = 5`, the iterations would look like:
- Step 3: `third = 1 + 2 = 3`
- Step 4: `third = 2 + 3 = 5`
- Step 5: `third = 3 + 5 = 8`

The output for `n = 5` would be `8`, as there are 8 distinct ways to climb a staircase with 5 steps.

### Recap:
This problem is solved efficiently using dynamic programming by recognizing the relationship between the current step and the previous two steps, and iterating over the solution.
