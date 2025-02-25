from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # Count frequency of each letter
        char_freq = Counter(s)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(char_freq.items(), key=lambda x: -x[1])

        total_presses = 0
        for index, (char, freq) in enumerate(sorted_chars):
            # Determine press cost based on position (0-8: 1 press, 9-17: 2 presses, 18-25: 3 presses)
            press_cost = (index // 9) + 1
            total_presses += press_cost * freq

        return total_presses
