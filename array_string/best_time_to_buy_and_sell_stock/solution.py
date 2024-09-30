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
