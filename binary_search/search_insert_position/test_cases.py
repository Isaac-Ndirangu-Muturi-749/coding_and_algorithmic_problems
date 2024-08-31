from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2, "Test case 1 failed"

    # Test case 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1, "Test case 2 failed"

    # Test case 3
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4, "Test case 3 failed"

    print("All test cases passed!")

if __name__ == "__main__":
    run_tests()
