class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the input list is empty, return an empty string
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Loop through all strings in the array
        for s in strs[1:]:
            # Check if the current string starts with the prefix
            while s[:len(prefix)] != prefix:
                # If not, reduce the prefix length by one
                prefix = prefix[:-1]
                # If prefix becomes empty, return ""
                if not prefix:
                    return ""

        return prefix
