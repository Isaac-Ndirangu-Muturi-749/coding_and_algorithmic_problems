class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative or ends with 0 (but not 0 itself), it can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original = x

        # Reverse the digits of the number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # Check if the original number is the same as the reversed number
        return original == reversed_num
