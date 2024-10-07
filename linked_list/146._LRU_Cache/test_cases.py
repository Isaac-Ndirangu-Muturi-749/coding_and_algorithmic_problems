from solution import Solution

def run_tests():
    # Example 1
    # Initialize LRUCache with a capacity of 2
    lRUCache = Solution.LRUCache(2)

    # Sequence of operations
    # cache is {1=1}
    lRUCache.put(1, 1)

    # cache is {1=1, 2=2}
    lRUCache.put(2, 2)

    # return 1 (found in cache)
    assert lRUCache.get(1) == 1, "Test case 1 failed"

    # cache is {1=1, 3=3}, evict key 2
    lRUCache.put(3, 3)

    # return -1 (key 2 was evicted)
    assert lRUCache.get(2) == -1, "Test case 2 failed"

    # cache is {3=3, 4=4}, evict key 1
    lRUCache.put(4, 4)

    # return -1 (key 1 was evicted)
    assert lRUCache.get(1) == -1, "Test case 3 failed"

    # return 3 (found in cache)
    assert lRUCache.get(3) == 3, "Test case 4 failed"

    # return 4 (found in cache)
    assert lRUCache.get(4) == 4, "Test case 5 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
