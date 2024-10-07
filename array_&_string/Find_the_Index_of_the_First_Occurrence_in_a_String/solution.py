class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0

        # Get the lengths of both strings
        haystack_len = len(haystack)
        needle_len = len(needle)

        # Loop through the haystack and check for needle's first occurrence
        for i in range(haystack_len - needle_len + 1):
            # If the substring of haystack from i to i + needle_len matches the needle, return i
            if haystack[i:i + needle_len] == needle:
                return i

        # If no match is found, return -1
        return -1
