To solve the problem of computing the stock span, we can design an efficient algorithm using a **monotonic stack**. The main idea is to maintain a stack of indices that represent the previous days where the stock price was less than or equal to the current day's price.

### Key Concepts:
1. **Span**: The span for a given day is the number of consecutive days (starting from the current day and going backward) where the stock price was less than or equal to the price of the current day.
2. **Monotonic Stack**: We use a stack to store the indices of stock prices, ensuring that the prices in the stack are in a non-decreasing order. The stack helps us quickly find the previous day where the stock price was greater than the current price, allowing us to compute the span efficiently.

### Approach:
1. **For each price**:
   - If the stack is empty, it means the current price is greater than all previous prices. The span is the number of days from the start to today (i.e., span = current day index + 1).
   - If the stack is not empty, we pop elements from the stack while the price at the top of the stack is less than or equal to the current price. This way, we find the nearest day where the stock price was greater than the current price.
   - The span for the current day is then the difference between the current day index and the index of the last element left in the stack (after popping).
2. **Push the current day's index onto the stack** to keep track of the prices for future span calculations.

### Detailed Algorithm:
1. **Initialize** an empty stack and an empty result list.
2. **For each price**:
   - Pop from the stack while the stack is not empty and the price at the index in the stack is less than or equal to the current price.
   - If the stack becomes empty, it means the current price is greater than all previous prices, and the span is the current day index + 1.
   - If the stack is not empty, the span is the difference between the current day index and the index of the last element in the stack.
   - Push the current day's index onto the stack.

### Code Implementation:

```python
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
```

### Explanation:
- **`StockSpanner` class**: Contains a `stack` to store pairs of (price, span). Each entry in the stack holds the price and its computed span.
- **`next(price)` method**:
  - Starts with a span of 1 for the current day.
  - Uses the stack to find the previous days' prices that are less than or equal to the current price.
  - Computes the span by adding the spans of the days removed from the stack.
  - Pushes the current price and its span onto the stack.
  - Returns the span for the current day.

### Time Complexity:
- Each price is pushed and popped from the stack at most once, so the time complexity for each `next(price)` call is **O(1)**.
- Since at most `10^4` calls will be made to `next`, the overall complexity is **O(n)** where `n` is the number of `next` calls.

### Example Walkthrough:

#### Input:
```python
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))   # Output: 1
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(70))   # Output: 2
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(75))   # Output: 4
print(stockSpanner.next(85))   # Output: 6
```

**Explanation**:
- `100`: No previous prices, so span = 1.
- `80`: The price is smaller than `100`, so span = 1.
- `60`: The price is smaller than both `100` and `80`, so span = 1.
- `70`: The price is greater than `60`, so span = 2 (current price and the previous price `60`).
- `60`: The price is smaller than `70`, so span = 1.
- `75`: The price is greater than `60` and `70`, so span = 4.
- `85`: The price is greater than all previous prices, so span = 6.

### Example Output:
```python
[1, 1, 1, 2, 1, 4, 6]
```

### Conclusion:
The algorithm efficiently computes the span for each stock price in **O(1)** time using a monotonic stack, making it suitable for handling a large number of queries (up to 10,000). The stack ensures that we can quickly calculate the span without having to check all previous prices for each new price.
