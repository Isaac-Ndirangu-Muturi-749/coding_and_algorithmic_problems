from solution import WordDictionary

def run_tests():
    wordDictionary = WordDictionary()

    # Test case 1: Adding words
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")

    # Test case 2: Searching for non-existent word
    result1 = wordDictionary.search("pad")  # Expected: False
    assert result1 == False, f"Test case 1 failed: Expected False, got {result1}"

    # Test case 3: Searching for existing word
    result2 = wordDictionary.search("bad")  # Expected: True
    assert result2 == True, f"Test case 2 failed: Expected True, got {result2}"

    # Test case 4: Searching with wildcard at the start
    result3 = wordDictionary.search(".ad")  # Expected: True
    assert result3 == True, f"Test case 3 failed: Expected True, got {result3}"

    # Test case 5: Searching with wildcards in the middle
    result4 = wordDictionary.search("b..")  # Expected: True
    assert result4 == True, f"Test case 4 failed: Expected True, got {result4}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
