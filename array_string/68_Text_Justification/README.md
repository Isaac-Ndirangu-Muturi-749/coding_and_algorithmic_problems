Here’s a corrected and clean version of the provided Python code, along with explanations for better readability and understanding:

Corrected Code

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


---

Explanation

Variables:

1. res: A list to store fully justified lines of text.


2. line: A list to temporarily store words for the current line.


3. length: The cumulative length of the words in line (excluding spaces).


4. i: Pointer to traverse the words list.




---

Key Steps:

1. Line Construction:

Check if adding a word exceeds maxWidth.

If so, distribute spaces evenly across words in the current line:

Compute extra_space (remaining spaces to be distributed).

Compute spaces (evenly distributed spaces per slot) and remainder (leftover spaces).

Distribute the extra spaces to the words from left to right.




2. Final Line Handling:

For the last line, words are left-justified (separated by a single space).

Remaining spaces are added to the right to meet maxWidth.





---

Example Walkthrough

Input:

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

Process:

1. First Line:

Words: ["This", "is", "an"]

Length: 10 (4 + 2 + 2)

Extra Spaces: 16 - 10 = 6

Spaces: 6 // 2 = 3, Remainder: 6 % 2 = 0


Line: "This    is    an"



2. Second Line:

Words: ["example", "of", "text"]

Length: 13 (7 + 2 + 4)

Extra Spaces: 16 - 13 = 3

Spaces: 3 // 2 = 1, Remainder: 3 % 2 = 1


Line: "example  of text"



3. Last Line:

Words: ["justification."]

Line: "justification.  " (left-justified with trailing spaces).




Output:

[
    "This    is    an",
    "example  of text",
    "justification.  "
]


---

Complexity Analysis:

1. Time Complexity: , where  is the total number of words in words. Each word is processed once, and space distribution is linear for each line.


2. Space Complexity: , for storing the result in the res list.



This solution efficiently handles text justification while adhering to all the given rules.

The problem is about formatting a list of words to fit into lines of a given width (maxWidth), adhering to specific justification rules.

Key Requirements:

1. Full Justification:

Distribute extra spaces as evenly as possible.

If the number of spaces does not divide evenly, extra spaces go to the leftmost slots.



2. Left Justification (for the last line):

Words are left-justified, and the remaining spaces are added at the end.



3. Constraints:

Words are packed greedily, fitting as many words as possible in each line without exceeding maxWidth.





---

Algorithm

1. Group Words into Lines:

Use a greedy approach to determine how many words fit into a single line.

Keep track of the current line's length (including spaces between words).



2. Format Each Line:

For non-final lines:

Calculate the total spaces required to fill the line to maxWidth.

Distribute spaces evenly between words.


For the final line:

Left-justify: Add a single space between words, and pad the remaining space at the end.




3. Edge Cases:

Lines with a single word: Left-justify the word and pad the rest with spaces.





---

Code Implementation

def fullJustify(words, maxWidth):
    result = []  # Stores the justified lines
    line = []  # Current line of words
    line_length = 0  # Current line length without spaces

    for word in words:
        # Check if adding the next word exceeds the maxWidth
        if line_length + len(line) + len(word) > maxWidth:
            # Justify the current line
            for i in range(maxWidth - line_length):
                # Distribute extra spaces evenly
                line[i % (len(line) - 1 or 1)] += " "
            result.append("".join(line))
            # Reset for the next line
            line, line_length = [], 0
        # Add the word to the current line
        line.append(word)
        line_length += len(word)

    # Handle the last line (left-justified)
    result.append(" ".join(line).ljust(maxWidth))
    return result


---

Example Walkthrough

Example 1:

Input:

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

Process:

1. Group Words:

Line 1: "This is an" → Fits within 16.

Line 2: "example of text" → Fits within 16.

Line 3: "justification." → Left-justify.



2. Justify:

Line 1: Add spaces evenly → "This    is    an".

Line 2: Add spaces evenly → "example  of text".

Line 3: Left-justify → "justification.  ".




Output:

[
    "This    is    an",
    "example  of text",
    "justification.  "
]


---

Example 2:

Input:

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16

Process:

1. Group Words:

Line 1: "What must be" → Fits within 16.

Line 2: "acknowledgment" → Fits within 16.

Line 3: "shall be" → Left-justify.



2. Justify:

Line 1: Add spaces evenly → "What   must   be".

Line 2: Left-justify → "acknowledgment  ".

Line 3: Left-justify → "shall be        ".




Output:

[
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
]


---

Complexity Analysis

1. Time Complexity: 

Each word is processed once while forming lines.

Space distribution for each line is linear in length.



2. Space Complexity: 

Storing the result requires space proportional to the input size.




This approach is efficient and handles edge cases such as a single word or a very large number of words gracefully.

This part of the code is part of a text justification algorithm. Let's break it down step by step:


---

Context

The goal is to justify a line of text so that it fits exactly within the given maxWidth. This involves distributing extra spaces evenly between words.

Key Variables

line_length: The total length of all words currently in the line (excluding spaces).

line: A list of words currently in the line.

word: The next word being considered for the line.

maxWidth: The total width the line must fit into.

result: A list to store fully justified lines.



---

Code Breakdown

Condition

if line_length + len(line) + len(word) > maxWidth:

This checks if adding the next word (word) and the required spaces between words (len(line)) would exceed the maxWidth. If true, the current line is full and needs to be justified.


---

Justify the Line

for i in range(maxWidth - line_length):
    # Distribute extra spaces evenly
    line[i % (len(line) - 1 or 1)] += " "

maxWidth - line_length:
This calculates how many extra spaces are needed to make the line's total length equal to maxWidth.

