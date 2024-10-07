class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples with Roman numeral symbols and their corresponding values
        value_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        roman = []  # List to accumulate the Roman numeral result

        # Iterate over the value-symbol pairs
        for value, symbol in value_to_roman:
            # While num is greater than or equal to the value, subtract the value and append the symbol
            while num >= value:
                num -= value
                roman.append(symbol)

        # Join all Roman numeral parts into a single string and return
        return "".join(roman)
