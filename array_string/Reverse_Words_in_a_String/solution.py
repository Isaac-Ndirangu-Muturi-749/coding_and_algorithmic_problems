class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Strip leading and trailing spaces, split by spaces
        words = s.split()  # This also takes care of multiple spaces between words

        # Step 2: Reverse the list of words
        reversed_words = words[::-1]

        # Step 3: Join the reversed words with a single space
        return ' '.join(reversed_words)
