The problem can be solved efficiently using a binary search algorithm. Binary search reduces the search space by half on each iteration, making it ideal for scenarios like this where we need to identify a specific value within a known range.

Here's the implementation:

### **Python Code**

```python
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n  # Initialize the search range
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle point
            result = guess(mid)  # Call the guess API with the mid value
            if result == 0:
                return mid  # Correct guess
            elif result == -1:
                high = mid - 1  # The picked number is lower
            else:  # result == 1
                low = mid + 1  # The picked number is higher
```

---

### **Explanation of the Code**

1. **Initialize Search Range**:
   - Start with `low = 1` and `high = n` since the number is between 1 and \( n \).

2. **Binary Search**:
   - Compute the midpoint `mid = (low + high) // 2`.
   - Use the `guess` API to check if `mid` is:
     - Equal to the picked number (`guess(mid) == 0`).
     - Higher than the picked number (`guess(mid) == -1`).
     - Lower than the picked number (`guess(mid) == 1`).

3. **Adjust Search Range**:
   - If `guess(mid) == -1`, reduce the upper limit: `high = mid - 1`.
   - If `guess(mid) == 1`, increase the lower limit: `low = mid + 1`.

4. **Return the Result**:
   - When `guess(mid) == 0`, return `mid` as the correct number.

---

### **Time Complexity**
- The binary search algorithm has a time complexity of \( O(\log n) \), as the range is halved on each iteration.

### **Space Complexity**
- The space complexity is \( O(1) \), as no additional space is used beyond the variables.

---

### **Examples**

#### Example 1:
```python
# Input
n = 10
pick = 6
# guess API would behave as:
# guess(5) -> 1 (pick is higher)
# guess(7) -> -1 (pick is lower)
# guess(6) -> 0 (correct)
# Output
print(Solution().guessNumber(10))  # Output: 6
```

#### Example 2:
```python
# Input
n = 1
pick = 1
# guess API would behave as:
# guess(1) -> 0 (correct)
# Output
print(Solution().guessNumber(1))  # Output: 1
```

#### Example 3:
```python
# Input
n = 2
pick = 1
# guess API would behave as:
# guess(1) -> 0 (correct)
# Output
print(Solution().guessNumber(2))  # Output: 1
```
