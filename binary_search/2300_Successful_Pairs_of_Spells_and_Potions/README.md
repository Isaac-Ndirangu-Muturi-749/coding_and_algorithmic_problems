To solve this problem efficiently, we can leverage sorting and binary search to count successful pairs for each spell. Calculating the product of all spells with all potions directly would result in an  solution, which is inefficient for large inputs. Instead, we can use the following approach:


---

Algorithm:

1. Sort the Potions Array:

Sorting allows us to use binary search to efficiently find the number of potions that satisfy the condition for each spell.



2. Iterate Through Each Spell:

For each spell, calculate the minimum potion strength needed for a successful pair:




\text{threshold} = \lceil \frac{\text{success}}{\text{spell}} \rceil

The number of successful potions is the length of the potions array minus the index of this potion.


3. Return the Result:

Store the count for each spell and return the result.





---

Python Implementation:

from bisect import bisect_left

def successfulPairs(spells, potions, success):
    # Step 1: Sort the potions array
    potions.sort()
    m = len(potions)
    
    # Step 2: Calculate the number of successful pairs for each spell
    result = []
    for spell in spells:
        # Find the threshold potion strength
        threshold = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
        # Use binary search to find the first potion >= threshold
        index = bisect_left(potions, threshold)
        # Number of successful potions
        result.append(m - index)
    
    return result


---

Example Walkthrough:

Example 1:

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))  # Output: [4, 0, 3]

1. Sort potions: [1, 2, 3, 4, 5]


2. Iterate through spells:

Spell 5:

Threshold = 

Binary search index = 1

Successful potions = 


Spell 1:

Threshold = 

Binary search index = 5 (out of bounds)

Successful potions = 


Spell 3:

Threshold = 

Binary search index = 2

Successful potions = 




3. Result: [4, 0, 3]




---

Complexity Analysis:

1. Sorting:

Sorting the potions array takes , where  is the length of the potions array.



2. Binary Search:

For each spell, binary search takes . Since there are  spells, this step takes .



3. Overall Complexity:

.





---

Constraints:

Efficiently handles up to  spells and potions due to the logarithmic search step.

Handles large values of success without overflow by using integer division.


This implementation is efficient and meets the problem's constraints.


If you want to solve the problem without using the bisect library for binary search, we can implement the binary search manually. Here's the updated solution:


---

Algorithm:

The core idea remains the same:

1. Sort the potions array.


2. For each spell, compute the threshold (ceil(success / spell)).


3. Use a manual binary search function to find the first index in the sorted potions array where the value is greater than or equal to the threshold.




---

Python Implementation:

def successfulPairs(spells, potions, success):
    # Step 1: Sort the potions array
    potions.sort()
    m = len(potions)

    # Manual binary search function
    def binary_search(target):
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # Step 2: Calculate successful pairs for each spell
    result = []
    for spell in spells:
        threshold = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
        index = binary_search(threshold)
        result.append(m - index)  # Number of successful potions is the remaining ones

    return result


---

Example Walkthrough:

Example 1:

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
print(successfulPairs(spells, potions, success))  # Output: [4, 0, 3]

1. Sort potions: [1, 2, 3, 4, 5]


2. Iterate through spells:

Spell 5:

Threshold = 

Binary search for : Index = 1

Successful potions = 


Spell 1:

Threshold = 

Binary search for : Index = 5 (out of bounds)

Successful potions = 


Spell 3:

Threshold = 

Binary search for : Index = 2

Successful potions = 




3. Result: [4, 0, 3]




---

Complexity Analysis:

1. Sorting:

Sorting the potions array takes , where  is the length of the potions array.



2. Manual Binary Search:

Each binary search takes . For  spells, this step takes .



3. Overall Complexity:

.





---

Key Difference:

Instead of using bisect_left from the bisect library, we implemented a manual binary search, which achieves the same functionality.

