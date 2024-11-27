To solve the problem of finding the maximum profit from buying and selling stock, we need to take into account the following:

- We can perform as many transactions as possible, provided that we sell before we buy the next stock.
- The goal is to maximize the total profit.

### Approach:
1. **Identify local peaks and valleys**: Every time the price increases from one day to the next, you can profit by buying on the lower day and selling on the higher day. Essentially, the strategy is to sum up every increase between consecutive days.
2. **Ignore drops**: If the price drops or stays the same, there is no profit to be made by holding the stock.

### Greedy Strategy:
We can simply go through the list of prices and, whenever we find a price that is higher than the previous day, we calculate the difference and add it to the profit.

### Code Implementation:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # Loop through the prices array
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, we can profit by buying yesterday and selling today
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
```

### Explanation:
1. We loop through the `prices` array starting from day 1 (`i = 1`).
2. For each day `i`, if the price on that day (`prices[i]`) is greater than the price on the previous day (`prices[i - 1]`), we add the difference to our `total_profit`.
3. After iterating through all the prices, the `total_profit` will hold the maximum profit we can achieve.

### Example Walkthrough:

#### Example 1:
- Input: `prices = [7, 1, 5, 3, 6, 4]`
- We compare consecutive prices:
  - Day 1 to Day 2: `1 < 7` → no transaction.
  - Day 2 to Day 3: `5 > 1` → profit = `5 - 1 = 4`.
  - Day 3 to Day 4: `3 < 5` → no transaction.
  - Day 4 to Day 5: `6 > 3` → profit = `6 - 3 = 3`.
  - Day 5 to Day 6: `4 < 6` → no transaction.
- Total profit = `4 + 3 = 7`.

#### Example 2:
- Input: `prices = [1, 2, 3, 4, 5]`
- We compare consecutive prices:
  - Day 1 to Day 2: `2 > 1` → profit = `2 - 1 = 1`.
  - Day 2 to Day 3: `3 > 2` → profit = `3 - 2 = 1`.
  - Day 3 to Day 4: `4 > 3` → profit = `4 - 3 = 1`.
  - Day 4 to Day 5: `5 > 4` → profit = `5 - 4 = 1`.
- Total profit = `1 + 1 + 1 + 1 = 4`.

#### Example 3:
- Input: `prices = [7, 6, 4, 3, 1]`
- The prices keep decreasing, so no profit can be made. The total profit remains `0`.

### Time Complexity:
- **O(n)**: We iterate through the prices array once, where `n` is the length of the array.

### Space Complexity:
- **O(1)**: We are using a constant amount of extra space regardless of the input size.

This greedy solution efficiently calculates the maximum profit that can be achieved through multiple transactions in linear time.
