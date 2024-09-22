class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary to hold lists of anagrams
        anagram_map = defaultdict(list)

        # Iterate over each string in the input list
        for s in strs:
            # Initialize a frequency list of size 26 for 'a' to 'z'
            count = [0] * 26

            # Count the frequency of each character in the string
            for char in s:
                count[ord(char) - ord('a')] += 1

            # Convert the list to a tuple to use as a key
            key = tuple(count)

            # Append the original string to the list corresponding to the frequency key
            anagram_map[key].append(s)

        # Return the list of anagram groups
        return list(anagram_map.values())
