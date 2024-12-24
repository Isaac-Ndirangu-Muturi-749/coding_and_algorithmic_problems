class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        # Check "Bulky"
        bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or (length * width * height) >= 10**9

        # Check "Heavy"
        heavy = mass >= 100

        # Determine the category
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"
