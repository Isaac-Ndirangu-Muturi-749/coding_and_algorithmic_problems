class StockSpanner:

    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Initial span is 1 (for the current day itself)
        span = 1

        # Pop from the stack while the price at the top is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add the span of the popped element to the current span

        # Push the current price and its span onto the stack
        self.stack.append((price, span))

        # Return the computed span
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
