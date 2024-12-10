This problem is a classic **dynamic programming (DP)** problem, where the goal is to find the minimum cost to reach the top of the staircase.

---

### **Approach**
The idea is to determine the minimum cost to reach each step, and use that to compute the minimum cost to reach the top.

1. Let `dp[i]` represent the minimum cost to reach the \(i\)-th step.
2. You can reach the \(i\)-th step either from the \((i-1)\)-th step or the \((i-2)\)-th step:
   - If you come from \((i-1)\)-th step, the cost is `dp[i-1] + cost[i-1]`.
   - If you come from \((i-2)\)-th step, the cost is `dp[i-2] + cost[i-2]`.
3. Recurrence relation:
   \[
   dp[i] = \min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
   \]
4. Base cases:
   - `dp[0] = 0` (starting from step 0 incurs no cost).
   - `dp[1] = 0` (starting from step 1 incurs no cost).

5. The final result is `dp[n]`, where \(n = \text{len(cost)}\).

To optimize space, we can use two variables to store the last two DP states instead of maintaining a full array.

---

### **Python Implementation**
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Initialize the first two steps
        prev2 = 0
        prev1 = 0

        # Compute the minimum cost for each step
        for i in range(2, n + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2 = prev1
            prev1 = curr

        return prev1
```

---

### **Explanation**
1. **Input Example 1**: `cost = [10, 15, 20]`
   - \(dp[0] = 0\), \(dp[1] = 0\)
   - \(dp[2] = \min(dp[1] + cost[1], dp[0] + cost[0]) = \min(0 + 15, 0 + 10) = 10\)
   - \(dp[3] = \min(dp[2] + cost[2], dp[1] + cost[1]) = \min(10 + 20, 0 + 15) = 15\)
   - Output: `15`

2. **Input Example 2**: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`
   - \(dp[0] = 0\), \(dp[1] = 0\)
   - \(dp[2] = \min(dp[1] + cost[1], dp[0] + cost[0]) = \min(0 + 100, 0 + 1) = 1\)
   - \(dp[3] = \min(dp[2] + cost[2], dp[1] + cost[1]) = \min(1 + 1, 0 + 100) = 2\)
   - Continue until \(dp[10] = 6\)
   - Output: `6`

---

### **Complexity Analysis**
1. **Time Complexity**: \(O(n)\)
   - We compute the minimum cost for each step once.
2. **Space Complexity**: \(O(1)\)
   - We use only two variables (`prev1` and `prev2`) to store the DP states.

This solution is efficient and handles the constraints effectively.
