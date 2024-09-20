class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create dictionaries to count frequencies of characters
        count_s = {}
        count_t = {}

        # Count frequencies of characters in s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Count frequencies of characters in t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Compare the frequency dictionaries
        return count_s == count_t
