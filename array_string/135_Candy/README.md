This problem can be solved efficiently using a two-pass greedy algorithm. The idea is to allocate candies while ensuring both requirements are met:

1. Each child gets at least one candy.


2. Children with higher ratings than their neighbors get more candies than their neighbors.



Approach:

Two-Pass Greedy Algorithm:

1. Left-to-right pass:

Traverse the array from left to right.

If a child's rating is higher than their left neighbor, give the child more candies than the neighbor.



2. Right-to-left pass:

Traverse the array from right to left.

If a child's rating is higher than their right neighbor, ensure they have more candies than their neighbor. This might require updating their candy count to the maximum of the current value and the value needed to satisfy this condition.



3. Sum up the candies after the two passes to get the minimum candies needed.



Algorithm:

1. Initialize an array candies with the size of ratings, filled with 1 (since each child must get at least one candy).


2. Perform the left-to-right pass to adjust candies based on ratings.


3. Perform the right-to-left pass to further adjust candies based on ratings.


4. Return the sum of all values in candies.




---

Code Implementation:

def candy(ratings):
    n = len(ratings)
    # Initialize candies array with 1 for each child
    candies = [1] * n

    # Left-to-right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right-to-left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Sum up the candies
    return sum(candies)


---

Complexity Analysis:

Time Complexity:

The algorithm traverses the array twice (left-to-right and right-to-left), so the time complexity is O(n).


Space Complexity:

The candies array uses O(n) additional space.




---

Example Walkthrough:

Example 1:

Input: ratings = [1, 0, 2]

1. Initial candies array: [1, 1, 1]


2. Left-to-right pass:

At i = 1: ratings[1] < ratings[0] → No change.

At i = 2: ratings[2] > ratings[1] → candies[2] = candies[1] + 1 = 2.

Result after pass: [1, 1, 2].



3. Right-to-left pass:

At i = 1: ratings[1] < ratings[2] → No change.

At i = 0: ratings[0] > ratings[1] → candies[0] = max(candies[0], candies[1] + 1) = 2.

Result after pass: [2, 1, 2].



4. Total candies: 2 + 1 + 2 = 5.



Output: 5.


---

Example 2:

Input: ratings = [1, 2, 2]

1. Initial candies array: [1, 1, 1].


2. Left-to-right pass:

At i = 1: ratings[1] > ratings[0] → candies[1] = candies[0] + 1 = 2.

At i = 2: ratings[2] == ratings[1] → No change.

Result after pass: [1, 2, 1].



3. Right-to-left pass:

At i = 1: ratings[1] > ratings[2] → No change.

At i = 0: ratings[0] < ratings[1] → No change.

Result after pass: [1, 2, 1].



4. Total candies: 1 + 2 + 1 = 4.



Output: 4.


---

Edge Cases:

1. Single child:
Input: [10]
Output: 1 (only one candy needed).


2. All ratings are the same:
Input: [1, 1, 1]
Output: 3 (each child gets one candy).


3. Strictly increasing ratings:
Input: [1, 2, 3, 4]
Output: 10 (candies = [1, 2, 3, 4]).


4. Strictly decreasing ratings:
Input: [4, 3, 2, 1]
Output: 10 (candies = [4, 3, 2, 1]).




---

This algorithm efficiently handles all cases while adhering to the problem's constraints.

