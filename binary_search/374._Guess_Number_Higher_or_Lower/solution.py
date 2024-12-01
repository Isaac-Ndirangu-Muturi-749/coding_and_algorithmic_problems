# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

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
