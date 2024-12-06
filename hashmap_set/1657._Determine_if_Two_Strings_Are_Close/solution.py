class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: If lengths are different, return False
        if len(word1) != len(word2):
            return False

        # Step 2: Count character frequencies manually
        freq1 = [0] * 26  # Frequency for word1
        freq2 = [0] * 26  # Frequency for word2
        for char in word1:
            freq1[ord(char) - ord('a')] += 1
        for char in word2:
            freq2[ord(char) - ord('a')] += 1

        # Step 3: Check if both words have the same character set
        for i in range(26):
            if (freq1[i] > 0 and freq2[i] == 0) or (freq2[i] > 0 and freq1[i] == 0):
                return False

        # Step 4: Compare the sorted frequencies
        return sorted(freq1) == sorted(freq2)
