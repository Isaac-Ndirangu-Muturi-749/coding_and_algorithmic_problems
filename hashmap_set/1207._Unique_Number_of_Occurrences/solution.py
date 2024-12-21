class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

            # Count the frequency of each value in the array
            freq = {}
            for num in arr:
                freq[num] = freq.get(num, 0) + 1

            # Check if frequencies are unique
            occurrences = set(freq.values())
            return len(occurrences) == len(freq)
