class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # def gcd(a: int, b: int) -> int:
        #     while b:
        #         a, b = b, a % b
        #     return a

        def gcd(a: int, b: int) -> int:
            while a != b:
                if a > b:
                    a -= b
                else:
                    b -= a
            return a

        # Check if str1 + str2 is equal to str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        # Calculate the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        # Return the substring of length gcd_length from str1
        return str1[:gcd_length]

