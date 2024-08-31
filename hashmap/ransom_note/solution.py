from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count the frequency of each character in ransomNote and magazine
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        # Compare the frequencies
        for char, count in ransom_counter.items():
            if magazine_counter[char] < count:
                return False

        return True
