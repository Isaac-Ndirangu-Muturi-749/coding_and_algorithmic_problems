def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to the right of the last seen duplicate character
            left = char_index[s[right]] + 1

        # Update the character's last seen index
        char_index[s[right]] = right

        # Calculate the maximum length of the substring
        max_length = max(max_length, right - left + 1)

    return max_length
