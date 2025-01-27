class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) < 2:
            return 0

        n = len(prices)
        leftProfit = [0] * n  # Max profit for one transaction up to day i
        rightProfit = [0] * n  # Max profit for one transaction from day i to the end

        # Compute leftProfit
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            leftProfit[i] = max(leftProfit[i - 1], prices[i] - minPrice)

        # Compute rightProfit
        maxPrice = prices[-1]
        for i in range(n - 2, -1, -1):
            maxPrice = max(maxPrice, prices[i])
            rightProfit[i] = max(rightProfit[i + 1], maxPrice - prices[i])

        # Combine leftProfit and rightProfit
        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, leftProfit[i] + rightProfit[i])

        return maxProfit
