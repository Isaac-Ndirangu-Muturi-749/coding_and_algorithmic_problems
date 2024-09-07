Here is the implementation of the `Trie` (prefix tree) class:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        """
        Initialize the trie object.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts the string word into the trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
```

### Explanation:
- **TrieNode Class**: This class represents a node in the trie. It has two attributes:
  - `children`: A dictionary to store references to child nodes.
  - `is_end_of_word`: A boolean that marks whether the node is the end of a word.

- **Trie Class**:
  - **`__init__()`**: Initializes the root of the trie, which is an empty `TrieNode`.
  - **`insert(word)`**: This method inserts a word into the trie, character by character. If a character is not already present in the current node's children, a new node is created. At the end of the word, we mark the node as the end of the word.
  - **`search(word)`**: This method checks whether the word exists in the trie by traversing the trie based on the characters of the word. It returns `True` only if the last character corresponds to a node that marks the end of a word.
  - **`startsWith(prefix)`**: This method checks if there is any word in the trie that starts with the given prefix by checking whether each character of the prefix exists in the trie.

### Example Usage:

```python
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # Output: True
print(trie.search("app"))     # Output: False
print(trie.startsWith("app")) # Output: True
trie.insert("app")
print(trie.search("app"))     # Output: True
```

### Complexity:
- **Insert**: O(m), where `m` is the length of the word.
- **Search**: O(m), where `m` is the length of the word.
- **StartsWith**: O(m), where `m` is the length of the prefix.
