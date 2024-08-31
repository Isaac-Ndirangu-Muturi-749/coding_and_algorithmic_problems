class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Initialize frequency arrays for ransomNote and magazine
        ransom_count = [0] * 26
        magazine_count = [0] * 26

        # Fill the frequency array for ransomNote
        for char in ransomNote:
            ransom_count[ord(char) - ord('a')] += 1

        # Fill the frequency array for magazine
        for char in magazine:
            magazine_count[ord(char) - ord('a')] += 1

        # Compare the frequency arrays
        for i in range(26):
            if ransom_count[i] > magazine_count[i]:
                return False

        return True
