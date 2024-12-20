class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, product):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Add product to the suggestions if less than 3
            if len(node.suggestions) < 3:
                node.suggestions.append(product)

    def search(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                # No matching prefix found, append empty lists
                result.extend([[]] * (len(prefix) - len(result)))
                break
        return result


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Step 1: Sort products lexicographically
        products.sort()

        # Step 2: Build the Trie and insert all products
        trie = Trie()
        for product in products:
            trie.insert(product)

        # Step 3: Retrieve suggestions for each prefix of searchWord
        return trie.search(searchWord)


