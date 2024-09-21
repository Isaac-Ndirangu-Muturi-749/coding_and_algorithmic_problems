To find the number of set bits (1s) in the binary representation of a positive integer, we can use several approaches. Let's look at an efficient way to implement this, followed by optimization considerations for repeated calls.

### Approach 1: Bit Manipulation

We can count the number of set bits by using the following technique:

1. Initialize a counter to `0`.
2. Use a while loop to repeatedly check if the least significant bit (LSB) is set (i.e., `1`) and shift the bits to the right until all bits have been processed.
3. Each time the LSB is `1`, increment the counter.

Here’s how you can implement it:

### Solution Code:

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Check if the least significant bit is 1
            count += n & 1
            # Right shift by 1 to check the next bit
            n >>= 1
        return count
```

### Explanation:

- **n & 1** checks if the least significant bit of `n` is set (1).
- **n >>= 1** shifts the bits of `n` to the right by one, effectively removing the least significant bit.
- The loop continues until `n` becomes `0`, counting all set bits along the way.

### Example Outputs:

```python
sol = Solution()

# Example 1:
print(sol.hammingWeight(11))  # Output: 3 (binary: 1011)

# Example 2:
print(sol.hammingWeight(128))  # Output: 1 (binary: 10000000)

# Example 3:
print(sol.hammingWeight(2147483645))  # Output: 30 (binary: 1111111111111111111111111111101)
```

### Time Complexity:
- **Time Complexity**: O(k), where k is the number of bits in the integer. Since we are shifting the bits, each iteration reduces the number of bits by 1.
- **Space Complexity**: O(1), since we only use a constant amount of space.

---

### Optimized Approach: Brian Kernighan's Algorithm

A more efficient way to count the number of set bits is by using **Brian Kernighan's Algorithm**. This method works by continuously flipping the least significant set bit (1) to 0. The number of iterations is equal to the number of set bits in the binary representation.

Here's the optimized version:

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Remove the lowest set bit
            n &= (n - 1)
            count += 1
        return count
```

### Explanation:

- **n &= (n - 1)** removes the lowest set bit in `n`. Each time we do this, we eliminate one `1` from the binary representation.
- This process continues until `n` becomes `0`, and the counter keeps track of how many set bits have been removed.

### Why is this faster?

Brian Kernighan's algorithm only loops as many times as there are set bits in `n`. This means that for numbers with fewer set bits, this method will be faster than the basic approach.

### Example Outputs with Optimized Approach:

```python
sol = Solution()

# Example 1:
print(sol.hammingWeight(11))  # Output: 3 (binary: 1011)

# Example 2:
print(sol.hammingWeight(128))  # Output: 1 (binary: 10000000)

# Example 3:
print(sol.hammingWeight(2147483645))  # Output: 30 (binary: 1111111111111111111111111111101)
```

### Follow-Up Optimization:

If the function is called many times, you can store the results for small integers (such as caching results for 8-bit or 16-bit numbers) in a table (lookup table). For larger numbers, the solution can divide the number into smaller parts and sum the set bits using the precomputed results.

This will give **O(1)** time for each lookup at the cost of extra space.

### Summary:
- The basic bit-shifting approach runs in O(k) time where k is the number of bits.
- Brian Kernighan's algorithm is more efficient in practice, running in O(b) time where b is the number of set bits.
- For repeated calls, a lookup table can further optimize the process, giving constant-time complexity for each query.
