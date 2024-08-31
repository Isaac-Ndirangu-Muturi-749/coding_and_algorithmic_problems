from solution import Solution

solution = Solution()

# Test case 1
assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

# Test case 2
assert solution.isPalindrome("race a car") == False

# Test case 3
assert solution.isPalindrome(" ") == True

print("All test cases passed!")
