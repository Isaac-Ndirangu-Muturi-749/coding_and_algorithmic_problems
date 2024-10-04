class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Handle the case of negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n > 0:
            # If n is odd, multiply the current product to the result
            if n % 2 == 1:
                result *= x

            # Square the current product and halve n
            x *= x
            n //= 2

        return result