line[i % (len(line) - 1 or 1)]:
This distributes the extra spaces evenly between words:

len(line) - 1: The number of spaces between words (since spaces exist between words, not after the last word).

or 1: Handles the special case where there is only one word in the line (so there are no spaces between words). In this case, the extra spaces are added to the end of the single word.

i % (len(line) - 1 or 1): Cycles through the spaces between words repeatedly, adding one space at a time to each space slot.




---

Append to Result

result.append("".join(line))

After all spaces are distributed, the words and spaces in line are concatenated into a single string using "".join(line).

The fully justified line is added to the result list.



---

Example Walkthrough

Input:

Words: ["This", "is", "an", "example"]

maxWidth = 16


1. Current Line: ["This", "is", "an"]

line_length = len("This") + len("is") + len("an") = 10

Adding "example" (len("example") = 7) would exceed maxWidth (10 + 2 (spaces) + 7 = 19 > 16).



2. Justify the Line:

Extra spaces needed: maxWidth - line_length = 16 - 10 = 6.

Distribute spaces:

len(line) - 1 = 2 (2 spaces between words).

Add spaces cyclically:

1st space slot: "This "

2nd space slot: "is  "

Repeat: "This  ", "is   ", etc.



Final justified line: "This  is   an"



3. Add the line to result and start the next line with "example".




---

Special Case: Single Word

For a line with one word:

len(line) - 1 = 0

or 1 ensures the loop still runs, and spaces are added to the end of the single word.


Example:

line = ["example"], maxWidth = 16

Justified line: "example       " (6 extra spaces at the end).



---

Why This Works

The logic ensures:

1. Spaces are distributed as evenly as possible.


2. Any leftover spaces are added from left to right, as required by justification rules.



Let's focus on how the modulus operator (%) works in this case and why it's used to distribute spaces evenly.


---

The Code

for i in range(maxWidth - line_length):
    line[i % (len(line) - 1 or 1)] += " "


---

Key Points to Understand

1. maxWidth - line_length:

This gives the number of extra spaces that need to be distributed across the words in the line.



2. len(line) - 1:

This represents the number of gaps between words in the line.

Example: In the line ["This", "is", "an"], there are 2 gaps:

This | is | an



3. i % (len(line) - 1):

The modulus operator is used to cycle through the gaps repeatedly.

If there are 2 gaps (i.e., len(line) - 1 = 2), the indices of the gaps are:

0 (gap between "This" and "is")
1 (gap between "is" and "an")


When distributing spaces:

For i = 0, space is added to the 0th gap.

For i = 1, space is added to the 1st gap.

For i = 2, it cycles back to the 0th gap (since 2 % 2 = 0).

For i = 3, it cycles back to the 1st gap (since 3 % 2 = 1).



4. or 1:

Handles the special case when there is only 1 word in the line (and thus len(line) - 1 = 0).

To avoid division by zero, or 1 makes sure the modulus operator cycles over 1.





---

Example Walkthrough

Example Input

Words: ["This", "is", "an"]

maxWidth = 16


Step 1: Calculate Extra Spaces

line_length = 10 (length of "This is an" without spaces).

maxWidth - line_length = 16 - 10 = 6 (6 spaces need to be added).


Step 2: Number of Gaps

len(line) - 1 = 3 - 1 = 2 (2 gaps between the words).


Step 3: Distribute Spaces

Loop runs 6 times (maxWidth - line_length = 6).

Cycle through gaps using %:

i = 0: Add space to 0th gap: "This " is an

i = 1: Add space to 1st gap: "This " "is " an

i = 2: Add space to 0th gap: "This  " "is " an

i = 3: Add space to 1st gap: "This  " "is  " an

i = 4: Add space to 0th gap: "This   " "is  " an

i = 5: Add space to 1st gap: "This   " "is   " an



Final Line:

"This   is   an"


---

Why % Is Needed

Without %, the loop would not "cycle" through the gaps—it would just run out of bounds or break after filling only the first few gaps. % ensures that:

1. Spaces are distributed evenly across all gaps.


2. When the loop runs out of gaps, it starts again from the beginning, ensuring all extra spaces are allocated.




---

Special Case: Single Word

If line = ["Hello"] and maxWidth = 10:

len(line) - 1 = 0, so or 1 makes it 1.

All extra spaces (maxWidth - line_length = 5) are added after the word:

"Hello     "


This ensures the algorithm handles all scenarios properly.

The calculation to determine gaps between words is based on the number of words in the current line. Here's how it works:


---

Key Idea

If you have n words in a line, the number of gaps between the words is n - 1.


Example:

For the line ["This", "is", "an"]:

There are 3 words (n = 3).

The number of gaps between the words is:

n - 1 = 3 - 1 = 2


So, the gaps are:

1. 0th gap: Between "This" and "is".


2. 1st gap: Between "is" and "an".




---

Visual Representation

Let's visualize how the gaps are numbered:

"This" | "is" | "an"
   0       1

Gap 0: Space between "This" and "is".

Gap 1: Space between "is" and "an".



---

General Rule for Gaps

If there is 1 word, there are 0 gaps (no space needed between words).

If there are 2 words, there is 1 gap.

If there are 3 words, there are 2 gaps, and so on.


The gaps are always numbered from 0 to (n - 2).


---

Why This Matters for the Code

In the code:

line[i % (len(line) - 1 or 1)] += " "

len(line) - 1 determines the number of gaps.

i % (len(line) - 1) ensures that spaces are added to the gaps repeatedly in order, starting from gap 0 and cycling back.


This logic allows the algorithm to distribute extra spaces evenly across all gaps.

