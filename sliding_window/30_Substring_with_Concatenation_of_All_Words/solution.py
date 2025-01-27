from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not s or not words:
            return []

        # Length of each word and total concatenated substring
        word_length = len(words[0])
        total_length = word_length * len(words)

        # Count of all words
        word_count = Counter(words)

        # Result list
        result = []

        # Iterate with offset
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()

            while right + word_length <= len(s):
                # Extract the current word from the substring
                word = s[right:right + word_length]
                right += word_length

                # If the word is part of `words`
                if word in word_count:
                    current_count[word] += 1

                    # If a word occurs too many times, move `left` to shrink the window
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_length]] -= 1
                        left += word_length

                    # Check if the window size matches `total_length`
                    if right - left == total_length:
                        result.append(left)

                # If the word is not part of `words`, reset the window
                else:
                    current_count.clear()
                    left = right

        return result
