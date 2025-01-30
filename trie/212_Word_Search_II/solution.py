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
