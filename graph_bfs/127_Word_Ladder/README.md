Solution: Word Ladder (Shortest Transformation Sequence)

This problem requires us to find the shortest transformation sequence from beginWord to endWord, where each transformation changes exactly one letter and the new word must exist in wordList.


---

Approach

Since we need to find the shortest transformation sequence, the best approach is Breadth-First Search (BFS) because:

1. BFS finds the shortest path in an unweighted graph.


2. Each word in the dictionary can be treated as a graph node, with an edge existing if a word can be transformed into another by changing one letter.




---

Steps

1. Convert wordList into a set for O(1) lookups.


2. Use BFS starting from beginWord:

Use a queue to store (word, transformation_length).

Try changing each letter of the word ('a' to 'z').

If the new word exists in wordList, add it to the queue and remove it from wordList (to avoid cycles).



3. Return the transformation length when endWord is found.


4. If BFS ends without finding endWord, return 0.




---

Implementation

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)  # Convert to set for O(1) lookups
        if endWord not in wordSet:
            return 0  # If endWord is not in the dictionary, no valid transformation

        queue = deque([(beginWord, 1)])  # BFS queue: (current_word, steps)
        
        while queue:
            word, steps = queue.popleft()
            
            # Try changing each character in the word
            for i in range(len(word)):
                original_char = word[i]
                
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == original_char:
                        continue  # Skip if the character is the same
                    
                    new_word = word[:i] + char + word[i+1:]  # Modify one letter
                    
                    if new_word == endWord:
                        return steps + 1  # Found the shortest path
                    
                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))  # Add to BFS queue
                        wordSet.remove(new_word)  # Remove from set to prevent revisits
        
        return 0  # No transformation sequence found


---

Explanation of Code

1. Preprocess the wordList as a set for fast lookup.


2. Use BFS to explore word transformations:

For each word, try changing each letter and check if it exists in the set.

If endWord is found, return the step count.

Otherwise, add valid words to the queue and remove them from the set (to avoid visiting them again).



3. Return 0 if no valid sequence is found.




---

Complexity Analysis

Time Complexity: O(M × 26 × N) = O(MN)

M: Length of each word (max 10).

N: Number of words in wordList (max 5000).

Each word transformation requires iterating M positions and 26 possible letters.


Space Complexity: O(N)

BFS queue and wordSet both store words, leading to O(N) space usage.




---

Example Walkthrough

Example 1

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

BFS Steps:

hit (1)
↓
hot (2)
↓
dot, lot (3)
↓
dog, log (4)
↓
cog (5)  -> Found the shortest path!

Output: 5


---

Example 2

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

Since cog is missing from wordList, no transformation sequence is possible.

Output: 0


---

Edge Cases

1. No possible transformation (Example 2).


2. All words are one letter apart:

Input: beginWord = "a", endWord = "c", wordList = ["a", "b", "c"]
Output: 2  # "a" -> "c" in two steps


3. Large word list with redundant entries.


4. beginWord already equals endWord (though the problem guarantees beginWord != endWord).




---

Final Thoughts

✅ BFS ensures the shortest transformation path.
✅ Set lookups prevent unnecessary revisits, optimizing performance.
✅ Handles edge cases well.

🚀 Optimized O(MN) solution for Word Ladder!

