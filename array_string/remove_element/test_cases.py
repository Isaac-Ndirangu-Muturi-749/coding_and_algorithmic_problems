from solution import Solution

solution = Solution()

# Test case 1
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
assert k == 2
assert sorted(nums[:k]) == [2, 2]

# Test case 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
assert k == 5
assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

print("All test cases passed!")
