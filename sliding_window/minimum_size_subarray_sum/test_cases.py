from solution import Solution

solution = Solution()

# Test case 1
assert solution.minSubArrayLen(7, [2,3,1,2,4,3]) == 2

# Test case 2
assert solution.minSubArrayLen(4, [1,4,4]) == 1

# Test case 3
assert solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0

print("All test cases passed!")
