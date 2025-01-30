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
