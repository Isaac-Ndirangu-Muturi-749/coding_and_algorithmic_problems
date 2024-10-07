class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        # Loop through the prices array
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, we can profit by buying yesterday and selling today
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
