To solve this problem efficiently with **linear runtime complexity (O(n))** and **constant space (O(1))**, we can use a **bit manipulation approach**. The key insight is that we need to count the bits in each position for all numbers in the array. If a number appears three times, the count of bits at every position must be a multiple of 3. The number that appears only once will leave some bits whose count is not divisible by 3, and those bits represent the single number.

### Approach:

1. **Bit Representation**:
   - Every integer is represented by 32 bits (for a 32-bit signed integer).
   - We can count the number of `1` bits at each bit position for all the numbers in the array.

2. **Bit Manipulation**:
   - For each bit position (from 0 to 31), count how many numbers have a `1` in that position.
   - If the count of `1` bits at a specific position is not divisible by 3, it means that this bit contributes to the unique number.

3. **Rebuild the Single Number**:
   - Using the bits that have counts not divisible by 3, we can reconstruct the number that appears exactly once.

### Solution Code:

```python
def singleNumber(nums):
    # Initialize two variables to keep track of bits.
    ones, twos = 0, 0

    for num in nums:
        # 'ones' will hold the bits which have appeared exactly 1 time (mod 3)
        ones = (ones ^ num) & ~twos

        # 'twos' will hold the bits which have appeared exactly 2 times (mod 3)
        twos = (twos ^ num) & ~ones

    # After processing all numbers, 'ones' will have the unique number
    return ones

# Example Usage:
nums1 = [2, 2, 3, 2]
print(singleNumber(nums1))  # Output: 3

nums2 = [0, 1, 0, 1, 0, 1, 99]
print(singleNumber(nums2))  # Output: 99
```

### Explanation:

1. **Tracking Bits**:
   - We use two variables `ones` and `twos` to keep track of bits.
     - `ones`: Tracks the bits that have appeared once so far.
     - `twos`: Tracks the bits that have appeared twice so far.

2. **Bitwise Operations**:
   - We use the XOR (`^`) operation to flip bits, and the AND (`&`) operation with negations to reset bits when needed.
   - After processing each number, the bits in `ones` and `twos` will be adjusted accordingly. If a bit appears three times, it will be removed from both `ones` and `twos`.

3. **Final Result**:
   - At the end of the iteration, the variable `ones` will hold the bits of the number that appears exactly once, while `twos` will be zeroed out for all other numbers that appeared three times.

### Time Complexity:

- The time complexity is **O(n)** because we iterate through the array once.

### Space Complexity:

- The space complexity is **O(1)** because we only use a constant amount of extra space (two variables `ones` and `twos`).

This solution meets the requirements of **linear runtime** and **constant space**.


Let's walk through the code and understand how it works using an example.

### Purpose of the Code:
The goal of this function is to find the unique number that appears exactly once in a list where every other number appears exactly three times. The challenge here is to keep track of the bits that appear 1, 2, or 3 times for each number in the array.

### Approach:
This code uses **bit manipulation** to track how many times a bit has appeared (modulo 3 times).

- **`ones`** keeps track of the bits that have appeared exactly **once**.
- **`twos`** keeps track of the bits that have appeared exactly **twice**.

Once the loop is done, **`ones`** will hold the unique number because the bits in the unique number will only have appeared once.

### Bitwise Operations:

1. **XOR (`^`)**: Toggles bits. For example, `a ^ b` flips bits that are different in `a` and `b`.
2. **AND with NOT (`& ~`)**: Resets certain bits (based on a mask). For example, `a & ~b` keeps only the bits in `a` where `b` is 0.

---

### Example Walkthrough:

Consider the list `nums = [2, 2, 3, 2]`, where `3` is the unique number that appears once, and `2` appears three times. Here's how the algorithm processes the list:

### Step-by-Step Execution:

#### 1. Initial State:
- `ones = 0`
- `twos = 0`

#### 2. First Number: `2`
- Binary representation of `2` is `10`.

- Update `ones`:
  - `ones = (ones ^ 2) & ~twos`
  - `ones = (0 ^ 2) & ~0 = 2` (since `0 ^ 2 = 2` and `~0 = all 1s`, `2 & 1s = 2`)

- Update `twos`:
  - `twos = (twos ^ 2) & ~ones`
  - `twos = (0 ^ 2) & ~2 = 0` (since `~2 = all 1s except the second bit`, `2 & ~2 = 0`)

After processing the first `2`, we have:
- `ones = 2`
- `twos = 0`

#### 3. Second Number: `2`
- Binary representation of `2` is `10`.

- Update `ones`:
  - `ones = (ones ^ 2) & ~twos`
  - `ones = (2 ^ 2) & ~0 = 0` (since `2 ^ 2 = 0`)

- Update `twos`:
  - `twos = (twos ^ 2) & ~ones`
  - `twos = (0 ^ 2) & ~0 = 2`

After processing the second `2`, we have:
- `ones = 0`
- `twos = 2`

#### 4. Third Number: `3`
- Binary representation of `3` is `11`.

- Update `ones`:
  - `ones = (ones ^ 3) & ~twos`
  - `ones = (0 ^ 3) & ~2 = 1` (since `~2` has all 1s except the second bit, `3 & ~2 = 1`)

- Update `twos`:
  - `twos = (twos ^ 3) & ~ones`
  - `twos = (2 ^ 3) & ~1 = 0` (since `2 ^ 3 = 1` and `1 & ~1 = 0`)

After processing `3`, we have:
- `ones = 1`
- `twos = 0`

#### 5. Fourth Number: `2`
- Binary representation of `2` is `10`.

- Update `ones`:
  - `ones = (ones ^ 2) & ~twos`
  - `ones = (1 ^ 2) & ~0 = 3` (since `1 ^ 2 = 3`)

- Update `twos`:
  - `twos = (twos ^ 2) & ~ones`
  - `twos = (0 ^ 2) & ~3 = 0` (since `~3 = all 0s, 2 & 0 = 0`)

After processing the last `2`, we have:
- `ones = 3`
- `twos = 0`

### Final Result:
At the end of the loop, `ones = 3`, which is the unique number that appeared only once in the array.

### Summary:
- **`ones`** tracks bits that have appeared exactly once (mod 3).
- **`twos`** tracks bits that have appeared exactly twice (mod 3).
- After processing all numbers, `ones` will hold the unique number that appeared once. In this example, it correctly identifies `3` as the number that appeared only once.
