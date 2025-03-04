class Solution:
    def minPartitions(self, s: str) -> int:
        unique_chars = set()
        partitions = 1  # At least one substring is needed

        for char in s:
            if char in unique_chars:  # Start a new substring if char repeats
                partitions += 1
                unique_chars.clear()
            unique_chars.add(char)

        return partitions
