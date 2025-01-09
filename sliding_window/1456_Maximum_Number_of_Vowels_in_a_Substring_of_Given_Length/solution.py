class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        max_vowels = 0

        # Count vowels in the first window of length k
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_vowels = vowel_count

        # Slide the window
        for i in range(k, len(s)):
            # Add the new character to the window
            if s[i] in vowels:
                vowel_count += 1
            # Remove the leftmost character from the window
            if s[i - k] in vowels:
                vowel_count -= 1
            # Update max_vowels
            max_vowels = max(max_vowels, vowel_count)

        return max_vowels
