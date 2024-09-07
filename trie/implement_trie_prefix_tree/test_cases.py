from solution import Trie

def run_tests():
    trie = Trie()

    # Test case 1: Insert and search for "apple"
    trie.insert("apple")
    assert trie.search("apple") == True, "Test case 1 failed"
    assert trie.search("app") == False, "Test case 2 failed"
    assert trie.startsWith("app") == True, "Test case 3 failed"

    # Test case 2: Insert "app" and search again
    trie.insert("app")
    assert trie.search("app") == True, "Test case 4 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
