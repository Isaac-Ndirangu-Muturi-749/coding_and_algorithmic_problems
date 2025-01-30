Solution: Word Search II (Find Words in a Grid)

We need to find all words from words that exist in board, where each word must be formed by sequentially adjacent cells (horizontally or vertically). The same cell cannot be used more than once in forming a word.


---

Efficient Approach: Trie + Backtracking

Since we have multiple words to search in the board, a Trie (Prefix Tree) can help us quickly find words while exploring the grid. We will use DFS (Depth-First Search) with backtracking to traverse the board efficiently.


---

Algorithm

1. Build a Trie from words:

Each word is inserted into the Trie, with a special end marker at the last letter.



2. Backtracking with DFS:

Iterate through each cell in the board.

If the character exists in the Trie, perform DFS to explore all valid word paths.

Mark visited cells to avoid using them more than once.

If a word is found, add it to the result and remove it from the Trie to prevent duplicate searches.



3. Optimize by Pruning:

Once a word is found, remove it from the Trie to avoid redundant searches.





---

Implementation

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store complete word at the end node

        # Step 2: Backtracking DFS
        def backtrack(r, c, parent):
            char = board[r][c]
            node = parent.children[char]
            
            # If we found a word, add it to the result and remove it from Trie
            if node.word:
                found_words.add(node.word)
                node.word = None  # Prevent duplicates

            # Mark cell as visited
            board[r][c] = "#"
            
            # Explore all possible directions (Up, Down, Left, Right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] in node.children:
                    backtrack(nr, nc, node)

            # Restore the cell after backtracking
            board[r][c] = char

            # Prune the Trie: If no children left, delete the node
            if not node.children:
                del parent.children[char]

        # Step 3: Start DFS from each cell
        found_words = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        
        return list(found_words)


---

Explanation

1. Build a Trie:

Each word from words is inserted into the Trie.

Example Trie for ["oath", "pea", "eat", "rain"]:

root
├── o ─── a ─── t ─── h (word: "oath")
├── p ─── e ─── a (word: "pea")
├── e ─── a ─── t (word: "eat")
├── r ─── a ─── i ─── n (word: "rain")



2. DFS Backtracking:

Start DFS from every cell in the board.

If a word is found, add it to found_words and remove it from the Trie.

Mark visited cells ("#") to avoid reusing them.

Restore the original cell after DFS.



3. Pruning the Trie:

If a Trie node becomes empty after finding a word, delete it to speed up future searches.





---

Complexity Analysis

Trie Construction: , where  is the number of words and  is the average word length.

Backtracking Search:  in the worst case, where:

 are board dimensions.

 represents the exponential DFS branching factor.


Trie Pruning Reduces Redundant Searches, improving practical performance.



---

Example Walkthrough

Example 1

Input:
board = 
[
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Process:

1. Build a Trie from words.


2. Start DFS from cells containing o, e, r, p.


3. Find "oath" and "eat", but "pea" and "rain" are not present in the board.




---

Example 2

Input:
board = 
[
  ["a","b"],
  ["c","d"]
]
words = ["abcb"]

Output: []

"abcb" cannot be formed without reusing letters.



---

Edge Cases

1. All words exist in the board.


2. Some words share common prefixes (Trie helps optimize).


3. Word list contains many words (Trie reduces redundant searches).


4. Small board with large words.


5. Words require full traversal of the board.




---

Final Thoughts

✅ Trie optimizes word lookups.
✅ Backtracking efficiently explores the grid.
✅ Trie pruning removes unnecessary searches.
🚀 Fast and efficient solution for Word Search II!

