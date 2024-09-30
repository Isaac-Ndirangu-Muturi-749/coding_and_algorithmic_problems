To solve the problem of finding the **maximum profit** from buying and selling a stock, we can approach it using a **greedy algorithm** that keeps track of the lowest price observed so far and calculates the potential profit at each day. Here's the detailed explanation and solution:

### Key Idea:
- We want to buy the stock at a **minimum price** and sell it at a **maximum price** after the day we bought it.
- At each day, we calculate the profit by assuming that the current price is the selling price, and the minimum price so far is the buying price.

### Approach:
1. **Iterate through the prices array** while keeping track of two things:
   - **min_price_so_far**: The lowest price observed up to the current day.
   - **max_profit**: The maximum profit achievable based on the current selling price and the minimum price so far.

2. For each day's price:
   - Update `min_price_so_far` if the current price is lower than the previous minimum price.
   - Calculate the profit if we sell at the current price and update `max_profit` if this new profit is higher than the previous `max_profit`.

3. **Return** the maximum profit at the end of the iteration. If there is no positive profit, the algorithm will return 0.

### Algorithm:
1. Initialize `min_price_so_far` to a large value (infinity).
2. Initialize `max_profit` to 0.
3. For each price in the array, do the following:
   - Update `min_price_so_far` to be the minimum of the current price and `min_price_so_far`.
   - Calculate the profit if you sell at the current price, and update `max_profit` if the current profit is larger than the previous `max_profit`.
4. Return `max_profit` at the end.

### Code Implementation:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = float('inf')  # Start with infinity as the initial minimum price
        max_profit = 0  # Initially, no profit is made

        for price in prices:
            # Update the minimum price observed so far
            min_price_so_far = min(min_price_so_far, price)

            # Calculate the potential profit at the current price
            profit = price - min_price_so_far

            # Update the maximum profit if the current profit is greater
            max_profit = max(max_profit, profit)

        return max_profit
```

### Explanation:
1. **min_price_so_far**: This variable keeps track of the lowest price encountered so far. We want to buy at the lowest possible price.
2. **max_profit**: This variable keeps track of the maximum profit possible by selling at the current price.
3. **Iterating through the prices**: For each price, we check whether the profit from buying at the `min_price_so_far` and selling at the current price is larger than the previous `max_profit`.

### Time Complexity:
- **O(n)**: We iterate through the `prices` array once, making this an O(n) solution, where `n` is the length of the array.

### Space Complexity:
- **O(1)**: We only use a few variables (`min_price_so_far` and `max_profit`), so the space complexity is constant.

### Example Walkthrough:

#### Example 1:
Input: `prices = [7,1,5,3,6,4]`

- Day 1: `price = 7`, `min_price_so_far = 7`, `profit = 0`, `max_profit = 0`
- Day 2: `price = 1`, `min_price_so_far = 1`, `profit = 0`, `max_profit = 0`
- Day 3: `price = 5`, `min_price_so_far = 1`, `profit = 4`, `max_profit = 4`
- Day 4: `price = 3`, `min_price_so_far = 1`, `profit = 2`, `max_profit = 4`
- Day 5: `price = 6`, `min_price_so_far = 1`, `profit = 5`, `max_profit = 5`
- Day 6: `price = 4`, `min_price_so_far = 1`, `profit = 3`, `max_profit = 5`

Output: `max_profit = 5`

#### Example 2:
Input: `prices = [7,6,4,3,1]`

- Day 1: `price = 7`, `min_price_so_far = 7`, `profit = 0`, `max_profit = 0`
- Day 2: `price = 6`, `min_price_so_far = 6`, `profit = 0`, `max_profit = 0`
- Day 3: `price = 4`, `min_price_so_far = 4`, `profit = 0`, `max_profit = 0`
- Day 4: `price = 3`, `min_price_so_far = 3`, `profit = 0`, `max_profit = 0`
- Day 5: `price = 1`, `min_price_so_far = 1`, `profit = 0`, `max_profit = 0`

Output: `max_profit = 0`

### Conclusion:
This algorithm efficiently finds the maximum profit by iterating through the prices array in a single pass, with a time complexity of **O(n)** and a space complexity of **O(1)**. If no profit can be made, it returns 0.
