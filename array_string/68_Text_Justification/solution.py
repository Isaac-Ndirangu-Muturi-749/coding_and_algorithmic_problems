class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []  # Stores the result lines
        line, length = [], 0  # Current line words and total length of words
        i = 0  # Pointer to traverse the words list

        while i < len(words):
            # Check if adding the next word exceeds the maxWidth
            if length + len(line) + len(words[i]) > maxWidth:
                # Line complete, calculate extra spaces to distribute
                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1)  # Evenly distributed spaces
                remainder = extra_space % max(1, len(line) - 1)  # Extra spaces to distribute from left to right

                for j in range(max(1, len(line) - 1)):  # Iterate over words in line (except last word)
                    line[j] += " " * spaces
                    if remainder > 0:  # Distribute remaining spaces
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))  # Add the justified line to result
                line, length = [], 0  # Reset for the next line

            # Add the current word to the line
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handling the last line (left-justified)
        last_line = " ".join(line)  # Words separated by a single space
        trail_space = maxWidth - len(last_line)  # Remaining spaces to the right
        res.append(last_line + " " * trail_space)

        return res
