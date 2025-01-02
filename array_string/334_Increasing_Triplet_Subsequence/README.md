To solve the problem in  time complexity and  space complexity, we can use a greedy approach with two variables to track the smallest and second smallest numbers in the array.


---

Approach:

1. Two Variables:

Use two variables, first and second, to track the smallest and second smallest numbers encountered so far.

Initially, set both first and second to infinity.



2. Iterate Through the Array:

For each number in nums:

If the number is smaller than first, update first to this number.

Else if the number is smaller than second but larger than first, update second to this number.

Else, if the number is larger than second, return True because we have found a triplet.




3. Return False:

If no such triplet is found after iterating through the array, return False.





---

Implementation:

def increasingTriplet(nums):
    first = float('inf')  # Smallest number
    second = float('inf')  # Second smallest number
    
    for num in nums:
        if num <= first:
            first = num  # Update smallest number
        elif num <= second:
            second = num  # Update second smallest number
        else:
            return True  # Found a number greater than both first and second
    
    return False  # No such triplet exists


---

Explanation of the Code:

1. Tracking the Smallest Numbers:

The variable first keeps track of the smallest number so far.

The variable second keeps track of the second smallest number that is greater than first.



2. Finding the Triplet:

If a number is found that is larger than both first and second, we have identified a triplet, and we return True.



3. Returning False:

If no such triplet is found after scanning the entire array, return False.





---

Complexity Analysis:

1. Time Complexity:

The algorithm traverses the array once, so the time complexity is .



2. Space Complexity:

Only two variables (first and second) are used, so the space complexity is .





---

Example Walkthrough:

Example 1:

nums = [1, 2, 3, 4, 5]

first = inf, second = inf

After iteration:

num = 1: first = 1

num = 2: second = 2

num = 3: True (3 > second)


Output: True


Example 2:

nums = [5, 4, 3, 2, 1]

first = inf, second = inf

After iteration:

num = 5: first = 5

num = 4: first = 4

num = 3: first = 3

num = 2: first = 2

num = 1: first = 1


No triplet found.

Output: False


Example 3:

nums = [2, 1, 5, 0, 4, 6]

first = inf, second = inf

After iteration:

num = 2: first = 2

num = 1: first = 1

num = 5: second = 5

num = 0: first = 0

num = 4: second = 4

num = 6: True (6 > second)


Output: True



---

This approach efficiently finds the triplet using only two variables and ensures  time complexity.

