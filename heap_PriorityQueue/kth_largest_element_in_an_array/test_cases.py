from solution import Solution

def run_tests():
    solution = Solution()

    # Test case 1
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, "Test case 1 failed"

    # Test case 2
    assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, "Test case 2 failed"

    print("All test cases passed!")

if __name__ == '__main__':
    run_tests()
