from solution import Solution

def run_tests():
    randomizedSet = Solution()

    # Test case 1
    assert randomizedSet.insert(1) == True, "Test case 1.1 failed: Expected True"
    assert randomizedSet.remove(2) == False, "Test case 1.2 failed: Expected False"
    assert randomizedSet.insert(2) == True, "Test case 1.3 failed: Expected True"

    random_val_1 = randomizedSet.getRandom()
    assert random_val_1 in {1, 2}, f"Test case 1.4 failed: Expected 1 or 2, got {random_val_1}"

    assert randomizedSet.remove(1) == True, "Test case 1.5 failed: Expected True"
    assert randomizedSet.insert(2) == False, "Test case 1.6 failed: Expected False"

    random_val_2 = randomizedSet.getRandom()
    assert random_val_2 == 2, f"Test case 1.7 failed: Expected 2, got {random_val_2}"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
