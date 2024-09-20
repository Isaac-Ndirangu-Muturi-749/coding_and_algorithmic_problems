class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes, where key is the character
        self.children = {}
        # Boolean flag to check if a node marks the end of a valid word
        self.is_end = False

class WordDictionary:

    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start from the root node
        node = self.root
        # Insert each character into the Trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the end of the word
        node.is_end = True

    def search(self, word: str) -> bool:
        # Helper function to perform DFS search, allowing wildcards
        def dfs(node, i):
            # If we've processed the entire word
            if i == len(word):
                return node.is_end

            char = word[i]

            # If the current character is a dot, try all possible child nodes
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # If the current character exists in children, continue DFS
                if char in node.children:
                    return dfs(node.children[char], i + 1)
                else:
                    return False

        # Start DFS from the root node
        return dfs(self.root, 0)
