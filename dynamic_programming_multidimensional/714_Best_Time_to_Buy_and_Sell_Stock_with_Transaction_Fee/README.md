To solve this problem, we can use **Dynamic Programming (DP)** to track the maximum profit at each day based on whether we hold a stock or not.

We define:
- **`hold`**: The maximum profit we can have if we are holding a stock on a given day.
- **`not_hold`**: The maximum profit we can have if we are not holding a stock on a given day.

### Transition Relations:
1. **If holding a stock on day \(i\)**:
   - We either continue holding the stock from the previous day or buy a new stock at the current price:
     \[
     hold[i] = \max(hold[i-1], not\_hold[i-1] - prices[i])
     \]

2. **If not holding a stock on day \(i\)**:
   - We either continue not holding from the previous day or sell the stock we are holding and pay the transaction fee:
     \[
     not\_hold[i] = \max(not\_hold[i-1], hold[i-1] + prices[i] - fee)
     \]

3. **Base Cases**:
   - At day \(0\):
     - If we buy the stock: \(hold[0] = -prices[0]\)
     - If we don't buy the stock: \(not\_hold[0] = 0\)

### Optimized Space Complexity:
Instead of maintaining full DP arrays for `hold` and `not_hold`, we only keep track of their current values, as each state only depends on the previous state.

---

### Python Implementation:
```python
def maxProfit(prices, fee):
    # Initialize the base cases
    hold = -prices[0]  # Maximum profit when holding a stock on day 0
    not_hold = 0       # Maximum profit when not holding a stock on day 0

    # Iterate through the days
    for price in prices[1:]:
        # Update the state variables
        hold = max(hold, not_hold - price)
        not_hold = max(not_hold, hold + price - fee)

    # The result is the maximum profit when not holding a stock at the end
    return not_hold
```

---

### Example Walkthrough:
#### Example 1:
```python
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(maxProfit(prices, fee))  # Output: 8
```

**Explanation**:
- Buy at day 0: \(-1\)
- Sell at day 3: \(+8 - 2 = +5\)
- Buy at day 4: \(-4\)
- Sell at day 5: \(+9 - 2 = +3\)
- Total profit: \(5 + 3 = 8\)

#### Example 2:
```python
prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(maxProfit(prices, fee))  # Output: 6
```

---

### Complexity Analysis:
1. **Time Complexity**: \(O(n)\), where \(n\) is the number of days (prices length), as we iterate through the prices once.
2. **Space Complexity**: \(O(1)\), since we only use two variables (`hold` and `not_hold`) to store the current state.

This approach ensures efficient computation for large input sizes.
