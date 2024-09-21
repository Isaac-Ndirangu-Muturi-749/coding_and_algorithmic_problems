class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        # Traverse the digits starting from the least significant one (rightmost)
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, increment it and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue the loop
            digits[i] = 0

        # If all digits were 9, we need to add 1 at the start
        return [1] + digits
