class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        flips = 0
        while a > 0 or b > 0 or c > 0:
            # Extract the least significant bits
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 0:
                # If c's bit is 0, both a and b's bits must be 0
                flips += bit_a + bit_b
            else:
                # If c's bit is 1, at least one of a or b's bits must be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1

            # Shift all numbers to the right to check the next bit
            a >>= 1
            b >>= 1
            c >>= 1

        return flips
