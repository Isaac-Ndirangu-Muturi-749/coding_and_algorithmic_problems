To solve this problem, we can follow these steps:

1. **Find the maximum number of candies** currently held by any kid.
2. For each kid, calculate the number of candies they would have if they were given all the `extraCandies`.
3. Compare this new number with the maximum candies from Step 1. If the new number is greater than or equal to the maximum, set the result for that kid to `True`. Otherwise, set it to `False`.
4. Return the resulting boolean array.

Here is the Python solution:

```python
def kidsWithCandies(candies, extraCandies):
    # Step 1: Find the maximum number of candies
    max_candies = max(candies)

    # Step 2: Calculate the result for each kid
    result = []
    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    # Step 3: Return the result array
    return result
```

---

### Example Runs

#### Example 1:
```python
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]
```

#### Example 2:
```python
candies = [4, 2, 1, 1, 2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, False, False, False]
```

#### Example 3:
```python
candies = [12, 1, 12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, True]
```

---

### Explanation
1. **Example 1**:
   - Max candies = 5
   - Results: `[5 >= 5, 6 >= 5, 8 >= 5, 4 < 5, 6 >= 5]`
2. **Example 2**:
   - Max candies = 4
   - Results: `[5 >= 4, 3 < 4, 2 < 4, 2 < 4, 3 < 4]`
3. **Example 3**:
   - Max candies = 12
   - Results: `[22 >= 12, 11 < 12, 22 >= 12]`

This solution is efficient with \(O(n)\) time complexity due to a single traversal of the `candies` array.
