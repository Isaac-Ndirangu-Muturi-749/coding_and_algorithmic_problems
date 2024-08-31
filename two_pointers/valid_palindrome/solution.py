class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: convert to lowercase and filter alphanumeric characters
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())

        # Check if the normalized string is the same forward and backward
        return normalized_str == normalized_str[::-1]
