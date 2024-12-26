class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

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
