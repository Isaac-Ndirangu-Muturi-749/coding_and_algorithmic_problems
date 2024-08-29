solution = Solution()

# Test case 1
assert solution.canConstruct("a", "b") == False

# Test case 2
assert solution.canConstruct("aa", "ab") == False

# Test case 3
assert solution.canConstruct("aa", "aab") == True

print("All test cases passed!")
