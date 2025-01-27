To solve this problem, we can use a dynamic programming approach. We aim to maximize the profit from at most two transactions.

Key Idea:

We track two transactions:

1. The first transaction's profit.


2. The second transaction's profit.



For each day, we'll calculate:

The maximum profit we can achieve with one transaction up to that day.

The maximum profit we can achieve with two transactions up to that day.



---

Algorithm:

1. Track profits for two transactions:

Use two arrays:

leftProfit[i]: Maximum profit we can achieve with one transaction from day 0 to day i.

rightProfit[i]: Maximum profit we can achieve with one transaction from day i to the last day.




2. Compute leftProfit:

Traverse the array from left to right.

Track the minimum price seen so far, and calculate the maximum profit we can achieve for each day.



3. Compute rightProfit:

Traverse the array from right to left.

Track the maximum price seen so far, and calculate the maximum profit we can achieve for each day.



4. Combine results:

For each day i, the total profit is leftProfit[i] + rightProfit[i].

Return the maximum total profit.





---

Code Implementation:

def maxProfit(prices):
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


---

Complexity Analysis:

Time Complexity:

O(n) for computing leftProfit.

O(n) for computing rightProfit.

O(n) for combining the results.
Total: O(n).


Space Complexity:

O(n) for the leftProfit and rightProfit arrays.
Total: O(n).




---

Example Walkthrough:

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]

1. Compute leftProfit:

[0, 0, 2, 2, 2, 3, 3, 4]



2. Compute rightProfit:

[4, 4, 4, 4, 4, 3, 3, 0]



3. Combine results:

leftProfit + rightProfit = [4, 4, 6, 6, 6, 6, 6, 4]



4. Maximum profit: 6



Output: 6


---

Example 2:

Input: prices = [1,2,3,4,5]

1. Compute leftProfit:

[0, 1, 2, 3, 4]



2. Compute rightProfit:

[4, 3, 2, 1, 0]



3. Combine results:

leftProfit + rightProfit = [4, 4, 4, 4, 4]



4. Maximum profit: 4



Output: 4


---

Example 3:

Input: prices = [7,6,4,3,1]

1. Compute leftProfit:

[0, 0, 0, 0, 0]



2. Compute rightProfit:

[0, 0, 0, 0, 0]



3. Combine results:

leftProfit + rightProfit = [0, 0, 0, 0, 0]



4. Maximum profit: 0



Output: 0


---

This solution is efficient and works well within the constraints.

