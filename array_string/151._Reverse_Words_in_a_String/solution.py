class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by spaces to extract words
        words = s.split()

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join the reversed list with a single space
        return " ".join(reversed_words)
