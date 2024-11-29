class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set of vowels (both lowercase and uppercase)
        s = list(s)  # Convert the string to a list to allow modification
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert the list back to a string and return
